-- phpMyAdmin SQL Dump
-- version 4.9.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: May 04, 2025 at 03:33 PM
-- Server version: 5.7.26
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `research_study_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `consent_form`
--

CREATE TABLE `consent_form` (
  `consent_form_id` int(11) NOT NULL,
  `date_signed` datetime DEFAULT NULL,
  `participant_participant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `consent_form`
--

INSERT INTO `consent_form` (`consent_form_id`, `date_signed`, `participant_participant_id`) VALUES
(1001, '2022-01-15 10:00:00', 101),
(1002, '2023-02-10 11:00:00', 101),
(1003, '2024-03-05 12:00:00', 101),
(1004, '2022-02-20 09:30:00', 102),
(1005, '2023-03-15 10:15:00', 102),
(1006, '2024-04-18 11:45:00', 102),
(1007, '2022-03-25 14:20:00', 103),
(1008, '2023-04-22 13:10:00', 103),
(1009, '2024-05-25 15:00:00', 103),
(1010, '2022-04-30 08:00:00', 104),
(1011, '2023-05-28 09:10:00', 104),
(1012, '2024-06-30 10:25:00', 104),
(1013, '2022-05-05 16:45:00', 105),
(1014, '2023-06-03 17:30:00', 105),
(1015, '2024-07-04 18:15:00', 105),
(1016, '2022-06-10 12:40:00', 106),
(1017, '2023-07-08 13:50:00', 106),
(1018, '2024-08-09 14:55:00', 106),
(1019, '2022-07-15 07:20:00', 107),
(1020, '2023-08-13 08:30:00', 107),
(1021, '2024-09-14 09:45:00', 107),
(1022, '2022-08-20 11:10:00', 108),
(1023, '2023-09-17 12:25:00', 108),
(1024, '2024-10-19 13:35:00', 108),
(1025, '2022-09-25 15:50:00', 109),
(1026, '2023-10-22 16:45:00', 109),
(1027, '2024-11-23 17:55:00', 109),
(1028, '2022-10-30 18:30:00', 110),
(1029, '2023-11-26 19:20:00', 110),
(1030, '2024-12-28 20:10:00', 110),
(1031, '2025-05-02 00:00:00', 111),
(1032, '2025-04-02 00:00:00', 111),
(1033, '2025-01-01 00:00:00', 111);

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

