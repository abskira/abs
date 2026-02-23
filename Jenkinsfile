pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'mon-app:latest'
        CONTAINER_NAME = 'mon-app'
    }
    
    stages {
        stage('📦 Récupération du code') {
            steps {
                checkout scm
                echo '✅ Code récupéré depuis GitHub'
                sh 'ls -la'  // Pour vérifier les fichiers
            }
        }
        
        stage('🐳 Construction de l\'image Docker') {
            steps {
                // Construction de l'image Docker
                sh 'docker build -t mon-app:latest .'
                echo '✅ Image Docker construite avec succès'
            }
        }
        
        stage('🧹 Nettoyage ancien conteneur') {
            steps {
                sh '''
                    echo "Arrêt et suppression de l'ancien conteneur..."
                    docker stop mon-app || true
                    docker rm mon-app || true
                '''
                echo '✅ Ancien conteneur supprimé'
            }
        }
        
        stage('🚀 Lancement du nouveau conteneur') {
            steps {
                sh '''
                    echo "Lancement du nouveau conteneur..."
                    docker run -d \\
                      -p 5000:5000 \\
                      --name mon-app \\
                      mon-app:latest
                    
                    echo "Conteneur lancé avec succès"
                '''
            }
        }
        
        stage('⏳ Attente du démarrage') {
            steps {
                sh 'sleep 10'
                echo '✅ Attente de 10 secondes terminée'
            }
        }
        
        stage('✅ Test de l\'application') {
            steps {
                sh '''
                    echo "Test de l'application..."
                    curl -f http://10.0.2.15:5000 || exit 1
                    echo "✅ Application répond correctement"
                '''
            }
        }
        
        stage('📊 Vérification des métriques') {
            steps {
                sh '''
                    echo "Vérification des métriques Prometheus..."
                    curl -f http://10.0.2.15:5000/metrics | grep flask_http_request_total || exit 1
                    echo "✅ Métriques disponibles"
                '''
            }
        }
    }
    
    post {
        success {
            echo '''
            ╔══════════════════════════════════════════════════╗
            ║   🎉  PIPELINE RÉUSSI !  🎉                      ║
            ╠══════════════════════════════════════════════════╣
            ║  Application déployée sur http://10.0.2.15:5000  ║
            ║  Métriques sur http://10.0.2.15:5000/metrics     ║
            ║  Dashboard Grafana: http://10.0.2.15:3000        ║
            ╚══════════════════════════════════════════════════╝
            '''
        }
        failure {
            echo '❌ Le pipeline a échoué. Vérifie les logs ci-dessus.'
        }
        always {
            echo 'Fin du pipeline.'
        }
    }
}
