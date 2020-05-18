-- MySQL dump 10.16  Distrib 10.1.26-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.26-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `earthquake`
--
USE `earthquake`;
DROP TABLE IF EXISTS `earthquake`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `earthquake` (
  `id` varchar(12) DEFAULT NULL,
  `mag` decimal(3,2) DEFAULT NULL,
  `place` varchar(73) DEFAULT NULL,
  `time` bigint(20) DEFAULT NULL,
  `updated` bigint(20) DEFAULT NULL,
  `tz` smallint(6) DEFAULT NULL,
  `url` varchar(62) DEFAULT NULL,
  `detail` varchar(84) DEFAULT NULL,
  `felt` varchar(4) DEFAULT NULL,
  `cdi` varchar(3) DEFAULT NULL,
  `mmi` varchar(5) DEFAULT NULL,
  `alert` varchar(6) DEFAULT NULL,
  `status` varchar(9) DEFAULT NULL,
  `tsunami` tinyint(4) DEFAULT NULL,
  `sig` smallint(6) DEFAULT NULL,
  `net` varchar(2) DEFAULT NULL,
  `code` varchar(10) DEFAULT NULL,
  `ids` varchar(49) DEFAULT NULL,
  `sources` varchar(13) DEFAULT NULL,
  `types` varchar(109) DEFAULT NULL,
  `nst` varchar(3) DEFAULT NULL,
  `dmin` varchar(12) DEFAULT NULL,
  `rms` decimal(5,4) DEFAULT NULL,
  `gap` varchar(6) DEFAULT NULL,
  `magType` varchar(5) DEFAULT NULL,
  `type` varchar(16) DEFAULT NULL,
  `title` varchar(81) DEFAULT NULL,
  `latitude` decimal(15,12) DEFAULT NULL,
  `longitude` decimal(15,13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;
