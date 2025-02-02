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
                sh 'ls -R ${WORKSPACE}'
                sh 'cd ${WORKSPACE} && . venv/bin/activate && PYTHONPATH=${WORKSPACE} pytest test/test_bank_account.py --junitxml=unit-test-results.xml'
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
                sh 'docker run -d -p 5000:5000 --name test-app bank_account_app'
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
                sh 'docker stop test-app && docker rm test-app'
            }
        }
        stage('Publish test reports'){
            steps {
                junit '**/*-test-results.xml'
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
            echo "Pipeline completed!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
