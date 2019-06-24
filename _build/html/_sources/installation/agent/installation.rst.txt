.. _agent-installation:

******************
Agent installation
******************

.. note::
   | The examples are done on a standard postgresql installation with a server running **centos 7** operating system
   | An agent is to be installed on each server running a postgresql instance. 

.. note::
   | Datasentinel needs **pg_stat_statements** extension. 

1. Download the agent
*********************

- Connect to your user interface URL with a admin user.
- Go to Tools submenu and click on agents.
- Download the agent (tar.gz format, available for redhat/centos 6 and 7)

.. note::
   If you use our on-premises platform, you can also copy directly the file **datasentinel-agent-rhel7.tar.gz** from the directory **/datasentinel/download**

.. note::
   To deploy the agent on a **Red Hat / Centos 6** use **datasentinel-agent-rhel6.tar.gz**


2. Start the agent
******************

| *The LD_LIBRARY_PATH must be set to the subdirectory lib*

.. code-block:: bash

   tar xvzf datasentinel-agent-rhel7.tar.gz
   export DATASENTINEL_PATH="`pwd`/datasentinel"
   export LD_LIBRARY_PATH=$DATASENTINEL_PATH/lib
   export PATH=$DATASENTINEL_PATH:$PATH
   datasentinel start agent

3. Token and upload server
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

4. Upload server and token validity
***********************************

| It also checks the communication between the agent and the server

.. code-block:: bash

    datasentinel show token


5. Postgresql user
******************

.. warning::
   For versions less than 10, the user must have the role superuser

- Version 9.2, 9.3, 9.4, 9.5, 9.6

.. code-block:: bash

   create user datasentinel password 'myPassword';
   alter user datasentinel with superuser;
   grant select on pg_authid to datasentinel;

- Version 10, 11

.. code-block:: bash

   create user datasentinel password 'myPassword';
   grant pg_monitor,pg_read_all_settings,pg_read_all_stats to datasentinel;
   grant select on pg_authid to datasentinel;


6. pg_hba.conf
**************

   - Add authorization for the user datasentinel to connect to all databases with a password

.. code-block:: bash

   # TYPE  DATABASE        USER            ADDRESS                 METHOD
   host    all             datasentinel    127.0.0.1/0             md5

- Restart postgresql

7. Postgresql instance
**********************

.. code-block:: bash

   cat > myInstance.json <<EOF
   {
     "host": "<<host_name>>",
     "port": <<postgres_port>>,
     "user": "datasentinel",
     "password": "myPassword",
     "tags": "application=<<application_name>>,environment=<<application_type>>,datacenter=<<datacenter>>"
   }
   EOF

.. code-block:: bash

   datasentinel add connection myConnectionName -f myInstance.json

.. note::
   | The tags are customisable. you can define your own tags.
   | They are very useful in the user interface for filtering, grouping data and to define Role based access.

8. Useful CLI commands
**********************

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

   Copyright 2019 (c) datasentinel- All rights reserved        www.datasentinel.io
   ================================================================================

      Agent:
         - start agent
         - stop agent
         - status agent
         - set port <port number>

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
                                "password": "value (optional)",
                              }
         - delete proxy
         - show proxy

9. APIs
*******

- All operations are available through direct APIs calls.
   
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

10. Internal storage
********************

The agent stores its configuration on the hidden directory **.datasentinel** under the user home.

Most of the operations need a token to be passed in the headers calls.

2 files are present:

- agent.yml
- connections.yml

.. note:: 

   You can modify the agent properties directly through theses files (except passwords which are encrypted)
