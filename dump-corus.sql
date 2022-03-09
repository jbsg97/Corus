-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: corus
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.38-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dispositivos`
--

DROP TABLE IF EXISTS `dispositivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dispositivos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `potencia` int(11) DEFAULT NULL,
  `fecha_alta` date DEFAULT NULL,
  `fecha_actualizacion` date DEFAULT NULL,
  `estatus_dispositivo_id` int(11) NOT NULL,
  `tipo_dispositivo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivos`
--

LOCK TABLES `dispositivos` WRITE;
/*!40000 ALTER TABLE `dispositivos` DISABLE KEYS */;
INSERT INTO `dispositivos` VALUES (1,'Test',800,'2022-03-08','2022-03-08',1,2),(6,'Test2',30,'2022-03-08',NULL,2,1),(7,'Test2',30,NULL,NULL,1,1),(8,'Test2',30,NULL,NULL,1,1),(9,'Test2',30,NULL,NULL,1,1),(10,'Test2',30,NULL,NULL,1,1),(11,'Test2',30,NULL,NULL,1,1),(12,'Test2',30,NULL,NULL,1,1),(13,'Test2',30,NULL,NULL,1,1),(14,'Test2',30,NULL,NULL,1,1),(15,'Test222',30,NULL,NULL,1,1);
/*!40000 ALTER TABLE `dispositivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lecturas`
--

DROP TABLE IF EXISTS `lecturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lecturas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dispositivo_id` int(11) DEFAULT NULL,
  `tipo_dispositivo_id` int(11) DEFAULT NULL,
  `potencia_actual` int(11) DEFAULT NULL,
  `timestamp` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lecturas`
--

LOCK TABLES `lecturas` WRITE;
/*!40000 ALTER TABLE `lecturas` DISABLE KEYS */;
INSERT INTO `lecturas` VALUES (4,1,1,70,'2022-03-08'),(5,1,1,70,'2022-03-08'),(6,1,1,60,'2022-03-08'),(7,2,1,60,'2022-03-08'),(8,3,1,60,'2022-03-08'),(9,3,1,50,'2022-03-08'),(10,8,1,800,'2022-03-08'),(11,66,1,800,'2022-03-08'),(12,66,1,800,'2022-03-08'),(13,66,2,800,'2022-03-08');
/*!40000 ALTER TABLE `lecturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mantenimientos`
--

DROP TABLE IF EXISTS `mantenimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `mantenimientos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dispositivo_id` int(11) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mantenimientos`
--

LOCK TABLES `mantenimientos` WRITE;
/*!40000 ALTER TABLE `mantenimientos` DISABLE KEYS */;
INSERT INTO `mantenimientos` VALUES (1,2,'2022-03-08'),(2,6,'2022-03-08'),(3,6,'2022-03-08');
/*!40000 ALTER TABLE `mantenimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_dispositvos`
--

DROP TABLE IF EXISTS `status_dispositvos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status_dispositvos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_dispositvos`
--

LOCK TABLES `status_dispositvos` WRITE;
/*!40000 ALTER TABLE `status_dispositvos` DISABLE KEYS */;
INSERT INTO `status_dispositvos` VALUES (1,'En operación'),(2,'En mantenimiento');
/*!40000 ALTER TABLE `status_dispositvos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo_dispositivos`
--

DROP TABLE IF EXISTS `tipo_dispositivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipo_dispositivos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_tipo_dispositivo` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo_dispositivos`
--

LOCK TABLES `tipo_dispositivos` WRITE;
/*!40000 ALTER TABLE `tipo_dispositivos` DISABLE KEYS */;
INSERT INTO `tipo_dispositivos` VALUES (1,'Celda'),(2,'Aerogenerador'),(3,'Turbina Hidroeléctrica');
/*!40000 ALTER TABLE `tipo_dispositivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'corus'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-08 21:44:08
