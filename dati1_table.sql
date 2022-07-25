/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 100422
 Source Host           : localhost:3306
 Source Schema         : test

 Target Server Type    : MySQL
 Target Server Version : 100422
 File Encoding         : 65001

 Date: 21/04/2022 23:44:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dati1_table
-- ----------------------------
DROP TABLE IF EXISTS `dati1_table`;
CREATE TABLE `dati1_table`  (
  `numeroRiga` int(255) NOT NULL,
  `numeroGE` int(255) NOT NULL,
  `ultimaVisita` date NOT NULL,
  `deltaTmax` int(255) NOT NULL,
  `nextDeadline` date NOT NULL,
  `nextDeadlineN` int(255) NOT NULL,
  `loc` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `cap` int(255) NULL DEFAULT NULL,
  `re` varchar(2) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `coord` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `lat` double NOT NULL,
  `long` double NOT NULL,
  PRIMARY KEY (`numeroRiga`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
