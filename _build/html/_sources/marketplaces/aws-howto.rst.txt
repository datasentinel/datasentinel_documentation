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
