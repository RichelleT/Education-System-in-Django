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
-- Table structure for table `buildAssign_assignment`
--

DROP TABLE IF EXISTS `buildAssign_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buildAssign_assignment` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `assign_name` varchar(1000) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `created_by_id` int DEFAULT NULL,
  `linked_module_id` bigint DEFAULT NULL,
  `set_added` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buildAssign_assignment_created_by_id_b637ab62_fk_auth_user_id` (`created_by_id`),
  KEY `buildAssign_assignme_linked_module_id_b2b9cb81_fk_testBuild` (`linked_module_id`),
  CONSTRAINT `buildAssign_assignme_linked_module_id_b2b9cb81_fk_testBuild` FOREIGN KEY (`linked_module_id`) REFERENCES `testBuilder_module` (`id`),
  CONSTRAINT `buildAssign_assignment_created_by_id_b637ab62_fk_auth_user_id` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildAssign_assignment`
--

LOCK TABLES `buildAssign_assignment` WRITE;
/*!40000 ALTER TABLE `buildAssign_assignment` DISABLE KEYS */;
/*!40000 ALTER TABLE `buildAssign_assignment` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-17 18:56:40
