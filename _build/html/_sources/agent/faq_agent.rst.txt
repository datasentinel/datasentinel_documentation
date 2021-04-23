.. _agent-faq:

*********
Agent FAQ
*********

1. On which distributions can I install the agent?
**************************************************

| The agent can be installed on any linux os.
|
| See :ref:`agent-installation`
| The agent is currently available on

    - Centos, RHEL 6
    - Centos, RHEL 7
    - Debian 8 (Jessie)
    - Debian 9 (Stretch)

| If the agent is not available in your current linux distribution, please ask us to deploy a new agent.

2. How the agent communicates with the platform?
************************************************

| The agent communicates with the platform in secured mode HTTPS.
|
| The platform allows the agent to send metrics by verifying the validity of its token

3. Can I automate the agent installation?
*****************************************

| You can easily automate the agent installation on dozens or hundreds of servers.
|
| The agent is delivered as a tar.gz executable file
| Simply uncompress it and configure it with the :ref:`agent-cli` or with :ref:`agent-apis`.


4. Can I change the agent listener port?
****************************************
.. note::
    | By default, the agent listens on port 8282.

| You can customize the port number with the :ref:`agent-cli` or with :ref:`agent-apis`

.. code-block:: bash

    datasentinel set port <<port_number>>

| Or directly in the configuration file located on **$HOME/.datasentinel/agent.yml**

.. warning::
   | You must restart the agent to take into account the new port number
   | Once restarted, you can communicate with the agent API on the new port


5. Can i change the sessions sampling interval?
***********************************************

.. note::
    | By default, the parameter collection_rate is set to 'high'
    | Session activity is then sampled every second

You can change the interval to 10 seconds by changing the collection_rate attribute 

| You can change the rate with the :ref:`agent-cli` or with :ref:`agent-apis`

.. code-block:: bash

    datasentinel set collection_rate low|high


6. How do i change the access token?
************************************

.. note::
    | Agents need a token to authenticate and communicate with the platform.
    | The token has an expiration date.
    | It is necessary to update the access token before its expiration date

1. The support team sends you a valid token
2. Update Datasentinel platform with the valid token
3. Agents automatically download the new token in order to be authorized to communicate with the platform

    **See documentation about** :ref:`token`


7. Does the agent store data in each PostgreSQL instance?
**********************************************************

| NO, The agent doesn't store any data


8. How the agent behaves in case of unavailability of the platform?
********************************************************************

| When the agent encounters a problem sending its metrics, (Network failure, platform not available, other reason....), 
| it continues to collect metrics but stores them locally (up to 24 hours in the subdirectory tmp).

.. note::

    | Once the incident is resolved, the agent automatically detects it and sends all of its metrics to the platform

9. How the agent behaves in case of unavailability of a PostgreSQL instance?
****************************************************************************

| When a PostgreSQL instance becomes unavailable (maintenance, reboot, ...), the agent stops its monitoring. 

.. note::

    | Once the instance becomes available again, the agent automatically reconnects to the instance and continues its monitoring


10. Can I turn off the collection of table and index statistics?
****************************************************************************

.. warning::

    | The collection of tables and indexes statistics is done every hour.
    | By default, if the number of tables on your PostgreSQL instance is greater than 1000, this feature is disabled due to a little overhead

You can change this value by adjusting the parameter **table-monitoring-limit** in the agent configuration file. 

.. note::

    | The agent configuration file is $HOME/.datasentinel/agent.yml
    | The **table-monitoring-limit** is under the **agent** section


11. How can i verify that pg_stat_statements is installed?
*********************************************************

.. warning::
   | The extension needs to be installed in the **postgres** database.

.. code-block:: bash

    SELECT current_database(), extname from pg_extension where extname ='pg_stat_statements';
    current_database |      extname       
    ------------------+--------------------
    postgres         | pg_stat_statements
    (1 row)


.. _agent-faq-status:

12. The agent is running but the CLI responds NO?
****************************************************************************

.. code-block:: bash

    $ps -ef | grep "datasentinel start agent" | grep -v grep
    postgres 29213     1  1 14:00 ?        00:00:00 datasentinel start agent

    $datasentinel status agent

    Copyright 2021 (c) datasentinel- All rights reserved        www.datasentinel.io
    ================================================================================

    Agent not started


The agent listens by default on port 8282. The CLI communicates with the running process via this port.

Verify that there is no firewall issue and the server name is resolved correctly

example

.. code-block:: bash

    $ ping `hostname`
    PING pg-sales-3420 (127.0.0.1) 56(84) bytes of data.

    curl -v telnet://`hostname`:8282
    * About to connect() to pg-sales-3420 port 8282 (#0)
    *   Trying 127.0.0.1...
    * Connected to pg-sales-3420 (127.0.0.1) port 8282 (#0)
