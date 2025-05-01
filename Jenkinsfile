pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    stages {
        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/heinsetwink/jenkins-lab-demo.git'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh 'python3 -m venv $VENV'
                sh './$VENV/bin/pip install --upgrade pip'
                sh './$VENV/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh './$VENV/bin/python -m unittest discover -s . -p "test_*.py"'
            }
        }

        stage('Run App') {
            steps {
                echo 'Starting Flask app...'
                sh 'nohup ./$VENV/bin/python3 app.py > app.log 2>&1 &'
            }
        }
    }
}

