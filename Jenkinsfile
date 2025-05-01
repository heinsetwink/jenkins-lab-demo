pipeline {
    agent any

    environment {
        // Define virtual environment directory and app directory (modify as per your setup)
        VENV_DIR = 'venv'
        APP_DIR = 'app.py'
    }

    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Code') {
            steps {
                script {
                    // Clone the repository and checkout the code
                    sh 'git clone https://github.com/heinsetwink/jenkins-lab-demo.git'
                    dir('jenkins-lab-demo') {
                        sh 'git checkout main'
                    }
                }
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                script {
                    // Create a virtual environment if not already created
                    sh 'python3 -m venv ${VENV_DIR}'
                    sh './${VENV_DIR}/bin/pip install --upgrade pip'
                    sh './${VENV_DIR}/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run tests using unittest
                    sh './${VENV_DIR}/bin/python -m unittest discover -s . -p test_*.py'
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    // Run Flask app in the background using nohup
                    sh 'nohup ./${VENV_DIR}/bin/python ${APP_DIR} > flask.log 2>&1 &'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after the pipeline'
        }
    }
}

