SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `dbProject` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `dbProject`;


DELIMITER ;

DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS carts;

CREATE TABLE IF NOT EXISTS `carts` (
  `uid` int(12) NOT NULL AUTO_INCREMENT,
  `customer` int(8) NOT NULL,
  `items` text NOT NULL,
  `price` int(8) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;


CREATE TABLE IF NOT EXISTS `products` (
  `uid` int(12) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `description` text NOT NULL,
  `price` int(8) NOT NULL DEFAULT '0',
  `stock` int(8) NOT NULL DEFAULT '0',
  `hidden` tinyint(8) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;


CREATE TABLE IF NOT EXISTS `users` (
  `uid` int(12) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `ssn` varchar(50) NOT NULL,
  `email` varchar(64) NOT NULL,
  `adress` varchar(64) NOT NULL,
  `zip_code` varchar(8) NOT NULL,
  `city` varchar(64) NOT NULL DEFAULT '',
  `phone` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  `cart_uid` int(8),
  `adminlevel` int(8) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`),
  UNIQUE KEY `ssn` (`ssn`),
  FOREIGN KEY (cart_uid) REFERENCES carts(uid)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;


CREATE TABLE IF NOT EXISTS `orders` (
  `uid` int(12) NOT NULL AUTO_INCREMENT,
  `customer` int(8) NOT NULL,
  `delivery_adress` varchar(64) NOT NULL,
  `delivery_zip` varchar(8) NOT NULL,
  `delivery_city` varchar(64) NOT NULL,
  `cart_uid` int(8) NOT NULL,
  `price` int(16) NOT NULL DEFAULT '0',
  PRIMARY KEY (`uid`),
  FOREIGN KEY (customer) REFERENCES users(uid)
  FOREIGN KEY (cart_uid) REFERENCES carts(uid)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;



INSERT INTO users (name,ssn,adress,email,zip_code,phone,password,adminlevel) VALUES ('Johan Kannel','12345','asdasd','johan.kannel@gmail.com',1232,24323,'123',3);
INSERT INTO users (name,ssn,adress,email,zip_code,phone,password,adminlevel) VALUES ('Fredrik Uvgård','123456','asdasd','fredrik.uvgard@gmail.com',1232,24323,'123',3);

INSERT INTO products (name,description,price,stock) VALUES ('Red ball','A basic red ball. Diameter: 1 meter',50,4);
INSERT INTO products (name,description,price,stock) VALUES ('Grass mower','A supersonic grassmower that mows your entire lawn in less than 2 seconds.',3000,1);
INSERT INTO products (name,description,price,stock) VALUES ('Space ship','Allows travel to other universes in little time!',2000,3);
