# How to set up an EC2 server

## Diagram 

The diagram below illustrates the relationship between the local host, AWS, and the EC2 Instance. This diagram can be referred back to when you are setting up a new instance to give a better understanding of what is required.

![](https://i.imgur.com/1GzNI3R.png)

## Step by Step Instructions

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

> 17. Click `Review and Launch`.

> 18. Check your details are correct.

> 19. Click `Launch`.

> 20. Select `Choose an existing key pair`, and choose the appropriate one (the one in your .ssh folder).

> 21. Check the acknowledgement and press `Launch Instances`.

> 22. Click on the instance id and wait for the instance to get set up (refresh your browser if necessary).

> 23. To the left of the instance name, click the checkbox and then click `Connect` in the top right.

> 24. Navigate to `SSH client`.

> 25. Run GitBash as an administrator, and navigate to your .ssh folder.

> 26. Type in the command found under `SSH CLIENT` (underneath `Example`) into your GitBash terminal.  

> 27. If a prompt appears, type in `yes`.

> 28. Connect to the internet with `sudo apt update -y`. Wait for it to run.

> 29. Then run an upgrade with `sudo apt upgrade -y`. Wait for it to run.

> 30. Get nginx with `sudo apt install nginx -y`. Wait for it to run.

> 31. On the `Connect to Instance` page where you copied the `ssh` command, navigate to `EC2 Instance Connect`.

> 32. Type the Public IP address into your browser and you should see a `Welcome to nginx!` confirmation page.