pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'echo "Linting (simulated)"'
            }
        }
        stage('Build') {
            steps {
                sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
        '''
            }
        }

        stage('Unit Test') {
    steps {
        sh '''
            . venv/bin/activate
            python -m unittest discover -s . -p "test_*.py"
        '''
    }
}

        stage('Docker Build') {
            steps {
                sh 'docker build -t todo-app .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 todo-app'
            }
        }
        stage('Selenium Test') {
            steps {
                sh 'docker build -t selenium-tests selenium'
                sh 'docker run --net=host selenium-tests'
            }
        }
    }
}
