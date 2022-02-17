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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-02-14 18:52:21.293787'),(2,'auth','0001_initial','2022-02-14 18:52:21.486196'),(3,'admin','0001_initial','2022-02-14 18:52:21.538471'),(4,'admin','0002_logentry_remove_auto_add','2022-02-14 18:52:21.545294'),(5,'admin','0003_logentry_add_action_flag_choices','2022-02-14 18:52:21.552745'),(6,'contenttypes','0002_remove_content_type_name','2022-02-14 18:52:21.595748'),(7,'auth','0002_alter_permission_name_max_length','2022-02-14 18:52:21.622399'),(8,'auth','0003_alter_user_email_max_length','2022-02-14 18:52:21.640487'),(9,'auth','0004_alter_user_username_opts','2022-02-14 18:52:21.648804'),(10,'auth','0005_alter_user_last_login_null','2022-02-14 18:52:21.673125'),(11,'auth','0006_require_contenttypes_0002','2022-02-14 18:52:21.674784'),(12,'auth','0007_alter_validators_add_error_messages','2022-02-14 18:52:21.681748'),(13,'auth','0008_alter_user_username_max_length','2022-02-14 18:52:21.705990'),(14,'auth','0009_alter_user_last_name_max_length','2022-02-14 18:52:21.730749'),(15,'auth','0010_alter_group_name_max_length','2022-02-14 18:52:21.744116'),(16,'auth','0011_update_proxy_permissions','2022-02-14 18:52:21.751129'),(17,'auth','0012_alter_user_first_name_max_length','2022-02-14 18:52:21.778226'),(18,'testBuilder','0001_initial','2022-02-14 18:52:21.990636'),(19,'testBuilder','0002_quizresult_linked_module','2022-02-14 18:52:22.022176'),(20,'testBuilder','0003_auto_20220210_0416','2022-02-14 18:52:22.040715'),(21,'testBuilder','0004_delete_usertomodule','2022-02-14 18:52:22.055898'),(22,'testBuilder','0005_alter_module_host','2022-02-14 18:52:22.065044'),(23,'buildAssign','0001_initial','2022-02-14 18:52:22.191433'),(24,'buildAssign','0002_auto_20220210_0513','2022-02-14 18:52:22.235061'),(25,'buildAssign','0003_auto_20220211_0526','2022-02-14 18:52:22.342906'),(26,'buildAssign','0004_answer_created_date','2022-02-14 18:52:22.364849'),(27,'buildAssign','0005_auto_20220211_0628','2022-02-14 18:52:22.426949'),(28,'buildAssign','0006_remove_assignresult_linked_module','2022-02-14 18:52:22.476548'),(29,'buildAssign','0007_answer_upload_txt','2022-02-14 18:52:22.496463'),(30,'buildAssign','0008_auto_20220211_1411','2022-02-14 18:52:22.582102'),(31,'buildAssign','0009_answer_limit','2022-02-14 18:52:22.618053'),(32,'buildAssign','0010_alter_answer_limit','2022-02-14 18:52:22.629634'),(33,'buildAssign','0011_alter_answer_limit','2022-02-14 18:52:22.639650'),(34,'buildAssign','0012_auto_20220211_1523','2022-02-14 18:52:22.731437'),(35,'buildAssign','0013_alter_assignment_limit','2022-02-14 18:52:22.804371'),(36,'buildAssign','0014_remove_assignment_limit','2022-02-14 18:52:22.830855'),(37,'buildAssign','0015_assignresult_lettergrade','2022-02-14 18:52:22.854031'),(38,'buildAssign','0016_auto_20220214_2225','2022-02-14 18:52:22.899634'),(39,'buildAssign','0017_auto_20220215_0145','2022-02-14 18:52:22.917588'),(40,'buildAssign','0018_alter_answer_answer','2022-02-14 18:52:22.928885'),(41,'register','0001_initial','2022-02-14 18:52:22.963895'),(42,'register','0002_auto_20220209_1133','2022-02-14 18:52:22.995184'),(43,'register','0003_alter_profile_programme','2022-02-14 18:52:23.022111'),(44,'sessions','0001_initial','2022-02-14 18:52:23.035877'),(45,'testBuilder','0006_alter_quiz_answ','2022-02-14 18:52:23.040773'),(46,'testBuilder','0007_alter_quiz_answ','2022-02-14 18:52:23.045676'),(47,'testBuilder','0008_quizresult_useransw','2022-02-14 18:52:23.071994'),(48,'testBuilder','0009_remove_quizresult_useransw','2022-02-14 18:52:23.096940'),(49,'testBuilder','0010_auto_20220211_0526','2022-02-14 18:52:23.159418'),(50,'testBuilder','0011_quizresult_lettergrade','2022-02-14 18:52:23.190557'),(51,'testBuilder','0012_auto_20220215_0145','2022-02-14 18:52:23.224378'),(52,'testBuilder','0013_alter_quiz_quest','2022-02-14 18:52:23.243585'),(53,'testBuilder','0014_alter_quiz_quest','2022-02-14 18:52:23.269038'),(54,'testBuilder','0015_auto_20220215_0232','2022-02-14 18:52:23.451569'),(55,'testBuilder','0016_auto_20220215_0235','2022-02-14 18:52:23.540429'),(56,'buildAssign','0019_alter_answer_question','2022-02-17 10:50:25.609875'),(57,'buildAssign','0020_alter_answer_answer','2022-02-17 10:50:25.661893'),(58,'buildAssign','0021_remove_answer_set_added','2022-02-17 10:50:25.690836'),(59,'buildAssign','0022_answer_set_added','2022-02-17 10:50:25.721777'),(60,'buildAssign','0023_auto_20220215_0434','2022-02-17 10:50:25.778829'),(61,'testBuilder','0017_alter_quiz_quest','2022-02-17 10:50:25.800341'),(62,'testBuilder','0018_auto_20220215_0927','2022-02-17 10:50:25.877368'),(63,'testBuilder','0019_remove_quizresult_linked_module','2022-02-17 10:50:25.919318'),(64,'testBuilder','0020_quizresult_linked_module','2022-02-17 10:50:25.951489'),(65,'testBuilder','0021_auto_20220215_2212','2022-02-17 10:50:26.013055');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
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
