pipeline {
    agent any
    environment {
        // Define docker image name and tag
        def imageName = 'lalitbits2023/notepad'
        def imageTag = 'v2'
    }

    stages {
        stage('Check Docker Image Version') {
            steps {
                script {
                    def response = bat (
                        script: "curl -s -o NUL -w %%{http_code} https://hub.docker.com/v2/repositories/%imageName%/tags/%imageTag%",
                        returnStdout: true
                    ).trim()

                    if (response == "200") {
                        echo "Image version ${imageName} exists on Docker Hub."
                    } else if (response == "404") {
                        echo "Image version ${imageTag} does not exist on Docker Hub."
                    } else {
                        echo "Error checking image version. HTTP Status: ${response}"
                    }
                }
            }
        }
    }
}