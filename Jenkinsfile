pipeline {
  agent any
  stages {
    stage('install dependencies ') {
      steps {
        sh '''python3 -v
pip3 install -r requirements.txt'''
      }
    }

    stage('test') {
      steps {
        sh 'python3 -m unittest  -v'
      }
    }

  }
}