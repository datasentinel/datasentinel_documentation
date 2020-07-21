******************
Execution plans
******************

.. note::
   | There are 2 differents ways of viewing execution plans with Datasentinel
   | - in live sessions dashboard
   | - in query history dashboard if the **pg_store_plans** extension is installed


**Extension**
*************

**PG_STORE_PLANS** store execution plans like **PG_STAT_STATEMENTS** does for queries.

.. note::
   | This extension is **OPTIONAL**
   | Datasentinel automatically takes it into account if it is installed


When it is installed, you have acces to 
 - Historical statistics of each plan for a query id     
 - Execution plans

See http://pgstoreplans.osdn.jp/pg_store_plans.html for more details.


**Installation**
****************

1. Download source files
************************

The extension can be downloaded here https://github.com/datasentinel/pg_store_plans


2. Compile and deploy
*********************

- Version < 9.6 (example done with 9.4)

.. code-block:: bash

   export PATH=/usr/pgsql-9.4/bin:$PATH

- Version 9.6

.. code-block:: bash

   export PATH=/usr/pgsql-9.6/bin:$PATH

- Version 10

.. code-block:: bash

   export PATH=/usr/pgsql-10/bin:$PATH

- Version 11

.. code-block:: bash

   export PATH=/usr/pgsql-11/bin:$PATH

- Version 12

.. code-block:: bash

   export PATH=/usr/pgsql-12/bin:$PATH

- All

.. code-block:: bash

   cd pg_store_plans
   export USE_PGXS=true
   make
   make install


3. Modify postgresql.conf
*************************

- Add the following lines

.. note::
   | Add **pg_store_plans** to **shared_preload_libraries** parameter

.. code-block:: bash

    pg_store_plans.log_analyze = false
    pg_store_plans.log_timing = false
    pg_store_plans.max=1000
    pg_store_plans.track=all
    pg_store_plans.plan_format=text
    pg_store_plans.min_duration=0
    pg_store_plans.log_buffers=false
    pg_store_plans.log_triggers=false
    pg_store_plans.verbose=false
    pg_store_plans.save=false

4. Restart postgresql
*********************

5. Create the extensions
************************

- connect as a superuser

.. code-block:: bash

    CREATE EXTENSION pg_store_plans;
