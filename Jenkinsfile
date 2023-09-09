#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_SSH_KEY = credentials('github-ssh')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                // Checkout based on the configured credentials in the current Jenkins Job
                checkout scm
            }
        }
        stage("Build docker"){
            steps {
                sh "sudo usermod -a -G docker jenkins"
                sh "docker images"
            }
        }
    }
}