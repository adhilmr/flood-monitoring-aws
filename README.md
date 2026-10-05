# 🌊 Flood Monitoring System on AWS

A cloud-based flood monitoring application developed as an academic project to demonstrate **cloud computing, virtualization, and Infrastructure as Code (IaC)** using AWS.

The system simulates rainfall and water-level sensor readings using Python and generates a flood alert when the water level exceeds a defined threshold.

## 📌 Problem Statement

Flooding can cause significant damage to people, infrastructure, and property. Early detection of rising water levels can help provide timely warnings.

This project demonstrates a simplified monitoring system using simulated environmental data instead of physical sensors.

## 🎯 Objectives

* Simulate rainfall and water-level data.
* Monitor water-level thresholds.
* Generate flood alerts for dangerous levels.
* Deploy the application on an AWS EC2 virtual machine.
* Demonstrate cloud virtualization and Infrastructure as Code.

## 🏗️ Architecture

```text
Simulated Sensor Data
        ↓
Python Application
        ↓
Threshold Analysis
        ↓
 ┌──────┴──────┐
 ↓             ↓
SAFE        FLOOD ALERT
        ↓
     AWS EC2
```

## ☁️ AWS Infrastructure

The application is deployed on **Amazon EC2**, which provides the virtualized computing environment.

Supporting AWS concepts include:

* **EC2** — Virtual machine for application deployment
* **VPC** — Network isolation
* **Security Group** — Instance-level firewall
* **Terraform** — Infrastructure as Code
* **AWS CLI** — AWS resource management

**Region:** `ap-south-1` (Mumbai)

## 🐍 Application

The Python application generates simulated environmental readings and compares the water level against a predefined threshold.

Example:

```text
Rainfall   : 93 mm
Water Level: 91 cm

⚠️ FLOOD ALERT!
```

Safe conditions produce a normal status instead.

## 🛠️ Technologies

| Technology   | Purpose                |
| ------------ | ---------------------- |
| Python       | Monitoring logic       |
| AWS EC2      | Virtualized computing  |
| AWS VPC      | Networking             |
| Terraform    | Infrastructure as Code |
| AWS CLI      | Cloud management       |
| Linux        | Server environment     |
| Git & GitHub | Version control        |

## 🚀 Deployment

Infrastructure is provisioned using Terraform:

```text
Terraform Configuration
        ↓
terraform init
        ↓
terraform plan
        ↓
terraform apply
        ↓
AWS Infrastructure
        ↓
EC2 Application
```

## 🔮 Future Improvements

* Real IoT sensors
* AWS IoT Core integration
* Web dashboard
* CloudWatch monitoring
* Email/SMS alerts
* Database integration
* Docker containerization
* CI/CD pipeline

## 👨‍💻 Author

**Adhil**

AWS Virtualization & Cloud Computing Academic Project
