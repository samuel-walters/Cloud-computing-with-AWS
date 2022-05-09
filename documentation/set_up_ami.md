# Setting up an AMI

## Diagram

The diagram below illustrates AMIs being created from different EC2 instances. It is then illustrated that these AMIs can be used to create additional instances, with the new instances being based off the instance used to create the AMI.

![](https://i.imgur.com/EqpI9zV.png)

## Instructions

> 1. Go to your EC2 Instance, and click `Actions`. Click `Images and templates`, and choose `Create image`.

> 2. Name your image an appropriate name (for example eng110_sam_app_ami)

> 3. Add tag. For key, put `Name`, and for value put the same string you provided above.

> 4. Click `Create image`, and click on the AMI's ID.

> 5. Wait for the AMI status to change to `Available`.

> 6. Click your AMI, and go to `Launch instance from AMI`. 

> 7. Go through the same steps as when you created the EC2 instance, and make sure to select the security group you have already created.

> 8. Connect via ssh to your new instance launched from the AMI. But in the command, replace `root` with `ubuntu`. 