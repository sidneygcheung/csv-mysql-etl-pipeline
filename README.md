# CSV to MySQL ETL Pipeline

## Overview
This project is a Python-based ETL (Extract, Transform, Load) pipeline that imports structured data from CSV files into a MySQL database. It handles states, cities, and customer data, demonstrating relational database design, data ingestion, and basic ETL workflows.

---

## Features
- Imports state data from CSV into MySQL
- Imports city data linked to states
- Imports customer records linked to city/state IDs
- Uses environment variables for secure database configuration
- Batch inserts for efficient database loading
- Debug mode for step-by-step execution tracing

---

## Tech Stack
- Python 3
- MySQL
- mysql-connector-python
- python-dotenv
- CSV module

---

## Project Structure
state_script.py        - Imports states from CSV  
city_script.py         - Imports cities and builds relationships  
customer_script.py     - Imports customer data with foreign keys  
states.csv             - State dataset  
location.csv           - City/state dataset  
sample_people.csv      - Customer dataset  
.env                   - Environment variables (NOT committed)

---

## Environment Variables
Create a `.env` file in the project root:

DB_HOST=localhost  
DB_USER=your_user  
DB_PASSWORD=your_password  
DB_NAME=your_database  

---

## How to Run

### 1. Install dependencies
pip install mysql-connector-python python-dotenv

### 2. Start MySQL server
sudo systemctl start mysql

### 3. Run scripts
python state_script.py  
python city_script.py  
python customer_script.py  

---

## What This Project Demonstrates
- ETL pipeline design
- CSV data ingestion
- Relational database mapping
- Foreign key relationships (state → city → customer)
- Environment-based configuration
- Debug-driven development workflow

---

## Notes
- Ensure MySQL server is running before executing scripts
- Scripts assume database schema already exists
- Data should not contain duplicate primary keys unless handled
