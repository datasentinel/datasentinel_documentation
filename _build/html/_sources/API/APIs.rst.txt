.. _api:

************
Workload API
************


**Endpoints**
*************

- API can be reached at **https://<<datasentinel_platform_server>>/ds-api/**

.. note::
   | If you use the SaaS architecture, the server is **app.datasentinel.io**


.. note::
   | A toolkit, wich provides examples of use, is available on `Github <https://github.com/datasentinel/datasentinel_toolkit>`_
   | 
   | The toolkit is installed by default on the **on-premises** platform (/datasentinel/soft/datasentinel_toolkit)


**User token generation**
*************************

In order to use datasentinel API, you need to generate an access token. 
**The access token is valid for 1 day**

.. raw:: html

   <h6><span style="margin-left:30px;font-weight:bold; color: #45d6b5">POST</span>&nbsp;/ds-api/user-token</h6>


- Authentication

   | You need to be authenticated with your username and password

- Example 

.. code:: bash
  
  curl -u myUser:myPassword -k -X POST https://app.datasentinel.io/ds-api/user-token


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
  curl -u myUser:myPassword -k -X GET https://app.datasentinel.io/ds-api/user-token?token=$TOKEN


- Response

.. code:: bash

    {
        "email": "contact@datasentinel.io",
        "expire_time": "2020-04-28 13:58:53",
        "organization_name": "ds-data",
        "user": "datasentinel"
    }

**Workload report**
*********************

.. note::
   | Export your entire workload as a PDF file 
   | Here is an example :download:`pdf <workload_example.pdf>`


.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#ff8c69">&nbsp;/ds-api/activity/workload-report</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/workload-report' -d @body.json -o myReport.pdf

- Request example (body.json)

.. code:: bash

  {
      "utc_time": true,
      "from": "2020-02-28 00:00:00",
      "to": "2020-02-29 01:00:00",
      "filters": [
          {
              "tag": "pg_instance",
              "value": "pg-crm-0926@:9342"
          }
      ],
      "sections": [
          "pg_instance",
          "top_queries",
          "top_segments",
          "data_size",
          "sessions_workload",
          "parameters"
      ]
  }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "sections" is an array of the type of activity desired.
    |

.. note:: 
   | If not specified, all sections are exported
   | for a **developer profile**, only top_queries, top_segments, and sessions_workload are available


+---------------------------------------+--------------------------------------------------------------------------------------------------+
| available section                     | Description                                                                                      |
+=======================================+==================================================================================================+
| pg_instance                           | global workload  (databases activity, server)                                                    |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| top_queries                           | top consumer queries (by execution time, blocks read, blocks hit)                                |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| top_segments                          | top tables, indexes...  (by blocks read, by blocks hit)                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| sessions_workload                     | sessions workload group by event type, by event, by database, by user, by query                  |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| data_size                             | databases, tables and indexes size                                                               |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| parameters                            | configuration parameters group by category                                                       |
+---------------------------------------+--------------------------------------------------------------------------------------------------+

**Sessions workload**
*********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/sessions-workload</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/sessions-workload' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-29 06:00:00",
      "to": "2020-01-29 08:00:00 ",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

  [
    {
      "time": "2020-01-29 06:00:13",
      "queryid": "1530125615",
      "application": "sales",
      "application_name": "N/A",
      "client_host_name": "127.0.0.1/32",
      "command_type": "SELECT",
      "database": "postgres",
      "datacenter": "paris",
      "environment": "production",
      "pg_instance": "pg-sales-0223@:9342",
      "pg_version": "10.11",
      "process_id": "24943 - :9342",
      "provider": "amazon",
      "query_md5_id": "0873c77e877bd3d284317e9537bbff9e",
      "server": "pg-sales-0223",
      "user_name": "datasentinel",
      "wait_event": "CPU",
      "wait_event_type": "CPU"
    },
    {
      "time": "2020-01-29 06:00:48",
      "queryid": "1338018050",
      "application": "sales",
      "application_name": "N/A",
      "client_host_name": "127.0.0.1/32",
      "command_type": "SELECT",
      "database": "postgres",
      "datacenter": "paris",
      "environment": "production",
      "pg_instance": "pg-sales-0223@:9342",
      "pg_version": "10.11",
      "process_id": "24979 - :9342",
      "provider": "amazon",
      "query_md5_id": "de248cd86cdd098e9bc09964ff42391f",
      "server": "pg-sales-0223",
      "user_name": "datasentinel",
      "wait_event": "CPU",
      "wait_event_type": "CPU"
    },
    .../...
  ]

