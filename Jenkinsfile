pipeline {
  agent {
    label 'docker-slave'
  }
  stages {
    stage('Test') {
      steps {
        sh '''
          ls -al
          pwd
          cat /etc/os-release
lsb_release -a
hostnamectl
          
          '''
        
      }
    }
  }
}
