# 🌊 Flood Monitoring System on AWS

A simple cloud-based Flood Monitoring System built as an academic project to demonstrate **virtualization and cloud computing using Amazon Web Services (AWS)**.

The system simulates environmental sensor data such as **rainfall and water level**, processes the data using a Python application, and generates an alert when the water level reaches a dangerous threshold.

---

## 📌 Problem Statement

Floods can cause serious damage to people, property, roads, and infrastructure. A monitoring system can help detect dangerous water levels early and provide an alert.

For this project, real physical sensors are not required. Instead, the system **simulates rainfall and water-level sensor readings using Python**.

The application is deployed on an **AWS EC2 virtual machine**, demonstrating how cloud virtualization can be used to run an environmental monitoring application.

---

## 🎯 Objectives

- Simulate rainfall and water-level sensor data.
- Monitor the simulated water level.
- Detect when the water level crosses a danger threshold.
- Generate a flood warning/alert.
- Deploy the application on an AWS EC2 instance.
- Demonstrate virtualization using AWS.
- Learn basic AWS, Linux, Python, Terraform, and networking concepts.

---

## 🧠 How the Project Works

The basic flow is:

```text
Simulated Sensor Data
        ↓
   Python Application
        ↓
 Read Rainfall / Water Level
        ↓
 Compare with Threshold
        ↓
   ┌────┴────┐
   ↓         ↓
Safe       Danger
   ↓         ↓
Normal     Flood Alert
```

### Example

Suppose the application uses:

```text
Water level threshold = 80 cm
```

If the simulated sensor produces:

```text
Water level = 45 cm
```

The system reports:

```text
Status: SAFE
```

If it produces:

```text
Water level = 90 cm
```

The system reports:

```text
⚠️ FLOOD ALERT!
```

The project can later be extended to use a web interface, email/SMS notifications, real sensors, or other AWS services.

---

# ☁️ AWS Architecture

The main AWS service used for the project is:

### Amazon EC2

**EC2 (Elastic Compute Cloud)** provides a virtual server in the AWS cloud.

Instead of running the Python application only on the local Windows computer, we create an EC2 virtual machine and run the application there.

```text
             AWS Cloud
                 │
                 ▼
        ┌─────────────────┐
        │   Amazon EC2    │
        │ Virtual Machine │
        └────────┬────────┘
                 │
                 ▼
        Python Flood Monitor
                 │
          ┌──────┴──────┐
          ▼             ▼
       SAFE         FLOOD ALERT
```

### AWS Region

The project uses:

```text
ap-south-1
```

This is the AWS Mumbai region.

---

# 🖥️ Local Development Environment

The project was developed using:

- Windows 11
- PyCharm
- Python
- PowerShell
- AWS CLI
- Terraform
- Git/GitHub
- AWS EC2

---

# 📁 Project Structure

A simple project structure is:

```text
flood-aws/
│
├── model.py
├── README.md
│
└── terraform/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── terraform.tfvars
```

The exact structure can be expanded as the project develops.

---

# 🐍 Python Application

The Python application is responsible for simulating the flood monitoring logic.

The main idea is:

```python
rainfall = ...
water_level = ...

if water_level >= threshold:
    print("FLOOD ALERT!")
else:
    print("Water level is safe.")
```

The application does not require a physical sensor for the academic demonstration.

Instead, values can be generated or entered as simulated readings.

---

# 🔊 Flood Alert

The simplest version of the project generates a text alert:

```text
⚠️ FLOOD ALERT!
Water level is above the safe threshold.
```

A future version could add:

- 🔊 Computer sound/buzzer
- 📧 Email notification
- 📱 SMS notification
- 🌐 Web dashboard
- 📊 Graphs
- ☁️ AWS CloudWatch monitoring
- 🗄️ Database storage
- 📡 Real IoT sensors

For the current academic version, a Python-generated alert is sufficient to demonstrate the core concept.

---

# 🌐 Why AWS?

The professor required the project to demonstrate **virtualization**.

AWS EC2 is suitable because an EC2 instance is a **virtual machine running in AWS's cloud infrastructure**.

Instead of purchasing a physical server:

