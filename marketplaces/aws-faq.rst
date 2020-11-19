.. _aws_faq:

*******************
AWS marketplace FAQ
*******************

.. note::
    | You can also look at our :ref:`global_faq`


1. How to connect to the GUI?
*****************************

| Once you get your Datasentinel server running, you can log to it via the web browser.
|
| The user is **datasentinel**
| The password is your EC2 instance id. You can get it from the AWS console.
|
| Datasentinel is a subscription application and will start charging you after you start monitoring instances.

2. How to configure instances?
******************************

Datasentinel comes with 2 methods :

    You can use either the Agent-based or the Agentless feature to monitor your instances. (See :ref:`agentless`)

3. Can i monitor rds or aurora instances for PostgreSQL?
***********************************************************

Yes, use the Agentless feature to configure and monitor your managed instances.

4. Can I use it to monitor my on premises instances from the cloud or vice versa?
*********************************************************************************
Yes, you can monitor both cloud and on-premises instances as long as you have connectivity to the instance you want to monitor.


5. How to configure SSL?
************************

| Datasentinel uses a self signed certificate configured with NGINX
| 
| The self-signed certificate is located in **/etc/nginx/certs** directory
| You can change it with your own certificate.

1. Generate a certificate for the platform machine

2. Replace existing files with the real certificate (cert_datasentinel.pem and key_datasentinel.pem)

3. Restart NGINX (sudo systemctl restart nginx)


6. Can i change the https listening port?
*****************************************

| Datasentinel listens on default https port 443.
| You can change the port, by updating the config file **datasentinel.conf** located in **/etc/nginx/conf.d**
| Then, restart nginx: sudo systemctl restart nginx
|
| Do not forget to update your aws security group accordingly
|
| If you use local agents, you need to update the upload server with the new port number.


7. AWS EC2 sizing
*****************

1. CPU AND MEMORY


    **t2.large** is the Minimum Required Instance Type

    This instance size allows monitoring up to 10 instances.

2. STORAGE

    The needed storage will depend on several factors

    The number of PostgreSQL instances to monitor

    The data retention period (default 14 days)

    The number of tags associated to each instance.

    The number of distinct queries (pg_stat_statements)


    An average value has been observed of 150 MB per day per instance

    For example

        You have 50 PostgreSQL instances

        The default data retention is used : 14 days

        You have 5 custom tags per instance

        With this configuration, the needed space to store data is 50 * 150 * 14 = **100 GB**


The values displayed below are default values for standard workloads and default data retention

.. image:: ../images/sizing.png
   :scale: 100 %
   :align: center
