# End-to-End Data Pipeline using Apache Airflow

## 📌 Project Overview
This project demonstrates an end-to-end data pipeline built using Python, PostgreSQL, and Apache Airflow. The pipeline extracts e-commerce data from CSV files, transforms it using Pandas, and loads it into a PostgreSQL database.

## 🏗️ Architecture
CSV Files → Extract → Transform → Load → PostgreSQL → Airflow Automation

## ⚙️ Workflow
1. Extract data from CSV files
2. Transform data using Pandas (data cleaning & formatting)
3. Load data into PostgreSQL
4. Automate the pipeline using Airflow DAG

## 🔄 Airflow DAG
The pipeline is divided into 3 tasks:
- extract_task
- transform_task
- load_task

These tasks run sequentially:
extract → transform → load

## 🚀 Features
- Multi-step ETL pipeline
- Automated workflow using Airflow
- Logging implemented for monitoring
- Retry mechanism for failure handling
- Cross-environment setup (Windows + WSL)

## 🛠️ Tech Stack
- Python
- Pandas
- PostgreSQL
- Apache Airflow
- WSL (Linux)

## 📂 Project Structure

data-pipeline-project/

│
├── data/

├── scripts/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│
├── README.md
├── requirements.txt


## 📊 Future Improvements
- Add dashboard (Power BI / Tableau)
- Deploy Airflow on cloud (AWS/GCP)
- Add real-time data processing

## 👨‍💻 Author
Abhay Barad
