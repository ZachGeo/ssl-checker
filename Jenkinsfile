#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_TOKEN = credentials('ssl-checker-jenkins-github-token')
    }
    parameters {
        string (defaultValue: 'latest', description: 'The version of the docker image', name: 'DOCKER_IMAGE_VERSION')
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
        stage("Login to Dockerhub") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: 'dockerhub-token', usernameVariable: 'dockerhub-username')]) {
                    sh '''
                        echo "${dockerhub-token} | docker login -u ${dockerhub-username} --password-stdin
                    '''
                }
            }
        }
        stage("Push Image to Registry"){
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', passwordVariable: '', usernameVariable: 'dockerhub-username')]) {
                    sh "docker tag ssl-checker ${dockerhub-username}/ssl-checker:${params.DOCKER_IMAGE_VERSION}"
                    sh "docker push ${dockerhub-username}/ssl-checker:${params.DOCKER_IMAGE_VERSION}"
                }
            }
        }
    }
    post{
        always{
            sh 'docker logout'
        }
    }
}