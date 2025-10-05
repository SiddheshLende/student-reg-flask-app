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
                # Create and activate virtual environment
                python3 -m venv venv
                . venv/bin/activate

                # Upgrade pip and install dependencies inside venv
                python3 -m pip install --upgrade pip
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
