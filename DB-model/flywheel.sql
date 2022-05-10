-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: flywheel
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `answer`
--

DROP TABLE IF EXISTS `answer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `answer` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `questionId` int unsigned NOT NULL,
  `englishPhrase` varchar(500) NOT NULL,
  `linkToAudio` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `questionIdIndex` (`questionId`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `answer`
--

LOCK TABLES `answer` WRITE;
/*!40000 ALTER TABLE `answer` DISABLE KEYS */;
INSERT INTO `answer` VALUES (1,1,'A cat sits on the table','1_A_cat_sits_on_the_table.mp3'),(2,1,'The cat sits on the table','2_The_cat_sits_on_the_table.mp3'),(3,1,'A cat is sitting on the table','3_A_cat_is_sitting_on_the_table.mp3'),(4,1,'The cat is sitting on the table','4_The_cat_is_sitting_on_the_table.mp3'),(5,2,'A cat sits on the table','1_A_cat_sits_on_the_table.mp3'),(6,2,'The cat sits on the table','2_The_cat_sits_on_the_table.mp3'),(7,2,'A cat is sitting on the table','3_A_cat_is_sitting_on_the_table.mp3'),(8,2,'The cat is sitting on the table','4_The_cat_is_sitting_on_the_table.mp3'),(9,3,'I am an engineer','9_I_am_an_engineer.mp3'),(10,3,'I\'m an engineer','10_I_m_an_engineer.mp3'),(11,4,'I am an electronics engineer','11_I_am_an_electronics_engineer.mp3'),(12,4,'I\'m an electronics engineer','12_I_m_an_electronics_engineer.mp3');
/*!40000 ALTER TABLE `answer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grammartheme`
--

DROP TABLE IF EXISTS `grammartheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grammartheme` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `theme` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grammartheme`
--

LOCK TABLES `grammartheme` WRITE;
/*!40000 ALTER TABLE `grammartheme` DISABLE KEYS */;
INSERT INTO `grammartheme` VALUES (1,'Am/is/are'),(2,'Am/is/are questions'),(3,'Present continuous'),(4,'Present continuous questions'),(5,'Simple present');
/*!40000 ALTER TABLE `grammartheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grammarthemestat`
--

DROP TABLE IF EXISTS `grammarthemestat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `grammarthemestat` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `themeId` int unsigned NOT NULL,
  `themeStat` int unsigned NOT NULL,
  `lastAttempt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `userIdIndex` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grammarthemestat`
--

LOCK TABLES `grammarthemestat` WRITE;
/*!40000 ALTER TABLE `grammarthemestat` DISABLE KEYS */;
/*!40000 ALTER TABLE `grammarthemestat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `question`
--

DROP TABLE IF EXISTS `question`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `question` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nativePhrase` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `question`
--

LOCK TABLES `question` WRITE;
/*!40000 ALTER TABLE `question` DISABLE KEYS */;
INSERT INTO `question` VALUES (1,'Кошка сидит на столе'),(2,'Кот сидит на столе'),(3,'Я инженер'),(4,'Я инженер-электронщик');
/*!40000 ALTER TABLE `question` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questionstat`
--

DROP TABLE IF EXISTS `questionstat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questionstat` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `questionId` int unsigned NOT NULL,
  `questionStat` int unsigned NOT NULL,
  `lastAttempt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userIdIndex` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questionstat`
--

LOCK TABLES `questionstat` WRITE;
/*!40000 ALTER TABLE `questionstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `questionstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questiontogrammartheme`
--

DROP TABLE IF EXISTS `questiontogrammartheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questiontogrammartheme` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `questionId` int unsigned NOT NULL,
  `themeId` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `themeIdIndex` (`themeId`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questiontogrammartheme`
--

LOCK TABLES `questiontogrammartheme` WRITE;
/*!40000 ALTER TABLE `questiontogrammartheme` DISABLE KEYS */;
INSERT INTO `questiontogrammartheme` VALUES (1,1,3),(2,1,5),(3,2,3),(4,2,5),(5,3,1),(6,4,1);
/*!40000 ALTER TABLE `questiontogrammartheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questiontoword`
--

DROP TABLE IF EXISTS `questiontoword`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questiontoword` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `questionId` int unsigned NOT NULL,
  `wordId` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wordIdIndex` (`wordId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questiontoword`
--

LOCK TABLES `questiontoword` WRITE;
/*!40000 ALTER TABLE `questiontoword` DISABLE KEYS */;
INSERT INTO `questiontoword` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,2,1),(7,2,2),(8,2,3),(9,2,4),(10,2,5),(11,3,6),(12,4,7),(13,4,6);
/*!40000 ALTER TABLE `questiontoword` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questiontowordtheme`
--

DROP TABLE IF EXISTS `questiontowordtheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questiontowordtheme` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `questionId` int unsigned NOT NULL,
  `themeId` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `themeIdIndex` (`themeId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questiontowordtheme`
--

LOCK TABLES `questiontowordtheme` WRITE;
/*!40000 ALTER TABLE `questiontowordtheme` DISABLE KEYS */;
/*!40000 ALTER TABLE `questiontowordtheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(200) NOT NULL,
  `full_name` varchar(200) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `passwordHash` varchar(200) NOT NULL,
  `level` int unsigned DEFAULT NULL,
  `attempts` int unsigned DEFAULT NULL,
  `lastVisit` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usernameIndex` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'johndoe','John Doe','johndoe@example.com','$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW',NULL,NULL,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `word`
--

DROP TABLE IF EXISTS `word`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `word` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `word` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `wordIndex` (`word`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `word`
--

LOCK TABLES `word` WRITE;
/*!40000 ALTER TABLE `word` DISABLE KEYS */;
INSERT INTO `word` VALUES (1,'cat'),(7,'electronics'),(6,'engineer'),(4,'on'),(2,'sit'),(3,'sitting'),(5,'table');
/*!40000 ALTER TABLE `word` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wordstat`
--

DROP TABLE IF EXISTS `wordstat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wordstat` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `wordId` int unsigned NOT NULL,
  `wordStat` int unsigned NOT NULL,
  `lastAttempt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userIdIndex` (`userId`) /*!80000 INVISIBLE */
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wordstat`
--

LOCK TABLES `wordstat` WRITE;
/*!40000 ALTER TABLE `wordstat` DISABLE KEYS */;
/*!40000 ALTER TABLE `wordstat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wordtheme`
--

DROP TABLE IF EXISTS `wordtheme`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wordtheme` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `theme` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wordtheme`
--

LOCK TABLES `wordtheme` WRITE;
/*!40000 ALTER TABLE `wordtheme` DISABLE KEYS */;
/*!40000 ALTER TABLE `wordtheme` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wordthemestat`
--

DROP TABLE IF EXISTS `wordthemestat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `wordthemestat` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `userId` int unsigned NOT NULL,
  `themeId` int unsigned NOT NULL,
  `themeStat` int unsigned NOT NULL,
  `lastAttempt` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `userIdIndex` (`userId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wordthemestat`
--

LOCK TABLES `wordthemestat` WRITE;
/*!40000 ALTER TABLE `wordthemestat` DISABLE KEYS */;
/*!40000 ALTER TABLE `wordthemestat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-09 20:05:25
