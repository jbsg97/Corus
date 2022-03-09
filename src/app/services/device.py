from ..config.db import db
from datetime import datetime
from ..models.device import Device, Records, Maintenance
from ..schemas.device import (
    DeviceSchema, 
    RecordSchema, 
    EnergySchema, 
    MaintenanceSchema
)
from sqlalchemy.sql import func

class DeviceService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def fetch(self):
        try:
            device_schema = DeviceSchema(many=True)
            devices = db.session.query(Device).all()
            if not devices:
                return None
            return None if not devices else device_schema.dump(devices)
        except Exception as e:
            return None

    def fetch_by_type(self, type_id):
        try:
            device_schema = DeviceSchema(many=True)
            devices = db.session.query(Device)\
                .filter(Device.tipo_dispositivo_id == type_id ).all()
            if not devices:
                return None
            return None if not devices else device_schema.dump(devices)
        except Exception as e:
            return None

    def retrieve(self, id):
        try:
            device_schema = DeviceSchema()
            device = db.session.query(Device).filter(Device.id == id).first()
            if not device:
                return None
            return None if not device else device_schema.dump(device)
        except Exception as e:
            return None

    def create(self, data):
        try:
            device_schema = DeviceSchema()
            device = Device(
                nombre = data['nombre'],
                potencia = data['potencia'],
                estatus_dispositivo_id = data['estatus_dispositivo_id'],
                tipo_dispositivo_id = data['tipo_dispositivo_id'],
                fecha_alta = datetime.now()
            )
            db.session.add(device)
            db.session.commit()
            return device_schema.dump(data)
        except Exception as e:
            print(e)
            return None

    def update(self, device_id, data):
        try:
            device_schema = DeviceSchema()
            db.session.query(Device).filter(Device.id == device_id).update(
                {
                    'nombre': data['nombre'],
                    'potencia': data['potencia'],
                    'estatus_dispositivo_id': data['estatus_dispositivo_id'],
                    'tipo_dispositivo_id': data['tipo_dispositivo_id'],
                    'fecha_actualizacion': datetime.now()
                }
                ,synchronize_session=False)
            db.session.commit()
            device_updated = db.session.query(Device).filter(Device.id == device_id).first()
            return device_schema.dump(device_updated)

        except Exception as e:
            print(e)
            return None

    def delete(self, device_id):
        try:
            device_schema = DeviceSchema()
            device = Device.query.filter(Device.id == device_id).first()
            if device:
                Device.query.filter(Device.id == device_id).delete()
                db.session.commit()
                return device_schema.dump(device)
            return False
        except:
            return None


class RecordService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def fetch(self):
        try:
            record_schema = RecordSchema(many=True)
            records = db.session.query(Records).all()
            if not records:
                return None
            return None if not records else record_schema.dump(records)
        except Exception as e:
            return None

    def fetch_by_type(self, type_id):
        try:
            record_schema = RecordSchema(many=True)
            records = db.session.query(Records)\
                .filter(Records.tipo_dispositivo_id == type_id).all()
            if not records:
                return None
            return None if not records else record_schema.dump(records)
        except Exception as e:
            return None

    def fetch_by_device(self, device_id):
        try:
            record_schema = RecordSchema(many=True)
            records = db.session.query(Records)\
                .filter(Records.dispositivo_id == device_id).all()
            if not records:
                return None
            return None if not records else record_schema.dump(records)
        except Exception as e:
            return None

    def retrieve(self, id):
        try:
            record_schema = RecordSchema()
            record = db.session.query(Records).filter(Records.id == id).first()
            if not record:
                return None
            return None if not record else record_schema.dump(record)
        except Exception as e:
            return None

    def create(self, data):
        try:
            record_schema = RecordSchema()
            device = Device.query\
                .filter(
                    Device.id == data['dispositivo_id'],
                    Device.estatus_dispositivo_id == 2
                ).first()
            if device:
                return False
            record = Records(
                tipo_dispositivo_id = data['tipo_dispositivo_id'],
                potencia_actual = data['potencia_actual'],
                dispositivo_id = data['dispositivo_id'],
                timestamp = datetime.now()
            )
            db.session.add(record)
            db.session.commit()
            return record_schema.dump(data)
        except Exception as e:
            return None

    def update(self, record_id, data):
        try:
            record_schema = RecordSchema()
            db.session.query(Records).filter(Records.id == record_id).update(
                {
                    'tipo_dispositivo_id': data['tipo_dispositivo_id'],
                    'potencia_actual': data['potencia_actual'],
                    'dispositivo_id': data['dispositivo_id'],
                }
                ,synchronize_session=False)
            db.session.commit()
            # Update device power
            db.session.query(Device).filter(Device.id == data['dispositivo_id']).update(
                {
                    'potencia': data['potencia_actual'],
                    'fecha_actualizacion': datetime.now()
                }
                ,synchronize_session=False)
            db.session.commit()
            record_updated = db.session.query(Records).filter(Records.id == record_id).first()
            return record_schema.dump(record_updated)

        except Exception as e:
            print(e)
            return None

    def delete(self, record_id):
        try:
            record_schema = RecordSchema()
            record = Records.query.filter(Records.id == record_id).first()
            if record:
                Records.query.filter(Records.id == record_id).delete()
                db.session.commit()
                return record_schema.dump(record)
            return False
        except:
            return None

    def total_energy(self):
        try:
            energy_schema = EnergySchema(many=True)
            total_energy = db.session\
                .query(
                    Records.dispositivo_id,
                    func.sum(Records.potencia_actual).label('energia')
                )\
                .group_by(Records.dispositivo_id)\
                .all()
            print(total_energy)
            return energy_schema.dump(total_energy)
        except Exception as e:
            return None


class MaintenanceService:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def fetch(self):
        try:
            maintenance_devices_schema = MaintenanceSchema(many=True)
            maintenance_devices = db.session.query(Maintenance).all()
            if not maintenance_devices:
                return None
            return None if not maintenance_devices else maintenance_devices_schema.dump(maintenance_devices)
        except Exception as e:
            return None

    def create(self, data):
        try:
            maintenance_devices_schema = MaintenanceSchema()
            maintenance_device = Maintenance(
                dispositivo_id = data['dispositivo_id'],
                fecha_ingreso = datetime.now()
            )
            db.session.add(maintenance_device)
            db.session.commit()
            # Device status changed to in maintenance
            DEVICE_IN_MAINTENANCE = 2
            db.session.query(Device).filter(Device.id == data['dispositivo_id']).update(
                {
                    'estatus_dispositivo_id': DEVICE_IN_MAINTENANCE
                }
                ,synchronize_session=False)
            db.session.commit()
            return maintenance_devices_schema.dump(data)
        except Exception as e:
            print(e)
            return None

    def retrieve(self, device_id):
        try:
            maintenance_devices_schema = MaintenanceSchema()
            maintenance_device = db.session.query(Maintenance)\
                .filter(Maintenance.dispositivo_id == device_id)\
                .first()
            if not maintenance_device:
                return None
            return None if not maintenance_device else maintenance_devices_schema.dump(maintenance_device)
        except Exception as e:
            print(e)
            return None
