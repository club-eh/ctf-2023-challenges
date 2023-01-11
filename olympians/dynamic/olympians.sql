CREATE DATABASE `ctf`;

USE `ctf`;

DROP TABLE IF EXISTS `olympians`;
CREATE TABLE `olympians` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `description` char(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4;

LOCK TABLES `olympians` WRITE;
INSERT INTO `olympians` VALUES (1,'Zeus','Also known as Jupiter, king of Gods and ruler of Mount Olympus. God of the sky, thunder, law, order, and justice.'),(2,'Hera','Also known as Juno, queen of the Gods and the Goddess of marriage, women, childbirth, and family.'),(4,'Poseidon','Also known as Neptune, god of the seas, water, storms, hurricanes, earthquakes and horses.'),(5,'Dementer','Also known as Ceres, goddess of the harvest, fertility, agriculture, nature and the seasons. She presided over grains and the fertility of the earth.'),(6,'Athena','Also known as Minerva, goddess of wisdom, handicraft, and warfare. The daughter of Zeus and the Oceanid Metis.'),(7,'Apollo','God of light, the Sun, prophecy, philosophy, archery, truth, inspiration, poetry, music, arts, manly beauty, medicine, healing, and plague.'),(8,'Artemis','Also known as Diana, goddess of the hunt, the wilderness, virginity, the Moon, archery, childbirth, protection and plague.'),(9,'Ares','Also known as Mars, god of war, violence, bloodshed and manly virtues.'),(10,'Aphrodite','Also known as Venus, goddess of love, pleasure, passion, procreation, fertility, beauty and desire.'),(11,'Hephaestus','Also known as Vulcan, god of the forge. Master blacksmith and craftsman of the gods.'),(12,'Hermes','Also known as Mercury, messenger of the gods; god of travel, commerce, communication, borders, eloquence, diplomacy, thieves, and games. He was also the guide of dead souls.'),(13,'Dionysus','Also known as Bacchus, god of wine, the grapevine, fertility, festivity, ecstasy, madness and resurrection. Patron god of the art of theatre.'),(14,'qC2b0w6ZVlGY2aPH','xkcd.com/327/clubeh{41w4y5_54n17123_1npu75_BC42dpKy}');
UNLOCK TABLES;