**Top queries**
***************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/top-queries</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/acitity/top_queries' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-20",
      "to": "2020-01-21",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "by": "total_time",
      "limit": 10,
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | The 2 following parameters allow to define the sorting column as well as the number of rows returned
    |
    | "by": sorting column. (default total_time)
    | Possible values:
    | - calls, local_blks_dirtied, local_blks_hit, local_blks_read, local_blks_written, rows, shared_blks_dirtied, 
    | - shared_blks_hit, shared_blks_read, shared_blks_written, 
    | - temp_blks_read, temp_blks_written, total_time, blk_read_time, blk_write_time
    | 
    | "limit": The number of rows returned (default 20)
    |
    | "output":  the output can be json or csv (default json)

- Response

.. code:: bash

  [
    {
      "pg_instance": "pg-sales-3420@:9342",
      "database": "sales",
      "user": "sales_user",
      "query_md5_id": "617ec53d06c3f7138b3790c87ccb391e",
      "query_id": "1053048887",
      "calls": 264256688,
      "local_blks_dirtied": 0,
      "local_blks_hit": 0,
      "local_blks_read": 0,
      "local_blks_written": 0,
      "rows": 93,
      "shared_blks_dirtied": 159,
      "shared_blks_hit": 528514486,
      "shared_blks_read": 31,
      "shared_blks_written": 0,
      "temp_blks_read": 0,
      "temp_blks_written": 0,
      "total_time": 2504295,
      "blk_read_time": 0,
      "blk_write_time": 0,
      "text": "DELETE FROM sbtest2 WHERE id=$1"
    },
    {
      "pg_instance": "pg-sales-3420@:9342",
      "database": "sales",
      "user": "sales_user",
      "query_md5_id": "8599d511ac1e7df8eec514b3ff1db635",
      "query_id": "3837882988",
      "calls": 264218627,
      "local_blks_dirtied": 0,
      "local_blks_hit": 0,
      "local_blks_read": 0,
      "local_blks_written": 0,
      "rows": 120,
      "shared_blks_dirtied": 259,
      "shared_blks_hit": 528437796,
      "shared_blks_read": 57,
      "shared_blks_written": 0,
      "temp_blks_read": 0,
      "temp_blks_written": 0,
      "total_time": 2535561,
      "blk_read_time": 0,
      "blk_write_time": 0,
      "text": "DELETE FROM sbtest1 WHERE id=$1"
    }, 
    .../...
  ]

**Queries summary**
*******************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/queries-summary</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/queries-summary' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-021-20",
      "to": "2020-02-21",
      "filters": [  {
              "tag": "pg_instance",
              "value": "pg-sales-1734@:9342"
            }
        ],      
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

    [
      {
        "pg_instance": "pg-sales-1734@:9342",
        "database": "postgres",
        "calls": 317120,
        "local_blks_dirtied": 0,
        "local_blks_hit": 0,
        "local_blks_read": 0,
        "local_blks_written": 0,
        "rows": 393531,
        "shared_blks_dirtied": 0,
        "shared_blks_hit": 369970,
        "shared_blks_read": 0,
        "shared_blks_written": 0,
        "temp_blks_read": 0,
        "temp_blks_written": 0,
        "total_time": 56147,
        "blk_read_time": 0,
        "blk_write_time": 0,
        "perc_90": 3,
        "perc_95": 11,
        "perc_99": 12
      },
      {
        "pg_instance": "pg-sales-1734@:9342",
        "database": "sales",
        "calls": 227101072,
        "local_blks_dirtied": 0,
        "local_blks_hit": 0,
        "local_blks_read": 0,
        "local_blks_written": 0,
        "rows": 3576859082,
        "shared_blks_dirtied": 3897894,
        "shared_blks_hit": 5333055541,
        "shared_blks_read": 25057,
        "shared_blks_written": 0,
        "temp_blks_read": 0,
        "temp_blks_written": 0,
        "total_time": 33701425,
        "blk_read_time": 0,
        "blk_write_time": 0,
        "perc_90": 1,
        "perc_95": 1,
        "perc_99": 1
      }
    .../...
  ]

