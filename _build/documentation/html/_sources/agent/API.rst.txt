.. _agent-apis:

****
API
****

.. note::
   | The agent can be configured through direct API calls

**Endpoints**
*************

- Agent APIs can be reached at **<<http_mode>>://<<host_name>>:<<port_number>>**

   | **http_mode** http or https
   | **host_name** The host where the agent is installed
   | **port_number** By default 8282 (updatable)


**Agent management**
*********************

Configuration details
=====================

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8">GET</span>&nbsp;/api/agent/status</h6>

- Example 

.. code:: bash
  
  curl -k -X GET https://pg-sales-0223:8282/api/agent/status


- Response

.. code:: bash

  {
    "version": "1.9.3",
    "port": 8282,
    "last_upload": "",
    "collection_rate": "low",
    "start_time": "2020-02-07 13:08:08",
    "proxy": {
      "host": "",
      "port": 0,
      "user": "",
      "password": ""
    },
    "upload_server": {
      "host": "51.15.236.159",
      "port": 443
    },
    "connections": {
      "connections": 1,
      "running": 1,
      "not running": 0
    }
  }

Stop
=====

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/api/agent/stop</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PUT 'https://pg-sales-0223:8282/api/agent/stop' 


- Response

.. code:: bash

  {
  "status": "Agent stopped"
  }

Change the port number
======================

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/agent/port/{{port_number}}</span></h6>

- Path parameter:

   | The new port number

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8282/api/agent/port/15524' 


- Response

.. code:: bash

    {
    "status": "Port changed successfully! The agent has been stopped"
    }

Change the collection rate
==========================

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/agent/collection-rate/{{precision}}</span></h6>

- Path parameter:

   | The collection rate : low or high
   | low : Session activity is sampled every 10 seconds
   | high : Session activity is sampled every second

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8282/api/agent/collection-rate/low' 


- Response

.. code:: bash

    {
    "status": "Collection rate successfully changed"
    }

**Upload server**
*****************

Set
===

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/api/server</span></h6>

- Example 

.. code:: bash
  
  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" -X PUT https://pg-sales-0223:8282/api/server -f body.json

- Request example (body.json)

.. code:: bash

    {
      "host": "app.datasentinel.io",
      "port": 443
    }

- Response

.. code:: bash

    {
      "status": "OK"
    }

Show
=====

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8">GET</span>&nbsp;/api/server</h6>

- Example 

.. code:: bash
  
  curl -k -X GET https://pg-sales-0223:8282/api/server


- Response

.. code:: bash

    {
      "host": "app.datasentinel.io",
      "port": 443
    }


Test
=====

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/api/server/test-upload</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request POST 'https://pg-sales-0223:8383/api/server/test-upload' 

- Response

.. code:: bash

    {
      "status": "OK"
    }

**Proxy**
*********

Set
===

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/api/proxy</span></h6>

- Example 

.. code:: bash
  
  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --header 'Content-Type: application/json' -X POST https://pg-sales-0223:8282/api/proxy -f body.json

- Request example (body.json)

.. code:: bash

    {
      "host": "proxy-server",
      "port": 12443,
      "user": "",
      "password": ""
    }

- Response

.. code:: bash

    {
      "status": "Proxy set"
    }

Show
=====

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8">GET</span>&nbsp;/api/proxy</h6>

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" -X GET https://pg-sales-0223:8282/api/proxy


- Response

.. code:: bash

    {
      "host": "proxy-server",
      "port": 12443,
      "user": "",
      "password": ""
    }

Delete
=======

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #c4162a">DELETE</span><span style="color:#c4162a">&nbsp;/api/proxy</span></h6>

- Example 

.. code:: bash
  
  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" -X DELETE https://pg-sales-0223:8383/api/proxy


- Response

.. code:: bash

    {
      "status": "OK"
    }


**Connections**
***************

Show
=====

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8">GET</span>&nbsp;/api/connections</h6>

- Example 

.. code:: bash
  
  curl -k -X GET https://pg-sales-0223:8282/api/connections


- Response

.. code:: bash

    [
      {
        "name": ":9342",
        "host": "pg-sales-0223",
        "port": 9342,
        "user": "datasentinel",
        "password": "sentinel",
        "tags": "application=sales,environment=production,provider=amazon,datacenter=paris",
        "enabled": true,
        "connected": true
      }
    ]

Enable all
==========

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/connections/enable</span></h6>


- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8383/api/connections/enable' 


- Response

.. code:: bash

    {
      "status": "OK"
    }

Disable all
===========

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/connections/disable</span></h6>


- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8383/api/connections/disable' 


- Response

.. code:: bash

    {
      "status": "OK"
    }

**Connection**
***************

Add
=====

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/api/connections/{{connection_name}}</span></h6>

- Path parameter:

   | The connection name

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://pg-sales-0223:8383/api/connections/sales_prod' -f body.json

- Request example (body.json)

.. code:: bash

    {
        "name": "sales_prod",
        "host": "pg-sales-0223",
        "port": 9342,
        "user": "datasentinel",
        "password": "sentinel",
        "tags": "application=sales,environment=production,provider=amazon,datacenter=paris"
    }


- Response

.. code:: bash

    {
      "status": "Connection created and connected!"
    }

Show
=====

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/api/connections/{{connection_name}}</span></h6>

- Path parameter:

   | The connection name

- Example 

.. code:: bash
  
  curl -k -X GET https://pg-sales-0223:8383/api/connections/sales_prod


- Response

.. code:: bash

    {
      "name": "sales_prod",
      "host": "pg-sales-0223",
      "port": 9342,
      "user": "datasentinel",
      "password": "sentinel",
      "tags": "application=sales,environment=production,provider=amazon,datacenter=paris",
      "enabled": false,
      "connected": false
    }


Delete
=======

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #c4162a">DELETE</span><span style="color:#c4162a">&nbsp;/api/connections/{{connection_name}}</span></h6>

- Path parameter:

   | The connection name

- Example 

.. code:: bash
  
  curl -k -X DELETE https://pg-sales-0223:8383/api/connections/sales_prod


- Response

.. code:: bash

    {
      "status": "Connection deleted!"
    }


Enable
======

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/connections/{{connection_name}}/enable</span></h6>

- Path parameter:

   | The connection name

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8383/api/connections/sales_prod/enable' 


- Response

.. code:: bash

    {
      "status": "Connection enabled!"
    }

Disable
=======

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/api/connections/{{connection_name}}/disable</span></h6>


- Path parameter:

   | The connection name

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --request PATCH 'https://pg-sales-0223:8383/api/connections/sales_prod/disable' 


- Response

.. code:: bash

    {
      "status": "Connection disabled!"
    }

Update
=======

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/api/connections/{{connection_name}}</span></h6>

- Path parameter:

   | The connection name

- Example 

.. code:: bash

  export TOKEN=<<datasentinel_token>>
  curl -k --header "api-token: $TOKEN" --header 'Content-Type: application/json' --request PUT 'https://pg-sales-0223:8383/api/connections/sales_prod' -f body.json

- Request example (body.json)

.. code:: bash

    {
        "host": "pg-sales-0223",
        "port": 9342,
        "user": "datasentinel",
        "password": "sentinel",
        "tags": "application=sales,environment=development,provider=amazon,datacenter=paris"
    }

- Response

.. code:: bash

    {
      "status": "Connection updated!"
    }

