# 🌦️ Weather Data Pipeline using AWS

This project automates the **ingestion**, **transformation**, and **storage** of real-time weather data using **AWS services** like S3 and Glue, along with **Python** scripting.

It fetches current weather data from [WeatherAPI.com](https://www.weatherapi.com/), stores it locally in JSON format, and uploads it to an AWS S3 bucket. Then an AWS Glue job transforms the raw data into a structured format and saves it back to S3.

---

## 🚀 Project Workflow

1. 🔄 Fetch weather data (temperature, humidity, pressure, etc.) using the Weather API.
2. 💾 Save the data locally as JSON files.
3. ☁️ Upload raw data to an **S3 raw bucket**.
4. 🔧 Trigger a **Glue ETL job** to clean/flatten the data.
5. 📂 Store transformed data into the **S3 processed bucket**.
6. 📝 Upload logs both locally and to **S3 log folder**.

---

## 📊  Architecture Diagram
[WeatherAPI] → [Local JSON File] → [S3 /raw/] → [AWS Glue Job] → [S3 /transformed/] → [Athena or Analysis]
                                        ↓
                                    [S3 /logs/]

---
## 🛠️ Technologies Used

- **Python 3.x**
- **AWS S3**
- **AWS Glue**
- **Boto3 (Python SDK for AWS)**
- **Requests (Python HTTP library)**

---

## 📁 Folder Structure
```
weather-data-pipeline-aws/
│
├── .gitignore # Git ignore rules
├── README.md # Project documentation
├── fetch_log.txt # Log file for API fetches
├── weather_data_fetcher.py # Python script to fetch data
├── weather_data_transform.py # Glue job script (ETL)
├── weather_data_<...>.json # Sample fetched weather files
└── ...
```
---

## 🏁 Run Locally

### 1️⃣ Install Dependencies

```bash
pip install boto3 requests

```

2️⃣ Configure AWS credentials:

```bash
aws configure
```
Make sure your IAM user has access to S3 and Glue services.

3️⃣ Run the ingestion script:
This script fetches live weather data using www.weatherapi.com API and stores it as JSON files in your local project directory.
```bash
python weather_data_fetcher.py
```
This will:
Fetch live weather data.
Save it locally as weather_data_<city>_<timestamp>.json
Log the result in fetch_log.txt
Upload data and log to S3.

---
## ☁️ AWS Glue ETL Job

After data is fetched and uploaded to S3 (/raw/ folder), run your AWS Glue job to process it.
The job will:

Read raw JSON from s3://<your-bucket>/raw/
Flatten the structure
Save the transformed data to s3://<your-bucket>/transformed/

---

## ✅ S3 Output Structure
```
s3://weather-data-tejaswini/
├── raw/
│   └── weather_data_Pune_2025-07-20_00-41-31.json
│   └── ...
├── transformed/
│   └── weather_data_flattened.json
├── logs/
    └── fetch_log.txt
```
---

## 🧪 Sample Log Output

```text
Weather data fetched successfully for city: Pune
Data saved to weather_data_Pune_2025-07-19_15-54-13.json
Uploaded weather_data_Pune_2025-07-19_15-54-13.json to S3 bucket: weather-data-tejaswini/raw/
Uploaded log file to S3 bucket: weather-data-tejaswini/logs/

```

---
## 📌 Notes
Replace bucket name and region as per your AWS configuration.
You can automate the Glue trigger via Lambda or scheduler if needed (future scope).
Ensure your IAM roles have necessary permissions.

