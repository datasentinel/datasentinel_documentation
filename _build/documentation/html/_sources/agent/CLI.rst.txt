.. _agent-cli:

****
CLI
****

.. note::
   | The agent can be configured through the CLI

.. note::
   | The agent stores its configuration on the hidden directory **.datasentinel** under the user home.
   |
   | 2 files are used
   |  - agent.yml
   |  - connections.yml

**Prerequisites**
*****************

See how to :ref:`agent-installation`.

Set environment variables to execute CLI commands

.. code-block:: bash

    export DATASENTINEL_PATH="<<INSTALL_DIRECTORY>>/datasentinel"
    export LD_LIBRARY_PATH=$DATASENTINEL_PATH/lib
    export PATH=$DATASENTINEL_PATH:$PATH


**Agent management**
*********************

Show commands
==============

- Just type 

.. code:: bash

  datasentinel

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

    Agent:
          - start agent
          - stop agent
          - status agent
          - set port <port number>
          - set collection-rate <low|high>
                  low: The sessions collection is done every 10 seconds
                  high: The sessions collection is done every second  (Default value)

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



Status
=======

.. code:: bash
  
  datasentinel status agent


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

            Agent
              Version : 1.9.3                                             
                  Port : 8241                                              
            Start time : 2020-02-15 14:55:40                               
      Collection rate : high                                              

            Proxy
                  host :                                                   
                  port : 0                                                 
                  user :                                                   
              password :                                                   

          Upload
                  host : 51.158.125.244                                    
                  port : 443                                               

      Connections
              declared : 1                                                 
              running : 1                                                 
          not running : 0                                                 


Start
=====

.. code:: bash
  
  datasentinel start agent


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Starting the agent...


  To show the status : datasentinel status agent


Stop
=====

.. code:: bash
  
  datasentinel stop agent


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  The agent is stopped!


Change the port number
======================

.. code:: bash
  
  datasentinel set port 9121


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Agent port successfully set! The agent has been stopped, you need to restart it

.. _collection_rate:

Change the collection rate
==========================


.. code:: bash
  
  datasentinel set collection-rate low|high

- Parameter:

   | The collection rate : low or high
   | low : Session activity is sampled every 10 seconds
   | high : Session activity is sampled every second

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Collection rate successfully set to low!


            Agent
              Version : 1.9.3                                             
                  Port : 8241                                              
            Start time : 2020-02-15 14:55:40                               
      Collection rate : low                                               

            Proxy
                  host :                                                   
                  port : 0                                                 
                  user :                                                   
              password :                                                   

          Upload
                  host : 51.158.125.244                                    
                  port : 443                                               

      Connections
              declared : 1                                                 
              running : 1                                                 
          not running : 0                          



**Upload server**
*****************

Set
===

- Change the server where metrics are sent

.. code:: bash
  
  datasentinel set server app.datasentinel.io 443


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Server successfully set!


          Server
                  host : app.datasentinel.io                               
                  port : 443                                               

Show
=====

- Show the server where metrics are sent

.. code:: bash
  
  datasentinel show server


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

          Server
                  host : app.datasentinel.io                               
                  port : 443                                               
 

Test
=====

.. code:: bash
  
  datasentinel test server


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  TEST: The upload server is reachable and up!


          Server
                  host : app.datasentinel.io                               
                  port : 443                                               
   

**Proxy**
*********

Set
===

- create a json file with proxy settings and update the agent

.. code:: bash
  
  cat > proxy.json << EOF
  {
      "host": "myProxyHostName",
      "port": 4587,
      "user": "username (optional)",
      "password": "value (optional)"
  }
  EOF

  datasentinel set proxy -f proxy.json


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Proxy successfully set!


            Proxy
                  host : myProxyHostName                                          
                  port : 4587                                              
                  user :                                                   
              password :    



Show
=====

.. code:: bash
  
  datasentinel show proxy


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

            Proxy
                  host : hostname                                          
                  port : 4587                                              
                  user :                                                   
              password : 

Delete
=======

.. code:: bash
  
  datasentinel delete proxy


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Proxy successfully deleted!


            Proxy
                  host :                                                   
                  port : 0                                                 
                  user :                                                   
              password :  


**Connections**
***************

Show
=====

