**************************
Frequently asked questions
**************************

.. note::

    | For agent related questions, see :ref:`agent-faq`

1. What should I configure on firewalls if I use the SAAS architecture?
***********************************************************************

| You need to configure your firewalls to allow the agents to communicate with our datasentinel platform
| in both ways (push and pull)

    - server: app.datasentinel.io
    - port: 443

| You need to configure the user PCs to communicate with the agents
| in one way (User PC -> agent)

    - The agent default port is 8282. You can update it with the :ref:`agent-cli` or with :ref:`agent-apis`

2. What should I configure on firewalls if I use the On-premises architecture?
******************************************************************************

| You need to configure your firewalls to allow the agents to communicate with the datasentinel platform
| in both ways (push and pull)

    - server: <<Your platform server>>
    - port: 443

| You need to configure the platform to communicate with the agents
| in one way (Platform -> agent)

    - The agent default port is 8282. You can update it with the :ref:`agent-cli` or with :ref:`agent-apis`


3. How can i change the default self-signed certificate?
*********************************************************

.. note::
    | On-premises platform uses a self signed certificate configured with NGINX
    | The self-signed certificate is located in **/etc/nginx/certs** directory
    | You can change it with your own certificate.

1. Generate a certificate for the platform machine
2. Replace existing files with the real certificate (cert_datasentinel.pem and key_datasentinel.pem)
3. Restart NGINX

4. How do i change the access token?
************************************

.. note::
    | Agents need a token to authenticate and communicate with the platform.
    | The token has an expiration date.
    | It is necessary to update the access token before its expiration date

1. The support team sends you a valid token
2. Update Datasentinel platform with the valid token

    **See documentation about** :ref:`token`

.. _sizing_platform:

5. What is the platform sizing recommendation?
**********************************************

Sizing the Platform

**1. CPU and MEMORY**

- The needed values depend on the number of users. The most consuming resources are SELECT queries executed on the platform

**2. STORAGE**

The needed storage will depend on several factors

- The number of PostgreSQL instances to monitor
- The data retention period (default 14 days)
- The number of tags associated to each instance.
- The number of distinct queries (pg_stat_statements)

An average value has been observed of 150 MB per day per instance

**For example**

- You have 50 PostgreSQL instances
- The default data retention is used : 14 days
- You have 5 custom tags per instance

With this configuration, the needed space to store data is 50 * 150 * 14 = 100 GB

.. note::

    | We strongly recommend a machine with scale capabilities like virtual machines for example

The values displayed below are default values for standard workloads and default data retention

.. image:: images/sizing.png
   :scale: 100 %
   :align: center