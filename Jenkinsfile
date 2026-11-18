
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Starting DevOps Project'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                sh 'docker compose up -d'
                sh 'sleep 15'
            }
        }

        stage('Selenium Testing') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pytest -v tests/'
            }
        }
    }

    post {
        always {
            sh 'docker compose down'
        }

        success {
            echo 'All tests passed successfully!'
        }

        failure {
            echo 'Build or testing failed!'
        }
    }
}
