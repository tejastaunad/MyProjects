# This code was created to understand the basic CFT without any User data.

# VPC_cft.json can be added while creating the CFT in cloudformation in AWS to create a basic VPC which trigers an ec2 instance having IGW(internet gate way), one private and one public subnet, with one private and public route-table for respective subnets and a security group for allowing trafic into EC2 instance.

#Over all Components
1 vpc
1 IGW
2 subnets (priv and pub)
2 route table (priv and pub)
1 security-group
