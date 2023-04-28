pipeline {
    
    agent {
        label 'docker'
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    BRANCH_NAME = master
                    git url: "https://github.com/pongsatorn-r/Assignment_infosec.git", branch: BRANCH_NAME
                }
            }
        }
        stage('Build Docker image') {
            steps {
                sh 'docker build -t myimage .'
            }
        }
        stage('Run Docker container') {
            steps {
                sh 'docker run -d myimage'
            }
        }
    }
}
