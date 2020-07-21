******************
pg_stat_statements
******************

.. note::
   | This extension is part of the official PostgreSQL contrib package `See Documentation <https://www.postgresql.org/docs/current/pgstatstatements.html>`_
   | 
   | Datasentinel needs this extension

**Installation**
****************

1. Modify postgresql.conf
*************************

- Add the following lines

.. code-block:: bash

   shared_preload_libraries = 'pg_stat_statements'
   track_activity_query_size = 2048
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
