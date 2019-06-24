***************
Troubleshooting
***************

You have installed the agent , configured a postgresql instance and you don't see the instance in the user interface.
Follow these steps to identify the root cause.

.. raw:: html

   <h1>1. On the local machine where the agent is installed</h1>

Check the agent status and the uploaded server
************************************************

.. code-block:: bash

   datasentinel status agent

.. code-block:: text

          Agent
             Version : 1.9.3                                             
                Port : 8282                                              
          Start time : 2020-02-07 13:08:08                               
     Collection rate : high                                              

          Proxy
                host :                                                   
                port : 0                                                 
                user :                                                   
            password :                                                   

         Upload
                host : 51.15.236.159                                     
                port : 443                                               

    Connections
            declared : 1                                                 
             running : 1                                                 
         not running : 0                                                 



Check the token is not expired
********************************

.. code-block:: bash

   datasentinel show token

.. code-block:: text


               Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODM2OTUyNzcsImlhdCI6MTU3NjM1MTI3MiwiZGF0YWJhc2UiOiJkcy1kYXRhIn0.UQRxutKrJv7WVAaHCN3Fh_wnXJLst54s93lADIP_n-Y

        Organization : ds-data                                           
     Expiration Date : 2020-03-08 19:21:17                               


Check the connections
***********************

.. code-block:: bash

   datasentinel show connections

.. code-block:: text

    name                 status     state      host                 port   user           
    --------------------------------------------------------------------------------
    :9342                enabled    running    pg-sales-1734          9342 datasentinel   
    tags : application=sales,environment=production,provider=amazon,datacenter=lyon        

Check the agent log file
************************

| The agent writes all its actions in the file **datasentinel.log** located in the subdirectory **log**

You should not see any ERROR

.. code-block:: text

    2019-12-15 15:54:13,021 - datasentinel - INFO - Agent metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:13,041 - datasentinel - INFO - pg_store_plans size : 20
    2019-12-15 15:54:13,042 - datasentinel - INFO - Interval stats cache size : 173 
    2019-12-15 15:54:13,110 - datasentinel - INFO - PG Server metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:19,742 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:19,810 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:29,823 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:29,893 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:39,879 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:39,965 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:49,980 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:54:50,073 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443
    2019-12-15 15:55:00,075 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:55:00,201 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443
    2019-12-15 15:55:09,209 - datasentinel - INFO - Active sessions metrics sent to https://51.158.110.62:443
    2019-12-15 15:55:09,285 - datasentinel - INFO - PG status metrics sent to https://51.158.110.62:443

.. raw:: html

   <h1>2. On the machine where the platform is installed</h1>

Check the log files
***********************

| All log files are located in the directory **/datasentinel/log**
| The file **backend_to_influx.log** shows the metrics sent by agents to the InfluxDB database.


.. code-block:: text

    2019-12-15 14:48:15 - backend_to_influx - INFO - Write 39451 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.015501
    2019-12-15 14:48:24 - backend_to_influx - INFO - Write 39340 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.869292
    2019-12-15 14:48:24 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.008472
    2019-12-15 14:48:33 - backend_to_influx - INFO - Write 37104 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.027474
    2019-12-15 14:48:33 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.008452
    2019-12-15 14:48:43 - backend_to_influx - INFO - Write 43914 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.020828
    2019-12-15 14:48:43 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.009041
    2019-12-15 14:48:53 - backend_to_influx - INFO - Write 38204 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.017448
    2019-12-15 14:48:53 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.007804
    2019-12-15 14:49:03 - backend_to_influx - INFO - Write 33644 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.029447
    2019-12-15 14:49:03 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.016561
    2019-12-15 14:49:13 - backend_to_influx - INFO - Write 38292 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.024353
    2019-12-15 14:49:13 - backend_to_influx - INFO - Write 253 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.009062
    2019-12-15 14:49:15 - backend_to_influx - INFO - Write 1432 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.014299
    2019-12-15 14:49:15 - backend_to_influx - INFO - Write 39443 bytes from 51.158.106.191 to influxdb - database ds-data in 0:00:00.013594
