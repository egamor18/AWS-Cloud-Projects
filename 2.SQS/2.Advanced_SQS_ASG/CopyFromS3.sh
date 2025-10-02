#!/bin/bash
# Update packages
yum update -y

# Install AWS CLI and Python 3 (Amazon Linux 2/2023 usually comes with Python3)
yum install -y awscli python3 python3-pip

# Install boto3
pip3 install --upgrade boto3


# Make a working directory
mkdir -p /home/ec2-user/scripts
cd /home/ec2-user/scripts

# Download Python script from S3
aws s3 cp s3://sa.akla-general-bucket-eu-north1/consumer.py .

# Run the Python script
python3 consumer.py > /var/log/consumer.log 2>&1