CREATE TABLE `dataset` (
  `dataset_id` int(11) NOT NULL,
  `sra_id` varchar(45) DEFAULT NULL,
  `fastq_file` varchar(45) DEFAULT NULL,
  `read_type` varchar(45) DEFAULT NULL,
  `read_length` int(45) DEFAULT NULL,
  `primers` varchar(45) DEFAULT NULL,
  `bam_file` varchar(45) DEFAULT NULL,
  `file_size` double DEFAULT NULL,
  `participant_participant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `dataset`
--

INSERT INTO `dataset` (`dataset_id`, `sra_id`, `fastq_file`, `read_type`, `read_length`, `primers`, `bam_file`, `file_size`, `participant_participant_id`) VALUES
(1, 'SRA001', 'http://example.com/fastq_file_1.fastq', 'forward', 150, '695F', NULL, NULL, 101),
(2, 'SRA002', 'http://example.com/fastq_file_2.fastq', 'paired end', 250, '803F, 337R', NULL, NULL, 101),
(3, 'SRA003', 'http://example.com/fastq_file_3.fastq', 'forward', 150, '695F', NULL, NULL, 102),
(4, 'SRA004', 'http://example.com/fastq_file_4.fastq', 'paired end', 250, '803F, 337R', NULL, NULL, 102),
(5, 'SRA005', 'http://example.com/fastq_file_5.fastq', 'forward', 150, '695F', NULL, NULL, 103),
(6, 'SRA006', 'http://example.com/fastq_file_6.fastq', 'paired end', 300, '803F, 337R', NULL, NULL, 103),
(7, 'SRA007', 'http://example.com/fastq_file_7.fastq', 'forward', 150, '695F', NULL, NULL, 104),
(8, 'SRA008', 'http://example.com/fastq_file_8.fastq', 'paired end', 250, '803F, 337R', NULL, NULL, 104),
(9, 'SRA009', 'http://example.com/fastq_file_9.fastq', 'forward', 150, '695F', NULL, NULL, 105),
(10, 'SRA010', 'http://example.com/fastq_file_10.fastq', 'paired end', 250, '803F, 337R', NULL, NULL, 105),
(11, 'SRA011', 'http://example.com/fastq_file_11.fastq', 'forward', 150, '695F', NULL, NULL, 106),
(12, 'SRA012', 'http://example.com/fastq_file_12.fastq', 'paired end', 250, '803F, 337R', NULL, NULL, 106),
(13, 'SRA013', 'http://example.com/fastq_file_13.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_13.bam', 2.5, 107),
(14, 'SRA014', 'http://example.com/fastq_file_14.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_14.bam', 3, 107),
(15, 'SRA015', 'http://example.com/fastq_file_15.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_15.bam', 4, 108),
(16, 'SRA016', 'http://example.com/fastq_file_16.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_16.bam', 5, 108),
(17, 'SRA017', 'http://example.com/fastq_file_17.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_17.bam', 3.5, 109),
(18, 'SRA018', 'http://example.com/fastq_file_18.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_18.bam', 4.2, 109),
(19, 'SRA019', 'http://example.com/fastq_file_19.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_19.bam', 5.3, 110),
(20, 'SRA020', 'http://example.com/fastq_file_20.fastq', NULL, NULL, NULL, 'http://example.com/bam_file_20.bam', 6, 110),
(21, 'SRA021', 'http://example.com/fastq_file_21.fastq', 'forward', 250, '695F', NULL, NULL, 111);

-- --------------------------------------------------------

--
-- Table structure for table `participant`
--

CREATE TABLE `participant` (
  `participant_id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `participant`
--

INSERT INTO `participant` (`participant_id`, `name`, `age`, `sex`) VALUES
(101, 'Emily Rodgers', 25, 'female'),
(102, 'Michael Smith', 35, 'Male'),
(103, 'Sophia Martinez', 29, 'Female'),
(104, 'James Anderson', 42, 'Male'),
(105, 'Olivia Brown', 67, 'Female'),
(106, 'Daniel Wilson', 58, 'Male'),
(107, 'Isabella Taylor', 19, 'Female'),
(108, 'Ethan Moore', 75, 'Male'),
(109, 'Mia Clark', 33, 'Female'),
(110, 'William Davis', 47, 'Male'),
(111, 'Cory Wong', 35, 'male');

-- --------------------------------------------------------

--
-- Table structure for table `research_study`
--

CREATE TABLE `research_study` (
  `study_id` int(11) NOT NULL,
  `study_name` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `research_study`
--

INSERT INTO `research_study` (`study_id`, `study_name`) VALUES
(1, '16S rRNA Sequencing of Human Microbiome Samples (Stomach)'),
(2, '16S rRNA Sequencing of Human Microbiome Samples (Colon)'),
(3, 'Whole Genome Sequencing of Cancer-Related Mutations'),
(4, 'Whole Genome Sequencing of Human Populations for Genetic Variability'),
(5, 'Gut Microbiota in Untreated Diffuse Large B Cell Lymphoma Patients');

-- --------------------------------------------------------

--
-- Table structure for table `study_datasets`
--

CREATE TABLE `study_datasets` (
  `dataset_dataset_id` int(11) NOT NULL,
  `research_study_study_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `study_datasets`
--

INSERT INTO `study_datasets` (`dataset_dataset_id`, `research_study_study_id`) VALUES
(1, 1),
(3, 1),
(5, 1),
(7, 1),
(9, 1),
(11, 1),
(2, 2),
(4, 2),
(6, 2),
(8, 2),
(10, 2),
(12, 2),
(13, 3),
(15, 3),
(17, 3),
(19, 3),
(14, 4),
(16, 4),
(18, 4),
(20, 4),
(1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `study_participants`
--

CREATE TABLE `study_participants` (
  `research_study_study_id` int(11) NOT NULL,
  `participant_participant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `study_participants`
--

INSERT INTO `study_participants` (`research_study_study_id`, `participant_participant_id`) VALUES
(1, 101),
(2, 101),
(5, 101),
(1, 102),
(2, 102),
(1, 103),
(2, 103),
(1, 104),
(2, 104),
(1, 105),
(2, 105),
(1, 106),
(2, 106),
(3, 107),
(4, 107),
(3, 108),
(4, 108),
(3, 109),
(4, 109),
(3, 110),
(4, 110);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `consent_form`
--
ALTER TABLE `consent_form`
  ADD PRIMARY KEY (`consent_form_id`,`participant_participant_id`),
  ADD KEY `fk_consent_form_participant1_idx` (`participant_participant_id`);

--
-- Indexes for table `dataset`
--
ALTER TABLE `dataset`
  ADD PRIMARY KEY (`dataset_id`,`participant_participant_id`),
  ADD KEY `fk_dataset_participant_idx` (`participant_participant_id`);

--
-- Indexes for table `participant`
--
ALTER TABLE `participant`
  ADD PRIMARY KEY (`participant_id`);

--
-- Indexes for table `research_study`
--
ALTER TABLE `research_study`
  ADD PRIMARY KEY (`study_id`);

--
-- Indexes for table `study_datasets`
--
ALTER TABLE `study_datasets`
  ADD PRIMARY KEY (`dataset_dataset_id`,`research_study_study_id`),
  ADD KEY `fk_study_datasets_research_study1_idx` (`research_study_study_id`);

--
-- Indexes for table `study_participants`
--
ALTER TABLE `study_participants`
  ADD PRIMARY KEY (`research_study_study_id`,`participant_participant_id`),
  ADD KEY `fk_study_participants_participant1_idx` (`participant_participant_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `consent_form`
--
ALTER TABLE `consent_form`
  ADD CONSTRAINT `fk_consent_form_participant1` FOREIGN KEY (`participant_participant_id`) REFERENCES `participant` (`participant_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `dataset`
--
ALTER TABLE `dataset`
  ADD CONSTRAINT `fk_dataset_participant` FOREIGN KEY (`participant_participant_id`) REFERENCES `participant` (`participant_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `study_datasets`
--
ALTER TABLE `study_datasets`
  ADD CONSTRAINT `fk_study_datasets_dataset1` FOREIGN KEY (`dataset_dataset_id`) REFERENCES `dataset` (`dataset_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_study_datasets_research_study1` FOREIGN KEY (`research_study_study_id`) REFERENCES `research_study` (`study_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Constraints for table `study_participants`
--
ALTER TABLE `study_participants`
  ADD CONSTRAINT `fk_study_participants_participant1` FOREIGN KEY (`participant_participant_id`) REFERENCES `participant` (`participant_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `fk_study_participants_research_study1` FOREIGN KEY (`research_study_study_id`) REFERENCES `research_study` (`study_id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
