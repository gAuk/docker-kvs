pipeline {
  agent any
  environment {
    DOCKERHUB_USER = "tyamana"
    BUILD_HOST = "ubuntu@3.112.194.165"
    BUILD_PORT = "20022"
    PROD_HOST = "ubuntu@3.112.194.165"
    PROD_PORT = "20023"
    BUILD_TIMESTAMP = sh(script: "date +%Y%m%d-%H%M%S", returnStdout: true).trim()
  }
  stages {
    stage('Pre Check') {
      steps {
      }
    }
    stage('Build') {
      steps {
        sh "cat docker-compose.build.yml"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker-compose -f docker-compose.build.yml down'"
	sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker volume prune -f'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker-compose -f docker-compose.build.yml build'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker-compose -f docker-compose.build.yml up -d'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker-compose -f docker-compose.build.yml ps'"
      }
    }
    stage('Test') {
      steps {
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker container exec dockerkvs_apptest pytest -v test_app.py'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker container exec 'dockerkvs_webtest pytest -v test_static.py'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker container exec 'dockerkvs_webtest pytest -v test_selenium.py'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker-compose -f docker-compose.build.yml down'"
      }
    }
    stage('Register') {
      steps {
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker tag dockerkvs_web ${DOCKERHUB_USER}/dockerkvs_web:${BUILD_TIMESTAMP}'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker tag dockerkvs_app ${DOCKERHUB_USER}/dockerkvs_app:${BUILD_TIMESTAMP}'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker push ${DOCKERHUB_USER}/dockerkvs_web:${BUILD_TIMESTAMP}'"
        sh "podman exec jenkins_c ssh -p ${BUILD_PORT} ${BUILD_HOST} 'docker push ${DOCKERHUB_USER}/dockerkvs_app:${BUILD_TIMESTAMP}'"
      }
    }
    stage('Deploy') {
      steps {
        sh "cat docker-compose.prod.yml"
        sh "echo 'DOCKERHUB_USER=${DOCKERHUB_USER}' > .env"
        sh "echo 'BUILD_TIMESTAMP=${BUILD_TIMESTAMP}' >> .env"
        sh "cat .env"
        sh "podman exec jenkins_c ssh -p ${PROD_PORT} ${PROD_HOST} 'docker-compose -f docker-compose.prod.yml up -d'"
        sh "podman exec jenkins_c ssh -p ${PROD_PORT} ${PROD_HOST} 'docker-compose -f docker-compose.prod.yml ps'"
      }
    }
  }
}
