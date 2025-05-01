pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/heinsetwink/jenkins-lab-demo.git'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run App') {
            steps {
                echo 'Starting Flask app...'
                sh 'nohup python3 app.py &'
            }
        }
    }
}

