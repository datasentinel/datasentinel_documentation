.. _pg_stat_statements:


******************
pg_stat_statements
******************

.. note::
   | This extension is part of the official PostgreSQL contrib package `See Documentation <https://www.postgresql.org/docs/current/pgstatstatements.html>`_
   | 
   | Datasentinel needs this extension

.. warning::
   | To be installed in the **postgres** database.
   

**Installation**
****************

1. Modify postgresql.conf
*************************

- Add the following lines

.. code-block:: bash

   shared_preload_libraries = 'pg_stat_statements'
   track_activity_query_size = 65536
   pg_stat_statements.track = all

.. warning::

   | If you see lots of utility commands (other than SELECT, INSERT, UPDATE, DELETE),
   | you can disable their collect by setting this parameter:
   |
   | pg_stat_statements.track_utility = off


2. Reload conf
**************

- connect as a superuser

.. code-block:: bash

   SELECT pg_reload_conf();

3. Create the extension
************************

- connect as a superuser

.. code-block:: bash

    CREATE EXTENSION pg_stat_statements;

4. Check the extension
************************

.. code-block:: bash

    SELECT current_database(), extname from pg_extension where extname ='pg_stat_statements';
    current_database |      extname       
    ------------------+--------------------
    postgres         | pg_stat_statements
    (1 row)

