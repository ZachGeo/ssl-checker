#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_SSH_KEY = credentials('github-jenkins')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                sh "git config --global --unset credential.helper"
                // Checkout based on the configured credentials in the current Jenkins Job
                checkout scm
            }
        }
        stage("List Current Diretory"){
            steps {
                sh "sudo docker images"
            }
        }
    }
}