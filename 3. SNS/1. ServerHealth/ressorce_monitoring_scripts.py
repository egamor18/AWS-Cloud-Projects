import boto3
import psutil

# SNS topic ARN
TOPIC_ARN = "arn:aws:sns:eu-north-1:353615901447:ServerAlerts"


# Initialize SNS client
sns = boto3.client('sns', region_name='eu-north-1')

# Threshold CPU usage %
THRESHOLD = 22

cpu_usage = psutil.cpu_percent(interval=5)
if cpu_usage > THRESHOLD:
    message = f"⚠️ High CPU usage detected: {cpu_usage}%"
    sns.publish(
        TopicArn=TOPIC_ARN,
        Message=message,
        Subject="Server Health Alert"
    )
    print("Alert sent!")
else:
    print(f"CPU usage is normal: {cpu_usage}%")
