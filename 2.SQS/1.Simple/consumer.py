import boto3
import json
import time

sqs = boto3.client('sqs', region_name='eu-north-1')
queue_url = "https://sqs.eu-north-1.amazonaws.com/353615901447/OrderQueue"

def process_orders():
    while True:
        messages = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=5,
            WaitTimeSeconds=10
        )
        if "Messages" in messages:
            for msg in messages["Messages"]:
                order = json.loads(msg["Body"])
                print(f"Processing order: {order}")

                # Delete after processing
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=msg["ReceiptHandle"]
                )
        else:
            print("No messages in queue. Waiting...")

if __name__ == "__main__":
    process_orders()
