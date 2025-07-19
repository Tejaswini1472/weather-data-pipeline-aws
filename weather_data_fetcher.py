import requests
import json
from datetime import datetime
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# WeatherAPI.com API key and city
API_KEY = "your_api_key_here"  # Replace with your real API key  from https://www.weatherapi.com.
CITY = "Pune"

# API URL
URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}"

try:
    # Call API
    response = requests.get(URL)
    response.raise_for_status()  # Raise error for bad status codes (like 404, 500)

    data = response.json()
    print("Weather data fetched successfully!")

    # Save to local JSON file
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"weather_data_{CITY}_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f" Data saved to {filename}")

    # Add logging
    with open("fetch_log.txt", "a") as log:
        log.write(f"{timestamp} - Fetched data for {CITY}\n")

    # AWS S3 Upload
    BUCKET_NAME = "weather-data-tejaswini"  # Replace with your bucket name
    s3 = boto3.client("s3")

    # Upload weather JSON to raw/
    try:
        s3.upload_file(filename, BUCKET_NAME, f"raw/{filename}")
        print(f" Uploaded {filename} to S3 bucket: {BUCKET_NAME}/raw/")
    except FileNotFoundError:
        print(" The file was not found for upload.")
    except NoCredentialsError:
        print(" AWS credentials not available.")
    except ClientError as e:
        print(f" AWS error: {e}")

    # Upload log file to logs/
    log_filename = "fetch_log.txt"
    try:
        s3.upload_file(log_filename, BUCKET_NAME, f"logs/{log_filename}")
        print(f" Uploaded log file to S3 bucket: {BUCKET_NAME}/logs/")
    except FileNotFoundError:
        print(" Log file not found for upload.")
    except NoCredentialsError:
        print(" AWS credentials not available for log upload.")
    except ClientError as e:
        print(f" AWS log upload error: {e}")

except requests.exceptions.RequestException as e:
    print(" Failed to fetch weather data from API.")
    print(f"Error: {e}")
except json.JSONDecodeError:
    print(" Failed to parse JSON response.")
except Exception as e:
    print(f" An unexpected error occurred: {e}")
