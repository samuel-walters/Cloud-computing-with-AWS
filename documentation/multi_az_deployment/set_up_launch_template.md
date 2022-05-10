# Set Up a Launch Template

> 1. For `Launch template name`, remember naming conventions - dashes, lowercase. For example, you may choose:

    eng110-sam-asg-lt

> 2. For the `Template version description`, put in the same name you used above.

> 3. Tick the box next to the `Provide guidance to help me set up a template that I can use with EC2 Auto Scaling`.

> 4. Expand `Template tags`. Click `Add tag`, and for `Key`, put in `Name`, and for `Value`, put in the name you used above (for example eng110-sam-asg-lt).

> 5. For the AMI section, click `Browse more AMIs`. Click the free-tier checkbox, and scroll down to the bottom and select the Ubuntu server.

> 6. For `Instance type`, choose t2 micro.

> 7. Key - Select the right key you are using.

> 8. For the security group - Select the right one (in this case the one created for the app).

> 9. Click `Advanced Details` - scroll down to the bottom and copy and paste in the provision.sh script under `User data`.

> 10. Check your details in `Summary`, and click `Create launch template`. 


