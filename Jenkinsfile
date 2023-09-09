#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_SSH_KEY = credentials('github-jenkins')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                // Checkout based on the configured credentials in the current Jenkins Job
                checkout scm
            }
        }
        stage('Initialize Docker'){
            def dockerHome = tool 'myDocker'
            env.PATH = "${dockerHome}/bin:${env.PATH}"
        }
        stage("List Current Diretory"){
            steps {
                //sh "docker build -t ssl-checker ."
                sh "docker images"
            }
        }
    }
}