**Query statistics**
********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/query</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/query' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "query_md5_id": "",
      "utc_time": true,
      "from": "2020-01-20",
      "to": "2020-01-21",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "output": "json"
    }

- Parameters:

    | "query_md5_id": The query id (md5 value) computed by Datasentinel
    |
    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

  [
    {
      "pg_instance": "pg-sales-2429@:9342",
      "database": "sales",
      "user": "sales_user",
      "query_md5_id": "617ec53d06c3f7138b3790c87ccb391e",
      "query_id": "1053048887",
      "calls": 264256688,
      "local_blks_dirtied": 0,
      "local_blks_hit": 0,
      "local_blks_read": 0,
      "local_blks_written": 0,
      "rows": 93,
      "shared_blks_dirtied": 159,
      "shared_blks_hit": 528514486,
      "shared_blks_read": 31,
      "shared_blks_written": 0,
      "temp_blks_read": 0,
      "temp_blks_written": 0,
      "total_time": 2504295,
      "blk_read_time": 0,
      "blk_write_time": 0,
      "text": "DELETE FROM sbtest2 WHERE id=$1"
    },
    {
      "pg_instance": "pg-sales-2429@:9342",
      "database": "sales",
      "user": "sales_user",
      "query_md5_id": "8599d511ac1e7df8eec514b3ff1db635",
      "query_id": "3837882988",
      "calls": 264218627,
      "local_blks_dirtied": 0,
      "local_blks_hit": 0,
      "local_blks_read": 0,
      "local_blks_written": 0,
      "rows": 120,
      "shared_blks_dirtied": 259,
      "shared_blks_hit": 528437796,
      "shared_blks_read": 57,
      "shared_blks_written": 0,
      "temp_blks_read": 0,
      "temp_blks_written": 0,
      "total_time": 2535561,
      "blk_read_time": 0,
      "blk_write_time": 0,
      "text": "DELETE FROM sbtest1 WHERE id=$1"
    }, 
    .../...
  ]

**PG instance informations**
****************************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/pg-instance-infos</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/pg-instance-infos' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-021-20",
      "to": "2020-02-21",
      "filters": [],
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

    [
      {
        "pg_instance": "pg-crm-0926@:9342",
        "tags": "{\"application\": \"crm\", \"datacenter\": \"lyon\", \"environment\": \"production\", \"provider\": \"azure\"}",
        "version": "11.6",
        "version_full": "PostgreSQL 11.6 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-39), 64-bit",
        "start_time": "2020-02-17 17:28:41",
        "uptime": "3 days 07:31:07",
        "server": "pg-crm-0926"
      },
      {
        "pg_instance": "pg-crm-1523@:9342",
        "tags": "{\"application\": \"crm\", \"datacenter\": \"lyon\", \"environment\": \"production\", \"provider\": \"azure\"}",
        "version": "11.6",
        "version_full": "PostgreSQL 11.6 on x86_64-pc-linux-gnu, compiled by gcc (GCC) 4.8.5 20150623 (Red Hat 4.8.5-39), 64-bit",
        "start_time": "2020-02-17 17:27:58",
        "uptime": "3 days 07:31:07",
        "server": "pg-crm-1523"
      },
    .../...
  ]

