import sys
import json
import boto3


s3 = boto3.client('s3')

#Replace these with your S3 bucket and key (JSON source file)
bucket = 'weather-data-tejaswini'
key = 'raw/weather_data_Pune_2025-07-18_22-15-35.json'
output_key = 'transformed/weather_data_flattened.json'

# Get the JSON data
response = s3.get_object(Bucket=bucket,Key=key)
content = response['Body'].read().decode('utf-8')
data = json.loads(content)

# Transformation: Flattening nested JSON

flattened_data = {
    "location_name": data['location']['name'],
    "region": data['location']['region'],
    "country": data['location']['country'],
    "latitude": data['location']['lat'],
    "longitude": data['location']['lon'],
    "timezone": data['location']['tz_id'],
    "localtime": data['location']['localtime'],
    
    "last_updated": data['current']['last_updated'],
    "temperature_c": data['current']['temp_c'],
    "humidity": data['current']['humidity'],
    
    "condition_text": data['current']['condition']['text'],
    "condition_code": data['current']['condition']['code']
}

# Convert to JSON string
output_json =json.dumps(flattened_data)

# Upload to S3 (transformed folder)
s3.put_object(Bucket=bucket, Key=output_key, Body=output_json)

print("Transformation complete and uploaded to:",output_key)