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
-- Table structure for table `buildAssign_assignresult`
--

DROP TABLE IF EXISTS `buildAssign_assignresult`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buildAssign_assignresult` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `correct` int NOT NULL,
  `percentage` int NOT NULL,
  `total` int NOT NULL,
  `grade` varchar(10) NOT NULL,
  `attempted_time` datetime(6) NOT NULL,
  `attempted_by_id` int DEFAULT NULL,
  `linked_assign_id` bigint DEFAULT NULL,
  `link_ques_id` bigint DEFAULT NULL,
  `lettergrade` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `buildAssign_assignre_attempted_by_id_6c28c38a_fk_auth_user` (`attempted_by_id`),
  KEY `buildAssign_assignre_linked_assign_id_a9585055_fk_buildAssi` (`linked_assign_id`),
  KEY `buildAssign_assignre_link_ques_id_2d07aab3_fk_buildAssi` (`link_ques_id`),
  CONSTRAINT `buildAssign_assignre_attempted_by_id_6c28c38a_fk_auth_user` FOREIGN KEY (`attempted_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `buildAssign_assignre_link_ques_id_2d07aab3_fk_buildAssi` FOREIGN KEY (`link_ques_id`) REFERENCES `buildAssign_answer` (`id`),
  CONSTRAINT `buildAssign_assignre_linked_assign_id_a9585055_fk_buildAssi` FOREIGN KEY (`linked_assign_id`) REFERENCES `buildAssign_assignment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buildAssign_assignresult`
--

LOCK TABLES `buildAssign_assignresult` WRITE;
/*!40000 ALTER TABLE `buildAssign_assignresult` DISABLE KEYS */;
/*!40000 ALTER TABLE `buildAssign_assignresult` ENABLE KEYS */;
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