**PG instance activity**
************************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/pg-instance</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/pg-instance' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-29 06:00:00",
      "to": "2020-01-29 08:00:00 ",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "compute": "details",
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "compute" : optional field (default: details)
    |             2 possible values :
    |                 . summary : Overall activity per PostgreSQL instance
    |                 . details : Detailed activity per minute, per PostgreSQL instance
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

  [
    {
      "time": "2020-01-29 06:00:00",
      "pg_instance": "pg-sales-0223@:9342",
      "database": "all",
      "blk_read_time": 0,
      "blk_write_time": 0,
      "blks_hit": 24695,
      "blks_read": 0,
      "num_backends": 55,
      "temp_bytes": 0,
      "temp_files": 0,
      "tup_deleted": 0,
      "tup_fetched": 11455,
      "tup_inserted": 0,
      "tup_returned": 27885,
      "tup_updated": 0,
      "xact_commit": 1679,
      "xact_rollback": 35
    },
    {
      "time": "2020-01-29 06:01:00",
      "pg_instance": "pg-sales-0223@:9342",
      "database": "all",
      "blk_read_time": 0,
      "blk_write_time": 0,
      "blks_hit": 24764,
      "blks_read": 0,
      "num_backends": 55,
      "temp_bytes": 0,
      "temp_files": 0,
      "tup_deleted": 0,
      "tup_fetched": 11466,
      "tup_inserted": 0,
      "tup_returned": 29059,
      "tup_updated": 0,
      "xact_commit": 1681,
      "xact_rollback": 35
    },
    .../...
  ]

**PG background activity**
**************************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/pg-background</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/pg-background' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-29 06:00:00",
      "to": "2020-01-29 08:00:00 ",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "compute": "summary",
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "compute" : optional field (default: details)
    |             2 possible values :
    |                 . summary : Overall activity per PostgreSQL instance
    |                 . details : Detailed activity per minute, per PostgreSQL instance
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

    [
      {
        "time": "2020-01-29 06:00:00",
        "pg_instance": "pg-sales-0223@:9342",
        "buffers_alloc": 0,
        "buffers_backend": 0,
        "buffers_backend_fsync": 0,
        "buffers_checkpoint": 0,
        "buffers_clean": 0,
        "checkpoint_sync_time": 0,
        "checkpoint_write_time": 0,
        "checkpoints_req": 0,
        "checkpoints_timed": 1
      },
      {
        "time": "2020-01-29 06:01:00",
        "pg_instance": "pg-sales-0223@:9342",
        "buffers_alloc": 0,
        "buffers_backend": 0,
        "buffers_backend_fsync": 0,
        "buffers_checkpoint": 0,
        "buffers_clean": 0,
        "checkpoint_sync_time": 0,
        "checkpoint_write_time": 0,
        "checkpoints_req": 0,
        "checkpoints_timed": 4
      },
    .../...
  ]

