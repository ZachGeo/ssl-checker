#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_TOKEN = credentials('ssl-checker-jenkins-github-token')
        DOCKER_REGISTRY_USERNAME = credentials('docker-registry-username')
        DOCKER_REGISTRY_TOKEN = credentials('ssl-checker-jenkins-dockerhub-token')
    }
    parameters {
        string defaultValue: '', description: '', name: 'dockerhub-id'
        string defaultValue: 'latest', description: '', name: 'docker-image-version'
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
                sh "docker build -t ssl-checker ."
            }
        }
        stage("Push Docker Image"){
            steps {
                sh '''
                    echo "${DOCKER_REGISTRY_TOKEN} | docker login -u ${DOCKER_REGISTRY_USERNAME} --password-stdin"
                    docker images
                '''
                //sh "docker tag ssl-checker ${params.dockerhub-id}/ssl-checker:${params.docker-image-version}"
            }
        }
    }
}