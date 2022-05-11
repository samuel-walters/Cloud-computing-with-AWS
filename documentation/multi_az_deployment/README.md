# Multi AZs Deployment

The AWS Cloud is made up of a number of Regions, which are physical locations around the world, such as Oregon, United States; North Virginia, United States; Ireland; and Tokyo.

Within each Region exists a number of separate physical data centers, known as Availability Zones. Each Availability Zone is a self-contained facility with its own power, connectivity, and networking capabilities. Most Regions are home to 2-3 different Availability Zones each, providing adequate redundancy when necessary within a given Region.

All Availability Zones within a single Region are connected to one another through private fiber-optic networking, allowing each Availability Zone to communicate with one another and transfer data quickly and efficiently as required.

Amazon Multi-AZ deployments provide enhanced availability for the product/app/database within a single AWS Region. With Multi-AZ, your data is synchronously replicated to a standby in a different Availability Zone (AZ)

## Server Instance

The server instance for your database is best thought of as the physical machine that controls the structure of your database and routes all your data that is contained within the storage layer.

## Storage Layer

The storage layer is an SSD-backed virtualized representation of all the actual data within your database. The keyword to focus on here is virtualized, which is Amazon’s fancy way of saying that the storage layer which represents the actual data in your system is not attached to any one physical location or machine, but instead is virtualized and propagated to numerous locations (six in total across three Availability Zones in most cases).

## Load Balancer

Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer as your incoming traffic changes over time. It can automatically scale to the vast majority of workloads.

A load balancer serves as the single point of contact for clients. The load balancer distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones. This increases the availability of your application. You add one or more listeners to your load balancer.

## Listener

A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

The below diagram shows two different listener groups determining how the load balancer distributes requests to the targets (for example, a target may be an EC2 instance):

