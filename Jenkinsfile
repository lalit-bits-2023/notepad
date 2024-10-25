pipeline {
    agent any
    environment {
        // Define docker image name and tag
        def imageName = 'lalitbits2023/notepad'
        def imageTag = '2'
    }

    stages {
        stage('Check Docker Image Version') {
            steps {
                script {
                    def imageCounter = 1
                    while (true) {
                        def response = bat (
                            script: "curl -s -o NUL -w %%{http_code} https://hub.docker.com/v2/repositories/%imageName%/tags/v%imageTag%",
                            returnStdout: true
                        ).trim()

                        response = response.split()[-1]

                        if (response == "200") {
                            echo "Image version ${imageName}:v${imageCounter} exists on Docker Hub."
                            imageCounter += 1
                        } else if (response == "404") {
                            echo "Image version ${imageName}:v${imageCounter} does not exist on Docker Hub."
                            echo "Next Image version should be ${imageName}:v${imageCounter}."
                            break
                        } else {
                            echo "Error checking image version. HTTP Status: ${response}"
                        }
                    }
                }
            }
        }
    }
}