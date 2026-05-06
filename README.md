# IoT Vehicle Telematics Data Pipeline

## Project Overview

This project implements a production-grade end-to-end ETL data pipeline for IoT vehicle telemetry data using AWS and PySpark.

Modern vehicles continuously generate sensor data such as speed, engine temperature, battery level, and diagnostic codes. This pipeline ingests, processes, analyzes, and visualizes that data to extract actionable insights and detect anomalies.

---

## Key Highlights 
- Ingest telemetry data in near real-time
- Store raw data in Amazon S3
- Perform scalable ETL using PySpark
- Generate multi-dimensional analytics datasets
- Detect vehicle anomalies & behavioral patterns
- Load curated data into Amazon Redshift
- Create visual insights using plots

---

## Architecture

```
Sensor/Data Source → API Gateway → AWS Lambda → S3 (Raw Layer)
                                               ↓
                                        PySpark ETL
                                               ↓
                           S3 (Processed + Aggregated Layers)
                                               ↓
                                   Amazon Redshift
                                               ↓
                                       Visualization
```

---

## 📂 Project Structure

```
Vehicle-Telematics-Pipeline /
|
|-- config/
|   |-- config.py
|   |-- logger.py
|
|-- src/
|   |-- aws/
|   |   |-- lambda_function.py
|   |
|   |-- data_ingestion/
|   |   |-- data_ingestion.py
|   |
|   |-- data_processing/
|   |   |-- aggregation.py
|   |   |-- anomaly_detection.py
|   |   |-- time_series_analysis.py
|   |   |-- data_processor.py
|   |
|   |-- visualization/
|   |   |-- aggregation_visualizattion.py
|   |   |-- anomaly_visualization.py
|   |   |-- relationship_analysis.py
|   |   |-- rolling_metrics.py
|   |   |-- timeseries_analysis.py
|   |   |-- trip_analysis.py
|   |
|   |-- load_phase/
|   |   |--  create_tables.py
|   |   |-- query_executor.py
|   |
|   |-- process.py 
|   |-- load_to_redshift.py
|   |-- visualize.py 
|
|-- data/
|   |-- v2.csv
|
|-- logs/
|   |-- app.log
|
|-- screenshots/
|   |-- device_avg_speed.png
|   |-- device_vs_time_heatmap.png
|   |-- hourly_speed_trend.png
|   |-- rolling_metrics.png
|   |-- speed_spike.png
|   |-- temp_anomaly.png
|   |-- speed_vs_eload.png
|   |-- temp_vs_eload.png
|   |-- timeseries_plot.png
|   |-- trip_duration_comparision.png
|   |-- trip_speed_distribution.png
|
|-- .gitignore
|-- requirements.txt
|-- README.md
```

---

## Tech Stack

* **Cloud**: AWS (API Gateway, S3, Lambda, Redshift Serverless)
* **Processing**: PySpark
* **Language**: Python
* **Visualization**: Matplotlib
* **Storage Format**: JSON(raw), Parquet(processed)

---

## Features

- Uses real-world dataset instead of synthetic data
- Scalable PySpark ETL pipeline
- Advanced anomaly detection (rule-based + statistical)
- Time-series analytics
- Multi-layer data lake architecture
- Optimized storage using Parquet
- Data warehouse integration (Redshift)
- End-to-end data engineering workflow

---

## Data Pipeline Flow

### 1. Data Ingestion

- CSV dataset is streamed using Python script
- API Gateway triggers Lambda
- Lambda:

  - Validates data
  - Adds metadata
  - Stores data in S3 (raw layer)

### 2. Data Storage (S3)

- `/raw/` -> incoming data (JSON)
- `/processed/` -> cleaned data (parquet)
- `/aggregated/` -> analytics-ready data (parquet)

### 3. Data Processing (Pyspark)

- Read raw JSON from S3
- Clean data (nulls, duplicates, invalid values)
- Convert data types & timestamps
- Feature engineering (hour, day, week, month)
- Window functions:
  - rolling averages
  - lag features
  - rate calculations
- Anomaly detection:
  - rule-based + statistical (z-score)
- Aggregations:
  - trip-level
  - device-level
  - time-based

### 4. Analytics Layer

- Generate datasets:
  - processed
  - time-series
  - anomaly
  - aggregated
- Perform correlation analysis
- Data quality checks

### 5. Data Warehouse (Redshift)

- Load aggregated data into Redshift
- Tables:
  - vehicle_metrics
  - trip_metrics
  - anomaly_summary
- Enables structured querying & reporting

### 6. Visualization

- Time-series plots (speed, temperature)
- Rolling metrics visualization
- Anomaly highlighting
- Scatter plots & aggregations
- Output as images or notebooks
---

## Dataset

- Source: Levin Vehicle Telematics Dataset (Kaggle)
- Link: https://www.kaggle.com/datasets/yunlevin/levin-vehicle-telematics/data?select=v2.csv
---

## Setup Instructions

### 1. Clone Repository

```
-> git clone https://github.com/Parashuram-V-Pawar/IoT_Vehicle_Telematics_Data_Pipeline.git
-> cd IoT_Vehicle_Telematics_Data_Pipeline
```

### 2. Create Virtual Environment

```
-> python3 -m venv venv
-> source venv/bin/activate  # Mac/linux
-> venv\Scripts\activate      # Windows
```

### 3. Install Dependencies:

```
pip install -r requirements.txt
```

### 4. Create lambda function:
-> Refer docs/lambda for the lambda guide

### 5. Setup serverless Redshift:
-> Refer docs/redshift for the redshift guide

### 6. Run the pipeline using:
```
python process.py
python load_to_redshift.py
python visualize.py
```
---

## Lambda Configuration

### Variables

| Key         | Value            |
| ----------- | ---------------- |
| BUCKET_NAME | your-bucket-name |

---

## Future Improvements

- Add real-time streaming 
- Add monitoring (CloudWatch + Alerts)
- Build dashboard (Power BI / Tableau)
- Implement ML models for predictions

---

## Author
```
Name: Parashuram V Pawar
GitHub username: Parashuram-V-Pawar
```
