terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# AWS provider
provider "aws" {
  region = "ap-south-1"
}

# Find the latest Ubuntu 24.04 AMI
data "aws_ami" "ubuntu" {
  most_recent = true

  # Canonical (Ubuntu) AWS account
  owners = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Security Group (Firewall)
resource "aws_security_group" "flood_sg" {
  name        = "flood-monitoring-sg"
  description = "Security group for flood monitoring EC2"

  # Allow SSH
  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow HTTP
  ingress {
    description = "HTTP"
    from_port     = 80
    to_port       = 80
    protocol      = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow outgoing traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 virtual machine
resource "aws_instance" "flood_server" {
  ami           = data.aws_ami.ubuntu.id
  instance_type = "t3.micro"
  key_name = "my-key"
   

  # Attach our Security Group
  security_groups = [aws_security_group.flood_sg.name]

  # EC2 name
  tags = {
    Name = "Flood-Monitoring-Server"
  }
}