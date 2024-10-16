pipeline {
    agent any
    environment {
        def imageName = 'my-docker-image4'
        def imageTag = 'latest'
    }

    stages {
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
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'Notepad') {
                        dockerImage.push()
                    }
                }
            }
        }
        stage('Clean up') {
            steps {
                script {
                    //def imageName = 'my-docker-image3'
                    //def imageTag = 'latest'
                    // Optionally, remove the image from the local environment after pushing
                    //sleep(time: 1, unit: 'MINUTES') // Sleep for 2 minutes
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

