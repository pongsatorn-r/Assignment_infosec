pipeline {
    
    
    stages {
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
