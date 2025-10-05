pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/SiddheshLende/student-reg-flask-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd stud-reg-flask-app
                python3 -m venv venv || true
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                cd stud-reg-flask-app
                nohup python3 app.py &
                '''
            }
        }
    }
}