![](https://i.imgur.com/XKPE6Ql.png)

# Launch template for ASG

An Amazon EC2 Auto Scaling group (ASG) contains a collection of EC2 instances that share similar characteristics and are treated as a logical grouping for the purposes of fleet management and dynamic scaling.

Before you can create an Auto Scaling group using a launch template, you must create a launch template with the parameters required to launch an EC2 instance. These parameters include the ID of the Amazon Machine Image (AMI) and an instance type.

A launch template provides full functionality for Amazon EC2 Auto Scaling and also newer features of Amazon EC2 such as the current generation of Amazon EBS Provisioned IOPS volumes (io2), EBS volume tagging, T2 Unlimited instances, Elastic Inference, and Dedicated Hosts.

Use the following procedure to create a new launch template. After you create your launch template, you can create the Auto Scaling group

# Launch configuration

Launch templates (LTs) are newer than launch configurations (LCs) and provide more options to work with. Thus, the AWS documentation recommends use of launch templates (LTs) over launch configuration (LCs):

    We recommend that you create Auto Scaling groups from launch templates to ensure that you're getting the latest features from Amazon EC2.

One of the practical key differences between LT and LC is the fact that LC is immutable. Once you define it, you can't edit it. Only a replacement is an option. However, a single LT can have multiple versions:

    defining a launch template instead of a launch configuration allows you to have multiple versions of a template. With versioning, you can create a subset of the full set of parameters and then reuse it to create other templates or template versions.

Also LTs provide more EC2 options for you to configure, for example, dedicated hosting can be set only using a LT. Similarly, ability to use T2 unlimited burst credit option is only available in a LT.

Thus if you can, its better to follow AWS recommendation and use LT.

# Autoscaling policy - options

AWS Auto Scaling is a service that automatically monitors and adjusts compute resources to maintain performance for applications hosted in the Amazon Web Services (AWS) public cloud.

AWS Auto Scaling lets you build scaling plans that automate how groups of different resources respond to changes in demand. You can optimize availability, costs, or a balance of both. AWS Auto Scaling automatically creates all of the scaling policies and sets targets for you based on your preference.

It’s easy to get started with AWS Auto Scaling using the AWS Management Console, Command Line Interface (CLI), or SDK. AWS Auto Scaling is available at no additional charge. You pay only for the AWS resources needed to run your applications and Amazon CloudWatch monitoring fees.

# What is a VPC?

Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that a company operates in their own data center, with the benefits of using the scalable infrastructure of AWS.

## Example

Isolated environment: need to have my own space. I'm the only one who has the key (VPC) to the main door. After that, people need NACL key to get into the bedrooms. Security groups: locks for the cupboard, chest etc.  

## Why use a VPC?

When you open up a service within a public cloud, it is effectively open to the world and can be at risk to attacks from the internet. In order to lock your instances down and secure them against attacks from the outside, you lock them within a VPC. The VPC restricts what sort of traffic, IP addresses and users can access your instances.

This prevents unwanted guests accessing your resources and secures you from things like DDOS attacks. Not all services require access to the internet, so those can be locked away safely within a private network. You can then expose only certain machines to the internet.

## What is an internet gateway?

If the network is private, instances can use an egress-only internet gateway to connect to the internet over IPv6, but the internet cannot establish connections to the private instances over IPv6.

But in short, an internet gateway connects the VPC to the internet and to other AWS services through the Amazon EC2 network edge.

## What is a routing table?

A route table contains a set of rules, called routes, that are used to determine where network traffic from your VPC is directed. Each route in a route table specifies the range of IP addresses where you want the traffic to go (the destination) and the gateway, network interface, or connection through which to send the traffic (the target).

For example: it's a traffic light - controls the traffic. Routes traffic depending on the business's needs. 

## What is a Subnet?

A subnet is a range of IP addresses in the VPC. You can attach AWS resources, such as EC2 instances and RDS DB instances, to subnets. 

When you create a subnet, you specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR block. Each subnet must reside entirely within one Availability Zone and cannot span zones. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single zone.

### Types of Subnet

Depending on how you configure your VPC, subnets can be considered public, private, or VPN-only:

* Public subnet: The subnet's IPv4 or IPv6 traffic is routed to an internet gateway or an egress-only internet gateway and can reach the public internet.

* Private subnet: The subnet’s IPv4 or IPv6 traffic is not routed to an internet gateway or egress-only internet gateway and cannot reach the public internet.

* VPN-only subnet: The subnet doesn't have a route to the internet gateway, but it has its traffic routed to a virtual private gateway for a Site-to-Site VPN connection.

## What is a CIDR block?

CIDR is an acronym that stands for Classless Inter-Domain Routing. In simpler terms, a CIDR block is an IP address range. A VPC can accommodate two CIDR blocks, one for IPv4 and another for IPv6.

Here is an example of a CIDR block with a 16-bit subnet: 10.10.0.0/16. This block would allow for the creation of up to 65,536 IP addresses. Each address would start with 10.10, but you can enter any value between 0 and 255 into the last two positions.

## What is a subnet mask?

The subnet mask determines how many IP addresses can be created from the CIDR block. Amazon requires that a CIDR block include a subnet mask ranging from 16 to 28. The two most commonly used subnet sizes are 16 bits and 24 bits.

A network administrator selects a subnet mask to divide a network into smaller sub-networks.

## What is IP-Networking?

An IP network refers to any group of devices, each with their own unique IP addresses, connected under the same network topology. Devices connected to a shared IP network can send and receive information.

A private IP network allows data to be shared between connected devices securely, by enforcing password protected connectivity that allows only those devices in your office or home to access the IP network.

## What is NACL?

A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. For example, security groups and NACLs both use sets of inbound and outbound rules to control traffic to and from resources in a VPC (but security groups and NACLs operate at separate layers in the VPC, have slightly different default rules, and don't handle response traffic the same way).

### Difference between security group and NACL?

Security group is the firewall of EC2 Instances.

Network ACL is the firewall of the VPC Subnets.

Network ACLs are applicable at the subnet level, so any instance in the subnet with an associated NACL will follow rules of NACL. That’s not the case with security groups, security groups has to be assigned explicitly to the instance.

This means any instances within the subnet group gets the rule applied. With Security group, you have to manually assign a security group to the instances.

### Rules: allow and deny

Security group supports allow rules only (by default all rules are denied). e.g. You cannot deny a certain IP address from establishing a connection.

Network ACL supports allow and deny rules. By deny rules, you could explicitly deny a certain IP address to establish a connection example: Block IP address 123.201.57.39 from establishing a connection to an EC2 Instance.

### Examples

NACL works as the stadium security that checks tickets. The Security Group works as the second layer check at different sections within the stadium, e.g. media booth, player section, VIP section.

Another example is the cinema: you can only go to the screen you bought the ticket for. You get in the cinema with the ticket (NACL), but from there you can only go to a specific screen (Security Group).









