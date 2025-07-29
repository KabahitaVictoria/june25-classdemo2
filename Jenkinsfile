pipeline {
    // Define the pipeline agent; can either be container or vm
    agent any 

    environment {
        // Define any environment variables here
        VENV = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/KabahitaVictoria/june25-classdemo2.git' // Specify your Git repository URL here
            }
        } 
        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python3 -m venv $VENV
                . $VENV/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                // Activate the virtual environment and run tests
                sh '''
                . $VENV/bin/activate
                pytest 
                '''
            }
        }
    }
}