**Server activity**
*******************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/server</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/server' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-29 06:00:00",
      "to": "2020-01-29 08:00:00 ",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "compute": "summary",
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "compute" : optional field (default: details)
    |             2 possible values :
    |                 . summary : Overall activity per PostgreSQL instance
    |                 . details : Detailed activity per minute, per PostgreSQL instance
    |
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

    [
      {
        "time": "2020-01-29 06:00:36",
        "server": "pg-sales-0223",
        "cpu_model": "AMD EPYC 7281 16-Core Processor",
        "cores": 2,
        "cpus": 2,
        "os_idle": 0.03,
        "os_iowait": 0,
        "os_nice": 0,
        "os_system": 14,
        "os_user": 85.5,
        "load_avg_1m": 2.48,
        "mem_active": 1043222528,
        "mem_available": 1237970944,
        "mem_buffers": 136032256,
        "mem_cached": 1352306688,
        "mem_free": 107945984,
        "mem_inactive": 642015232,
        "mem_perc": 35.7,
        "mem_shared": 134320128,
        "mem_total": 1923837952,
        "mem_used": 327553024,
        "bytes_recv": 1059046,
        "bytes_sent": 1106510,
        "packets_recv": 3207,
        "packets_sent": 3225,
        "read_bytes": 0,
        "read_count": 0,
        "read_time": 0,
        "write_bytes": 856064,
        "write_count": 90,
        "write_time": 303,
        "swap_free": 0,
        "swap_in": 0,
        "swap_out": 0,
        "swap_perc": 0,
        "swap_total": 0,
        "swap_used": 0
      },
      {
        "time": "2020-01-29 06:01:36",
        "server": "pg-sales-0223",
        "cpu_model": "AMD EPYC 7281 16-Core Processor",
        "cores": 2,
        "cpus": 2,
        "os_idle": 17.98,
        "os_iowait": 0.01,
        "os_nice": 0,
        "os_system": 11,
        "os_user": 70.81,
        "load_avg_1m": 2.11,
        "mem_active": 1043349504,
        "mem_available": 1237643264,
        "mem_buffers": 136040448,
        "mem_cached": 1352425472,
        "mem_free": 107491328,
        "mem_inactive": 642011136,
        "mem_perc": 35.7,
        "mem_shared": 134320128,
        "mem_total": 1923837952,
        "mem_used": 327880704,
        "bytes_recv": 1067069,
        "bytes_sent": 1110658,
        "packets_recv": 3216,
        "packets_sent": 3242,
        "read_bytes": 0,
        "read_count": 0,
        "read_time": 0,
        "write_bytes": 765952,
        "write_count": 73,
        "write_time": 145,
        "swap_free": 0,
        "swap_in": 0,
        "swap_out": 0,
        "swap_perc": 0,
        "swap_total": 0,
        "swap_used": 0
      },
    .../...
  ]

**Data size**
*************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/data-size</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/data-size' -d @body.json

- Request example (body.json)

.. code:: bash

    {
      "utc_time": true,
      "from": "2020-01-29 06:00:00",
      "to": "2020-01-29 08:00:00 ",
      "filters": [
        {
          "tag": "pg_instance",
          "value": "pg-sales-0223@:9342"
        }
      ],
      "compute": "summary,
      "output": "json"
    }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | "compute" : optional field (default: details)
    |             2 possible values :
    |                 . summary : Overall activity per PostgreSQL instance
    |                 . details : Detailed activity per hour, per PostgreSQL instance
    | "output":  the output can be csv or json (default: json)

- Response

.. code:: bash

  [
    {
      "time": "2020-01-29 06:04:49",
      "application": "sales",
      "database": "pgbench",
      "datacenter": "paris",
      "environment": "production",
      "pg_instance": "pg-sales-0223@:9342",
      "pg_version": "10.11",
      "provider": "amazon",
      "server": "pg-sales-0223",
      "data_size": 337042567
    },
    {
      "time": "2020-01-29 06:04:49",
      "application": "sales",
      "database": "postgres",
      "datacenter": "paris",
      "environment": "production",
      "pg_instance": "pg-sales-0223@:9342",
      "pg_version": "10.11",
      "provider": "amazon",
      "server": "pg-sales-0223",
      "data_size": 7773319
    },
    {
      "time": "2020-01-29 06:04:49",
      "application": "sales",
      "database": "sales",
      "datacenter": "paris",
      "environment": "production",
      "pg_instance": "pg-sales-0223@:9342",
      "pg_version": "10.11",
      "provider": "amazon",
      "server": "pg-sales-0223",
      "data_size": 296483975
    },
    .../...
  ]

**Tables activity**
*******************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/tables</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/tables' -d @body.json

- Request example (body.json)

