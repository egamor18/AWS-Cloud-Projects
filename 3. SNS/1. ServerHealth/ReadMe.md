---

# **Project: “Server Health Alert System” Using AWS SNS**

**Goal:**
Send an automated alert via email (or SMS) whenever a server (or local script) detects high CPU usage.

**Key AWS Services Used:**

* **SNS** → send notifications (Email/SMS).
* **CloudWatch / Local Script** → detect events.

---

## **Project Overview**

1. **Topic Creation**: Create an SNS topic (e.g., `ServerAlerts`).
2. **Subscription**: Subscribe your email or phone number to the topic.
3. **Event Detection**: A script monitors CPU usage.
4. **Notification**: When CPU usage exceeds a threshold, the script publishes a message to SNS.
5. **Receive Alert**: You get an email/SMS immediately.

---

## **Step 1: Create an SNS Topic**

Using AWS Console or CLI:

```bash
aws sns create-topic --name ServerAlerts
```
NOTE: Replace 123456789012 with your AWS Account Number

Save the returned **ARN**, e.g.:

```
arn:aws:sns:eu-north-1:123456789012:ServerAlerts
```

---

## **Step 2: Subscribe to the Topic**

Example (Email subscription):

```bash
aws sns subscribe \
    --topic-arn arn:aws:sns:eu-north-1:123456789012:ServerAlerts \
    --protocol email \
    --notification-endpoint your-email@example.com
```

> Check your email and **confirm the subscription**.

---

## **Step 3: Create a Monitoring Script**

Here’s a simple **Python example** using `psutil` and `boto3`:

```python
import boto3
import psutil

# SNS topic ARN
TOPIC_ARN = "arn:aws:sns:eu-north-1:123456789012:ServerAlerts"

# Initialize SNS client
sns = boto3.client('sns', region_name='eu-north-1')

# Threshold CPU usage %
THRESHOLD = 80

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
```

* Install dependencies:

```bash
pip install boto3 psutil
```

* Make sure your AWS credentials are configured (`aws configure`).

---

## **Step 4: Run and Test**

* Run the script manually or set it up as a **cron job** to monitor periodically.
* If CPU exceeds the threshold, you receive an **email alert** immediately.

---

## **Optional Extensions**

1. Monitor other metrics: Memory usage, Disk space.
2. Send alerts to multiple endpoints: Email, SMS, Slack (via Lambda).
3. Integrate with CloudWatch for real server monitoring.

---
Yes 👍 On Linux you can **stress-test your CPU** with tools like `stress` or `stress-ng`.

---


________________________________________________________________________________________

### 🔹 Install `stress`

On Ubuntu/Debian:

```bash
sudo apt update
sudo apt install stress -y
```

On Amazon Linux:

```bash
sudo yum install stress -y
```

---

### 🔹 Run a simple CPU stress test

```bash
stress --cpu 4 --timeout 30s
```

* `--cpu 4` → spins 4 workers (1 per CPU core, adjust to your machine).
* `--timeout 30s` → run the test for 30 seconds.

---

### 🔹 Using `stress-ng` (more powerful)

```bash
sudo apt install stress-ng -y
stress-ng --cpu 4 --timeout 30s --metrics-brief
```

* Provides detailed metrics: load, CPU usage, etc.

---

👉 Tip: While the test is running, open another terminal and run:

```bash
top
```

or

```bash
mpstat 1
```

