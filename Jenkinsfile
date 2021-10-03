pipeline {
  agent any
  stages {
    stage('install dependencies ') {
      steps {
        sh '''python -v
              pip install -r requirements.txt'''
      }
    }

    stage('test') {
      steps {
        sh 'python -m unittest  -v'
      }
    }

  }
}
