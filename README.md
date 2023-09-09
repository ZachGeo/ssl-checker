# SSL-CHECKER


## Description
This project is focused on checking the expiration of the certificate for multiple domain names. If certificate is expiring in a short manner then we will get a notification in our Slack workspace.

## Requirements
A Slack workspace is mandatory. Also, you should create an OAuth Token for Your Workspace with the relative privilages.

## Usage
cd /path/to/ssl-checker

sudo docker build -t ssl-checker .

sudo docker run -e "SLACK_TOKEN=<your-workspace-OAuth-token>" -e "SLACK_CHANNEL=<your-slack-channel>" -d -ti --name ssl-checker ssl-checker

## Update Domain Names List
To add your domain names which you want to check the expiration time of their certificate, you need to update the `input.csv` file. The file shoud have the information as shown below.

> hostname,port,servername
