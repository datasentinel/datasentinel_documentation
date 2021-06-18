.. _agent-installation:

******************
Agent installation
******************

.. note::
   | The examples are done on a standard postgresql installation with a server running **centos 7** operating system
   | An agent is to be installed on each server running a postgresql instance. 

.. note::
   | Datasentinel needs the **pg_stat_statements** extension to be installed in your PostgreSQL instances

.. warning::
   | Extensions need to be installed in the **postgres** database of your instances

1. Download the agent
*********************

Download the latest version of agents.

•	 `RedHat/Centos 8 <https://app.datasentinel.io/ds-api/download/datasentinel-agent-rhel8.tar.gz>`_ 
•	 `RedHat/Centos 7 <https://app.datasentinel.io/ds-api/download/datasentinel-agent-rhel7.tar.gz>`_ 
•	 `RedHat/Centos 6 <https://app.datasentinel.io/ds-api/download/datasentinel-agent-rhel6.tar.gz>`_ 
•	 `Debian Buster <https://app.datasentinel.io/ds-api/download/datasentinel-agent-debian-buster.tar.gz>`_ 
•	 `Debian Stretch <https://app.datasentinel.io/ds-api/download/datasentinel-agent-debian-stretch.tar.gz>`_ 
•	 `Debian Jessie <https://app.datasentinel.io/ds-api/download/datasentinel-agent-debian-jessie.tar.gz>`_ 

.. note::
   | For other distributons, please contact us at support@datasentinel.io
   | The agent is available on linux only

2. Start the agent
******************

| *The LD_LIBRARY_PATH must be set to the subdirectory lib*

.. code-block:: bash

   tar xvzf datasentinel-agent-rhel7.tar.gz
   export DATASENTINEL_PATH="`pwd`/datasentinel"
   export LD_LIBRARY_PATH=$DATASENTINEL_PATH/lib
   export PATH=$DATASENTINEL_PATH:$PATH
   datasentinel start agent

3. Test the status
******************

.. code-block:: bash

   datasentinel status agent

- Output
  
   .. code-block:: bash

         Copyright 2021 (c) datasentinel- All rights reserved        www.datasentinel.io
         ================================================================================
         
                        Agent
                           Version : 2.6.0                                             
                              Port : 8282                                              
                        Start time : 2021-04-21 07:45:53                               
                  Collection rate : high                                              
            Table monitoring limit : 1000                                              
                     Sql max size : 256000                                            
         
                        Proxy
                              host :                                                   
                              port : 0                                                 
                              user :                                                   
                        password :                                                   
         
                     Upload
                              host : upload_server                                      
                              port : 443                                               
         
                  Connections
                        declared : 0                                                 
                           running : 0                                                 
                     not running : 0                                                 


.. warning::

   The agent is running but the CLI responds NO? Check this point :ref:`agent-faq-status`


4. Token and upload server
**************************

| A token is required in order to communicate with the repository
| Copy the token value directly from the user interface (Agents submenu) 

.. code-block:: bash

    datasentinel set server <<repository_server>> <<port>>
    datasentinel set token <<token_value>>

.. note::
   | By default, the server is our cloud platform https://app.datasentinel.io and the port is 443

.. note::
   | By default, the agent exchanges with the repository in SSL mode
   | It uses a self-signed certificate present in the config subdirectory:

   - cert_datasentinel.pem
   - key_datasentinel.pem

5. Upload server and token validity
***********************************

| It also checks the communication between the agent and the server

.. code-block:: bash

    datasentinel show token


6. Postgresql user
******************

.. warning::
   For versions less than 10, the user must have the role superuser

- Version 9.2, 9.3, 9.4, 9.5, 9.6

.. code-block:: bash

   create user datasentinel password 'myPassword';
   alter user datasentinel with superuser;

- Version 10, 11, 12, 13

.. code-block:: bash

   create user datasentinel password 'myPassword';
   grant pg_monitor,pg_read_all_settings,pg_read_all_stats to datasentinel;


7. pg_hba.conf
**************

- Add authorization for the user datasentinel to connect to all databases with a password

