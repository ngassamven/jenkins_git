pipeline {
    agent any
    stages {
        stage('Extraction') {
            steps {
                script {
                    // Clone du repo si nécessaire et exécution du script extract.py
                    sh 'python extract.py'
                }
            }
        }
        
        stage('Transformation') {
            steps {
                script {
                    // Exécution du script de transformation
                    sh 'python transform.py'
                }
            }
        }
        
        stage('Chargement') {
            steps {
                script {
                    // Exécution du script de chargement
                    sh 'python load.py'
                }
            }
        }
    }
}
