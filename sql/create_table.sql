DROP TABLE IF EXISTS `transactions_with_card`;
CREATE TABLE `transactions_with_card` (
  `id` int NOT NULL AUTO_INCREMENT,
  `year` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `value` varchar(255) DEFAULT NULL,
  `space` int DEFAULT NULL,
  `time` float(25,20)
  PRIMARY KEY (`id`)
) 