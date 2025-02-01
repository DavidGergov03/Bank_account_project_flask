pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DavidGergov03/Bank_account_project_flask.git'
            }
        }
        stage('Install Dependencies') {
            steps {
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
