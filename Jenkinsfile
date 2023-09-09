#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_SSH_KEY = credentials('github-jenkins')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                checkout scm
            }
        }
        stage("List Current Diretory"){
            steps {
                sh "ls"
                sh "pwd"
            }
        }
    }
}