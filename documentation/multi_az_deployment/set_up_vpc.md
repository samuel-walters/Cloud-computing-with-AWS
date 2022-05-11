# Diagram

![](https://i.imgur.com/mC4cXt1.png)

# Create VPC

> 1. Search VPC. 

> 2. Make sure you are in the right region before continuing (Ireland).

> 3. Click `Launch VPC Wizard`.

> 4. Click `VPC only`. 

> 5. Correct naming conventions for the Name. For example, eng110-sam-vpc

> 5. For `iPv4 CIDR`, put `10.0.0.0/16`.

> 6. `Tenancy` should be `default`.

> 6. Click `Create VPC`. 

## Create Internet gateway

> 1. Go to `Internet Gateways` and check you are in the correct region as well.

> 2. Click `Create internet gateway`. 

> 3. For the name tag, choose the correct naming conventions. For example, eng110-sam-ig.

> 4. Click `Create internet gateway`.

> 5. Select your internet gateway and click `Attach to VPC`.

> 6. Choose the VPC you created and select `Attach internet gateway`.

## Create Subnet (public)

> 1. Click `Create subnet`. 

> 2. Choose the correct VPC ID (the one you set up).

> 3. Choose a Subnet name with appropriate naming conventions (for example eng110-sam-sn).

> 4. For the IPv4 CIDR block, put in `10.0.10.0/24`.


## Create Route Table (RT)

> 1. Go to `Route Tables` on the left-hand side.

> 2. Click `Create Table`. 

> 3. Naming conventions - eng110-sam-rt.

> 4. Choose the correct `VPC`.

> 5. Click Add new tag, filling in the key with `Name` and the value with the RT name.

> 6. Click `Create route table`. 

> 7. Click on the route table you generated and click `Routes`.

> 7. Click `Edit Routes`.

> 8. Select 'Internet gateway' from drop down list.

> 9. Define the value with `0.0.0.0/0`. This is for public use.

> 8. For `Target`, select your public subnet.

> 9. Destination should be 0.0.0.0/0.

> 11. Click `Save changes`. 

# Testing VPC

> 1. Launch an EC2 instance from an AMI.

> 2. In networking select your VPC.

> 3. Connect to the launched EC2 instance and check if it works for you and for others.