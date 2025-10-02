# Flask Calculator App with Docker & Amazon ECR

This project expands on the earlier Flask app that adds two numbers.  
**Upgrades include:**
1. A GUI-based calculator.
2. Containerization of the app using Docker.
3. Deployment on **Amazon EC2** via **Amazon ECR**.

---

## **Part 1: Setup and Push Image to ECR**

### **Step 1: Create an IAM Role for EC2 to Access ECR**

1. Go to **AWS Management Console → IAM → Roles → Create role**.
2. **Select trusted entity**: AWS service → EC2 → Next.
3. **Attach permissions**:
   - Option A (simpler): `AmazonEC2ContainerRegistryFullAccess`
4. **Name the role** (e.g., `EC2-ECR-Role`) → Create role.
5. **Attach role to EC2**:
   - EC2 Console → Instances → Select instance → Actions → Security → **Modify IAM Role** → Choose `EC2-ECR-Role` → Save.
6. **Verify access**:
```bash
ssh -i your-key.pem ec2-user@<EC2_PUBLIC_IP>
aws ecr get-login-password --region <your-region>
```

---

### **Step 2: Install Docker on EC2 (Amazon Linux 2023)**

```bash
sudo dnf update -y
sudo dnf install -y docker
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker ec2-user
```

* Log out and back in for group changes to take effect.
* Test Docker:

```bash
docker run hello-world
```

---

### **Step 3: Prepare Your Flask App**

Project structure:

```
calculator-app/
├── app.py
├── requirements.txt
└── Dockerfile
```

* `app.py`: Flask app code.  
* `requirements.txt`: Python dependencies (e.g., `flask`).  
* `Dockerfile`: Instructions to containerize the app.

---

### **Step 4: Build and Test Locally**

```bash
docker build -t calculator-app .
docker run -p 5000:5000 calculator-app
```

* Access at: `http://<EC2_PUBLIC_IP>:5000`

---

### **Step 5: Create an ECR Repository**

```bash
aws ecr create-repository --repository-name calculator-app
```

---

### **Step 6: Authenticate Docker with ECR**

```bash
aws ecr get-login-password --region eu-north-1 \
| docker login --username AWS --password-stdin 353615901447.dkr.ecr.eu-north-1.amazonaws.com
```

---

### **Step 7: Tag and Push Image**

```bash
docker tag calculator-app:latest 353615901447.dkr.ecr.eu-north-1.amazonaws.com/calculator-app:latest
docker push 353615901447.dkr.ecr.eu-north-1.amazonaws.com/calculator-app:latest
```

* Verify in AWS Console → ECR → `calculator-app` → Images.

---

## **Part 2: Pull and Run Image on EC2**

### **EC2 Security Group Inbound Rules**

Ensure your EC2 security group allows:

- **Port 22 (SSH)**: ✅ Remote access  
- **Port 443 (HTTPS)**: ✅ Secure web traffic  
- **Port 5000 (Custom TCP)**: ✅ Flask app traffic  

---

### **Step 1: Authenticate Docker with ECR**

```bash
aws ecr get-login-password --region eu-north-1 \
| docker login --username AWS --password-stdin 353615901447.dkr.ecr.eu-north-1.amazonaws.com
```

---

### **Step 2: Pull the Docker Image from ECR**

```bash
docker pull 353615901447.dkr.ecr.eu-north-1.amazonaws.com/calculator-app:latest
```

---

### **Step 3: Run the Container**

```bash
docker run -d --restart always -p 5000:5000 \
353615901447.dkr.ecr.eu-north-1.amazonaws.com/calculator-app:latest
```

---

### **Step 4: Test Your App**

Open a browser:

```
http://<EC2-Public-IP>:5000
```

You should see the Flask Calculator app running.

---

## **✅ Full Workflow Summary**

1. Write Flask app and `Dockerfile`.  
2. Build Docker image locally.  
3. Create an ECR repository.  
4. Authenticate Docker with ECR.  
5. Tag and push image to ECR.  
6. Configure EC2 (IAM role + Docker + Security Group).  
7. Pull image on EC2.  
8. Run the container with port mapping.  
9. Access the app in your browser.

---

**Technologies & Skills:** Flask, Python, Docker, Amazon EC2, Amazon ECR, containerization, cloud deployment.


