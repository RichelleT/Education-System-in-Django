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
-- Table structure for table `testBuilder_quiz`
--

DROP TABLE IF EXISTS `testBuilder_quiz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `testBuilder_quiz` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `op1` longtext NOT NULL,
  `op2` longtext NOT NULL,
  `op3` longtext NOT NULL,
  `op4` longtext NOT NULL,
  `answ` varchar(7) NOT NULL,
  `test_sel_id` bigint DEFAULT NULL,
  `quest` longtext NOT NULL,
  `linked_module_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `testBuilder_quiz_test_sel_id_faab079d_fk_testBuilder_test_id` (`test_sel_id`),
  KEY `testBuilder_quiz_linked_module_id_32cca22e_fk_testBuild` (`linked_module_id`),
  CONSTRAINT `testBuilder_quiz_linked_module_id_32cca22e_fk_testBuild` FOREIGN KEY (`linked_module_id`) REFERENCES `testBuilder_module` (`id`),
  CONSTRAINT `testBuilder_quiz_test_sel_id_faab079d_fk_testBuilder_test_id` FOREIGN KEY (`test_sel_id`) REFERENCES `testBuilder_test` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testBuilder_quiz`
--

LOCK TABLES `testBuilder_quiz` WRITE;
/*!40000 ALTER TABLE `testBuilder_quiz` DISABLE KEYS */;
/*!40000 ALTER TABLE `testBuilder_quiz` ENABLE KEYS */;
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
