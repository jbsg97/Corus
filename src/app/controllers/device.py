from flask_restx import Resource, reqparse, Namespace, fields
from flask import request
from ..services.device import DeviceService, RecordService, MaintenanceService

api = Namespace('Dispositivos y Registros', description='Endpoints para mostrar información sobre dispositivos y registros')

class DeviceListController(Resource):
    device_service = DeviceService()
    parser_device = reqparse.RequestParser()
    parser_device.add_argument('device_type_id', type=int, help='Buscar por ID Tipo Dispositivo')

    @api.doc(parser=parser_device)
    def get(self):
        if request.args.get("device_type_id"):
            devices = self.device_service.fetch_by_type(
                request.args.get("device_type_id")
            )
            return {'dispositivos': devices, 'status': 'Ok'}
        devices = self.device_service.fetch()
        if devices:
            return {'dispositivos': devices, 'status': 'Ok'}
        return {
            'dispositivos': {} , 
            'status': 'Error al obtener todos los dispositivos'
        }, 404

    def post(self):
        data = request.json
        device = self.device_service.create(data)
        if device:
            return {'dispositivo': device, 'status': 'Creado con exito'}, 201
        return {
            'dispositivo': {} , 
            'status': 'Error al guardar el dispositivo'
        }, 404


class DeviceController(Resource):
    device_service = DeviceService()
    def get(self, id):
        device = self.device_service.retrieve(id)
        if device:
            return {'dispositivo': device, 'status': 'Ok'}
        return {
            'dispositivos': {} , 
            'status': 'No se encontro un dispositivo con el id proporcionado'
        }, 404

    def put(self, id):
        data = request.json
        device = self.device_service.update(id, data)
        if device:
            return {'dispositivo': device, 'status': 'Actualizado con exito'}
        return {
            'dispositivo': {} , 
            'status': 'Error al actualizar el dispositivo'
        }, 404

    def delete(self, id):
        device = self.device_service.delete(id)
        if device:
            return {'dispositivo': device, 'status': 'Eliminado con exito'}
        elif device == False:
            return {'dispositivo': {}, 'status': 'El id ingresado no existe'}
        return {
            'dispositivo': {} , 
            'status': 'Error al eliminar el dispositivo'
        }, 404


class RecordListController(Resource):
    record_service = RecordService()
    parser_record = reqparse.RequestParser()
    parser_record.add_argument('device_type_id', type=int, help='Buscar por ID Tipo Dispositivo')
    parser_record.add_argument('device_id', type=int, help='Buscar por ID Dispositivo')
    
    @api.doc(parser=parser_record)
    def get(self):
        if request.args.get("device_type_id"):
            records = self.record_service.fetch_by_type(request.args.get("device_type_id"))
            return {'registros': records, 'status': 'Ok'}
        if request.args.get("device_id"):
            records = self.record_service.fetch_by_device(request.args.get("device_id"))
            return {'registros': records, 'status': 'Ok'}
        records = self.record_service.fetch()
        if records:
            return {'registros': records, 'status': 'Ok'}
        return {
            'registros': {} , 
            'status': 'Error al obtener todos los registros'
        }, 404

    def post(self):
        data = request.json
        record = self.record_service.create(data)
        if record:
            return {'registro': record, 'status': 'Creado con exito'}, 201
        elif record == False:
            return {
                'registro': {}, 
                'status': 'No se permite registros ya que el dispositivo esta en mantenimiento'
            }, 404
        return {
            'dispositivo': {} , 
            'status': 'Error al guardar el registro'
        }, 404


class RecordController(Resource):
    record_service = RecordService()

    def get(self, id):
        record = self.record_service.retrieve(id)
        if record:
            return {'registro': record, 'status': 'Ok'}
        return {
            'Registro': {} , 
            'status': 'No se encontro registro con el id proporcionado'
        }, 404

    def put(self, id):
        data = request.json
        record = self.record_service.update(id, data)
        if record:
            return {'registro': record, 'status': 'Actualizado con exito'}
        return {
            'registro': {} , 
            'status': 'Error al actualizar el registro'
        }, 404

    def delete(self, id):
        record = self.record_service.delete(id)
        if record:
            return {'registro': record, 'status': 'Eliminado con exito'}
        elif record == False:
            return {'registro': {}, 'status': 'El id ingresado no existe'}
        return {
            'registro': {} , 
            'status': 'Error al eliminar el registro'
        }, 404


class TotalEnergyController(Resource):
    record_service = RecordService()
    def get(self):
        energy = self.record_service.total_energy()
        if energy:
            return {'energia': energy, 'status': 'Ok'}
        return {
            'Registro': {} , 
            'status': 'No se encontraron registros de energia'
        }, 404


class MaintenanceListController(Resource):
    maintenance_service = MaintenanceService()
    def get(self):
        maintenance_devices = self.maintenance_service.fetch()
        if maintenance_devices:
            return {'dispositivos': maintenance_devices, 'status': 'Ok'}
        return {
            'registros': {} , 
            'status': 'Error al obtener todos los dispositivos en mantenimiento'
        }, 404

    def post(self):
        data = request.json
        maintenance_device = self.maintenance_service.create(data)
        if maintenance_device:
            return {'dispositivo': maintenance_device, 'status': 'Creado con exito'}, 201
        return {
            'dispositivo': {} , 
            'status': 'Error al guardar el dispositivo en mantenimiento'
        }, 404


class MaintenanceController(Resource):
    maintenance_service = MaintenanceService()
    def get(self, device_id):
        maintenance_device = self.maintenance_service.retrieve(device_id)
        if maintenance_device:
            return {'dispositivo': maintenance_device, 'status': 'Ok'}
        return {
            'registros': {} , 
            'status': 'No se encontraron dispositivos en mantenimiento con el id ingresado'
        }, 404