```text
Physical Server
      ↓
Virtual Machine
      ↓
AWS EC2
```

We use AWS to provision the virtual computing environment.

This demonstrates:

- Cloud computing
- Server virtualization
- Remote computing
- Linux server administration
- Networking
- Application deployment

---

# 🔧 AWS CLI

AWS CLI allows the terminal to communicate with AWS.

Check whether AWS CLI is installed:

```powershell
aws --version
```

Check the current AWS CLI configuration:

```powershell
aws configure list
```

Verify which AWS identity is being used:

```powershell
aws sts get-caller-identity
```

Set the default region when configuring AWS CLI:

```text
ap-south-1
```

> Never put your AWS Secret Access Key inside this README, GitHub repository, source code, or Terraform files.

---

# 🏗️ Terraform

Terraform is used as **Infrastructure as Code (IaC)**.

Instead of manually creating every AWS resource through the AWS Console, Terraform lets us describe the infrastructure in configuration files.

Basic workflow:

```text
Terraform Code
      ↓
terraform init
      ↓
terraform validate
      ↓
terraform plan
      ↓
terraform apply
      ↓
AWS Resources
```

---

# 📦 Terraform Provider

Terraform needs an AWS provider so that it knows how to communicate with AWS.

Example:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}
```

Provider configuration:

```hcl
provider "aws" {
  region = "ap-south-1"
}
```

### What is a provider?

A provider is a Terraform plugin that allows Terraform to interact with an external platform.

For this project:

```text
Terraform
    ↓
AWS Provider
    ↓
AWS
```

---

# 🚀 Terraform Commands

Go into the Terraform directory:

```powershell
cd "C:\Users\adhur\OneDrive\Desktop\flood-aws\terraform"
```

Initialize Terraform:

```powershell
terraform init
```

This downloads the required provider plugins.

---

## Validate

Check whether the Terraform configuration is syntactically valid:

```powershell
terraform validate
```

Expected result:

```text
Success! The configuration is valid.
```

---

## Format

Format Terraform files:

```powershell
terraform fmt
```

---

## Plan

See what Terraform intends to create:

```powershell
terraform plan
```

This does not normally create the infrastructure. It shows the proposed changes.

---

## Apply

Create the infrastructure:

```powershell
terraform apply
```

Terraform will ask for confirmation.

Type:

```text
yes
```

when you are ready to create the resources.

---

## Destroy

When the project is finished, remove Terraform-managed resources:

```powershell
terraform destroy
```

Then confirm with:

```text
yes
```

This is especially important for AWS resources that can incur charges.

---

# 🖥️ EC2

The planned EC2 setup is a small virtual machine suitable for demonstrating the project.

Conceptually:

```text
AWS
 │
 └── EC2
      │
      ├── Virtual CPU
      ├── Memory
      ├── Storage
      └── Linux Operating System
             │
             └── Python Flood Monitoring Application
```

The exact instance type should be selected according to the current AWS Free Tier/eligibility and project requirements.

---

# 🌐 Networking

An EC2 instance needs networking to communicate with other systems.

Important concepts:

### VPC

A **VPC (Virtual Private Cloud)** is a logically isolated network in AWS.

```text
AWS
 │
 └── VPC
      │
      ├── Subnet
      │
      ├── Route Table
      │
      └── Internet Gateway
```

### Subnet

A subnet is a smaller network inside the VPC.

### Internet Gateway

An Internet Gateway allows communication between the VPC and the public internet when the routing and security configuration allow it.

### Security Group

A security group acts as a virtual firewall for the EC2 instance.

For example, SSH access normally uses:

```text
TCP
Port 22
```

If a web application is exposed, HTTP normally uses:

```text
TCP
Port 80
```

Only open the ports that are actually required.

---

# 🔐 Security

Do not commit sensitive AWS credentials to Git.

Never put these in GitHub:

```text
AWS Access Key
AWS Secret Access Key
Private SSH Key
Passwords
Tokens
```

Use AWS CLI configuration, IAM roles, environment variables, or other appropriate credential mechanisms.

A `.gitignore` file should also prevent Terraform-generated state and local files from accidentally being committed.

Example:

```gitignore
.terraform/
*.tfstate
*.tfstate.*
*.tfvars
*.tfvars.json
```

If a `.tfvars` file contains only non-sensitive project variables, it can be handled differently, but credentials should never be stored in it.

---

# 🧪 Testing the Application

Run the Python application locally:

```powershell
python model.py
```

or:

```powershell
py model.py
```

The application should display the simulated readings and corresponding status.

Example:

```text
Rainfall: 72 mm
Water Level: 45 cm

