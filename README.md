# Green Taxi Data ETL Pipeline 

A simple and efficient Python-based ETL (Extract, Load, Transform) script that fetches NYC Green Taxi trip data from a public S3 bucket and loads it into a PostgreSQL database.

##  Overview
This project demonstrates how to:
- Handle Parquet file formats using **Pandas** and **PyArrow**.
- Establish a connection with a **PostgreSQL** database using **SQLAlchemy**.
- Securely automate the process of data ingestion for data analysis.

##  Tech Stack
- **Language:** Python 3.x
- **Libraries:** Pandas, SQLAlchemy, Psycopg2, PyArrow
- **Database:** PostgreSQL
- **Data Source:** NYC Taxi & Limousine Commission (TLC) Trip Record Data

##  Prerequisites
Make sure you have the following installed:
- Python
- PostgreSQL
- Required Python packages:
  ```bash
  pip install pandas sqlalchemy psycopg2 pyarrow
