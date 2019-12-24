-- phpMyAdmin SQL Dump
-- version 4.4.15.9
-- https://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 23, 2019 at 10:18 PM
-- Server version: 5.6.37
-- PHP Version: 5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Neonatal`
--

-- --------------------------------------------------------

--
-- Table structure for table `Complaints`
--

CREATE TABLE IF NOT EXISTS `Complaints` (
  `name` varchar(50) NOT NULL,
  `specialrequest` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Complaints`
--

INSERT INTO `Complaints` (`name`, `specialrequest`) VALUES
('ghada', 'good'),
('sama', 'nice'),
('sam', 'hello'),
('ahmed', 'nice'),
('sondos', 'complaint'),
('mohamed', 'complain');

-- --------------------------------------------------------

--
-- Table structure for table `Doctors`
--

CREATE TABLE IF NOT EXISTS `Doctors` (
  `name` varchar(255) DEFAULT NULL,
  `department` varchar(255) DEFAULT NULL,
  `id` int(10) NOT NULL DEFAULT '0',
  `gender` varchar(7) DEFAULT NULL,
  `Birthdate` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Doctors`
--

INSERT INTO `Doctors` (`name`, `department`, `id`, `gender`, `Birthdate`) VALUES
('ghada', 'neonatal', 1, NULL, '0000-00-00'),
('sam', 'radiology', 2, NULL, '0000-00-00'),
('mona', 'neonatal', 3, NULL, '0000-00-00'),
('sondos', 'neonatal', 4, NULL, '0000-00-00'),
('ahmed', 'department', 5, NULL, '0000-00-00'),
('example', 'radiology', 6, NULL, '0000-00-00'),
('neveen', 'lab', 7, NULL, '0000-00-00'),
('ahmed', 'department', 8, NULL, '0000-00-00'),
('ahmed', 'lab', 9, NULL, '0000-00-00'),
('example', 'radiology', 10, NULL, '0000-00-00'),
('Hadeel', 'neonatal', 12, NULL, '0000-00-00'),
('noha', 'neonatal', 13, NULL, '0000-00-00'),
('samar', 'neonatal', 14, NULL, '0000-00-00'),
('name', 'speciality', 15, NULL, '0000-00-00'),
('name', 'speciality', 19, NULL, '0000-00-00'),
('s', 'spe', 20, 'Male', '0000-00-00'),
('sosooo', 'neonatal', 25, 'Female', '1998-09-04'),
('mohamed', 'neonatal', 26, 'Male', '1988-03-03'),
('ibrahim', 'radiology', 28, 'Male', '1888-03-04'),
('sara', 'neonatal', 30, 'Female', '1977-03-08'),
('mariam', 'neonatal', 88, 'Female', '1996-05-07'),
('example', 'radiology', 12367890, NULL, '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `DOC_Neo`
--

CREATE TABLE IF NOT EXISTS `DOC_Neo` (
  `D_code` int(11) DEFAULT NULL,
  `N_code` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `DOC_Neo`
--

INSERT INTO `DOC_Neo` (`D_code`, `N_code`) VALUES
(1, 3),
(4, 6),
(3, 13);

-- --------------------------------------------------------

--
-- Table structure for table `Neonates`
--

CREATE TABLE IF NOT EXISTS `Neonates` (
  `firstname` varchar(255) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `id` int(10) NOT NULL,
  `birthdate` date DEFAULT NULL,
  `gender` varchar(7) DEFAULT NULL,
  `status` longtext,
  `Nid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Neonates`
--

INSERT INTO `Neonates` (`firstname`, `lastname`, `id`, `birthdate`, `gender`, `status`, `Nid`) VALUES
('k', 's', 1, NULL, NULL, NULL, 0),
('sama', 'sayed', 3, '2019-12-03', NULL, NULL, 0),
('v', 'q', 6, '2019-12-26', 'Male', 'good', 0),
('sam', 'f', 8, '2019-02-07', 'name', NULL, 0),
('sam', 'k', 9, '2019-12-04', 'Female', NULL, 0),
('d', 'd', 10, NULL, NULL, NULL, 0),
('omer', 'sayed', 12, '2019-11-02', 'Male', 'good', 0),
('ahmed', 'sayed', 13, '2019-12-02', 'Male', 'good', 0),
('esraa', 'ahmed', 17, '2019-12-09', 'Female', 'NCARE', 0),
('f', 'b', 18, '2019-03-31', 'Male', 'ICARE', 0),
('sara', 'ahmed', 30, '2019-12-03', 'Female', 'ICARE', 0),
('logy', 'tamer', 32, '2019-05-06', 'Female', 'ICARE', 0),
('ali', 'tamer', 60, '2019-03-05', 'Male', 'ICARE', 0),
('mostafa', 'sayed', 88, '2019-02-05', 'Male', 'ICARE', 0);

-- --------------------------------------------------------

--
-- Table structure for table `NICU`
--

CREATE TABLE IF NOT EXISTS `NICU` (
  `Id` int(11) NOT NULL DEFAULT '0',
  `LOCATION` char(20) DEFAULT NULL,
  `device_name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `NICU`
--

INSERT INTO `NICU` (`Id`, `LOCATION`, `device_name`) VALUES
(2, 'tt', 'example'),
(3, 'neonatal', 'medical device'),
(11, 'neonatal', 'device');

-- --------------------------------------------------------

--
-- Table structure for table `NICU DEVICIES`
--

CREATE TABLE IF NOT EXISTS `NICU DEVICIES` (
  `Nid` int(11) NOT NULL,
  `devices` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `nurses`
--

CREATE TABLE IF NOT EXISTS `nurses` (
  `name` varchar(255) NOT NULL,
  `Code` int(11) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `bday` date NOT NULL,
  `Nssn` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nurses`
--

INSERT INTO `nurses` (`name`, `Code`, `gender`, `bday`, `Nssn`) VALUES
('ghada', 1, 'Female', '1666-02-02', 0),
('samar', 4, 'Female', '1991-06-07', 0);

-- --------------------------------------------------------

--
-- Table structure for table `parents`
--

CREATE TABLE IF NOT EXISTS `parents` (
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `ssn` int(20) NOT NULL,
  `address` varchar(255) NOT NULL,
  `phone` int(20) NOT NULL,
  `sex` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `parents`
--

INSERT INTO `parents` (`firstname`, `lastname`, `ssn`, `address`, `phone`, `sex`) VALUES
('ahmed', 'm', 1, 'klm', 555, 'male'),
('abdulla', 'sayed', 8, 'masr', 203, 'Male'),
('ahmed', 'tamer', 10, 'masr', 20, 'Male');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Doctors`
--
ALTER TABLE `Doctors`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `DOC_Neo`
--
ALTER TABLE `DOC_Neo`
  ADD KEY `N_code` (`N_code`),
  ADD KEY `D_code` (`D_code`);

--
-- Indexes for table `Neonates`
--
ALTER TABLE `Neonates`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- Indexes for table `parents`
--
ALTER TABLE `parents`
  ADD PRIMARY KEY (`ssn`),
  ADD UNIQUE KEY `ssn` (`ssn`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `DOC_Neo`
--
ALTER TABLE `DOC_Neo`
  ADD CONSTRAINT `doc_neo_ibfk_1` FOREIGN KEY (`N_code`) REFERENCES `Neonates` (`id`),
  ADD CONSTRAINT `doc_neo_ibfk_2` FOREIGN KEY (`D_code`) REFERENCES `Doctors` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
