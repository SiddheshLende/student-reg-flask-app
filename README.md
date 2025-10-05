# student-reg-flask-app  
# Overview
This project is a simple Flask web application that allows users to register students, store their information in a MySQL database, and view all registered students. It is deployed on an AWS EC2 instance and can be automated with Jenkins CI/CD.  
# Features  
Student Registration Form  
Store data in MySQL database  
View registered students in a tabular format  
Optional: Edit/Delete student records  
Deployment via Jenkins pipeline  
# Prerequisites  
AWS EC2 instance (Ubuntu)  
Python 3.12+  
MySQL server running  
Git installed  
Jenkins installed (optional for CI/CD)  
Security Group with port 5000 open for Flask  
# Installation & Setup  
Clone Repository  
git clone https://github.com/siddheshlende/student-reg-flask-app.git
cd student-reg-flask-app  
Create Virtual Environment  
python3 -m venv venv  
source venv/bin/activate  
Install Dependencies  
pip install --upgrade pip  
pip install -r requirements.txt  
MySQL Database Setup  
Login to MySQL:  
mysql -u root -p  
Create Database and Table:  
CREATE DATABASE student_db;

USE student_db;  
CREATE TABLE students (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(50),  
    email VARCHAR(50),  
    phone VARCHAR(20),  
    course VARCHAR(50),  
    address TEXT  
);  
Update database credentials in app.py:  
conn = mysql.connector.connect(  
    host="localhost",  
    user="your_mysql_user",  
    password="your_mysql_password",  
    database="student_db"  
)  
Run Flask App  
python3 app.py  
Access the app in browser: http://<EC2_PUBLIC_IP>:5000  
nohup python3 app.py > flask.log 2>&1 &  
tail -f flask.log  

# Jenkins CI/CD Deployment  
Install Jenkins on EC2  
Create a new Pipeline job with your GitHub repo  
Use the following Jenkinsfile:  
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/siddheshlende/student-reg-flask-app.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install --break-system-packages -r requirements.txt
                '''
            }
        }
        stage('Run Flask App') {
            steps {
                sh '''
                    . venv/bin/activate
                    nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}

