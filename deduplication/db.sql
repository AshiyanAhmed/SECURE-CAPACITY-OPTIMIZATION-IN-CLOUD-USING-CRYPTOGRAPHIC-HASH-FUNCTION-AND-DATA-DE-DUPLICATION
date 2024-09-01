/*
SQLyog Trial v13.1.8 (64 bit)
MySQL - 10.4.10-MariaDB : Database - cetkr_dedup
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cetkr_dedup` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cetkr_dedup`;

/*Table structure for table `assign_work` */

DROP TABLE IF EXISTS `assign_work`;

CREATE TABLE `assign_work` (
  `assign_id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `wid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assign_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `assign_work` */

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `lid` int(11) DEFAULT NULL,
  `cid` int(20) NOT NULL AUTO_INCREMENT,
  `complaint` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `reply` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`lid`,`cid`,`complaint`,`date`,`reply`) values 
(8,1,'bad','2023-04-02 16:20:38','okay will look into it');

/*Table structure for table `doubts` */

DROP TABLE IF EXISTS `doubts`;

CREATE TABLE `doubts` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `doubt` varchar(150) DEFAULT NULL,
  `reply` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `doubts` */

insert  into `doubts`(`did`,`mid`,`date`,`doubt`,`reply`) values 
(1,8,'2023-05-07','jshfjsfsf','pending'),
(2,8,'2023-05-07','What is a doubt?','pending'),
(3,1,'2023-05-07','hask','pending'),
(4,8,'2023-05-07','What is it?','pending'),
(5,16,'2023-05-07','who is it','ok'),
(6,11,'2023-05-07','who is nihal','pending'),
(7,11,'2023-05-07','what','pending'),
(8,16,'2023-05-07','what is it','seri da'),
(9,16,'2023-05-07','new doubt','yes'),
(10,16,'2023-05-07','jhfjh','good doubt\r\n'),
(11,1,'2023-05-07','first doubt','pending');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(20) NOT NULL AUTO_INCREMENT,
  `mid` int(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `feedback` varchar(120) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`mid`,`date`,`feedback`) values 
(1,8,'2023-05-07','Ashiyan is good'),
(2,8,'2023-05-07','Nihal is bad'),
(3,8,'2023-05-07','Arjun is teamleader'),
(4,16,'2023-05-07','its good');

/*Table structure for table `file` */

DROP TABLE IF EXISTS `file`;

CREATE TABLE `file` (
  `fid` int(20) NOT NULL AUTO_INCREMENT,
  `filename` varchar(50) DEFAULT NULL,
  `lid` int(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `hash` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `file` */

insert  into `file`(`fid`,`filename`,`lid`,`description`,`hash`,`date`) values 
(2,'c.png',8,'adaad','c6bafb41a334fb28d24983227184901d07e1623c45146936f55b64a6afe95eebce0ca8e38b254c2a0548dab76e3abc770e05','2023-03-11'),
(3,'abc.jpg',8,'jabajaba','9ed54a59c3f4633f9dec7a4fc91a87c6595a156f38fd4eb8180c610a77f9e0d9a76a13e522057f4e011399175572d45ab89f','2023-04-24');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(90) DEFAULT NULL,
  `password` varchar(90) DEFAULT NULL,
  `type` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(5,'arjun_here','12345','team leader'),
(6,'yoyo','1232133','team leader'),
(8,'ali','ali','member'),
(9,'arjun','arjun','member'),
(10,'ravi','123','team leader'),
(11,'nihal','123','team leader'),
(12,'ashiyan','12345','member'),
(14,'udith','12345','member'),
(15,'adwaid','123','member'),
(16,'razi','123','member'),
(23,'karthik','12345','team leader');

/*Table structure for table `member` */

DROP TABLE IF EXISTS `member`;

CREATE TABLE `member` (
  `mid` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(20) DEFAULT NULL,
  `tid` int(20) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` int(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `member` */

insert  into `member`(`mid`,`lid`,`tid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(2,8,NULL,'Arjun','K','Ramanthali','Payyanur',670351,9876565677,'arjun@gmail.com'),
(3,12,8,'ashiyan','ahmed','pynr','pynr',89383,89776976597,'ashiyan@gmail.com'),
(4,13,8,'imthiyaz','ali','knghd','kasrgod',902380,9481209120,'ali@gmail.com'),
(5,14,8,'udith','nar','cheemeni','cheemeni post',670342,8718265835,'udith@gmail.com'),
(6,15,11,'Adwaid','m v','ezhilode','edat',670342,8726376423,'adwaid@gmail.com'),
(7,16,11,'Razi','Yahya','Matool','matool',670021,6438763847,'razi@gmail.com');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(20) NOT NULL AUTO_INCREMENT,
  `tlid` int(20) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

/*Table structure for table `team leader` */

DROP TABLE IF EXISTS `team leader`;

CREATE TABLE `team leader` (
  `tid` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(20) DEFAULT NULL,
  `fname` varchar(90) DEFAULT NULL,
  `lname` varchar(90) DEFAULT NULL,
  `place` varchar(90) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` int(20) DEFAULT NULL,
  `phone` bigint(90) DEFAULT NULL,
  `email` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `team leader` */

insert  into `team leader`(`tid`,`lid`,`fname`,`lname`,`place`,`post`,`pin`,`phone`,`email`) values 
(4,11,'Nihal','Anwar','Trikaripur','Payyanur',671315,8989878765,'nihal@gmail.com'),
(5,23,'Karthik','Murali','Chandera','Kalikkadavu',670213,8762264758,'karthik@gmail.com');

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `wid` int(20) NOT NULL AUTO_INCREMENT,
  `lid` int(20) DEFAULT NULL,
  `work_name` varchar(10) DEFAULT NULL,
  `work description` varchar(200) DEFAULT NULL,
  `completion date` date DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`wid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`wid`,`lid`,`work_name`,`work description`,`completion date`,`status`) values 
(2,2,'Addition','Adding data','2001-02-02','pending'),
(3,10,'Upload','File Upload','2023-09-09','pending'),
(6,11,'Project','Elixir project','2023-05-31','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
