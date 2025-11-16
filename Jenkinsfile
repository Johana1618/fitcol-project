pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Docker Compose Up') {
            steps {
                bat '''
                    echo "Deteniendo contenedores anteriores..."
                    docker compose down --remove-orphans || true

                    echo "Levantando contenedores con build..."
                    docker compose up -d --build

                    echo "Contenedores levantados."
                '''
            }
        }
    }
}
