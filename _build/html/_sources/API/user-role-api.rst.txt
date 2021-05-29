.. _user_api:

*****************
User and Role API
*****************


**Endpoints**
*************

- API can be reached at **https://<<datasentinel_platform_server>>**

.. note::
   | A toolkit, wich provides examples of use, is available on `Github <https://github.com/datasentinel/datasentinel_toolkit>`_
   | 
   | The toolkit is installed by default on the **on-premises** platform (/datasentinel/soft/datasentinel_toolkit)


**User token generation**
*************************

In order to use user and role API, you need to generate an access token. 
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

**Add a user**
**************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/ds-users</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://<<datasentinel_platform_server>>/ds-api/ds-users' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "email": "userName@myCompany.com",
      "password": "myPassword",
      "privilege": "admin",
      "profile": "data admin",
      "live_360": 1,
      "role": "No restriction",
    }

- Parameters:

    | **Required**
    | email: User email used to connect to Datasentinel
    | password : User password
    |
    | **Optional**
    | "privilege": read, read write or admin (default: **admin**) 
    | "profile":  developer or data admin (default: **data admin**)
    | "live_360": 0 or 1 (default: **1**) 
    | "role":  Role name (default: **No restriction**)



- Response

.. code:: bash

    {
      "status": "User with login userName created successfully"
    }

- Privilege parameter 
  
3 privileges are available. A privilege needs to be assigned to a user

+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Privilege                             | Description                                                                                      |
+=======================================+==================================================================================================+
| read                                  | - Read only acces to datasentinel                                                                |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| read write                            | - Read only acces to datasentinel                                                                |
|                                       | - Kill sessions                                                                                  |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| admin                                 | - Read only acces to datasentinel                                                                |
|                                       | - Kill sessions                                                                                  |
|                                       | - Agent, postgreSQL instance management                                                          |
|                                       | - User management                                                                                |
|                                       | - Datasentinel configuration management                                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------+

- Profile parameter 

2 profiles are available. A profile needs to be assigned to a user

+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Profile                               | Description                                                                                      |
+=======================================+==================================================================================================+
| developer                             | - Access limited to sessions workload and top queries features                                   |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| data admin                            | - Access unlimited                                                                               |
+---------------------------------------+--------------------------------------------------------------------------------------------------+

- live_360 parameter 

Live360 feature allows you to connect directly to the instances to have real-time information (See :ref:`live_360`)

+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Value                                 | Description                                                                                      |
+=======================================+==================================================================================================+
| 0                                     | Not allowed                                                                                      |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| 1                                     | Allowed                                                                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------+

- role parameter

Assign an existing role if you want to enable the **Role based access** feature, which allows you to restrict access to a subset of the perimeter of your PostgreSQL instances. 
You define roles with specific filters (Server, PG instance, datacenter, application, environment, etc, ...).



**Display user**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/ds-users/{{email}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/ds-users/userName@myCompany.com'

- Parameters:

    | email: User email

- Response

.. code:: bash

    {
        "id": 54,
        "login": "username",
        "email": "userName@myCompany.com",
        "profile": "data admin",
        "privilege": "admin",
        "role": "No restriction",
        "live_360": 1
    }

**Update user**
***************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/ds-api/ds-users/{{email}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request PUT 'https://<<datasentinel_platform_server>>/ds-api/ds-users/userName@myCompany.com'  -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "privilege": "read",
      "live_360": 0
    }

- Parameters:

    | email: User email
    |
    | **Optional**
    | "password": User password 
    | "privilege": read, read write or admin
    | "profile":  developer or data admin
    | "live_360": 0 or 1
    | "role":  Role name

- Response

.. code:: bash

    {
      "status": "User updated successfully!"
    }

**Delete user**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">DELETE</span><span style="color:gray">&nbsp;/ds-api/ds-users/{{email}}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request DELETE 'https://<<datasentinel_platform_server>>/ds-api/ds-users/userName@myCompany.com'

- Parameters:

    | email: User email

- Response

.. code:: bash

  {
    "message": "User deleted"
  }


**Display all users**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/ds-users</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/ds-users'

- Response

.. code:: bash

    [
      {
          "id": 2,
          "login": "datasentinel",
          "email": "contact@datasentinel.io",
          "profile": "data admin",
          "privilege": "admin",
          "role": "No restriction",
          "live_360": 1
      },
      {
          "id": 54,
          "login": "username",
          "email": "userName@myCompany.com",
          "profile": "data admin",
          "privilege": "read",
          "role": "No restriction",
          "live_360": 0
      }
  ]    