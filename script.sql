-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema quiz_project
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema quiz_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `quiz_project` DEFAULT CHARACTER SET utf8 ;
USE `quiz_project` ;

-- -----------------------------------------------------
-- Table `quiz_project`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quiz_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(155) NULL,
  `last_name` VARCHAR(155) NULL,
  `email` VARCHAR(155) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quiz_project`.`quizes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quiz_project`.`quizes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(155) NULL,
  `category` TINYINT NULL,
  `description` TEXT NULL,
  `question_1` TEXT NULL,
  `correct_answer_1` VARCHAR(255) NULL,
  `incorrect_answer_1_1` VARCHAR(255) NULL,
  `incorrect_answer_1_2` VARCHAR(255) NULL,
  `incorrect_answer_1_3` VARCHAR(255) NULL,
  `question_2` TEXT NULL,
  `correct_answer_2` VARCHAR(255) NULL,
  `incorrect_answer_2_1` VARCHAR(255) NULL,
  `incorrect_answer_2_2` VARCHAR(255) NULL,
  `incorrect_answer_2_3` VARCHAR(255) NULL,
  `question_3` TEXT NULL,
  `correct_answer_3` VARCHAR(255) NULL,
  `incorrect_answer_3_1` VARCHAR(255) NULL,
  `incorrect_answer_3_2` VARCHAR(255) NULL,
  `incorrect_answer_3_3` VARCHAR(255) NULL,
  `question_4` TEXT NULL,
  `correct_answer_4` VARCHAR(255) NULL,
  `incorrect_answer_4_1` VARCHAR(255) NULL,
  `incorrect_answer_4_2` VARCHAR(255) NULL,
  `incorrect_answer_4_3` VARCHAR(255) NULL,
  `question_5` TEXT NULL,
  `correct_answer_5` VARCHAR(255) NULL,
  `incorrect_answer_5_1` VARCHAR(255) NULL,
  `incorrect_answer_5_2` VARCHAR(255) NULL,
  `incorrect_answer_5_3` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_quizes_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_quizes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `quiz_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quiz_project`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quiz_project`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `like` INT NULL,
  `user_id` INT NOT NULL,
  `quiz_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_quizes_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_likes_quizes1_idx` (`quiz_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_quizes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `quiz_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_quizes1`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `quiz_project`.`quizes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `quiz_project`.`users_has_quizes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `quiz_project`.`users_has_quizes` (
  `user_id` INT NOT NULL,
  `quiz_id` INT NOT NULL,
  INDEX `fk_users_has_quizes_quizes1_idx` (`quiz_id` ASC) VISIBLE,
  INDEX `fk_users_has_quizes_users2_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_users_has_quizes_users2`
    FOREIGN KEY (`user_id`)
    REFERENCES `quiz_project`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_quizes_quizes1`
    FOREIGN KEY (`quiz_id`)
    REFERENCES `quiz_project`.`quizes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
