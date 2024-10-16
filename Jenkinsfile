pipeline {
    agent any

    stages {
        script {
            def imageName = 'my-docker-image4'
            def imageTag = 'latest'
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Define Docker image name and tag
                    //def imageName = 'my-docker-image3'
                    //def imageTag = 'latest'
                    
                    // Build the Docker image from the Dockerfile in the current workspace
                    def dockerImage = docker.build("${imageName}:${imageTag}")
                    
                    echo "Docker image ${imageName}:${imageTag} built successfully."
                }
            }
        }
        stage('Clean up') {
            steps {
                script {
                    //def imageName = 'my-docker-image3'
                    //def imageTag = 'latest'
                    // Optionally, remove the image from the local environment after pushing
                    bat "docker rmi ${imageName}:${imageTag}"
                }
            }
        }
        stage('Build') {
            steps {
                echo 'Building...'
                // Your build steps here
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

