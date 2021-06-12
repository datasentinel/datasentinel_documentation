.. _role_api:

*********************
Role Based Access API
*********************


**Role based access** is a feature allowing you to limit access to a subset of your PostgreSQL instances.

To enable this feature:

  1. Use predefined tags or associate new tags with your PostgreSQL clusters (See `How to use tags <https://www.datasentinel.io/blog/post/tags/>`_) 
  2. Create a role with a condition on one or more tags 
  3. Assign the Role to a User 

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

**Add a role**
**************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/roles/{{ role }}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://<<datasentinel_platform_server>>/ds-api/roles/MyNewRole' -d @body.json

- Request example (body.json)

.. code:: bash

    {
    "access": [
          {
              "filters": [
                  {
                      "tag": "pg_version",
                      "value": "11.8"
                  },
                  {
                      "tag": "environment",
                      "value": "production"
                  }
              ]
          }
      ]
  }

- Parameters:

    | role: Role name
    | 
    | access : filter array
    | Must be :
    |    { "filters" : tag / value array }
    |
    | **Tags must exist and be associated with one or more instances**

**Examples**

You want to define a role based access on production only instances **AND** located in London datacenter:

.. code:: bash

    "access": [
     { 
        "filters": 
          [ 
                  {"tag": "environment", "value": "production"},
                  {"tag": "datacenter", "value": "london"}
          ]
     }
    ]

You want to define a role based access on development **OR** uat instances :

.. code:: bash

    "access": [
      {
        "filters": 
          [
            { "tag": "environment", "value": "development" }
          ]
      },
      {
        "filters": 
          [
            { "tag": "environment", "value": "uat" }
          ]
      },
    ]


**You can combine Multiples AND / OR conditions**

- Response

.. code:: bash

  {
    "status": "Role name MyNewRole created successfully"
  }

**Display Role**
*****************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/roles/{{ role }}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/roles/myRole'

- Parameters:

    | role: Role name

- Response

.. code:: bash

      {
      "name": "myRole",
      "access": [
          {
              "filters": [
                  {
                      "tag": "pg_instance",
                      "value": "51.15.233.24@agentLess6"
                  }
              ]
          },
          {
              "filters": [
                  {
                      "tag": "pg_instance",
                      "value": "51.158.104.206@agentLess11"
                  }
              ]
          }
        ]
      }


**Update Role**
***************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #ff8c69">PUT</span><span style="color:#ff8c69">&nbsp;/ds-api/roles/{{ role }}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request PUT 'https://<<datasentinel_platform_server>>/ds-api/roles/MyNewRole'  -d @body.json

- Request example (body.json)

.. code:: bash

    {
    "access": [
          {
              "filters": [
                  {
                      "tag": "environment",
                      "value": "production"
                  }
              ]
          }
      ]
    }

- Parameters:

    | Role: Role name
    |
    | access : filter array
    | Must be :
    |    { "filters" : tag / value array }
    |

- Response

.. code:: bash

    {
      "status": "Role name MyNewRole updated successfully"
    } 

**Delete Role**
***************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: gray">DELETE</span><span style="color:gray">&nbsp;/ds-api/roles/{{ role }}</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request DELETE 'https://<<datasentinel_platform_server>>/ds-api/roles/MyNewRole'

- Parameters:

    | email: User email

- Response

.. code:: bash

  {
    "status": "Role name MyNewRole deleted successfully"
  }


**Display all Roles**
**********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/roles</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/roles'

- Response

.. code:: bash

    [
      {
          "name": "myRole",
          "access": [
              {
                  "filters": [
                      {
                          "tag": "pg_instance",
                          "value": "51.15.233.24@agentLess6"
                      }
                  ]
              },
              {
                  "filters": [
                      {
                          "tag": "pg_instance",
                          "value": "51.158.104.206@agentLess11"
                      }
                  ]
              }
          ]
      },
      {
          "name": "testrole",
          "access": [
              {
                  "filters": [
                      {
                          "tag": "pg_version",
                          "value": "11.8"
                      },
                      {
                          "tag": "pg_instance",
                          "value": "51.15.233.24@agentLess6"
                      }
                  ]
              }
          ]
      }
    ]   
  

**Display assigned users**
***************************
  
.. raw:: html

    <h6 ><span style="margin-left:30px;font-weight:bold;color: #3f6ed8">GET</span><span style="color:#3f6ed8">&nbsp;/ds-api/roles/{{ role }}/users</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request GET 'https://<<datasentinel_platform_server>>/ds-api/roles/myRole/users'

- Parameters:

    | role: Role name

- Response

.. code:: bash

    [
      {
          "id": 70,
          "login": "username",
          "email": "userName@myCompany.com",
          "profile": "data admin",
          "privilege": "admin",
          "role": "myRole",
          "live_360": 1
      }
    ]