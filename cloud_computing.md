# Cloud Computing

# What is Cloud Computing (and what is AWS)?

Cloud computing is the practice of using a network of remote servers hosted on the internet to store, manage and process data. It is an alternative to setting up and maintaining a server on local hardware. There are three big public cloud vendors: Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.

## Types of Cloud Computing

### Public Cloud

Public clouds are owned and operated by a third-party cloud service providers, which deliver their computing resources like servers and storage over the Internet. AWS (Amazon Web Services) is an example of a public cloud. With a public cloud, all hardware, software and other supporting infrastructure is owned and managed by the cloud provider. You access these services and manage your account using a web browser. 

### Private Cloud (on premises)

A private cloud refers to cloud computing resources used exclusively by a single business or organisation. A private cloud can be physically located on the company’s on-site datacenter. Some companies also pay third-party service providers to host their private cloud. A private cloud is one in which the services and infrastructure are maintained on a private network. 

### Hybrid cloud

Hybrid clouds combine public and private clouds, bound together by technology that allows data and applications to be shared between them. By allowing data and applications to move between private and public clouds, a hybrid cloud gives your business greater flexibility, more deployment options and helps optimise your existing infrastructure, security and compliance.

For example, banks can opt for a hybrid cloud computing architecture. Banks could store data such as a user's personal bank account details on their own premises where they have a great deal of control over the security of sensitive information. But areas of the business that are not sensitive, such as the registration page of the bank's website, could be put onto the cloud. That way, even if someone manages to gain access to the data, they do not gain any confidential information. By therefore adopting for a hybrid architecture, a bank can manage its own security whilst reaping the rewards of cloud computing such as cost effectiveness and scalability.  

## Benefits of Cloud Computing

* Security 

Many cloud providers offer a broad set of policies, technologies and controls that strengthen your security posture overall, helping protect your data, apps and infrastructure from potential threats.

* Cost 

Cloud computing eliminates the capital expense of buying hardware and software and setting up and running on-site datacenters—the racks of servers, the round-the-clock electricity for power and cooling, the IT experts for managing the infrastructure. It adds up fast.

Cloud computing also offers its users a `pay as you go` approach to pricing. For example, with AWS you pay only for the individual services you need, for as long as you use them, and without requiring long-term contracts or complex licensing. AWS pricing is similar to how you pay for utilities like water and electricity. You only pay for the services you consume, and once you stop using them, there are no additional costs or termination fees.

* Flexibility through Scalability 

Predicting future traffic is difficult, especially when unforeseen events can arise such as a pandemic. As people were locked inside for months on end, internet usage increased and the traffic websites received increased significantly. But cloud computing is flexible, and it can meet unpredictable events because it offers its users the ability to increase or decrease IT resources as needed to meet changing demand. 

* Reliability 

Cloud computing makes data backup, disaster recovery and business continuity easier and less expensive because data can be mirrored at multiple redundant sites on the cloud provider’s network. In AWS, for example, there exist different regions which are physical locations around the world where Amazon cluster data centers. Each group of logical data centers is called an Availability Zone (AZ), and each AWS Region consists of multiple, isolated, and physically separate AZs within a geographic area. That way, even if something disastrous happens to one AZ, such as a natural disaster like flooding, the product will not go done as AWS will automatically redirect the traffic for your instances to another AZ in the region.

Apps can even be deployed into mulitple regions. That way, if the Ireland region for AWS goes down, it can still serve the users from London. However, as you use more regions, the costs will become greater so the business will have to carry out a cost-benefit analysis. 

* Accessibility

Cloud computing ensures details such as a low latency can easily be achieved. For example, if the end user is based in Australia, the region you use could also be in Australia to improve their experience with the product. (SIDE NOTE: CDN - Contact delivery network. Helps latency/response time if the servers from the users are very far away.)

## Set up an EC2 server

> 1. Select location Ireland

> 2. Click EC2.

> 3. Select free tier.

> 4. Pick t2 micro.

> 5. Choose Ubuntu 18.

> 6. Set network to default

> 7. Set subnet to devops 1a.

> 8. Auto assign public ip - enable