# 🚀 Project: Order Processing Queue with AWS SQS

This project demonstrates how to **simulate an e-commerce order system** using **Amazon SQS** to decouple services.  

---

## 🎯 **Goal**

- A **producer** (order generator) sends messages (orders) to an SQS queue.  
- A **consumer** (worker) polls the queue, processes messages, and deletes them after successful handling.  
- This setup highlights **loose coupling** and **scalability** with AWS SQS.  

---

## 🔧 **Architecture Components**

- **Amazon SQS Queue** → Stores order messages.  
- **Producer (Python script)** → Sends new orders into the queue.  
- **Consumer (Python script)** → Polls the queue, processes orders, deletes them.  
- **EC2 Instance (`SQS_Operations`)** → Runs the producer and serves as the AMI base for scaling consumers.  
- **Auto Scaling Group (ASG)** → Dynamically launches consumer instances based on SQS queue length.  

---

## 📜 **Step 1: Create an SQS Queue**

```bash
aws sqs create-queue --queue-name OrderQueue
```

**Example Output:**

```json
{
    "QueueUrl": "https://sqs.eu-north-1.amazonaws.com/353615901447/OrderQueue"
}
```

---

## 📜 **Step 2: Producer Script (Send Messages)**

- Runs on the `SQS_Operations` EC2 instance.  
- Continuously sends test order messages into the queue.  

✅ **Workflow:**  
1. Run the **consumer script** in one terminal (listens for messages).  
2. Run the **producer script** in another terminal (sends orders).  
3. Observe orders flowing through SQS → consumer processes and deletes them.  

---

## 📜 **Step 3: Launch EC2 (`SQS_Operations`)**

1. Launch an EC2 instance named **`SQS_Operations`**.  
2. Install dependencies:  

```bash
sudo yum update -y
sudo yum install -y python3 python3-pip awscli
pip3 install boto3
```

3. Attach an **IAM Role** with permissions to access **SQS** and **S3**.  
4. Upload the **producer script** to the instance and run it.  
5. Verify messages in the queue using:  

```bash
aws sqs receive-message --queue-url https://sqs.eu-north-1.amazonaws.com/353615901447/OrderQueue
```

---

## 📜 **Step 4: Upload Consumer Script to S3**

- Upload `consumer.py` into your S3 bucket. Example:  

```bash
aws s3 cp consumer.py s3://your-bucket-name/
```

---

## 📜 **Step 5: Create AMI & Launch Template**

1. From the `SQS_Operations` instance, **create an AMI**.  
2. Create a **Launch Template** using this AMI.  
3. In the **User Data** field, insert the script (CopyFromS3.sh) to download and run the consumer.py script from S3:  

4. In **IAM Instance Profile**, select the IAM role created earlier.  

---

## 📜 **Step 6: Create Auto Scaling Group (ASG)**

1. Use the Launch Template created above.  
2. Enable **Automatic Scaling → Dynamic Scaling → Target Tracking Policy**.  
3. Configure scaling based on the SQS queue length (`ApproximateNumberOfMessagesVisible`).  

Example scaling policy JSON:

```json
{
  "CustomizedMetricSpecification": {
    "Dimensions": [
      {
        "Name": "QueueName",
        "Value": "OrderQueue"
      }
    ],
    "MetricName": "ApproximateNumberOfMessagesVisible",
    "Namespace": "AWS/SQS",
    "Statistic": "Average"
  }
}
```

This ensures consumer EC2 instances scale **horizontally** with message volume.  

---

## ✅ **Summary**

- Producer pushes messages (orders) into SQS.  
- Consumer EC2 instances (launched via ASG) pull and process orders.  
- Scaling is **automatically driven by SQS queue length**.  
- Demonstrates a **serverless-style, event-driven architecture** using AWS SQS + EC2 Auto Scaling.  

---

## 🛠️ **Technologies Used**
- **AWS SQS**  
- **Amazon EC2 + Auto Scaling**  
- **Amazon S3**  
- **IAM Roles & Policies**  
- **Python 3, boto3, AWS CLI**  
