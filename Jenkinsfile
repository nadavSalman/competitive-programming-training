pipeline {
  agent any
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