.. code:: bash

  {
    "utc_time": true,
    "from": "2020-01-29 06:00:00",
    "to": "2020-01-29 07:00:00",
    "filters": [ 
      { "tag": "pg_instance", "value": "pg-crm-2429@:9342" }
      ],
    "limit": 40,
    "by": "idx_blks_hit",
    "output": "json"
  }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | The 2 following parameters allow to define the sorting column as well as the number of rows returned
    |
    | "by": sorting column. (default heap_blks_hit)
    | Can be one of thoses values:
    | - heap_blks_hit, heap_blks_read, idx_blks_hit, idx_blks_read, idx_scan, 
    | - n_tup_del, n_tup_hot_upd, n_tup_ins, idx_tup_fetch, 
    | - n_tup_upd, relid, relkind, relpages, reltuples, seq_scan, seq_tup_read, 
    | - size, tidx_blks_hit, tidx_blks_read, toast_blks_hit, toast_blks_read,
    | - vacuum_count, autovacuum_count, analyze_count, autoanalyze_count
    | 
    | "limit": The number of rows returned (default 20)
    |
    | "output":  the output can be json or csv (default json)

- Response

.. code:: bash

  [
    {
      "pg_instance": "pg-crm-2429@:9342",
      "database": "crm",
      "schema_name": "public",
      "rel_name": "sbtest2",
      "heap_blks_hit": 102,
      "heap_blks_read": 3,
      "idx_blks_hit": 550977207,
      "idx_blks_read": 0,
      "idx_scan": 275488514,
      "idx_tup_fetch": 37,
      "n_tup_del": 37,
      "n_tup_hot_upd": 0,
      "n_tup_ins": 0,
      "n_tup_upd": 0,
      "relid": 16423,
      "relkind": "r",
      "relpages": 2703,
      "reltuples": 29703,
      "seq_scan": 0,
      "seq_tup_read": 0,
      "size": 22142976,
      "tidx_blks_hit": 0,
      "tidx_blks_read": 0,
      "toast_blks_hit": 0,
      "toast_blks_read": 0,
      "vacuum_count": 0,
      "autovacuum_count": 0,
      "analyze_count": 0,
      "autoanalyze_count": 0,
      "last_autoanalyze": "2020-01-07 03:12:09",
      "last_autovacuum": "2020-02-01 18:58:10"
    },
    {
      "pg_instance": "pg-crm-2429@:9342",
      "database": "crm",
      "schema_name": "public",
      "rel_name": "sbtest1",
      "heap_blks_hit": 108,
      "heap_blks_read": 6,
      "idx_blks_hit": 550930476,
      "idx_blks_read": 0,
      "idx_scan": 275465166,
      "idx_tup_fetch": 46,
      "n_tup_del": 46,
      "n_tup_hot_upd": 0,
      "n_tup_ins": 0,
      "n_tup_upd": 0,
      "relid": 16411,
      "relkind": "r",
      "relpages": 2703,
      "reltuples": 30260,
      "seq_scan": 0,
      "seq_tup_read": 0,
      "size": 22142976,
      "tidx_blks_hit": 0,
      "tidx_blks_read": 0,
      "toast_blks_hit": 0,
      "toast_blks_read": 0,
      "vacuum_count": 0,
      "autovacuum_count": 0,
      "analyze_count": 0,
      "autoanalyze_count": 0,
      "last_autoanalyze": "2020-01-03 05:50:51",
      "last_autovacuum": "2020-01-27 17:17:09"
    },
    .../...
  ]

**Indexes activity**
********************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/indexes</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/indexes' -d @body.json

- Request example (body.json)

.. code:: bash

  {
    "utc_time": true,
    "from": "2020-01-29 06:00:00",
    "to": "2020-01-29 07:00:00",
    "filters": [ 
      { "tag": "pg_instance", "value": "pg-crm-2429@:9342" }
      ],
    "limit": 40,
    "by": "idx_blks_hit",
    "output": "json"
  }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | The 2 following parameters allow to define the sorting column as well as the number of rows returned
    |
    | "by": sorting column. (default heap_blks_hit)
    | Can be one of thoses values:
    | - idx_blks_hit, idx_blks_read, idx_scan, 
    | - idx_tup_fetch, idx_tup_read 
    | - relpages, size
    | 
    | "limit": The number of rows returned (default 20)
    |
    | "output":  the output can be json or csv (default json)

