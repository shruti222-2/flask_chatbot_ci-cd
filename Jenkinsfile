pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    export FLASK_APP=main.py
                    export FLASK_ENV=development
                    flask run --host=0.0.0.0 --port=5000
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

