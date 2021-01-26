.. _user-management:

******************
User management
******************

.. note::
   | Datasentinel enables fine user management. 
   | You can create, drop users and affect them specific profiles and privileges
   |


Privileges
***********

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

Profiles
********

2 profiles are available. A profile needs to be assigned to a user

+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Profile                               | Description                                                                                      |
+=======================================+==================================================================================================+
| developer                             | - Access limited to sessions workload and top queries features                                   |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| data admin                            | - Access unlimited                                                                               |
+---------------------------------------+--------------------------------------------------------------------------------------------------+


Role based access
*****************

.. note::
   | The feature allows you to restrict access to a subset of the perimeter of your PostgreSQL instances. 


You define roles with specific filters (Server, PG instance, datacenter, application, environment, etc, ...) and assign them to your users.