Status: SAFE
```

Danger example:

```text
Rainfall: 125 mm
Water Level: 91 cm

⚠️ FLOOD ALERT!
Water level has crossed the danger threshold.
```

---

# 📊 Demonstration Flow

For the final academic demonstration:

### Step 1

Show the problem:

```text
Floods can occur when rainfall is high and water levels rise.
```

### Step 2

Show the Python application.

### Step 3

Run the application with safe sensor values.

Example:

```text
Water Level: 40 cm
Status: SAFE
```

### Step 4

Increase the simulated water level.

Example:

```text
Water Level: 90 cm
Status: FLOOD ALERT
```

### Step 5

Explain that the application can be deployed on an AWS EC2 virtual machine.

### Step 6

Show the EC2 instance and explain that it is the virtualized computing environment used to run the application.

### Step 7

Show Terraform and explain that the infrastructure can be created using Infrastructure as Code.

---

# 🧑‍🏫 Simple Explanation for the Professor

You can explain the project like this:

> "Our project is a Flood Monitoring System that simulates rainfall and water-level sensor data using Python. The application compares the water level against a predefined threshold and generates a flood alert when the level becomes dangerous. We use Amazon EC2 as the virtualized computing environment to deploy and run the application. Terraform is used to automate the AWS infrastructure using Infrastructure as Code."

---

# 🔄 Complete Project Flow

```text
             User / Sensor Simulation
                       │
                       ▼
              Python Application
                       │
                       ▼
             Rainfall + Water Level
                       │
                       ▼
              Threshold Checking
                       │
              ┌────────┴────────┐
              │                 │
          Safe Level       Dangerous Level
              │                 │
              ▼                 ▼
         Normal Status      Flood Alert
                                │
                                ▼
                         Future Extension:
                       Sound / Email / SMS
                                │
                                ▼
                         AWS EC2 Deployment
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Flood monitoring logic |
| AWS EC2 | Virtual machine / cloud computing |
| AWS VPC | Network infrastructure |
| AWS Security Group | Virtual firewall |
| Terraform | Infrastructure as Code |
| AWS CLI | Terminal access to AWS |
| Linux | Server operating system |
| Git | Version control |
| GitHub | Source code hosting |
| PyCharm | Python development |

---

# 📚 Concepts Demonstrated

This project demonstrates:

- Cloud computing
- Virtualization
- AWS EC2
- VPC networking
- Security Groups
- Linux server
- Python programming
- Infrastructure as Code
- Terraform
- AWS CLI
- Basic monitoring logic
- Environmental monitoring
- Alert generation

---

# 🚧 Future Improvements

The current project uses simulated sensor data. It can be extended into a more realistic system by adding:

1. Real water-level sensors.
2. Rainfall sensors.
3. IoT devices.
4. AWS IoT Core.
5. A web dashboard.
6. Database storage.
7. CloudWatch monitoring.
8. Email/SMS notifications.
9. Automatic scaling.
10. Containerization using Docker.
11. CI/CD using GitHub Actions or Jenkins.

---

# ⚠️ Cost Reminder

AWS resources can generate charges depending on the service, configuration, region, and account eligibility.

When the project is not being used:

```powershell
terraform destroy
```

should be considered for Terraform-managed resources.

Also check the AWS Console for resources that were created manually.

---

# 📌 Current Project Status

The project is being developed step by step.

Current focus:

```text
Python Flood Monitoring Logic
        ↓
AWS CLI Configuration
        ↓
Terraform
        ↓
AWS Networking
        ↓
EC2
        ↓
Application Deployment
        ↓
Testing & Demonstration
```

---

## 👨‍💻 Author

**Adhil**

Flood Monitoring System — AWS Virtualization Academic Project
