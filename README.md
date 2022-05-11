# Cloud Computing

# What is Cloud Computing (and what is AWS)?

Cloud computing is the practice of using a network of remote servers hosted on the internet to store, manage and process data. It is an alternative to setting up and maintaining a server on local hardware. There are three big public cloud vendors: Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.

## Types of Cloud Computing

### Public Cloud

Public clouds are owned and operated by third-party cloud service providers, which deliver their computing resources like servers and storage over the Internet. AWS (Amazon Web Services) is an example of a public cloud. With a public cloud, all hardware, software and other supporting infrastructure is owned and managed by the cloud provider. You access these services and manage your account using a web browser. 

### Private Cloud (On Premises)

A private cloud refers to cloud computing resources used exclusively by a single business or organisation. A private cloud can be physically located on the company’s on-site datacenter. Some companies also pay third-party service providers to host their private cloud.

### Hybrid Cloud

Hybrid clouds combine public and private clouds. By allowing data and applications to move between private and public clouds, a hybrid cloud gives the business greater flexibility, more deployment options, and helps optimise the business's existing infrastructure, security and compliance.

For example, banks can opt for a hybrid cloud computing architecture. Banks could store data such as a user's personal bank account details on their own premises where they have a great deal of control over the security of sensitive information. But areas of the business that are not sensitive, such as the registration page of the bank's website, could be put onto a public cloud. That way, even if someone manages to gain access to the data, they do not get their hands on any confidential information. By therefore adopting a hybrid approach, a bank can manage its own security but still reap the rewards of cloud computing such as cost effectiveness and scalability.  

## Benefits of Cloud Computing

* Security 

Many cloud providers offer a broad set of policies, technologies and controls that strengthen a company's security posture overall, helping them protect their data, apps and infrastructure from potential threats.

* Cost 

Cloud computing eliminates the capital expense of buying hardware and software and setting up and running on-site datacenters—the racks of servers, the round-the-clock electricity for power and cooling, the IT experts for managing the infrastructure. It adds up fast.

Cloud computing also offers its users a `pay as you go` approach to pricing. For example, with AWS you pay only for the individual services you need, for as long as you use them, and without requiring long-term contracts or complex licensing. AWS pricing is similar to how you pay for utilities like water and electricity. You only pay for the services you consume, and once you stop using them, there are no additional costs or termination fees.

* Flexibility through Scalability 

Predicting future traffic is difficult, especially when unforeseen events can arise such as a pandemic. As people were locked inside for months on end, internet usage increased and the traffic websites received increased significantly. But cloud computing is flexible, and it can meet the challenges posed by unpredictable events because it offers its users the ability to increase or decrease IT resources as needed to meet changing demand. 

* Reliability 

Cloud computing makes data backup, disaster recovery and business continuity easier and less expensive because data can be mirrored at multiple redundant sites on the cloud provider’s network. In AWS, for example, there exist different regions which are physical locations around the world where Amazon clusters data centers. Each group of logical data centers is called an Availability Zone (AZ), and each AWS Region consists of multiple, isolated, and physically separate AZs within a geographic area. That way, even if something disastrous happens to one AZ, such as a natural disaster, the product will not go down as AWS will automatically redirect the traffic for your instances to another AZ in the region.

Apps can even be deployed in mulitple regions. That way, if the Ireland region for AWS goes down, the company can still serve its users by relying upon another region - such as the London region for example. However, as a company uses more regions, the costs will become greater so the business will have to carry out a cost-benefit analysis. 

* Accessibility

Cloud computing ensures details such as a low latency can easily be achieved. For example, if the end user is based in Australia, the region you use could also be in Australia to improve their experience with the product. (SIDE NOTE: CDN - Contact delivery network. Helps latency/response time if the servers from the users are very far away.)

# Links

- [AMI information](documentation/AMI.md)
- [S3 information](documentation/s3.md)
- [Set up ec2](documentation/set_up_ec2.md)
- [Set up ami](documentation/set_up_ami.md)
- [Set up S3](documentation/set_up_s3.md)  
- [Multi Azs information](documentation/multi_az_deployment/README.md)  
- [Set up auto scaling](documentation/multi_az_deployment/set_up_auto_scaling_group.md)
- [VPC information](documentation/multi_az_deployment/vpc.md)
- [Set up VPC](documentation/multi_az_deployment/set_up_vpc.md)