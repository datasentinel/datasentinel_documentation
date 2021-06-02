.. _connection_api:

*************************
Connection Management API
*************************


**Endpoints**
*************

- API can be reached at **https://<<datasentinel_platform_server>>**

.. warning::
   | Connection API is only available for an **on-premises** installation and if you want to use the **Agentless** feature
   | 
   | If you prefer installing each agent locally, then adding a connection is done at the agent level with the agent :ref:`agent-cli` or with agent :ref:`agent-apis`.

.. note::
   | A toolkit, wich provides examples of use, is available on `Github <https://github.com/datasentinel/datasentinel_toolkit>`_
   | 
   | The toolkit is installed by default on the **on-premises** platform (/datasentinel/soft/datasentinel_toolkit)


**User token generation**
*************************

In order to use connection API, you need to generate an access token. 
**The access token is valid for 1 day**

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #45d6b5">POST</span>&nbsp;/ds-api/user-token</h6>

- Authentication

   | You need to be authenticated with your username and password
   | The user must have **data admin** profile with **admin** privilege

- Example 

.. code:: bash
  
  curl -u myUser:myPassword -k -X POST https://<<datasentinel_platform_server>>/ds-api/user-token


- Response

.. code:: bash

  {
    "user-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODAyMTYyMjQsImlhdCI6MTU4MDEyOTgxOSwiZGF0YWJhc2UiOiJNYWluIE9yZy4iLCJlbWFpbCI6InRlc3RAZGF0YXNlbnRpbmVsLmlvIiwidXNlciI6InRlc3QifQ.JMDvq2JPcqz9M0_it_0UtP9y79dClVwx9pDEzCl9HTk"
  }


**Display User token**
**********************

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #3f6ed8"">GET</span>&nbsp;/ds-api/user-token?token={user-token}</h6>

- Path parameter:

   | The token


- Example 

.. code:: bash
  
  export TOKEN=<<user_token>>
  curl -u myUser:myPassword -k -X GET https://<<datasentinel_platform_server>>/ds-api/user-token?token=$TOKEN


- Response

.. code:: bash

    {
        "email": "contact@datasentinel.io",
        "expire_time": "2020-04-28 13:58:53",
        "organization_name": "ds-data",
        "user": "datasentinel"
    }

**Add a connection**
********************************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "host": "pg-crm-2031",
      "port": 9342,
      "user": "datasentinel",
      "password": "password",
      "tags": "datacenter=paris,provider=aws,environment=production"
    }

- Parameters:

    | pg_name: Unique connection identifier name
    |
    | host : PostgreSQL host name
    | port: PostgreSQL port number 
    |
    | user: PostgreSQL user
    | password: PostgreSQL user password
    |
    | tags: list of key,value pairs (completely customisable)

- Response

.. code:: bash

    {
        "status": "Connection created and connected!"
    }


**Display connection**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production'

- Parameters:

    | pg_name: Unique connection identifier name

- Response

.. code:: bash

  {
        "connected": true,
        "enabled": true,
        "host": "pg-crm-2031",
        "name": "crm-production",
        "password": "password",
        "port": 9342,
        "tags": "datacenter=paris,provider=aws,environment=production",
        "user": "datasentinel"
    }

**Update connection**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request PUT 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production'  -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "host": "pg-crm-2031",
      "port": 9342,
      "user": "datasentinel",
      "password": "password",
      "tags": "datacenter=paris,provider=aws,environment=production"
    }

- Parameters:

    | pg_name: Unique connection identifier name
    |
    | host : PostgreSQL host name
    | port: PostgreSQL port number 
    |
    | user: PostgreSQL user
    | password: PostgreSQL user password
    |
    | tags: list of key,value pairs (completely customisable)

- Response

.. code:: bash

    {
        "status": "Connection updated!"
    }

**Disable connection**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}/disable</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request PATCH 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production/disable'

- Parameters:

    | pg_name: Unique connection identifier name

- Response

.. code:: bash

    {
        "status": "Connection disabled!"
    }

**Enable connection**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">PATCH</span><span style="color:gray">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}/enable</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request PATCH 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production/enable'

- Parameters:

    | pg_name: Unique connection identifier name

- Response

.. code:: bash

    {
        "status": "Connection enabled!"
    }

**Delete connection**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">DELETE</span><span style="color:gray">&nbsp;/ds-api/pool/pg-instances/{{pg_name}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request DELETE 'https://<<datasentinel_platform_server>>/ds-api/pool/pg-instances/crm-production'

- Parameters:

    | pg_name: Unique connection identifier name

- Response

.. code:: bash

    {
        "status": "Connection deleted!"
    }