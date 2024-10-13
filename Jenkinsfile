pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'clone....'
                docker images
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                docker -v
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                // Your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Your deploy steps here
            }
        }
    }
}