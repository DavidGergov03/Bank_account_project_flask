pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DavidGergov03/Bank_account_project_flask.git'
            }
        }
        stage('Setup Python Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh '. venv/bin/activate && echo Running tests...'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'echo Building the project...'
                sh 'docker build -t bank_account_app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying application...'
            }
        }
    }
}
