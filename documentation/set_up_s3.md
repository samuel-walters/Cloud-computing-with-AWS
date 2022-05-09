# Setting up S3

## Diagram

The diagram below illustrates the relationship between the local host, EC2, and S3.

![](https://i.imgur.com/iTxm1a2.png)

## Instructions

> 1. Launch an EC2 instance and connect to it via SSH.
> 2. Run the commands `sudo apt update -y` and `sudo apt upgrade -y`.
> 3. Run the command `python --version`. If it is below version 3, run the commands `sudo apt install python` and `sudo apt install python-pip -y`.
> 4. To change to the right version, type in `alias python=python3`. 
> 5. Install pip for python with the command `sudo apt install python3-pip`.
> 6. Install awscli with the command `sudo python3 -m pip install awscli`.
> 7. Run the command `aws configure` and enter the keys. The format is `json`, and the region is `eu-west-1`.
> 8. Create a bucket with the command `aws s3 mb s3://bucket-name`. Be mindful of the naming conventions here (hyphens, lowercase). For example, the command might look like this:

    aws s3 mb s3://eng110-sam

## Moving files from EC2 to S3

> 1. Create a file with `nano` or `touch` in the EC2 instance.
> 2. Move the file with the command `aws s3 cp filename s3://bucket-name/`. For example:

    aws s3 cp test.txt s3://eng110-sam/

## Downloading files from S3 to EC2

> 1. Use the command `aws s3 cp s3://bucket-name/file local_file`. For example:

    aws s3 cp s3://eng110-sam/test.txt test.txt