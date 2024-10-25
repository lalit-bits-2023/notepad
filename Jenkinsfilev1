pipeline {
    agent any
    environment {
        // Define docker image name and tag
        def imageName = 'lalitbits2023/notepad'
        def imageTag = 'v2'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sleep(time: 1, unit: 'MINUTES') // Sleep for 2 minutes
                // Your build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sleep(time: 1, unit: 'MINUTES') // Sleep for 2 minutes
                // Your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sleep(time: 1, unit: 'MINUTES') // Sleep for 2 minutes
                // Your deploy steps here
            }
        }
        stage('Build Docker Image') {
            steps {
                script {                    
                    // Build the docker image from the dockerfile present in the current workspace
                    echo "Building Docker Image ${imageName}:${imageTag}"
                    dockerImage = docker.build("${imageName}:${imageTag}")
                    echo "Docker Image ${imageName}:${imageTag} built successfully."
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    // Push the docker to DockerHub
                    echo "Pushing Docker Image on DockerHub"
                    docker.withRegistry('https://index.docker.io/v1/', 'Notepad') {
                        dockerImage.push()
                    }
                    echo "Docker Images pushed successfully."
                }
            }
        }
        stage('Cleanup Docker Image') {
            steps {
                script {
                    // Remove the docker image from the local environment after pushing
                    echo "Removing Docker Image"
                    bat "docker rmi ${imageName}:${imageTag}"
                    echo "Docker Image removed successfully."
                }
            }
        }
    }
}

