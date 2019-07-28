CREATE TABLE `links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `kurzbeschreibung` varchar(250) DEFAULT NULL,
  `link` varchar(300) NOT NULL,
  `erstpreis` float NOT NULL,
  `wunschpreis` float DEFAULT (((`erstpreis` / 4) * 3)),
  `hinzugefuegt` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `link_UNIQUE` (`link`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ALTER USER 'db_user'@'%' IDENTIFIED WITH mysql_native_password BY "the_password";