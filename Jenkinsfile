pipeline {
    agent any

    environment {
        VENV_PATH = './venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create virtual environment if it doesn't exist
                    if (!fileExists(VENV_PATH)) {
                        sh 'python3 -m venv venv'
                    }
                    sh './venv/bin/pip install --upgrade pip'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the tests
                    sh './venv/bin/python -m unittest discover -s . -p "test_*.py"'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Run the app with nohup
                    sh 'nohup ./venv/bin/python app.py &'
                }
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Cleaning up after the pipeline'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

