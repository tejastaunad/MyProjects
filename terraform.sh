#!/bin/bash
# this is to install terraform , configure its path and run it
wget https://releases.hashicorp.com/terraform/0.8.8/terraform_0.8.8_linux_amd64.zip
sudo apt-get install unzip
sudo mkdir terraform
sudo unzip terraform_0.8.8_linux_amd64.zip -d terraform
touch pathfile
echo 'export PATH=$PATH:your terraform path' >> pathfile
cat pathfile >> .profile
terraform --version
