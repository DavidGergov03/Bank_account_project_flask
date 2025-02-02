pipeline {
    agent {
        label 'docker-agent'
    }
    
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
                sh '. venv/bin/activate && pip install pytest'
            }
        }
        stage('Run unit tests') {
            steps {
                sh 'cd ${WORKSPACE} && . venv/bin/activate && PYTHONPATH=${WORKSPACE} pytest test/test_account.py --junitxml=unit-test-results.xml'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'echo Building the project...'
                sh 'docker build -t bank_account_app .'
            }
        }
        stage('Run container for testing') {
            steps {
                sh 'docker stop test-app-container && docker rm test-app'
                sh 'docker run -d -p 5001:5000 --name test-app-container bank_account_app'
                sleep(time: 5, unit: "SECONDS")
            }
        }
        stage('Run routes test') {
            steps {
                 sh 'cd ${WORKSPACE} && . venv/bin/activate && PYTHONPATH=${WORKSPACE} pytest test/test_routes.py --junitxml=integration-test-results.xml'
            }
        }
        stage('Stop and remove container') {
            steps {
                sh 'docker stop test-app-container && docker rm test-app'
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo Deploying application...'
            }
        }
    }
     post {
        always {
            echo "Publishing test results"
            junit '**/*-test-results.xml'
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
