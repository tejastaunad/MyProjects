

# Execute the VPC folder files before executing the Ec2_lamp folder files via terraform


# Creating 5 layer architecture

# Required tools:
Ubuntu VM ( As this is a learning session I would be using a virtual machine)
AWS CLI
Terraform

# Downloading and configuring AWSCLI
Download Aws cli from official website and extract the file
Step 1: Type-in "aws" command to confirm the proper instalation of aws cli
Step 2: Type-in "aws configure" command to configure aws cli to interact to aws server. (ie. you need to provide access key and security key)
[where to find you access key and security key if you have not downloaded it previously??!!
login to your aws account: IAM->Users->search for your username-> click on you user->Summary-> Security credentials -> download the csv file ]

# Downloading and installing Terraform
Step 1: wget https://releases.hashicorp.com/terraform/0.10.7/terraform_0.10.7_linux_amd64.zip?_ga=2.261908553.554745973.1508681491-2065576674.1508428556 (linux 64-bit)
step 2: Inorder to zip the above download you need to have a unzip so use:
sudo apt-get install vim
sudo vim .profile
paste this cmd "export PATH=$PATH:your terraform path" into .profile file.

# ALL DONE!!!

# Now that we have set up terraform and installed and set it running we can check it by typing-in "terraform" in the terminal and expect the following screen

# Creation of 5 layer architecture using terraform
# 5 layer architecture contain :
One VPC.
5 subnets : xelb(loadbalancer); WEB; APP; IELB(Memcache); DB.
One IGW(internet gateway).
One NAT(Network address translation ).
Two Route Table(public and private).
One NACL(Network access control list).

# User Data:
It is a bash script that is included while creating an EC2 instance, which helps in provisioning the software that is specified in user data at the time of creation of EC2 instance itself.

# Creating .sh file and referring the .sh file in main.tf.
Create a .sh file and type in the commands to be executed for instalation of LAMP stack and place it in your terraform folder and execute terraform commands, which will reffer this .sh file while launching the ec2 instance. (refer the .sh file in the attachment).
once the .sh file is created, parse the file name parameter as user_data = "${file("script.sh")}"  in the main.tf file.
