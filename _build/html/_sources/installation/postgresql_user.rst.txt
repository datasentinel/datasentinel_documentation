.. _postgresql-user:

***************
Postgresql user 
***************

Prerequisite
************

.. warning::
   For versions less than 10, the user must have the role superuser

- Version 9.4, 9.5, 9.6

.. code-block:: bash

   create user datasentinel password 'myPassword';
   alter user datasentinel with superuser;

- Version 10, 11, 12, 13

.. code-block:: bash

   create user datasentinel password 'myPassword';
   grant pg_monitor,pg_read_all_settings,pg_read_all_stats to datasentinel;


pg_hba.conf
**************

- Add authorization for the user datasentinel to connect to all databases with a password

.. code-block:: bash

   # TYPE  DATABASE        USER            ADDRESS                 METHOD
   host    all             datasentinel    127.0.0.1/0             md5

.. note::
   | The user needs to be able to connect to all databases.

- Reload the configuration

SSL connection
**********************

.. warning::
   | Only Available for Agentless connections

You can configure Datasentinel to use SSL connections to your PostgreSQL instances

Here are the steps to follow:

- Go to Agentless Settings 

- Your connection name must begin with **ssl**. (example ssl_crm_production)

- Copy the certificates to the **/datasentinel/ssl** directory of the platform

- The name of the certificate files must be standardized starting with the name of the connection, as below

Example:

.. code-block:: bash

   /datasentinel/ssl/ssl_crm_production_root.crt
   /datasentinel/ssl/ssl_crm_production_postgresql.crt
   /datasentinel/ssl/ssl_crm_production_postgresql.key
