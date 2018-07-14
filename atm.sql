SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `atm`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_account` (IN `name` VARCHAR(50), IN `account_number` INT, IN `pin` INT, IN `address` VARCHAR(100), IN `mobile_no` INT, IN `ifsc_code` VARCHAR(11))  begin
    insert into account_holder(name,account_number,pin,address,mobile_no,ifsc_code)
    values (name,account_number,pin,address,mobile_no,ifsc_code);
    end$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `account_holder`
--

CREATE TABLE `account_holder` (
  `name` varchar(50) NOT NULL,
  `account_number` int(11) NOT NULL,
  `total_balance` int(11) NOT NULL DEFAULT '0',
  `pin` int(11) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile_no` int(11) NOT NULL,
  `ifsc_code` varchar(11) NOT NULL,
  `last_deposit` int(11) DEFAULT NULL,
  `last_withdraw` int(11) DEFAULT NULL,
  `last_status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Triggers `account_holder`
--
DELIMITER $$
CREATE TRIGGER `after_update_account_holder` AFTER UPDATE ON `account_holder` FOR EACH ROW begin
    IF new.last_status = 'withdraw' THEN
    INSERT into transaction(account_number,current_balance,withdraw_amount) values(old.account_number,new.total_balance,new.last_withdraw);
    ELSEIF new.last_status = 'deposit' THEN
    INSERT into transaction(account_number,current_balance,deposit_amount) values(old.account_number,new.total_balance,new.last_deposit);
    END IF;
    end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `account_number` int(11) NOT NULL,
  `current_balance` int(11) NOT NULL,
  `withdraw_amount` int(11) DEFAULT NULL,
  `deposit_amount` int(11) DEFAULT NULL,
  `transaction_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account_holder`
--
ALTER TABLE `account_holder`
  ADD PRIMARY KEY (`account_number`),
  ADD UNIQUE KEY `UNIQUE` (`pin`);

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD KEY `Foreign Key` (`account_number`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `Foreign Key` FOREIGN KEY (`account_number`) REFERENCES `account_holder` (`account_number`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
