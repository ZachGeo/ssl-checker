#!/usr/bin/env groovy

pipeline {
    agent any
    environment {
        GIT_SSH_KEY = credentials('github-jenkins')
    }
    stages {
        stage("Clone Git Repository"){
            steps {
                git (
                    url: "https://github.com/ZachGeo/ssl-checker.git",
                    branch: "development",
                    credentialsId: "${env.GIT_SSH_KEY}"
                )
            }
        }
    }
}