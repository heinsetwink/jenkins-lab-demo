pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/heinsetwink/jenkins-lab-demo.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Nothing to build. Just Python files.'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python3 -m unittest discover -s . -p "*.py"'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy step (simulated)...'
            }
        }
    }
}

