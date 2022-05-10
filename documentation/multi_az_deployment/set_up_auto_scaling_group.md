# Setting Up an Auto Scaling Group

## Diagram

The below diagram illustrates the relationship between the user, the load balancer, the auto scaling group, and the EC2 instances (i.e. the targets):

![](https://i.imgur.com/92xqt7j.png)

## Launch template

> 1. For `Launch template name`, remember naming conventions - dashes, lowercase. For example, you may choose:

    eng110-sam-asg-lt

> 2. For the `Template version description`, put in the same name you used above.
> 3. Tick the box next to the `Provide guidance to help me set up a template that I can use with EC2 Auto Scaling`.
> 4. Expand `Template tags`. Click `Add tag`, and for `Key`, put in `Name`, and for `Value`, put in the name you used above (for example eng110-sam-asg-lt).
> 5. For the AMI section, click `Browse more AMIs`. Click the free-tier checkbox, and scroll down to the bottom and select the Ubuntu server (version 18.04).
> 6. For `Instance type`, choose t2 micro.
> 7. Key - Select the right key you are using.
> 8. For the security group - Select the right one (in this case the one created for the app).
> 9. Click `Advanced Details` - scroll down to the bottom and copy and paste in the provision.sh script under `User data`.
> 10. Check your details in `Summary`, and click `Create launch template`. 

## ASG

> 1. Remember naming conventions: dashes, lower-case. For example: `eng110-sam-asg-app`.
> 2. For the Networks, use 1a, 1b, 1c.
> 3. Attach new load balance: ALB(HTTP/S), internet facing, create a target group/select.
> 4. Fill in the `Group size and Scaling Policies` as shown below:

    For desired capacity, put 2 
    For minimum capacity, put 2
    For maximum capacity, put 3

> 5. Choose the appropriate Launch Template.
> 6. Choose the version you want to use for the Launch Template. For example, Default (1).
> 8. Select the appropriate security group (for example the one you created for the app).
> 9. For `Health checks`, put `EC2` at 300 seconds.
> 10. Advanced - Termination policies: `Default`.
> 11. Add appropriate Tags with the correct naming conventions (for example Name: eng110-sam-asg-resources).

## Setting up an Alarm for 50% CPU Utilization

> 1. Navigate to your newly set up ASG and click its box.
> 2. Select `Montioring`, then `CloudWatch`, then `Alarms`. 
> 3. Select `create a new alarm`.
> 4. Select `metric`.
> 5. Select `EC2` then select `Auto Scaling Group`.
> 6. Choose the `CPUUtilization` option.
> 7. Select `period`.
> 8. Set the value to 50 (50% CPU Usage).
> 9. Create a SNS topic.
> 10. Enter an appropriate name (for example eng110-sam-alarm-50percent-cpu).
> 11. Enter the email you want it to notify.
> 12. Add name and description with appropriate naming conventions (lowercase, dashes).
> 13. Create dynamic scaling policies.
> 14. From the dropdown menu select `Step scaling`.
> 15. Remember naming conventions when providing a name for the policy.
> 16. From the dropdown menu, select `CloudWatch alarm`.
> 17. Select an action from the dropdown menu.
> 18. Define the value of capacity units
> 19. Define time the instance needs to spin up