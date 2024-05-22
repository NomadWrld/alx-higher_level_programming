# 0x0D. SQL - Introduction

## Description

This project introduces basic SQL queries and operations. You will learn how to list, create, delete, and manipulate databases and tables. The tasks include creating databases and tables, inserting and updating data, and retrieving data with specific conditions.

## Requirements

- All scripts must be executable.
- All SQL queries should work with MySQL 5.7.x.
- The SQL files should be interpreted by the `mysql` command line tool.

## Project Structure

- **0-list_databases.sql:** Lists all databases.
- **1-create_database_if_missing.sql:** Creates a database if it doesn't exist.
- **2-remove_database.sql:** Deletes a database if it exists.
- **3-list_tables.sql:** Lists all tables in a specified database.
- **4-first_table.sql:** Creates a table called `first_table` with columns `id` (INT) and `name` (VARCHAR(256)).
- **5-full_table.sql:** Prints the full description of the table `first_table`.
- **6-list_values.sql:** Lists all rows of the table `first_table`.
- **7-insert_value.sql:** Inserts a new row into `first_table` with `id = 89` and `name = 'Best School'`.
- **8-count_89.sql:** Displays the number of records with `id = 89` in `first_table`.
- **9-full_creation.sql:** Creates a table called `second_table` and inserts multiple rows.
- **10-top_score.sql:** Lists all records of `second_table` ordered by `score` in descending order.
- **11-best_score.sql:** Lists all records with a `score >= 10` in `second_table`.
- **12-no_cheating.sql:** Updates the score of `Bob` to 10 in `second_table`.
- **13-change_class.sql:** Removes all records with a `score <= 5` in `second_table`.
- **14-average.sql:** Computes the average score of all records in `second_table`.
- **15-groups.sql:** Lists the number of records with the same score in `second_table`.
- **16-no_link.sql:** Lists all records of `second_table` with a non-empty `name` field ordered by descending score.

## Usage

1. **Ensure MySQL Server is Running:**
Make sure your MySQL server is running. Start it with a command like:
```sh
sudo service mysql start
