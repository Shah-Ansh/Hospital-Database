-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: Hosp
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Table structure for table `Accountant`
--

DROP TABLE IF EXISTS `Accountant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Accountant` (
  `Accountant_id` int NOT NULL AUTO_INCREMENT,
  `Accountant_name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `DOB` date NOT NULL,
  `Salary` int NOT NULL,
  PRIMARY KEY (`Accountant_id`),
  CONSTRAINT `Accountant_chk_1` CHECK ((`Gender` in (_utf8mb4'M',_utf8mb4'F')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Accountant`
--

LOCK TABLES `Accountant` WRITE;
/*!40000 ALTER TABLE `Accountant` DISABLE KEYS */;
INSERT INTO `Accountant` VALUES (1,'Amit Kumar','M','1990-05-15',60000),(2,'Sneha Sharma','F','1985-08-22',75000),(3,'Rajesh Singh','M','1992-11-08',55000),(4,'Pooja Gupta','F','1988-02-18',70000),(5,'Arjun Patel','M','1995-04-25',80000);
/*!40000 ALTER TABLE `Accountant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alma_Mater_Doctor`
--

DROP TABLE IF EXISTS `Alma_Mater_Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alma_Mater_Doctor` (
  `Doctor_ID` int NOT NULL,
  `Alma_Mater` varchar(255) NOT NULL,
  KEY `FK_Alma_Mater_Doctor_Alma_Mater_Doctor` (`Doctor_ID`),
  CONSTRAINT `FK_Alma_Mater_Doctor_Alma_Mater_Doctor` FOREIGN KEY (`Doctor_ID`) REFERENCES `Doctor` (`Doctor_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alma_Mater_Doctor`
--

LOCK TABLES `Alma_Mater_Doctor` WRITE;
/*!40000 ALTER TABLE `Alma_Mater_Doctor` DISABLE KEYS */;
INSERT INTO `Alma_Mater_Doctor` VALUES (2,'JIPMER'),(3,'PGIMER'),(4,'MMC'),(5,'Sankara Nethralaya'),(6,'AIIMS'),(7,'JIPMER'),(8,'PGIMER'),(9,'MMC'),(10,'Sankara Nethralaya'),(12,'iith');
/*!40000 ALTER TABLE `Alma_Mater_Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Alma_Mater_Nurse`
--

DROP TABLE IF EXISTS `Alma_Mater_Nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Alma_Mater_Nurse` (
  `Nurse_id` int NOT NULL,
  `Alma_Mater` varchar(255) NOT NULL,
  KEY `FK_Alma_Mater_Nurse_Alma_Mater_Nurse` (`Nurse_id`),
  CONSTRAINT `FK_Alma_Mater_Nurse_Alma_Mater_Nurse` FOREIGN KEY (`Nurse_id`) REFERENCES `Nurse` (`Nurse_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Alma_Mater_Nurse`
--

LOCK TABLES `Alma_Mater_Nurse` WRITE;
/*!40000 ALTER TABLE `Alma_Mater_Nurse` DISABLE KEYS */;
INSERT INTO `Alma_Mater_Nurse` VALUES (1,'Mahatma Gandhi Nursing Institute'),(2,'Sarojini Naidu School of Nursing'),(3,'Tagore Medical and Nursing College'),(4,'Indira Gandhi Institute of Nursing'),(5,'Ramanujan Nursing Academy'),(6,'iiith');
/*!40000 ALTER TABLE `Alma_Mater_Nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Bill`
--

DROP TABLE IF EXISTS `Bill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bill` (
  `Case_id` int NOT NULL,
  `Consultation_charges` int NOT NULL,
  `Operation_charges` int DEFAULT NULL,
  `Other_charges` int DEFAULT NULL,
  `Transaction_id` int NOT NULL,
  KEY `FK_Bill_Bill` (`Case_id`),
  CONSTRAINT `FK_Bill_Bill` FOREIGN KEY (`Case_id`) REFERENCES `Cases` (`Case_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bill`
--

LOCK TABLES `Bill` WRITE;
/*!40000 ALTER TABLE `Bill` DISABLE KEYS */;
INSERT INTO `Bill` VALUES (1,500,1000,NULL,101),(3,700,0,NULL,103),(4,800,1200,300,104),(5,900,1500,400,105),(21,1234,123,90,11);
/*!40000 ALTER TABLE `Bill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Cases`
--

DROP TABLE IF EXISTS `Cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Cases` (
  `Case_id` int NOT NULL AUTO_INCREMENT,
  `Patient_id` int NOT NULL,
  `Doctor_id` int DEFAULT NULL,
  `Case_Since` date NOT NULL,
  `Number_of_visits` int NOT NULL,
  `Last_visit` date NOT NULL,
  `Next_Appointment` date DEFAULT NULL,
  `Status` varchar(255) NOT NULL,
  PRIMARY KEY (`Case_id`),
  KEY `FK_patient_in_case` (`Patient_id`),
  KEY `FK_patient_in_case_2` (`Doctor_id`),
  CONSTRAINT `FK_patient_in_case` FOREIGN KEY (`Patient_id`) REFERENCES `Patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_patient_in_case_2` FOREIGN KEY (`Doctor_id`) REFERENCES `Doctor` (`Doctor_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cases`
--

LOCK TABLES `Cases` WRITE;
/*!40000 ALTER TABLE `Cases` DISABLE KEYS */;
INSERT INTO `Cases` VALUES (1,12,2,'2023-01-10',3,'2023-03-05','2023-04-10','In Progress'),(3,14,3,'2023-02-28',1,'2023-03-10',NULL,'SUCCESS'),(4,15,4,'2022-09-20',4,'2022-12-15','2023-12-13','In Progress'),(5,16,5,'2023-03-01',2,'2023-03-15','2023-04-01','In Progress'),(11,12,1,'2023-04-15',3,'2023-04-20','2023-05-10','Scheduled'),(12,13,2,'2023-03-05',1,'2023-03-10','2023-12-13','SUCCESS'),(13,14,3,'2023-05-20',2,'2023-05-25','2023-06-10','Scheduled'),(14,15,4,'2023-02-15',4,'2023-02-20','2023-03-05','Closed'),(15,16,5,'2023-04-10',2,'2023-04-15','2023-05-01','SUCCESS'),(16,17,1,'2023-06-15',3,'2023-06-20','2023-12-13','Scheduled'),(17,18,2,'2023-07-05',1,'2023-07-10','2023-07-20','In Progress'),(18,19,3,'2023-08-20',2,'2023-08-25','2023-09-10','SUCCESS'),(19,20,4,'2023-05-15',4,'2023-05-20','2023-06-05','Closed'),(20,21,5,'2023-07-10',2,'2023-07-15','2023-12-13','In Progress'),(21,32,12,'2023-12-03',1,'2023-12-03','2023-12-10','Active');
/*!40000 ALTER TABLE `Cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `Department_ID` int NOT NULL AUTO_INCREMENT,
  `Department_Name` varchar(255) NOT NULL,
  `HOD_ID` int DEFAULT NULL,
  `Department_Location` varchar(255) NOT NULL,
  PRIMARY KEY (`Department_ID`),
  KEY `FK_Department_Department_UP` (`HOD_ID`),
  CONSTRAINT `FK_Department_Department_UP` FOREIGN KEY (`HOD_ID`) REFERENCES `Doctor` (`Doctor_ID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'Cardiology',7,'T-HUB'),(2,'Neurology',3,'KCIS'),(3,'Dermatology',9,'VINDHYA-A6'),(4,'Pathology',10,'VINDHYA-A4'),(5,'Ophthalmology',11,'VINDHYA-A3');
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Doctor`
--

DROP TABLE IF EXISTS `Doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Doctor` (
  `Doctor_ID` int NOT NULL AUTO_INCREMENT,
  `Doctor_Name` varchar(255) NOT NULL,
  `Speciality` varchar(255) NOT NULL,
  `DOB` date NOT NULL,
  `Date_of_Joining` varchar(255) NOT NULL,
  `Age` varchar(255) NOT NULL,
  `Designation` varchar(255) NOT NULL,
  `Salary` int NOT NULL,
  `Department_ID` int DEFAULT NULL,
  PRIMARY KEY (`Doctor_ID`),
  KEY `FK_Doctor_Doctor` (`Department_ID`),
  CONSTRAINT `FK_Doctor_Doctor` FOREIGN KEY (`Department_ID`) REFERENCES `Department` (`Department_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Doctor`
--

LOCK TABLES `Doctor` WRITE;
/*!40000 ALTER TABLE `Doctor` DISABLE KEYS */;
INSERT INTO `Doctor` VALUES (1,'Dr. John Smith','Cardiologist','1980-01-15','2020-05-01','43','Senior Cardiologist',120000,1),(2,'Dr. Ananya Sharma','Cardiologist','1980-05-15','2021-01-15','42','Senior Consultant',1200000,1),(3,'Dr. Rajesh Patel','Neurologist','1975-08-22','2022-03-10','47','Head of Department',999999,2),(4,'Dr. Priya Kapoor','Dermatologist','1982-11-08','2020-07-05','39','Consultant',1000000,3),(5,'Dr. Arjun Menon','Pathologist','1978-02-18','2023-02-01','44','Senior Consultant',1300000,4),(6,'Dr. Sneha Joshi','Ophthalmologist','1985-04-25','2021-09-20','37','Consultant',1100000,5),(7,'Dr. Rahul Singh','Cardiologist','1987-06-30','2022-05-12','35','Head of Department',1600000,1),(8,'Dr. Nisha Reddy','Neurologist','1983-09-17','2020-11-08','38','Consultant',1100000,2),(9,'Dr. Aryan Kapoor','Dermatologist','1989-12-03','2023-04-15','32','Head of Department',1400000,3),(10,'Dr. Neha Verma','Pathologist','1984-03-20','2021-07-01','38','Head of Department',1200000,4),(11,'Dr. Karthik Rajan','Ophthalmologist','1986-07-12','2022-08-25','36','Head of Department',1700000,5),(12,'Neel','MBA','2004-12-01','2021-12-04','30','Heart',60000,2);
/*!40000 ALTER TABLE `Doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Medical_History`
--

DROP TABLE IF EXISTS `Medical_History`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Medical_History` (
  `Patient_id` int NOT NULL,
  `Diabetic` tinyint(1) NOT NULL,
  `Blood_pressure` tinyint(1) NOT NULL,
  `Description_of_past_conditions` varchar(255) DEFAULT NULL,
  KEY `FK_Medical_History_Medical_History_Update` (`Patient_id`),
  CONSTRAINT `FK_Medical_History_Medical_History_Update` FOREIGN KEY (`Patient_id`) REFERENCES `Patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Medical_History`
--

LOCK TABLES `Medical_History` WRITE;
/*!40000 ALTER TABLE `Medical_History` DISABLE KEYS */;
INSERT INTO `Medical_History` VALUES (12,1,0,'No significant past conditions'),(13,0,1,'Hypertension diagnosed last year'),(14,1,1,'Type 2 diabetes, controlled with medication'),(15,0,0,'No past conditions reported'),(16,1,1,'History of allergies and asthma');
/*!40000 ALTER TABLE `Medical_History` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Nurse`
--

DROP TABLE IF EXISTS `Nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Nurse` (
  `Nurse_id` int NOT NULL AUTO_INCREMENT,
  `Nurse_name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `Salary` int NOT NULL,
  PRIMARY KEY (`Nurse_id`),
  CONSTRAINT `Nurse_chk_1` CHECK ((`Gender` in (_utf8mb4'M',_utf8mb4'F')))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Nurse`
--

LOCK TABLES `Nurse` WRITE;
/*!40000 ALTER TABLE `Nurse` DISABLE KEYS */;
INSERT INTO `Nurse` VALUES (1,'Sakshi Sharma','F',55000),(2,'Rahul Kumar','M',60000),(3,'Neha Singh','F',50000),(4,'Amit Patel','M',65000),(5,'Priya Gupta','F',60000),(6,'ARCHIT','M',12);
/*!40000 ALTER TABLE `Nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Patient`
--

DROP TABLE IF EXISTS `Patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Patient` (
  `Patient_ID` int NOT NULL AUTO_INCREMENT,
  `Patient_Name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `Mobile_Number` bigint NOT NULL,
  `Blood_Group` varchar(255) NOT NULL,
  PRIMARY KEY (`Patient_ID`),
  CONSTRAINT `Patient_chk_1` CHECK ((`Gender` in (_utf8mb4'M',_utf8mb4'F')))
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Patient`
--

LOCK TABLES `Patient` WRITE;
/*!40000 ALTER TABLE `Patient` DISABLE KEYS */;
INSERT INTO `Patient` VALUES (12,'Aarav Kapoor','M',9876543210,'B+'),(13,'Diya Shah','F',8765432109,'O-'),(14,'Kabir Sharma','M',7654321098,'A+'),(15,'Aanya Singh','F',6543210987,'AB-'),(16,'Vihaan Patel','M',5432109876,'O+'),(17,'Anika Joshi','F',9876543211,'B-'),(18,'Advait Verma','M',8765432101,'A+'),(19,'Zara Khan','F',7654321092,'O-'),(20,'Arjun Khanna','M',6543210983,'AB+'),(21,'Ria Sharma','F',5432109874,'A+'),(22,'Vivaan Kapoor','M',9876543212,'A-'),(23,'Kiara Patel','F',8765432103,'B+'),(24,'Reyansh Singh','M',7654321094,'AB-'),(25,'Aaradhya Gupta','F',6543210985,'O+'),(26,'Aarav Malhotra','M',5432109876,'B-'),(27,'Diya Verma','F',9876543213,'A+'),(28,'Kabir Mehta','M',8765432104,'O-'),(29,'Aanya Kapoor','F',7654321095,'AB+'),(30,'Vihaan Sharma','M',6543210986,'O+'),(31,'Anaya Patel','F',5432109877,'B-'),(32,'Divyaraj','M',9898778866,'A+');
/*!40000 ALTER TABLE `Patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prerequisite_test`
--

DROP TABLE IF EXISTS `Prerequisite_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prerequisite_test` (
  `Test_type` varchar(255) NOT NULL,
  `Prerequisite_tests` varchar(255) NOT NULL,
  PRIMARY KEY (`Test_type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prerequisite_test`
--

LOCK TABLES `Prerequisite_test` WRITE;
/*!40000 ALTER TABLE `Prerequisite_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `Prerequisite_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Prescription`
--

DROP TABLE IF EXISTS `Prescription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Prescription` (
  `Case_id` int NOT NULL,
  `Prescription_no` int NOT NULL,
  `Medicines` varchar(255) NOT NULL,
  KEY `FK_Prescription_Prescription` (`Case_id`),
  CONSTRAINT `FK_Prescription_Prescription` FOREIGN KEY (`Case_id`) REFERENCES `Cases` (`Case_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Prescription`
--

LOCK TABLES `Prescription` WRITE;
/*!40000 ALTER TABLE `Prescription` DISABLE KEYS */;
INSERT INTO `Prescription` VALUES (1,101,'Aspirin, Metoprolol'),(3,103,'Acetaminophen, Amoxicillin'),(4,104,'Atorvastatin, Lisinopril'),(5,105,'Eye Drops, Prednisolone'),(1,101,'Aspirin, Metoprolol'),(3,103,'Acetaminophen, Amoxicillin'),(4,104,'Atorvastatin, Lisinopril'),(5,105,'Eye Drops, Prednisolone'),(21,123,'DOLO65');
/*!40000 ALTER TABLE `Prescription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Previous_Cases`
--

DROP TABLE IF EXISTS `Previous_Cases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Previous_Cases` (
  `Case_id` int NOT NULL,
  `Patient_ID` int NOT NULL,
  KEY `FK_Previous_Cases_Previous_Cases` (`Case_id`),
  KEY `FK_Previous_Cases_Previous_Cases_1` (`Patient_ID`),
  CONSTRAINT `FK_Previous_Cases_Previous_Cases` FOREIGN KEY (`Case_id`) REFERENCES `Cases` (`Case_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Previous_Cases_Previous_Cases_1` FOREIGN KEY (`Patient_ID`) REFERENCES `Patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Previous_Cases`
--

LOCK TABLES `Previous_Cases` WRITE;
/*!40000 ALTER TABLE `Previous_Cases` DISABLE KEYS */;
/*!40000 ALTER TABLE `Previous_Cases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Receptionist`
--

DROP TABLE IF EXISTS `Receptionist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Receptionist` (
  `Receptionist_id` int NOT NULL AUTO_INCREMENT,
  `Receptionist_Name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `DOB` date NOT NULL,
  `Salary` int NOT NULL,
  PRIMARY KEY (`Receptionist_id`),
  CONSTRAINT `Receptionist_chk_1` CHECK ((`Gender` in (_utf8mb4'M',_utf8mb4'F')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Receptionist`
--

LOCK TABLES `Receptionist` WRITE;
/*!40000 ALTER TABLE `Receptionist` DISABLE KEYS */;
INSERT INTO `Receptionist` VALUES (1,'Renu Sharma','F','1992-03-15',60000),(2,'Vikram Singh','M','1988-07-22',65000),(3,'Anjali Kapoor','F','1990-11-08',55000),(4,'Rajesh Patel','M','1985-05-18',70000),(5,'Neha Gupta','F','1987-09-25',75000);
/*!40000 ALTER TABLE `Receptionist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tests`
--

DROP TABLE IF EXISTS `Tests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tests` (
  `Case_id` int NOT NULL,
  `Test_type` varchar(255) NOT NULL,
  `Test_result` varchar(255) NOT NULL,
  KEY `FK_Tests_Tests_Update` (`Case_id`),
  CONSTRAINT `FK_Tests_Tests_Update` FOREIGN KEY (`Case_id`) REFERENCES `Cases` (`Case_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tests`
--

LOCK TABLES `Tests` WRITE;
/*!40000 ALTER TABLE `Tests` DISABLE KEYS */;
INSERT INTO `Tests` VALUES (1,'Blood Test','Normal'),(3,'X-ray','Negative'),(4,'CT Scan','Positive'),(5,'Ultrasound','Normal');
/*!40000 ALTER TABLE `Tests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Workers`
--

DROP TABLE IF EXISTS `Workers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Workers` (
  `Worker_id` int NOT NULL AUTO_INCREMENT,
  `Worker_name` varchar(255) NOT NULL,
  `Gender` char(1) NOT NULL,
  `DOB` date NOT NULL,
  `Salary_per_hour` int NOT NULL,
  `Shift` int NOT NULL,
  `Number_of_hours_worked_in_current_week` int NOT NULL,
  PRIMARY KEY (`Worker_id`),
  CONSTRAINT `Workers_chk_1` CHECK ((`Gender` in (_utf8mb4'M',_utf8mb4'F')))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Workers`
--

LOCK TABLES `Workers` WRITE;
/*!40000 ALTER TABLE `Workers` DISABLE KEYS */;
INSERT INTO `Workers` VALUES (1,'Amit Kumar','M','1993-05-15',200,1,40),(2,'Sneha Sharma','F','1988-08-22',250,2,35),(3,'Rajesh Singh','M','1995-11-08',180,1,38),(4,'Pooja Gupta','F','1990-02-18',220,2,30),(5,'Arjun Patel','M','1997-04-25',240,1,42);
/*!40000 ALTER TABLE `Workers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03  3:43:12
