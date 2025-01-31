pipeline {
    agent { 
        docker {
            image 'python:3.9'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DavidGergov03/Bank_account_project_flask.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '/usr/bin/python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'echo Running tests...'
                // Replace this with actual test command, e.g., for Python:
                // sh 'pytest'
            }
        }
        stage('Build Dcoker image') {
            steps {
                sh 'echo Building the project...'
                sh 'docker build -t bank_account_app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying application...'
                // Add deployment steps here (e.g., Docker, Kubernetes, SCP)
            }
        }
    }
}