.. code:: bash
  
  datasentinel show connections


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  name                 status     state      host                 port   user           
  --------------------------------------------------------------------------------
  :9342                enabled    running    pg-sales-1734          9342 datasentinel   
    tags : application=sales,environment=production,provider=amazon,datacenter=lyon        


Enable all
==========

.. code:: bash
  
  datasentinel enable all


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connections enabled!


  name                 status     state      host                 port   user           
  --------------------------------------------------------------------------------
  :9342                enabled    running    pg-sales-1734          9342 datasentinel   
    tags : application=sales,environment=production,provider=amazon,datacenter=lyon  


Disable all
===========

.. code:: bash
  
  datasentinel disable all


- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connections disabled!


  name                 status     state      host                 port   user           
  --------------------------------------------------------------------------------
  :9342                disabled   not running pg-sales-1734          9342 datasentinel   
    tags : application=sales,environment=production,provider=amazon,datacenter=lyon        
  

**Connection**
***************

Add
=====

- Create a JSON file with connection settings and update the agent

.. code:: bash
  
  cat > newConnection.json << EOF
  {
      "host": "pg-sales-1734",
      "port": 9342,
      "user": "datasentinel",
      "password": "sentinel",
      "tags": "application=sales,environment=production,provider=amazon,datacenter=lyon",
  }
  EOF

  datasentinel add connection myNewConnection -f newConnection.json 

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connection added!


                  Name : myNewConnection                                     
                Status : enabled                                           
                State : connected                                         

                  Host : pg-sales-1734                                     
                  Port : 9342                                              

                  user : datasentinel                                      
              password : sentinel                                          

                  tags : application=sales,environment=production,provider=amazon,datacenter=lyon



Show
=====

.. code:: bash
  
  datasentinel show connection myNewConnection

- Parameter 

   | The connection name

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

                  Name : myNewConnection                                     
                Status : enabled                                           
                State : connected                                         

                  Host : pg-sales-1734                                     
                  Port : 9342                                              

                  user : datasentinel                                      
              password : sentinel                                          

                  tags : application=sales,environment=production,provider=amazon,datacenter=lyon


Dump
=====

- Dump connection in JSON format

.. code:: bash
  
  datasentinel dump connection myNewConnection

- Parameter 

   | The connection name

- Response

.. code:: bash

  {
      "name": "myNewConnection",
      "host": "pg-sales-1734",
      "port": 9342,
      "user": "datasentinel",
      "password": "sentinel",
      "tags": "application=sales,environment=production,provider=amazon,datacenter=lyon",
      "enabled": true,
      "connected": true
  }
   
Delete
=======

.. code:: bash
  
  datasentinel delete connection myNewConnection

- Parameter 

   | The connection name

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connection successfully deleted!

Enable
======

.. code:: bash
  
  datasentinel enable connection myNewConnection

- Parameter 

   | The connection name

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connection enabled!


                  Name : myNewConnection                                     
                Status : enabled                                           
                State : connected                                         

                  Host : pg-sales-1734                                     
                  Port : 9342                                              

                  user : datasentinel                                      
              password : sentinel                                          

                  tags : application=sales,environment=production,provider=amazon,datacenter=lyon


Disable
=======

.. code:: bash
  
  datasentinel disable connection myNewConnection

- Parameter 

   | The connection name

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connection disabled!


                  Name : myNewConnection                                     
                Status : disabled                                          
                State : not connected                                     

                  Host : pg-sales-1734                                     
                  Port : 9342                                              

                  user : datasentinel                                      
              password : sentinel                                          

                  tags : application=sales,environment=production,provider=amazon,datacenter=lyon



Update
=======

.. code:: bash
  
  cat > updateConnection.json << EOF
  {
      "host": "pg-sales-1734",
      "port": 9342,
      "user": "datasentinel",
      "password": "sentinel",
      "tags": "application=sales,environment=production,provider=microsoft,datacenter=paris",
  }
  EOF

  datasentinel update connection myNewConnection -f updateConnection.json

- Parameter 

   | The connection name

- Response

.. code:: bash

  Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
  ================================================================================

  Connection updated!


                  Name : myNewConnection                                     
                Status : enabled                                           
                State : connected                                         

                  Host : pg-sales-1734                                     
                  Port : 9342                                              

                  user : datasentinel                                      
              password : sentinel                                          

                  tags : application=sales,environment=production,provider=microsoft,datacenter=paris
