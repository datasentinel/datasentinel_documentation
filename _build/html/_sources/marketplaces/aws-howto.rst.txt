.. _aws_howto:

************************************************************
Launch Datasentinel on AWS with MarketPlace metering service
************************************************************

1. AWS Marketplace Metering Service
***********************************

| As you register your PostgreSQL instances and monitor them, Datasentinel charges your Amazon Subscription through the AWS Marketplace Metering Service. 
|
| Datasentinel charges are based on the number of PostgreSQL instances you monitor each hour. 
| See the AWS Marketplace for details and pricing.

.. note:: 
    | For this type of deployment, you do not need to purchase individual licenses. 
    | If you want to use individual licenses in AWS, you can deploy an EC2 instance, install Datasentinel, and apply your license. 


2. EC2 requirements
*******************

The EC2 instance containing the Datasentinel server must meet the following requirements.

+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Requirement                           | Details                                                                                                                                        |
+=======================================+================================================================================================================================================+
| IAM role permission                   | | An **IAM** role with the **aws-marketplace:MeterUsage** permission must be associated with the EC2 instance                                  | 
|                                       | | This permission allows the role to contact the Metering Service API and record usage.                                                        |
|                                       | |                                                                                                                                              |
|                                       | | A user with rights to define and assign roles can create the role in either of the following ways:                                           |
|                                       | |    1. Create the role on the Configure Instance Details panel of the wizard                                                                  |
|                                       | |    2. `Manually create the role <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#create-iam-role>`_        |
|                                       | |                                                                                                                                              |
|                                       | | To get the **aws-marketplace:MeterUsage** permission, attach the AWS managed policy **AWSMarketplaceMeteringFullAccess** to the role.        |
|                                       | |                                                                                                                                              |
|                                       | | If a role with the required permissions is not associated with the EC2 instance,                                                             |
|                                       | | Datasentinel reports issues with metering service availability.                                                                              |
|                                       | |                                                                                                                                              |
|                                       | | For more information, see:                                                                                                                   |
|                                       | `Subscribing, Launching, and Managing Products on AWS <https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-getting-started.html>`_ |                                
|                                       |                                                                                                                                                |
|                                       |                                                                                                                                                |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Access to the metadata URL	        | | The EC2 instance must have HTTP connectivity to 169.254.169.254, which is a local IP address accessible only from within Amazon instances.   | 
|                                       | |                                                                                                                                              |
|                                       | | To validate that the EC2 instance can access the metadata service, execute the following command:                                            |
|                                       | | **curl http://169.254.169.254/latest/meta-data/**                                                                                            |
|                                       | | The command returns a list of available metadata items.                                                                                      |
|                                       | |                                                                                                                                              |
|                                       | | For more information:                                                                                                                        |
|                                       | | `Retrieving Instance Metadata <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html#instancedata-data-retrieval>`_ |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
| Access to the metering service        | | The EC2 instance must be able to reach the AWS Metering Service (MeterUsage API).                                                            |
|                                       | | The URL is: `<https://metering.marketplace.{region}.amazonws.com/>`_                                                                         |
|                                       | | The region is where your EC2 instance is running                                                                                             |
|                                       | |                                                                                                                                              |
|                                       | | For example: https://metering.marketplace.us-east-1.amazonaws.com                                                                            |
|                                       | |                                                                                                                                              |
|                                       | | To be able to launch Datasentinel, you must have an Internet gateway configured.                                                             |
|                                       | | The Metering Service has an endpoint on the public Internet.                                                                                 |
|                                       | | To access the Metering Service, your Virtual Private Cloud must be configured to allow an outbound HTTPS connection to the public Internet.  |
|                                       | | For more information, see https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html                                             |
|                                       | |                                                                                                                                              |
|                                       | | To validate that the EC2 instance can connect to the Metering Service, execute the following command:                                        |
|                                       | |                                                                                                                                              |
|                                       | | curl `<https://metering.marketplace.{region}.amazonws.com/>`_                                                                                |
|                                       | | Replace {region} with the region where your EC2 instance is running.                                                                         |
|                                       | |                                                                                                                                              |
|                                       | | You should receive **healthy** as a response from the server.                                                                                |
+---------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------+


3. How to subscribe to Datasentinel?
************************************

- Log in to the `AWS Marketplace <https://aws.amazon.com/marketplace>`_

- Enter **Datasentinel** in the search field

.. image:: ../images/aws_search.png
   :scale: 100 %
   :align: center


- Product information is displayed. Then click on the button

.. image:: ../images/aws_subscribe.png
   :scale: 100 %
   :align: center

- Subscription information is displayed. Then click on the button

.. image:: ../images/aws_configure.png
   :scale: 100 %
   :align: center

- Choose your desired region from the drop down list.

.. note::
    | We recommend choosing the region where your PostgreSQL instances are located



Then click on the button

.. image:: ../images/aws_launch.png
   :scale: 100 %
   :align: center

- Select an instance type that is at least a **t2.large**. Datasentinel is available on EC2 instances of type **t2** and **m5**

.. note::
    | See how to size your EC2 instance on our `FAQ <https://www.datasentinel.io/documentation/faq.html>`_

- Select a role with the required permission or create it (see the **EC2 requirements** section for more information)

.. image:: ../images/aws_iam_role.png
   :scale: 100 %
   :align: center


- Keep metadata accessible, both v1 and v2

.. image:: ../images/aws_metadata.png
   :scale: 100 %
   :align: center

- Set the storage size. (Default 20GB)

.. note::
    | See how to size your EC2 instance on our `FAQ <https://www.datasentinel.io/documentation/faq.html>`_

- Add security rules

.. image:: ../images/aws_security.png
   :scale: 100 %
   :align: center

- Then Launch the instance. It will take a few minutes to complete.

4.. How to connect to Datasentinel?
************************************

- How to access your EC2 instance

You can connect to the Linux AMI using SSH and the user **ec2-user**. Authentication is based on a public key

- To connect to **Datasentinel** application

Open a web browser and enter the host name (Public DNS) or IP address of your new **Datasentinel** instance as the URL. 

To log in, enter **datasentinel**  

The default password is **datasentinel**  (Change it once connected)


5.. How to add your PostgreSQL instances?
*****************************************

Once the installation is complete, all that remains is to configure the instances to monitor.


You will have the choice between the `Agent-based or Agentless mode <https://www.datasentinel.io/documentation/installation/platform/agentbasedOrAgentless.html>`_


* **Agent-based mode**

Install an agent locally on each server and configure it to communicate with the platform.  
`See Documentation <https://www.datasentinel.io/documentation/installation/agent/installation.html>`_

Ideal if you manage your own postgresql instances. 

* **Agentless mode**

Configure connections directly through the user graphical interface

Ideal if you use AWS managed instances (rds, aurora)

You can automate the addition of connections thanks to the `API <https://www.datasentinel.io/documentation/features/connection-api.html>`_ (Agentless mode)


* **Enjoy**