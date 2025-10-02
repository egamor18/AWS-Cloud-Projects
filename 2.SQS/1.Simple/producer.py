import boto3
import json
import random
import time

sqs = boto3.client('sqs', region_name='eu-north-1')
queue_url = "https://sqs.eu-north-1.amazonaws.com/353615901447/OrderQueue"

def send_order(order_id):
    order = {
        "order_id": order_id,
        "item": random.choice(["Laptop", "Phone", "Headphones"]),
        "quantity": random.randint(1, 5)
    }
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(order)
    )
    print(f"Sent: {order} | MessageId: {response['MessageId']}")

if __name__ == "__main__":
    for i in range(5):
        send_order(f"ORD-{1000+i}")
        time.sleep(2)
