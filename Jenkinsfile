pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/DavidGergov03/Bank_account_project_flask.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building the project...'
                // Replace this with your actual build command, e.g., for Java:
                // sh 'mvn package'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
                // Replace this with actual test command, e.g., for Python:
                // sh 'pytest'
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
