
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'GitHub checkout successful!'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker compose build'
            }
        }

        stage('Start Containers') {
            steps {
                bat 'docker compose up -d'
                bat 'powershell -NoProfile -Command "Start-Sleep -Seconds 20"'
            }
        }

        stage('Selenium Testing') {
            steps {
                bat 'py -m pip install -r requirements.txt'
                bat 'py -m pytest -v tests/'
            }
        }
    }

    post {
        always {
            bat(returnStatus: true, script: 'docker compose down')
        }

        success {
            echo 'SUCCESS: Docker and Selenium tests completed!'
        }

        failure {
            echo 'FAILED: Check Console Output for errors.'
        }
    }
}
