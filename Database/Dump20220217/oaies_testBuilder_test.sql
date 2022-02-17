-- MySQL dump 10.13  Distrib 8.0.28, for macos11 (x86_64)
--
-- Host: localhost    Database: oaies
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `testBuilder_test`
--

DROP TABLE IF EXISTS `testBuilder_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testBuilder_test` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `test_name` varchar(100) NOT NULL,
  `test_date` datetime(6) NOT NULL,
  `module_sel_id` bigint DEFAULT NULL,
  `host_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `testBuilder_test_module_sel_id_8fdd962f_fk_testBuilder_module_id` (`module_sel_id`),
  KEY `testBuilder_test_host_id_d54696b8_fk_auth_user_id` (`host_id`),
  CONSTRAINT `testBuilder_test_host_id_d54696b8_fk_auth_user_id` FOREIGN KEY (`host_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `testBuilder_test_module_sel_id_8fdd962f_fk_testBuilder_module_id` FOREIGN KEY (`module_sel_id`) REFERENCES `testBuilder_module` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testBuilder_test`
--

LOCK TABLES `testBuilder_test` WRITE;
/*!40000 ALTER TABLE `testBuilder_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `testBuilder_test` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 18:56:41
