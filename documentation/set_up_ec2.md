# How to set up an EC2 Instance

## Diagram 

The diagram below illustrates the relationship between the local host, AWS, and the two EC2 instances. This diagram can be referred back to when you are setting up a new instance to give a better understanding of what is required.

![](https://i.imgur.com/Ds3vD7s.png)

## Step by Step Instructions

### Creating and connecting to an EC2 Instance

> 1. In AWS, you must first select the region you are using. In this case, we are selecting Ireland as our location. 

> 2. In the search bar, search `EC2` and click on it.

> 3. In the `EC2 Dashboard`, click on the orange `Launch Instance` button and select `Launch Instance`.

> 4. On the left-hand side of the screen, tick the `Free tier only` box.

> 5. Now choose which AMI (Amazon Machine Image) you want to use. In this case, we are going to be using `Ubuntu Server 18.04 LTS`. 

> 6. Select an Instance Type. In this case, we will use `t2.micro`. 

> 7. Click `Next: Configure Instance Details`.

> 8. For `Subnet`, pick `DevOpsStudent Default 1a`.

> 9. Enable `Auto-assign Public IP`.

> 10. Click `Next: Add Storage`.

> 11. We will not change anything here. Click `Next: Add Tags`. 

> 12. Click `Add tag`. Under `key` enter `Name`, and under `value` enter eng110_yourname

> 13. Click `Configure Security Group`.

> 14. For Type `SSH`, under `Source`, change `Custom` to `My IP`.

> 15. Click `Add Rule`, and under type choose `HTTP`.

> 16. For `HTTP`, under `Source`, choose `Anywhere`.

> 17. Click `Add Rule`, and under `Type` choose `Custom TCP`.

> 18. Under `Port range`, put `3000.`.

> 19. Next to `Custom`, type `0.0.0.0/0`.

> 17. Click `Review and Launch`.

> 18. Check your details are correct.

> 19. Click `Launch`.

> 20. Select `Choose an existing key pair`, and choose the appropriate one (the one in your .ssh folder).

> 21. Check the acknowledgement and press `Launch Instances`.

> 22. Click on the instance id and wait for the instance to get set up (refresh your browser if necessary).

> 23. To the left of the instance name, click the checkbox and then click `Connect` in the top right.

> 24. Navigate to `SSH client`.

> 25. Run GitBash as an administrator, and navigate to your .ssh folder.

> 26. Type in the command found under `SSH client` (underneath `Example`) into your GitBash terminal.  

> 27. If a prompt appears, type in `yes`. You now have access to the EC2 Instance.

## Setting up the app

There are two methods for adding files to your EC2 Instance. Choose the one that is most convenient.

### WinSCP Method

> 1. [Download WinSCP](https://winscp.net/eng/download.php) and open it.

> 2. Under `File protocol` choose `SFTP`.

> 3. For the `Host name`, copy and paste in the line that appears under `Public IPv4 DNS` in AWS Instances for your EC2 instance. For example, it should look something like this:

        ec2-54-242-164-104.compute-1.amazonaws.com	

> 4. For `Username`, type in `ubuntu`. 

> 5. Click on `Advanced`. Under `SSH` on the left-hand side, click on `Authentication`. 

> 6. Select your private key file. If this is a .pem file, WinSCP will create a .ppk version in the same directory. The original .pem file will not be altered.

> 7. Click on `OK` and if you want to save the settings, click `Save`.

> 8. Click `Login`. When prompted, click `Yes`.

> 9. Drag and drop the files you want from your local host to the EC2 Instance using WinSCP. In this case, we will add the `App folder` as well as the `provision.sh` script (both of which are found in this GitHub repository). The below image shows the app folder in the local host that needs to be dragged to the EC2 Instance:

![](https://i.imgur.com/UpXKesN.png)

### scp Command Method

> 1. Running GitBash as an administrator, use this command to move files/folders: `scp -i location/file.pem -r folder ubuntu@ec2-ip.com:source/folder`. For example, the command may look like this:
        scp -i eng119.pem -r C:/Users/samwa/OneDrive/Desktop/vagrant/eng110_devops/app ubuntu@ec2-3-248-209-246.eu-west-1.compute.amazonaws.com:~/.
        Note: if you are moving a file, write the same command but without the -r. 

> 2. In this case, the `app` folder and the bash script `provision.sh` will be added to the EC2 instance.

## Setting up the Reverse Proxy

> 1. Once you have added the two files, double check they are there by typing in `ls` inside your EC2 instance. 

> 2. Run the command `chmod +x provision.sh` to make the script executable.

> 3. Run `provision.sh` by using the command `./provision.sh`.

> 4. If you are greeted with the error "-bash: ./provision.sh: /bin/bash^M: bad interpreter: No such file or directory", type in the command `sed -i -e 's/\r$//' provision.sh` and try again.

> 5. Wait for the script to run. 

> 6. Navigate to the app folder by typing `cd app`.

> 7. Install npm using the command `npm install`.

> 8. In the same directory, type in `npm start`.

> 9. On the `Connect to Instance` page where you copied the `ssh` command, navigate to `EC2 Instance Connect`.

> 10. Type the Public IPv4 address into your browser. Now everything should be working, and you should be able to access the Fibonacci page without entering a port number. 

## setting up mongod

> 1. Connect an EC2 Instance much like the one set up before. Name it `eng110_name_db`.


> 2. For the security group rules, for SSH, select `My IP`. Then add Type `Custom TCP` and for port put in `27017`. Under `Source`, fill in the ip for your app EC2 instance, and add /32 at the end. For example: `52.51.222.118/32`. Add a description that simply says `app ip`.

> 3. Remember to use the correct key.

> 4. Connect to the newly created EC2 instance in the exact same way.

> 5. Type in these commands, one by one:

        sudo apt-get update -y
        sudo apt-get upgrade -y
        sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927
        echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
        sudo apt-get update -y
        sudo apt-get upgrade -y
        sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
        sudo systemctl status mongod
        sudo systemctl start mongod
        sudo systemctl enable mongod
        sudo systemctl status mongod

> 6. Type in `cd /etc` and then type in `sudo nano mongod.conf`. Under `network interfaces`, for the ip put in `0.0.0.0`. Save and exit.

> 7. Type in these commands:

        sudo systemctl restart mongod
        sudo systemctl enable mongod
        sudo systemctl status mongod

> 8. In your app EC2 instance, type in `sudo echo "export DB_HOST=mongodb://your_db_ip:27017/posts" >> ~/.bashrc`. 

> 9. Run the command `source ~/.bashrc`.

> 9. Check the environment variable with the command `printenv DB_HOST`.

> 10. Still in the app EC2 instance, run the command `node seeds/seed.js`. 

> 11. Type in `npm start`. 

