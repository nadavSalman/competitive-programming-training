pipeline {
  agent {
    docker {
      image 'python:3.11-rc-alpine'
    }
  }
  stages {
    stage('install dependencies ') {
      steps {
        sh" echo nadav salman"
        sh '''python -v
              pip install -r requirements.txt'''
        sh 'pip -v'
      }
    }

    stage('test') {
      steps {
        sh 'python -m unittest  -v'
      }
    }

    stage('last') {
      steps {
        sh 'date'
      }
    }

  }
}
