pipeline {
    agent any

    stages {
        stage('Extraction') {
            steps {
                script {
                    echo '📥 Début de l’extraction des données...'
                    bat 'python extract.py'  // Utilisation de bat au lieu de sh sous Windows
                }
            }
        }

        stage('Transformation') {
            steps {
                script {
                    echo '🔄 Transformation des données...'
                    bat 'python transform.py'
                }
            }
        }

        stage('Chargement') {
            steps {
                script {
                    echo '📤 Chargement des données dans PostgreSQL...'
                    bat 'python load.py'
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline terminé avec succès !'
        }
        failure {
            echo '❌ Erreur dans le pipeline. Vérifiez les logs.'
        }
    }
}
