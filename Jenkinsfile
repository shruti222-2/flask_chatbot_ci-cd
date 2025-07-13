pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate.bat
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Flask App') {
            steps {
                bat """
                    call %VENV_DIR%\\Scripts\\activate.bat
                    set FLASK_APP=main.py
                    set FLASK_ENV=development
                    flask run --host=127.0.0.1 --port=5000
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
    }
}

