#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_TOKEN = credentials('ssl-checker-jenkins-github-token')
        DOCKER_REGISTRY_USERNAME = credentials('docker-registry-username')
        DOCKER_REGISTRY_TOKEN = credentials('ssl-checker-jenkins-dockerhub-token')
    }
    parameters {
        string (defaultValue: '', description: '', name: 'DOCKERHUB_ID')
        string (defaultValue: 'latest', description: '', name: 'DOCKER_IMAGE_VERSION')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                // Checkout based on the configured credentials in the current Jenkins Job
                checkout scm
            }
        }
        stage("Build Docker Image"){
            steps {
                sh "docker build -t ${DOCKER_REGISTRY_USERNAME}/ssl-checker ."
            }
        }
        stage("Login to Docker Registry"){
            steps {
                sh "echo ${DOCKER_REGISTRY_TOKEN} | docker login -u ${DOCKER_REGISTRY_USERNAME} --password-stdin"
            }
        }
        stage("Tag Image"){
            steps {
                sh 'docker tag ssl-checker $params.DOCKERHUB_ID/ssl-checker:$params.DOCKER_IMAGE_VERSION'
            }
        }
            //sh "docker tag ssl-checker ${params.DOCKERHUB_ID}/ssl-checker:${params.DOCKER_IMAGE_VERSION}"
            //sh "docker images"
            //sh "docker pull ${params.DOCKERHUB_ID}/covid_api:${params.DOCKER_IMAGE_VERSION}"
            //sh "docker push ${params.DOCKERHUB_ID}/ssl-checker:${params.DOCKER_IMAGE_VERSION}"
    }
}