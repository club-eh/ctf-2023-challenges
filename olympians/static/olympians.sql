-- MariaDB dump 10.19  Distrib 10.6.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: ctf
-- ------------------------------------------------------
-- Server version	10.6.8-MariaDB-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `one`
--

DROP TABLE IF EXISTS `one`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `one` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `description` char(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `one`
--

LOCK TABLES `one` WRITE;
/*!40000 ALTER TABLE `one` DISABLE KEYS */;
INSERT INTO `one` VALUES (1,'Zeus','Also known as Jupiter, king of Gods and ruler of Mount Olympus. God of the sky, thunder, law, order, and justice.'),(2,'Hera','Also known as Juno, queen of the Gods and the Goddess of marriage, women, childbirth, and family.'),(3,'.x.fLaG.x.','.x.CTF{2ln5KOVKYvd1QMN4FL}.x.'),(4,'Poseidon','Also known as Neptune, god of the seas, water, storms, hurricanes, earthquakes and horses.'),(5,'Dementer','Also known as Ceres, goddess of the harvest, fertility, agriculture, nature and the seasons. She presided over grains and the fertility of the earth.'),(6,'Athena','Also known as Minerva, goddess of wisdom, handicraft, and warfare. The daughter of Zeus and the Oceanid Metis.'),(7,'Apollo','God of light, the Sun, prophecy, philosophy, archery, truth, inspiration, poetry, music, arts, manly beauty, medicine, healing, and plague.'),(8,'Artemis','Also known as Diana, goddess of the hunt, the wilderness, virginity, the Moon, archery, childbirth, protection and plague.'),(9,'Ares','Also known as Mars, god of war, violence, bloodshed and manly virtues.'),(10,'Aphrodite','Also known as Venus, goddess of love, pleasure, passion, procreation, fertility, beauty and desire.'),(11,'Hephaestus','Also known as Vulcan, god of the forge. Master blacksmith and craftsman of the gods.'),(12,'Hermes','Also known as Mercury, messenger of the gods; god of travel, commerce, communication, borders, eloquence, diplomacy, thieves, and games. He was also the guide of dead souls.'),(13,'Dionysus','Also known as Bacchus, god of wine, the grapevine, fertility, festivity, ecstasy, madness and resurrection. Patron god of the art of theatre.');
/*!40000 ALTER TABLE `one` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-08-02 22:03:14
