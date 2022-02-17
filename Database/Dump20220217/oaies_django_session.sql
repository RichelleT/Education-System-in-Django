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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('gv10qd3m55ln60zorn2l7f6oi63r16b4','.eJxVjEEOwiAUBe_C2hCRFqhL9z0DefzPt1VTktKujHc3JF3odmYybxWxb1Pca17jzOqqjDr9sgR65qUJfmC5F01l2dY56Zbow1Y9Fs6v29H-DSbUqW0Fznrm4HNGb4WkuzCQxBgMphcjznucg3WdGBqsQ-eRKBDxEDyc-nwBCxg4yg:1nJgY4:jEdLVVqEm0c9OLpcP92qiYRTkMCkUWhkx2AgxkSSZOQ','2022-02-28 18:58:08.690119'),('ijs7t60piwlepfg4lsta562n4hygf666','.eJxVjDsOgzAQRO_iOrLA6_UnZXrOgJbdJZBEIGGootw9IFEkU857M2_T0rYO7VZ0aUcxV-PM5bfriJ86HUAeNN1ny_O0LmNnD8WetNhmFn3dTvfvYKAy7OvQa65zdpK48sQQqEYUZq8kkACgzl49hggVMmhyezBGQlHtg0Pz-QLXEDdL:1nJgcL:MfDuyl9h9f7Ihk4qk5f0PzoENCq6mT9tBZXa23ga-jE','2022-02-28 19:02:33.041877'),('v4mq56aly5rxuzx5auygm94kzw8x123l','.eJxVjE0OwiAYBe_C2hAUKODSvWdovj-kaiAp7cp4d23ShW7fzLyXGmFdyrh2mceJ1Vl5dfjdEOghdQN8h3prmlpd5gn1puiddn1tLM_L7v4dFOjlWxsSCJCccYZtDnGgwWMSkwgz2uw5AlBiE3O0TigfwUYv6OPJBkec1fsDAps40w:1nKeRs:vHbBmmaJo64_HGDRzMou9dLVaj4fNBKz3V-tGbGEOrw','2022-03-03 10:55:44.755867');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
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
