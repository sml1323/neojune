-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: kt2.elementsoft.biz    Database: kipris
-- ------------------------------------------------------
-- Server version	8.0.39

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
-- Table structure for table `tb24_110`
--

DROP TABLE IF EXISTS `tb24_110`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb24_110` (
  `uni_seq` int NOT NULL AUTO_INCREMENT,
  `biz_no` varchar(12) DEFAULT NULL,
  `corp_no` varchar(15) DEFAULT NULL,
  `applicant` varchar(50) NOT NULL,
  PRIMARY KEY (`uni_seq`)
) ENGINE=InnoDB AUTO_INCREMENT=390 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb24_110`
--

/*!40000 ALTER TABLE `tb24_110` DISABLE KEYS */;
INSERT INTO `tb24_110` VALUES (1,'510-82-01254','171331-0000045','김천대학교'),(2,' --','111331-0000154','대진대학교'),(3,' --','134511-0078144','경희대학교한방재료가공센터'),(4,' --','120171-0003917','가천의과학대학교 산학협력단'),(5,'301-82-14193','154731-0002937','청주대학교 산학협력단'),(6,'401-82-06498','211171-0001911','군장대학교 산학협력단'),(7,'616-82-16598','220171-0003255','제주한라대학교 산학협력단'),(8,'125-82-07370','131331-0002924','평택대학교 산학협력단'),(9,'204-82-07090','264271-0005033','서일대학교 산학협력단'),(10,'227-82-07190','144431-0001739','경동대학교 산학협력단'),(11,'119-82-03684','114371-0009224','서울대학교 산학협력단'),(12,'608-82-10332','190131-0003818','마산대학교 산학협력단'),(13,'505-82-06878','171271-0002164','경주대학교 산학협력단'),(14,'305-82-13385','160171-0004131','대전대학교 산학협력단'),(15,'120-82-07211','114671-0032500','서울벤처대학원대학교 산학협력단'),(16,'312-82-10329','161571-0004562','백석문화대학교 산학협력단'),(17,' --','200131-0000150','호남신학대학교'),(18,'605-82-08254','184171-0004480','동의대학교 산학협력단'),(19,' --','141271-0002714','상지영서대학교 산학협력단'),(20,'506-82-07282','171771-0003542','한동대학교 산학협력단'),(21,'310-82-05039','161171-0001631','청운대학교 산학협력단'),(22,'410-82-13479','204271-0002346','광주여자대학교 산학협력단'),(23,'616-82-16211','220171-0003148','제주관광대학교 산학협력단'),(24,'616-82-16453','220171-0003297','제주국제대학교 산학협력단'),(25,'206-86-27616','110111-3965732','한양대학교 기술지주회사'),(26,' --','131471-0015765','안산대학교 산학협력단'),(27,'312-82-10197','161571-0004637','백석대학교 산학협력단'),(28,'606-82-06939','184471-0002751','부산과학기술대학교 산학협력단'),(29,'403-82-09172','214971-0011218','원광보건대학교 산학협력단'),(30,'119-86-11824','110111-3992678','서울대학교 기술지주 '),(31,'402-82-15670','215171-0005703','전주비전대학교 산학협력단'),(32,' --','170171-0005989','수성대학교 산학협력단'),(33,'109-82-09788','254231-0005401','강서대학교 산학협력단'),(34,'505-82-09007','171271-0003154','동국대학교 와이즈캠퍼스 산학협력단'),(35,'217-81-27815','110111-4033017','삼육대학교 기술지주 '),(36,'408-82-13345','204171-0001390','광주대학교 산학협력단'),(37,'105-87-29638','110111-4066430','서강대학교 기술지주 '),(38,' --','144771-0001573','한중대학교 산학협력단'),(39,' --','194271-0004387','창원문성대학교 산학협력단'),(40,' --','184771-0000501','부산가톨릭대학교 산학협력단'),(41,' --','224171-0003441','탐라대학교 산학협력단'),(42,' --','114621-0029487','고려대학교공과대학교우장학회'),(43,'407-82-06216','211371-0004359','서남대학교 산학협력단'),(44,'209-81-49399','110111-4187765','고려대학교 기술지주 '),(45,' --','210131-0000025','예수대학교'),(46,' --','185171-0002938','고신대학교 산학협력단'),(47,' --','114471-0003000','동방대학원대학교 산학협력단'),(48,'131-86-17717','120111-0515348','인천대학교 기술지주 '),(49,'513-82-06995','176071-0002171','구미대학교 산학협력단'),(50,'127-82-12748','280171-0002065','경민대학교 산학협력단'),(51,' --','174171-0001686','영남이공대학교 산학협력단'),(52,'603-82-06565','121131-0002912','서울디지털대학교'),(53,'408-82-11027','204122-0000353','조선대학교 치과대학 교육문화재단'),(54,'621-81-83563','180111-0705913','부산대학교 기술지주'),(55,'120-82-07623','114671-0033433','한림국제대학원대학교 산학협력단'),(56,'201-86-15115','110111-4307355','동국대학교 기술지주 '),(57,'317-82-02348','154471-0004985','중원대학교 산학협력단'),(58,'504-82-09703','176271-0001947','대구과학대학교 산학협력단'),(59,'113-82-05855','254371-0011486','성공회대학교 산학협력단'),(60,'411-82-08310','205731-0004139','초당대학교 산학협력단'),(61,'506-82-07389','171771-0003500','포항대학교 산학협력단'),(62,'621-82-07091','234171-0001287','영산대학교 산학협력단'),(63,'408-81-88801','200111-0308126','조선대학교 기술지주 '),(64,'209-82-08599','114471-0002622','동덕여자대학교 산학협력단'),(65,'123-82-11863','135271-0001128','계원예술대학교 산학협력단'),(66,'409-86-21147','200111-0319735','전남대학교 기술지주회사'),(67,' --','114631-0037843','한국전력국제원자력대학원대학교'),(68,' --','120111-0570508','연세대학교 기술지주 '),(69,'307-82-06385','161231-0002699','한국영상대학교 산학협력단'),(70,'129-82-07580','131171-0002429','신구대학교 산학협력단'),(71,'217-82-04162','260171-0004156','한국성서대학교 산학협력단'),(72,'310-82-04724','164671-0001282','충남도립대학교 산학협력단'),(73,'134-82-10205','131471-0017977','한양대학교 에리카 산학협력단'),(74,' --','210131-0003029','예원예술대학교'),(75,'224-82-14988','141271-0004893','연세대학교 원주 산학협력단'),(76,'308-82-08289','164371-0004414','한국전통문화대학교 산학협력단'),(77,' --','264371-0004603','서울사이버대학교 산학협력단'),(78,'125-82-00760','134631-0000036','국제대학교'),(79,' --','280171-0002073','서정대학교 산학협력단'),(80,' --','110111-4875659','가톨릭대학교 기술지주 '),(81,'124-82-14432','134871-0005418','수원과학대학교 산학협력단'),(82,'209-82-08468','114471-0002664','서경대학교 산학협력단'),(83,' --','171711-0100063','포항공과대학교 기술지주 '),(84,' --','154571-0002614','강동대학교 산학협력단'),(85,'312-82-16264','161571-0007417','단국대학교 천안캠퍼스 산학협력단'),(86,'616-81-98007','220111-0092634','제주대학교 기술지주 '),(87,'206-86-66754','110111-4892398','세종대학교 기술지주 '),(88,'130-82-13627','121171-0001697','부천대학교 산학협력단'),(89,' --','230111-0196450','울산대학교 기술지주 '),(90,' --','254231-0006110','서울미디어대학원대학교 산학협력단'),(91,'408-82-13480','200171-0008788','조선이공대학교 산학협력단'),(92,'125-82-07332','131371-0002871','한국복지대학교 산학협력단'),(93,'615-82-08488','175071-0002122','가야대학교 산학협력단'),(94,'101-82-22512','110371-0013146','상명대학교 산학협력단'),(95,'211-88-48198','110111-4421725','국제대학교류원'),(96,'307-82-08705','164771-0004747','홍익대학교 세종캠퍼스 산학협력단'),(97,'610-82-13929','230171-0005465','한국전력 국제원자력대학원대학교 산학협력단'),(98,'124-87-32925','135811-0215426','성균관대학교 기술지주 '),(99,'127-82-12603','284431-0016359','경복대학교 산학협력단'),(100,'512-82-05237','175571-0001835','경북도립대학교 산학협력단'),(101,'212-82-08386','244171-0010484','국제영어대학원대학교 산학협력단'),(102,'504-86-07310','170111-0498031','경북대학교 기술지주 '),(103,'603-81-82061','180111-0828608','동아대학교 기술지주 '),(104,'121-82-15183','120171-0005905','청운대학교 인천캠퍼스 산학협력단'),(105,'134-87-14865','131411-0304528','한양대학교에리카 기술지주 '),(106,'126-82-07844','131271-0001114','여주대학교 산학협력단'),(107,'124-82-14766','134871-0005674','협성대학교 산학협력단'),(108,'314-86-52089','160111-0356025','한남대학교 기술지주회사 '),(109,'305-82-04964','160131-0000183','중부대학교'),(110,'206-82-07378','240171-0007675','한양여자대학교 산학협력단'),(111,'617-86-14117','180111-0890243','국립부경대학교 기술지주'),(112,'108-86-09672','110111-5317535','중앙대학교 기술지주 '),(113,'314-86-57013','160111-0365571','한밭대학교 기술지주 '),(114,'206-86-85687','110111-5298991','건국대학교 기술지주 '),(115,'410-82-13125','204171-0001332','송원대학교 산학협력단'),(116,'401-81-53451','211151-0005163','군산대학교건설소재알앤디협동조합'),(117,'404-82-05445','211231-0006294','전북과학대학교 산학협력단'),(118,'312-86-67932','164811-0080395','순천향대학교 기술지주회사'),(119,'617-86-19335','180111-0912922','부경대학교어간장연구소'),(120,'126-82-10072','134271-0001690','서울장신대학교 산학협력단'),(121,'515-82-06633','174871-0003753','호산대학교 산학협력단'),(122,'602-81-66525','180111-0940262','한국해양대학교 기술지주'),(123,'131-82-15711','120131-0005777','국립대학법인 인천대학교'),(124,'206-82-13206','240171-0010313','세종사이버대학교 산학협력단'),(125,'611-82-07755','191471-0002083','한국승강기대학교 산학협력단'),(126,'510-82-60724','171371-0002237','김천대학교 산학협력단'),(127,'613-82-09915','191171-0001560','연암공과대학교 산학협력단'),(128,'140-81-82139','135511-0259488','한국공학대학교 기술지주회사'),(129,'409-82-00708','200121-0000044','전남대학교출판부'),(130,'122-82-07541','124871-0003844','경인여자대학교 산학협력단'),(131,'408-82-18340','200131-0019383','송원대학교'),(132,'303-82-10645','151171-0004322','건국대학교 글로컬 산학협력단'),(133,'511-82-04142','175471-0002520','문경대학교 산학협력단'),(134,'612-82-05783','194971-0001529','거제대학교 산학협력단'),(135,'126-82-07863','134471-0002230','한국관광대학교 산학협력단'),(136,'579-87-00278','150111-0214895','충북대학교 기술지주 '),(137,'116-82-03287','111221-0001155','한국전문대학교육협의회'),(138,'898-88-00399','134611-0077590','한경대학교 기술지주 '),(139,'393-88-00308','134511-0282547','명지대학교 기술지주회사'),(140,'621-82-08538','184771-0000717','대동대학교 산학협력단'),(141,'630-82-00092','164771-0006826','고려대학교 세종 산학협력단'),(142,'118-81-32189','191111-0072319','경상국립대학교 기술지주 '),(143,'877-81-00340','161511-0193783','한국기술교육대학교 기술지주 '),(144,'267-88-00498','165011-0055393','세한대학교 기술지주회사 '),(145,'465-88-00506','110111-6088903','숙명여자대학교 기술지주 '),(146,'699-88-00415','110111-6161577','이화여자대학교 기술지주 '),(147,'201-82-07223','110171-0029783','숭의여자대학교 산학협력단'),(148,'818-86-00706','161211-0039553','공주대학교 기술지주 '),(149,'110-82-15112','274171-0006990','서울과학종합대학원대학교 산학협력단'),(150,'315-86-00788','151111-0061641','한국교통대학교 기술지주 '),(151,'812-81-00907','120111-0890534','가톨릭관동대학교 기술지주 '),(152,'142-81-31072','134511-0159118','단국대학교 기술지주회사'),(153,'244-87-00713','160111-0453285','충남대학교 기술지주 '),(154,'289-81-00747','131111-0484722','가천대학교 기술지주 '),(155,'675-81-00837','174811-0090011','대구한의대학교 기술지주'),(156,'408-82-13914','200171-0008796','조선간호대학교 산학협력단'),(157,'206-82-06194','111131-0000017','장로회신학대학교'),(158,'514-82-09850','176131-0000680','대구공업대학교 산학협력단'),(159,'125-82-07157','135471-0008972','국제대학교 산학협력단'),(160,'610-82-10636','230171-0002990','춘해보건대학교 산학협력단'),(161,'322-81-00855','110111-6614047','서울시립대학교 기술지주 '),(162,'507-81-14760','120111-0916611','인하대학교 기술지주 '),(163,'563-81-00908','160111-0466733','대전대학교 기술지주 '),(164,'142-81-20537','134511-0139441','경희대학교 기술지주 '),(165,'214-82-15001','110271-0012893','서울외국어대학원대학교 산학협력단'),(166,'210-82-08570','111322-0003884','서울과학기술대학교 아이티정책 전문대학원 교육연구재단'),(167,'608-86-10631','164811-0113625','호서대학교 기술지주회사'),(168,'131-84-00774','120185-0000162','겐트대학교코리아(분사무소)'),(169,'322-82-00250','161571-0010741','국제뇌교육종합대학원대학교 산학협력단'),(170,'390-86-01134','195511-0223689','인제대학교 기술지주 '),(171,'883-87-00954','194211-0290560','창원대학교 기술지주 '),(172,'606-86-63700','110111-6835312','서울과학기술대학교 기술지주'),(173,'131-84-00681','120185-0000112','수니코리아 엘엘씨(한국뉴욕주립대학교)'),(174,'135-82-10834','135971-0001364','동남보건대학교 산학협력단'),(175,'618-88-01244','211111-0055641','군산대학교 기술지주'),(176,'403-86-01406','210111-0143249','전북대학교 기술지주회사'),(177,'832-81-01410','110111-7127081','광운대학교 기술지주 '),(178,'449-87-00910','110111-6599356','숭실대학교 기술지주 '),(179,'654-86-01396','210111-0145477','전주대학교 기술지주회사'),(180,'633-82-00091','120171-0026117','인천가톨릭대학교 산학협력단'),(181,'372-82-00221','161571-0011640','글로벌사이버대학교 산학협력단'),(182,'417-82-05529','204731-0002316','한영대학교 산학협력단'),(183,'119-82-08433','110171-0068062','국립대학법인 서울대학교'),(184,'214-82-08306','110271-0011192','서울교육대학교 산학협력단'),(185,'110-82-14452','274271-0005396','서울기독대학교 산학협력단'),(186,'660-81-01775','174811-0106678','영남대학교 기술지주'),(187,'798-82-00379','205531-0009498','한국전력공과대학교'),(188,'155-88-00652','170111-0637879','국제기능대학교'),(189,'696-86-01857','134111-0563044','한림대학교 기술지주 '),(190,'528-87-02322','220111-0213298','제주한라대학교 기술지주'),(191,'615-82-07140','195571-0003176','김해대학교 산학협력단'),(192,'119-87-09382','201311-0085612','순천대학교 기술지주 '),(193,'416-82-14307','201371-0002206','청암대학교 산학협력단'),(194,'102-82-02673','110122-0002386','고려대학교교우장학회'),(195,'668-88-02141','180111-1351335','동의대학교 기술지주 '),(196,'221-81-47033','140111-0056166','강원대학교 기술지주회사'),(197,'657-87-02353','110111-8028189','연세대학교 바이오헬스 기술지주회사'),(198,'592-86-02097','135811-0424522','아주대학교 기술지주 '),(199,'215-82-07955','244271-0004716','한국체육대학교 산학협력단'),(200,'609-88-01667','110111-7481932','창업대학교 '),(201,'793-82-00340','205571-0009816','한국에너지공과대학교'),(202,'845-88-02151','150151-0016578','충청대학교 바이오테크 협동조합'),(203,'195-81-01719','150151-0015801','충청대학교 항공기술교육 협동조합'),(204,'607-82-09924','180171-0007454','부산교육대학교 산학협력단'),(205,'777-87-02244','164711-0126034','한국영상대학교 기술지주 '),(206,'124-82-17351','134871-0007258','신경대학교 산학협력단'),(207,'101-82-22792','110371-0013617','한국열린사이버대학교 산학협력단'),(208,'128-82-12101','285071-0005933','농협대학교 산학협력단'),(209,'291-82-00408','120171-0033279','겐트대학교코리아 산학협력단'),(210,'789-81-03017','180111-1475250','동서대학교 기술지주 '),(211,'209-88-01133','110111-6944147','국민대학교 기술지주'),(212,'621-82-06582','234171-0001253','동원과학기술대학교 산학협력단'),(213,'110-82-10494','274171-0006255','추계예술대학교 산학협력단'),(214,'709-81-02856','151111-0090856','건국대학교글로컬 기술지주'),(215,'308-82-06073','154631-0000363','금강대학교'),(216,'139-82-17784','120171-0031801','한국뉴욕주립대학교 산학협력단'),(217,'505-82-06937','174771-0001080','성운대학교 산학협력단'),(218,'265-81-03281','160111-0689541','목원대학교 기술지주 '),(219,'108-82-03160','115031-0000023','대한예수교장로회총신대학교'),(220,'134-82-06813','131471-0015814','서울예술대학교 산학협력단'),(221,'110-82-00282',' -','연세대학교'),(222,'506-82-03966',' -','한동대학교'),(223,'514-82-00577',' -','계명대학교'),(224,'112-82-00240',' -','서울대학교발전재단'),(225,'314-83-03215',' -','대한민국(한국전통문화대학교 총장)'),(226,'227-82-00412',' -','경동대학교'),(227,'307-83-00485',' -','대한민국(공주대학교총장)'),(228,'119-82-03160',' -','서울대학교산학협력재단'),(229,'402-82-15272',' -','전북대학교 산학협력단'),(230,'606-82-06851',' -','동서대학교 산학협력단'),(231,'503-82-09525',' -','계명문화대학교 산학협력단'),(232,'504-82-09678',' -','경북대학교 산학협력단'),(233,'609-82-09745',' -','국립창원대학교 산학협력단'),(234,'401-82-06407',' -','국립군산대학교 산학협력단'),(235,'621-82-06530',' -','부산대학교 산학협력단'),(236,'402-82-15573',' -','우석대학교 산학협력단'),(237,'135-82-10789',' -','경희대학교 산학협력단'),(238,'110-82-10456',' -','이화여자대학교 산학협력단'),(239,'314-82-09264',' -','충남대학교 산학협력단'),(240,'515-82-06652',' -','대경대학교 산학협력단'),(241,'121-82-10209',' -','인하대학교 산학협력단'),(242,'221-82-10213',' -','강원대학교 산학협력단'),(243,'301-82-13990',' -','충북보건과학대학교 산학협력단'),(244,'312-82-10144',' -','선문대학교 산학협력단'),(245,'210-82-08677',' -','광운대학교 산학협력단'),(246,'314-82-09342',' -','배재대학교 산학협력단'),(247,'613-82-11653',' -','경상국립대학교 산학협력단'),(248,'504-82-09775',' -','대구보건대학교 산학협력단'),(249,'206-82-07306',' -','한양대학교 산학협력단'),(250,'416-82-14326',' -','국립순천대학교 산학협력단'),(251,'135-82-10718',' -','용인예술과학대학교 산학협력단'),(252,'314-82-09250',' -','대전과학기술대학교 산학협력단'),(253,'305-82-14822',' -','우송대학교 산학협력단'),(254,'314-82-09380',' -','목원대학교 산학협력단'),(255,'303-82-06821',' -','국립한국교통대학교 산학협력단'),(256,'206-82-07325',' -','건국대학교 산학협력단'),(257,'617-82-06434',' -','국립부경대학교 산학협력단'),(258,'616-82-16375',' -','제주대학교 산학협력단'),(259,'301-82-16304',' -','충북대학교 산학협력단'),(260,'209-82-08298',' -','고려대학교 산학협력단'),(261,'312-82-10222',' -','남서울대학교 산학협력단'),(262,'603-82-07661',' -','부산보건대학교 산학협력단'),(263,'305-82-13430',' -','한남대학교 산학협력단'),(264,'503-82-09622',' -','계명대학교 산학협력단'),(265,'411-82-08251',' -','국립목포대학교 산학협력단'),(266,'210-82-08420',' -','서울과학기술대학교 산학협력단'),(267,'121-82-10382',' -','인천대학교 산학협력단'),(268,'613-82-09900',' -','경남과학기술대학교 산학협력단'),(269,'403-82-09152',' -','원광대학교 산학협력단'),(270,'105-82-13581',' -','서강대학교 산학협력단'),(271,'314-82-09226',' -','국립한밭대학교 산학협력단'),(272,'124-82-14602',' -','아주대학교 산학협력단'),(273,'515-82-06593',' -','대구한의대학교 산학협력단'),(274,'307-82-06478',' -','국립공주대학교 산학협력단'),(275,'226-82-12220',' -','국립강릉원주대학교 산학협력단'),(276,'305-82-13288',' -','중부대학교 산학협력단'),(277,'513-82-07067',' -','국립금오공과대학교 산학협력단'),(278,'301-82-16565',' -','청주교육대학교 산학협력단'),(279,'312-82-10071',' -','순천향대학교 산학협력단'),(280,'515-82-06574',' -','영남대학교 산학협력단'),(281,'409-82-11942',' -','전남대학교 산학협력단'),(282,'129-82-07687',' -','가천대학교 산학협력단'),(283,'108-82-05979',' -','중앙대학교 산학협력단'),(284,'401-82-06673',' -','호원대학교 산학협력단'),(285,'402-82-15554',' -','전주대학교 산학협력단'),(286,'613-82-09967',' -','한국국제대학교 산학협력단'),(287,'301-82-14081',' -','충청대학교 산학협력단'),(288,'506-82-07303',' -','포항공과대학교 산학협력단'),(289,'408-82-13442',' -','전남과학대학교 산학협력단'),(290,'209-82-08395',' -','국민대학교 산학협력단'),(291,'608-82-10351',' -','창신대학교 산학협력단'),(292,'101-82-12009',' -','성균관대학교 산학협력단'),(293,'409-82-11976',' -','서영대학교 산학협력단'),(294,'316-82-00707',' -','한서대학교 산학협력단'),(295,'137-82-04056',' -','김포대학교 산학협력단'),(296,'135-82-11191',' -','한국외국어대학교 연구 산학협력단'),(297,'603-82-07701',' -','동아대학교 산학협력단'),(298,'411-82-08270',' -','국립목포해양대학교 산학협력단'),(299,'106-82-12227',' -','숙명여자대학교 산학협력단'),(300,'110-82-10500',' -','연세대학교 산학협력단'),(301,'206-82-07591',' -','세종대학교 산학협력단'),(302,'615-82-06286',' -','인제대학교 산학협력단'),(303,'135-82-11060',' -','명지대학교 산학협력단'),(304,'610-82-10640',' -','울산대학교 산학협력단'),(305,'127-82-12767',' -','차의과학대학교 산학협력단'),(306,'305-82-13371',' -','대전보건대학교 산학협력단'),(307,'304-82-04786',' -','대원대학교 산학협력단'),(308,'106-82-12299',' -','단국대학교 산학협력단'),(309,'135-82-10872',' -','경기대학교 산학협력단'),(310,'408-82-13419',' -','조선대학교 산학협력단'),(311,'608-82-10384',' -','경남대학교 산학협력단'),(312,'308-82-06340',' -','건양대학교 산학협력단'),(313,'121-82-10290',' -','인천재능대학교 산학협력단'),(314,'301-82-14155',' -','서원대학교 산학협력단'),(315,'226-82-12123',' -','가톨릭관동대학교 산학협력단'),(316,'513-82-07131',' -','경운대학교 산학협력단'),(317,'508-82-06009',' -','국립안동대학교 산학협력단'),(318,'114-82-07929',' -','가톨릭대학교 산학협력단'),(319,'312-82-09934',' -','한국기술교육대학교 산학협력단'),(320,'312-82-10256',' -','호서대학교 산학협력단'),(321,'140-82-00056',' -','한국공학대학교 산학협력단'),(322,'210-82-08681',' -','덕성여자대학교 산학협력단'),(323,'617-82-06400',' -','동명대학교 산학협력단'),(324,'617-82-06453',' -','경성대학교 산학협력단'),(325,'301-82-14140',' -','한국교원대학교 산학협력단'),(326,'127-82-12675',' -','신한대학교 산학협력단'),(327,'224-82-08147',' -','상지대학교 산학협력단'),(328,'512-82-05260',' -','경북전문대학교 산학협력단'),(329,'124-82-14392',' -','한국농수산대학교 산학협력단'),(330,'606-82-06977',' -','신라대학교 산학협력단'),(331,'602-82-06349',' -','국립한국해양대학교 산학협력단'),(332,'508-82-06028',' -','안동과학대학교 산학협력단'),(333,'140-82-00094',' -','경기과학기술대학교 산학협력단'),(334,'124-82-14752',' -','한신대학교 산학협력단'),(335,'124-82-14446',' -','수원대학교 산학협력단'),(336,'125-82-07142',' -','한경국립대학교 산학협력단'),(337,'221-82-10381',' -','한림성심대학교 산학협력단'),(338,'101-82-12940',' -','한국방송통신대학교 산학협력단'),(339,'127-82-12864',' -','대진대학교 산학협력단'),(340,'135-82-10867',' -','강남대학교 산학협력단'),(341,'512-82-05241',' -','동양대학교 산학협력단'),(342,'201-82-04468',' -','동국대학교 산학협력단'),(343,'128-82-08698',' -','한국항공대학교 산학협력단'),(344,'304-82-04850',' -','세명대학교 산학협력단'),(345,'515-82-06875',' -','대구대학교 산학협력단'),(346,'123-82-12498',' -','연성대학교 산학협력단'),(347,'217-82-04051',' -','삼육대학교 산학협력단'),(348,'134-82-06754',' -','신안산대학교 산학협력단'),(349,'412-82-05825',' -','동신대학교 산학협력단'),(350,'515-82-06991',' -','경일대학교 산학협력단'),(351,'303-82-06840',' -','극동대학교 산학협력단'),(352,'126-82-07878',' -','청강문화산업대학교 산학협력단'),(353,'620-82-04301',' -','울산과학대학교 산학협력단'),(354,'130-82-13573',' -','유한대학교 산학협력단'),(355,'411-82-08299',' -','세한대학교 산학협력단'),(356,'108-82-06264',' -','숭실대학교 산학협력단'),(357,'217-82-04070',' -','인덕대학교 산학협력단'),(358,'606-82-06773',' -','경남정보대학교 산학협력단'),(359,'202-82-64173',' -','한세대학교 산학협력단'),(360,'204-82-07256',' -','서울시립대학교 산학협력단'),(361,'409-82-12072',' -','전남도립대학교 산학협력단'),(362,'123-82-11903',' -','성결대학교 산학협력단'),(363,'209-82-08319',' -','한성대학교 산학협력단'),(364,'123-82-12111',' -','안양대학교 산학협력단'),(365,'226-82-12138',' -','강원도립대학교 산학협력단'),(366,'124-82-14581',' -','오산대학교 산학협력단'),(367,'505-82-06882',' -','위덕대학교 산학협력단'),(368,'125-82-07161',' -','두원공과대학교 산학협력단 '),(369,'209-82-08468',' -','서경대학교 산학협력단'),(370,'113-82-05480',' -','동양미래대학교 산학협력단'),(371,'105-82-13617',' -','홍익대학교 산학협력단'),(372,'138-82-02916',' -','대림대학교 산학협력단'),(373,'410-82-13300',' -','남부대학교 산학협력단'),(374,'209-82-08357',' -','성신여자대학교 연구 산학협력단'),(375,'224-82-08467',' -','한라대학교 산학협력단'),(376,'312-82-10241',' -','상명대학교 천안 산학협력단'),(377,'101-82-06114',' -','동방대학교'),(378,'515-82-06711',' -','대구가톨릭대학교 산학협력단'),(379,'217-82-04099',' -','서울여자대학교 산학협력단'),(380,'101-82-11499',' -','배화여자대학교 산학협력단'),(381,'305-82-13347',' -','을지대학교 산학협력단'),(382,'312-82-10130',' -','나사렛대학교 산학협력단'),(383,'311-82-04843',' -','신성대학교 산학협력단'),(384,'410-82-13218',' -','호남대학교 산학협력단'),(385,'221-82-10284',' -','한림대학교 산학협력단'),(386,'617-82-06749',' -','부산외국어대학교 산학협력단'),(387,'128-83-00918',' -','대한민국(국방대학교총장)'),(388,'504-83-04802',' -','대한민국(경북대학교 첨단정보통신융합산업기술원장)'),(389,'417-82-05529',' -','한영대학교 산학협력단');
/*!40000 ALTER TABLE `tb24_110` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-11 21:11:01
