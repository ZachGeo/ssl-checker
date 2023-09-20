#!/usr/bin/env groovy

def slack_channel = 'ssl-checker-build'

pipeline {
    agent any
    environment {
        GIT_TOKEN = credentials('ssl-checker-jenkins-github-token')
        DOCKER_CREDS = credentials('dockerhub-credentials')
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
        stage("Login to Dockerhub"){
            steps {              
                sh 'echo ${DOCKER_CREDS_PSW} | docker login -u ${DOCKER_CREDS_USR} --password-stdin'
            }
        }
        stage("Push Image to Registry"){
            steps {
                sh 'docker tag ssl-checker ${DOCKER_CREDS_USR}/ssl-checker:${DOCKER_IMAGE_VERSION}'
                sh 'docker push ${DOCKER_CREDS_USR}/ssl-checker:${DOCKER_IMAGE_VERSION}'
            }
        }
    }
    post{
        always{
            sh 'docker logout'
        }
        success{
            sh 'docker rmi ${DOCKER_CREDS_USR}/ssl-checker:${DOCKER_IMAGE_VERSION}'
            slackSend channel: 'ssl-checker-build', color: '#008000', message: 'SUCCESS: JOB ${env.JOB_NAME}, BUILD ${env.BUILD_NUMBER}, IMAGE ${DOCKER_CREDS_USR}/ssl-checker:${DOCKER_IMAGE_VERSION}'

        }
        // failure{
        //     slackSend(
        //         channel: '${slack_channel}',
        //         color: '#FF0000',
        //         message: 'FAILURE: JOB ${env.JOB_NAME}, BUILD ${env.BUILD_NUMBER}'
        //     )
        // }
    }
}