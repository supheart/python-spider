/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50714
Source Host           : localhost:3306
Source Database       : testrelaxarticle

Target Server Type    : MYSQL
Target Server Version : 50714
File Encoding         : 65001

Date: 2017-02-28 15:43:45
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` bigint(20) DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `detailtime` datetime DEFAULT NULL,
  `imgsid` varchar(255) DEFAULT NULL,
  `imgwh` varchar(255) DEFAULT NULL,
  `hotComments` varchar(255) DEFAULT NULL,
  `commCount` varchar(255) DEFAULT NULL,
  `pubtime` datetime DEFAULT NULL,
  `mod_time` bigint(20) DEFAULT NULL,
  `cover_img` varchar(255) DEFAULT NULL,
  `content` longtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `avatar_sid` varchar(255) DEFAULT NULL,
  `avatar_url` varchar(255) DEFAULT NULL,
  `content` text,
  `datetime` time DEFAULT NULL,
  `good` int(255) DEFAULT NULL,
  `lou` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `timestamp` bigint(255) DEFAULT NULL,
  `user` varchar(255) DEFAULT NULL,
  `aid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for sourceimg
-- ----------------------------
DROP TABLE IF EXISTS `sourceimg`;
CREATE TABLE `sourceimg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `aid` varchar(255) DEFAULT NULL,
  `img1` varchar(255) DEFAULT NULL,
  `img2` varchar(255) DEFAULT NULL,
  `img3` varchar(255) DEFAULT NULL,
  `img4` varchar(255) DEFAULT NULL,
  `img5` varchar(255) DEFAULT NULL,
  `img6` varchar(255) DEFAULT NULL,
  `img7` varchar(255) DEFAULT NULL,
  `img8` varchar(255) DEFAULT NULL,
  `img9` varchar(255) DEFAULT NULL,
  `img10` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
