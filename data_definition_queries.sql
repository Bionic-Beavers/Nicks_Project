

DROP TABLE IF EXISTS `Organizations`;

CREATE TABLE `Organizations` (
  `organization_id` int(11) NOT NULL AUTO_INCREMENT UNIQUE,
  `name` varchar(255) NOT NULL,
  `imgPath` varchar(255) NOT NULL,
  `country` varchar(255) NOT NULL,
  `category` varchar(255) NOT NULL,
  `summary` text NULL,
  `source` varchar(255) NULL,

  PRIMARY KEY (`organization_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Employees`
--

LOCK TABLES `Organizations` WRITE;
INSERT INTO `Organizations` (`name`, `country`, `imgPath`, `summary`, `source`, `category`) 
VALUES ('American Red Cross', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=American_Red_Cross', NULL, 'https://www.redcross.org/', 'Health'),
        ('Focus on the Family', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=focus_on_the_family', NULL, 'https://www.focusonthefamily.com/', 'Faith'),
        ('National Cancer Institute', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=National_Cancer_Institute', NULL, 'https://www.cancer.gov/', 'Health'),
        ('City of Hope National Medical Center', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=City_of_Hope_National_Medical_Center', NULL, 'https://www.cityofhope.org/homepage', 'Health'),
        ('American Heart Association', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=american%20heart%20association', NULL, 'https://www.heart.org/', 'Health'),
        ('AARP', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=AARP_Foundation', NULL, 'https://www.aarp.org/aarp-foundation/', 'Social Welfare'),
        ('Ford Foundation', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=ford_foundation', NULL, 'https://www.fordfoundation.org/', 'Social Welfare'),
        ('Girl Scouts of America', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Girl_Scouts_of_the_USA', NULL, 'https://www.girlscouts.org/', 'Social Welfare'),
        ('Boy Scouts of America', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Boy%20Scouts', NULL, 'https://www.scouting.org/', 'Social Welfare'),
        ('Habitat for Humanity', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Habitat_for_Humanity', NULL, 'https://www.habitat.org/', 'Social Welfare'),
        ('The Heritage Foundation', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=The_Heritage_Foundation', NULL, 'https://www.heritage.org/', 'Social Welfare'),
        ('Lions Club International', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Lions_Clubs_International', NULL, 'https://www.lionsclubs.org/en', 'Social Welfare'),
        ('United Way', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=United_Way', NULL, 'https://www.unitedway.org/', 'Social Welfare'),
        ('Boys and Girls Clubs of America', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Boys_%26_Girls_Clubs_of_America', NULL, 'https://www.bgca.org/', 'Social Welfare'),
        ('Goodwill Industries', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Goodwill_Industries', NULL, 'https://www.bgca.org/', 'Social Welfare'),
        ('Campus Crusade for Christ', 'USA', 'http://flip3.engr.oregonstate.edu:8545/?q=Cru_(Christian_organization)', NULL, 'https://www.cru.org/', 'Faith');



              
UNLOCK TABLES;


