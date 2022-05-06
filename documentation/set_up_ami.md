# Setting up an AMI

![](https://i.imgur.com/EqpI9zV.png)

> 1. Go to your EC2 Instance, and click `Actions`. Clicck `Images and templates`, and choose `Create image`.

> 2. Name your image an appropriate name (for example eng110_sam_app_from_ami)

> 3. Add tag. For key, put `Name`, and for value put the same string you provided above.

> 4. Click `Create image`, and click on the AMI's ID.

> 5. Wait for the AMI status to change to `Available`.

> 6. Click your AMI, and go to `Launch instance from AMI`. 

> 7. Go through the same steps as when you created the EC2 instance, and make sure to select the security group you have already created.

> 8. Connect via ssh to your new instance launched from the AMI. But in the command, replace `root` with `ubuntu`. 