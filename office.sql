-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: office
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `adminid` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`adminid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (123,'Eswar nandivada','Female','eswar@codegnan.com','2001');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applicants`
--

DROP TABLE IF EXISTS `applicants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `applicants` (
  `aspirentid` int DEFAULT NULL,
  `notifid` int DEFAULT NULL,
  `filename` varchar(15) DEFAULT NULL,
  `fileupload` longblob,
  `applied_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` varchar(10) DEFAULT 'Pending',
  KEY `notifid` (`notifid`),
  KEY `aspirentid` (`aspirentid`),
  CONSTRAINT `applicants_ibfk_1` FOREIGN KEY (`notifid`) REFERENCES `notifications` (`notifid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `applicants_ibfk_2` FOREIGN KEY (`aspirentid`) REFERENCES `aspirent` (`aspirentid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applicants`
--

LOCK TABLES `applicants` WRITE;
/*!40000 ALTER TABLE `applicants` DISABLE KEYS */;
INSERT INTO `applicants` VALUES (2001,235,'laloyala.txt',_binary 'Hostel Management System\r\nPatient Management System\r\nOnline Examination System\r\nLibrary Management System\r\nFood Delivery application using Python\r\nCustom Messenger Application\r\nNews aggregator\r\nCalorie Counter Application\r\nImplementation Of Result Management System\r\nFeedback Information system\r\nBuilding a Fully Functional E Commerce Web Application using python\r\nOnline Employee Recruitment System\r\nImplementation of Live Weather Forecast Application using Python\r\nImplementation of Task Management System\r\n\r\n\r\nOnline Examination System\r\nEcommerce\r\nCalorie Counter Application\r\nFood Delivery\r\nFeedback Information system\r\nNews aggregator\r\nLibrary Management\r\nResult Management System\r\nMessenger\r\nOnline Employee recruitment system\r\nPMS\r\n\r\n\r\nHMS\r\nLive weather forecast\r\nTask Management System\r\nImplementation of Live Weather Forecast Application using Python\r\n\r\n','2023-03-17 16:19:52','Approved');
/*!40000 ALTER TABLE `applicants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `aspirent`
--

DROP TABLE IF EXISTS `aspirent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aspirent` (
  `aspirentid` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `experience` int DEFAULT NULL,
  `company` varchar(20) DEFAULT NULL,
  `emailid` varchar(30) DEFAULT NULL,
  `phone` int DEFAULT NULL,
  `address` tinytext,
  `gender` varchar(20) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`aspirentid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aspirent`
--

LOCK TABLES `aspirent` WRITE;
/*!40000 ALTER TABLE `aspirent` DISABLE KEYS */;
INSERT INTO `aspirent` VALUES (2001,'Eswar nandivada',21,1,'Codegnan','posieswar@gmail.com',25895,'  \r\n        vij','Male','2001');
/*!40000 ALTER TABLE `aspirent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `item` varchar(100) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `price` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `notifid` int NOT NULL,
  `adminid` int DEFAULT NULL,
  `fileupload` longblob,
  `notifname` tinytext,
  `from_date` date DEFAULT NULL,
  `to_date` date DEFAULT NULL,
  `filename` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`notifid`),
  KEY `adminid` (`adminid`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`adminid`) REFERENCES `admin` (`adminid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (235,123,_binary 'Hostel Management System\r\nPatient Management System\r\nOnline Examination System\r\nLibrary Management System\r\nFood Delivery application using Python\r\nCustom Messenger Application\r\nNews aggregator\r\nCalorie Counter Application\r\nImplementation Of Result Management System\r\nFeedback Information system\r\nBuilding a Fully Functional E Commerce Web Application using python\r\nOnline Employee Recruitment System\r\nImplementation of Live Weather Forecast Application using Python\r\nImplementation of Task Management System\r\n\r\n\r\nOnline Examination System\r\nEcommerce\r\nCalorie Counter Application\r\nFood Delivery\r\nFeedback Information system\r\nNews aggregator\r\nLibrary Management\r\nResult Management System\r\nMessenger\r\nOnline Employee recruitment system\r\nPMS\r\n\r\n\r\nHMS\r\nLive weather forecast\r\nTask Management System\r\nImplementation of Live Weather Forecast Application using Python\r\n\r\n','Flask Developer','2023-03-03','2023-03-03','laloyala.txt');
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `ordid` bigint NOT NULL AUTO_INCREMENT,
  `mobile_no` bigint DEFAULT NULL,
  `item` varchar(100) DEFAULT NULL,
  `qty` int DEFAULT NULL,
  `total_price` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`ordid`),
  KEY `mobile_no` (`mobile_no`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`mobile_no`) REFERENCES `signup` (`number`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (5,1234567890,'Chicken Fried Biryani',330,1,'2023-01-24');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `signup`
--

DROP TABLE IF EXISTS `signup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `signup` (
  `name` varchar(100) DEFAULT NULL,
  `number` bigint NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `signup`
--

LOCK TABLES `signup` WRITE;
/*!40000 ALTER TABLE `signup` DISABLE KEYS */;
INSERT INTO `signup` VALUES ('vasima',1234567890,'Female','vasima@123','vasimapatan@gmail.com'),('anusha',6304061929,'Female','Anusha@1999','anushabaditha1999@gmail.com'),('swapna',8500438820,'Female','Anusha@11','nandamswapna@gmail.com'),('Nandivada POSI ESWAR',9177806313,'Male','Eswar@2001','posieswarnandivada@gmail.com');
/*!40000 ALTER TABLE `signup` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-06 17:44:24
