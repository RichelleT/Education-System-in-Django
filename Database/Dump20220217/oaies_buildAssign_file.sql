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
-- Table structure for table `buildAssign_file`
--

DROP TABLE IF EXISTS `buildAssign_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buildAssign_file` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `upload_txt` varchar(100) DEFAULT NULL,
  `link_answ_id` bigint DEFAULT NULL,
  `link_assign_id` bigint DEFAULT NULL,
  `uploader_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `buildAssign_file_link_answ_id_5c57a251_fk_buildAssign_answer_id` (`link_answ_id`),
  KEY `buildAssign_file_link_assign_id_a6ba7187_fk_buildAssi` (`link_assign_id`),
  KEY `buildAssign_file_uploader_id_3013666d_fk_auth_user_id` (`uploader_id`),
  CONSTRAINT `buildAssign_file_link_answ_id_5c57a251_fk_buildAssign_answer_id` FOREIGN KEY (`link_answ_id`) REFERENCES `buildAssign_answer` (`id`),
  CONSTRAINT `buildAssign_file_link_assign_id_a6ba7187_fk_buildAssi` FOREIGN KEY (`link_assign_id`) REFERENCES `buildAssign_assignment` (`id`),
  CONSTRAINT `buildAssign_file_uploader_id_3013666d_fk_auth_user_id` FOREIGN KEY (`uploader_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildAssign_file`
--

LOCK TABLES `buildAssign_file` WRITE;
/*!40000 ALTER TABLE `buildAssign_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `buildAssign_file` ENABLE KEYS */;
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