.. code-block:: bash

   # TYPE  DATABASE        USER            ADDRESS                 METHOD
   host    all             datasentinel    127.0.0.1/0             md5

.. note::
   | The user needs to be able to connect to all databases.

- Reload the configuration

8. Postgresql instance
**********************

.. code-block:: bash

   cat > myInstance.json <<EOF
   {
     "host": "host_name",
     "port": postgres_port,
     "user": "datasentinel",
     "password": "myPassword",
     "tags": "application=application_name,environment=application_type,datacenter=datacenter"
   }
   EOF

.. code-block:: bash

   datasentinel add connection myConnectionName -f myInstance.json

.. note::
   | The tags are customisable. you can define your own tags.
   | They are very useful in the user interface for filtering, grouping data and to define Role based access.

.. note::
   | A script is present in the **datasentinel** subdirectory as an example. (connection_example.sh)


9. Useful CLI commands
**********************

.. note::
   See how to use the :ref:`agent-cli`

- Show the agent status

.. code-block:: bash

   datasentinel status agent

- Show the connections

.. code-block:: bash

   datasentinel show connections
                                          
.. note::
   Show all options by typing **datasentinel** alone

- Output

.. code-block:: bash

      Copyright 2021 (c) datasentinel- All rights reserved        www.datasentinel.io
      ================================================================================

         Agent:
               - start agent
               - stop agent
               - status agent
               - set port <port number>
               - set collection-rate <low|high>
                     low: The sessions collection is done every 10 seconds
                     high: The sessions collection is done every second  (Default value)
                     If the datasentinel extension is not installed, the collection-rate is automatically adujusted to low value 
               - set tables-monitoring-limit (default 1000)
                     The agent monitors the activity of tables and indexes if the number of tables in the connection is less than the defined limit
               - set sql-max-size (default 256000)
                     Only useful when the datasentinel extension is not installed!
                     The agent analyzes each sql during the sampling of active sessions (pg_stat_activity) 
                     to calculate an identifier (md5).
                     If the size of the analyzed sql exceeds the limit, the sql text will be truncated
         
         Connections: when the connections are disabled, the agent is disconnected.
               - enable all
               - disable all

         Connection:
               - add connection <name> -f <json file>
               - update connection <name> -f <json file>
                     json example: {
                                    "host": "hostname",
                                    "port": 4587,
                                    "user": "username",
                                    "password": "value",
                                    "tags": "key=value,key=value,..."
                                    }

               - update connection <name> samples <on|off> (default on)
                     collect and send sample queries, with literal values if present

               - delete connection <name>
               - enable connection <name>
               - disable connection <name>

               - show connections
               - show connection <name>
         
         Dump connection in JSON format:
               - dump connection <name>  

         Upload server:
               - set server <host> <port>
               - show server
               - test server

         Token:
               - set token <value>
               - show token
               
         Proxy:
               - set proxy -f <json file>
                     json example: {
                                    "host": "hostname",
                                    "port": 4587,
                                    "user": "username (optional)",
                                    "password": "value (optional)"
                                    }
               - delete proxy
               - show proxy


10. API
********

.. note:: 
   All operations are available through :ref:`agent-apis`.
   
.. note:: 
   The agent listens on port 8282 by default (updatable)

- Example 

.. code:: bash
  
  curl -k -X GET https://<<host_name>>:8282/api/agent/status


- output

.. code:: bash

  {
    "version": "1.0",
    "port": 8282,
    "last_upload": "",
    "start_time": "2019-09-01 14:25:09",
    "proxy": {
      "host": "",
      "port": 0,
      "user": "",
      "password": ""
    },
    "upload_server": {
      "host": "app.datasentinel.io",
      "port": 443
    },
    "connections": {
      "connections": 1,
      "running": 1,
      "not running": 0
    }
  }

11. Internal storage
********************

The agent stores its configuration on the hidden directory **.datasentinel** under the user home.

Most of the operations need a token to be passed in the headers calls.

2 files are present:

- agent.yml
- connections.yml

.. note:: 

   You can modify the agent properties directly through theses files (except passwords which are encrypted)
