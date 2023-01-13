pipeline {
  agent {
    label 'docker-slave'
  }
  stages {
    stage('Test') {
      steps {
        sh '''
          node --version
          ls -al
          pwd
          
          '''
        
      }
    }
  }
}
