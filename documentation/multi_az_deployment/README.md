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

### The Two Types of Load Balancer

Classic Load Balancer: this load balancer is likely to be the best choice if your routing and load-balancing needs can all be handled based on IP addresses and TCP ports.

Application Load Balancer: this load balancer can address more complex load-balancing needs by managing traffic at the application level. This is especially advantageous for next-generation infrastructure, such as that based on containers, or if you are building complex web applications in which requests for certain components should be directed to one cluster, while others go to a different one.

## Listener

A listener is a process that checks for connection requests, using the protocol and port that you configure. The rules that you define for a listener determine how the load balancer routes requests to its registered targets.

The below diagram shows two different listener groups determining how the load balancer distributes requests to the targets (for example, a target may be an EC2 instance):

![](https://i.imgur.com/XKPE6Ql.png)

# Launch template for ASG

An Amazon EC2 Auto Scaling group (ASG) contains a collection of EC2 instances that share similar characteristics and are treated as a logical grouping for the purposes of fleet management and dynamic scaling.

Before you can create an Auto Scaling group using a launch template, you must create a launch template with the parameters required to launch an EC2 instance. These parameters include the ID of the Amazon Machine Image (AMI) and an instance type.

A launch template provides full functionality for Amazon EC2 Auto Scaling and also newer features of Amazon EC2 such as the current generation of Amazon EBS Provisioned IOPS volumes (io2), EBS volume tagging, T2 Unlimited instances, Elastic Inference, and Dedicated Hosts.

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

## Four Golden Signals of Monitoring

The four golden signals of monitoring are latency, traffic, errors, and saturation. If you can only measure four metrics of your user-facing system, focus on these four. The time it takes to service a request. It's important to distinguish between the latency of successful requests and the latency of failed requests.

### Latency

The time it takes to service a request. 

### Traffic

A measure of how much demand is being placed on your system, measured in a high-level system-specific metric. For a web service, this measurement is usually HTTP requests per second.

### Errors

The rate of requests that fail, either explicitly (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with the wrong content), or by policy (for example, "If you committed to one-second response times, any request over one second is an error").

### Saturation

How "full" your service is. A measure of your system fraction, emphasizing the resources that are most constrained (e.g., in a memory-constrained system, show memory; in an I/O-constrained system, show I/O). Note that many systems degrade in performance before they achieve 100% utilisation, so having a utilisation target is essential.




