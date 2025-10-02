# Project Description

This project demonstrates the **end-to-end deployment of a Flask web application on AWS**.

## Goals

1. Deploy a simple Flask app on an **Amazon Linux 2023 EC2 instance**, exposing endpoints for a welcome message and dynamic addition of two numbers.  
2. Expand it into a **functional calculator**, containerize the app using **Docker**, push the image to an **Amazon ECR** repository, and pull & run it on another EC2 instance, showcasing a complete workflow for containerized application deployment on AWS.

## Technologies & Skills

Flask, Python, Docker, Amazon EC2, Amazon ECR, containerization, cloud deployment.

---


# Create an EC2 Security Group with the following Inbound Rules

Your current inbound rules allow the following:

- **Port 22 (SSH):** ✅ Remote access to the instance for management.  
- **Port 443 (HTTPS):** ✅ Secure web traffic (SSL/TLS).  
- **Port 5000 (Custom TCP):** ✅ Flask app traffic (since your `app.py` runs on port 5000).  

Attach this SG when creating the EC2

---


# 🚀 Run Flask on Amazon Linux 2023 with EC2 Instance Connect

### 1. **Connect to your EC2**

* From the AWS console, go to **EC2 → Instances → Connect**.
* Select **EC2 Instance Connect** and click **Connect**.

---

### 2. **Update your system**

```bash
sudo dnf update -y
```

---

### 3. **Install Python and pip**

Amazon Linux 2023 comes with Python 3, but let’s make sure:

```bash
python3 --version
```

If pip is missing:

```bash
sudo dnf install -y python3-pip
```

---

### 4. **Install Flask**

```bash
pip3 install flask
```

---

### 5. **Create your app file**

```bash
nano app.py
```

---

### 6. **Run the Flask app**

```bash
python3 app.py
```

You should see something like:

```
* Running on http://0.0.0.0:5000
```

---

### 7. **Test in browser**

Open:

```
http://<your-ec2-public-ip>:5000
```

You should see:

```
Hello! 🎉 This is my Python website running on EC2.
```

And if you try:

```
http://<your-ec2-public-ip>:5000/add/7/3
```

It should return:

```
The sum of 7 and 3 is 10
```

---