- Response

.. code:: bash

  [
    {
      "pg_instance": "pg-crm-2429@:9342",
      "database": "crm",
      "schema_name": "public",
      "rel_name": "sbtest2",
      "index_rel_name": "sbtest2_pkey",
      "idx_blks_hit": 550977159,
      "idx_blks_read": 0,
      "idx_scan": 275488514,
      "idx_tup_fetch": 37,
      "idx_tup_read": 38,
      "relpages": 278,
      "size": 2277376
    },
    {
      "pg_instance": "pg-crm-2429@:9342",
      "database": "crm",
      "schema_name": "public",
      "rel_name": "sbtest1",
      "index_rel_name": "sbtest1_pkey",
      "idx_blks_hit": 550930428,
      "idx_blks_read": 0,
      "idx_scan": 275465166,
      "idx_tup_fetch": 46,
      "idx_tup_read": 52,
      "relpages": 278,
      "size": 2277376
    },
    .../...
    ]

**Top consumers**
*****************

.. raw:: html

   <h6 ><span style="margin-left:30px;font-weight:bold;color: #45d6b5">POST</span><span style="color:#45d6b5">&nbsp;/ds-api/activity/top-consumers</span></h6>

- Example 

.. code:: bash

  export TOKEN=<<user_token>>
  curl -k --header "user-token: $TOKEN" --header 'Content-Type: application/json' --request POST 'https://app.datasentinel.io/ds-api/activity/top-consumers' -d @body.json

- Request example (body.json)

.. code:: bash

  {
    "utc_time": true,
    "from": "2020-01-29 06:00:00",
    "to": "2020-01-29 07:00:00",
    "filters": [ 
      { "tag": "pg_instance", "value": "pg-crm-2429@:9342" }
      ],
    "limit": 10,
    "group_by": "datacenter",
    "by": "db_time",
    "output": "json"
  }

- Parameters:

    | "utc_time" [Optional] Default: true
    |  When false , the timezone taken into account will depend on the timezone of the platform  
    |
    | "from": The start date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    | "end":  The end date. The format can be YYYY-MM-DD, YYYY-MM-DD HH:MI, YYYY-MM-DD HH:MI:SS
    |
    | "filters" is an optional array of tags ("tag" : Tag name, "value": Tag value) 
    |
    | The 3 following parameters allow to define the group, the sorting column as well as the number of rows returned
    |
    | "group_by": tag group. (default pg_instance)
    |  Can be one of defined tags.
    |
    | "by": sorting column. (default db_time)
    | Can be one of thoses values:
    | - db_time : Total time (ms) spent executing sqls, 
    | - memory : Total of memory (bytes) allocated (shared_buffers), 
    | - data_size : Total data size (bytes), 
    | - wal_size : Total size of WAL generated (bytes),
    | - cache_blocks_hit : Total number of blocks hit from cache
    | - disk_blocks_read : Total number of blocks read outside the PostgreSQL cache
    | 
    | "limit": The number of rows returned (default 20)
    |
    | "output":  the output can be json or csv (default json)

- Response

.. code:: bash

  [
    {
      "tag": "paris",
      "instances": 3,
      "db_time": 239673553,
      "wal_size": 52053547328,
      "memory_size": 49152,
      "data_size": 942975786,
      "cache_blocks_hit": 39601119635,
      "disk_blocks_read": 3897687
    },
    {
      "tag": "lille",
      "instances": 3,
      "db_time": 193989446,
      "wal_size": 85274148792,
      "memory_size": 49152,
      "data_size": 931415688,
      "cache_blocks_hit": 16088607267,
      "disk_blocks_read": 5931946
    },
    .../...
  ]