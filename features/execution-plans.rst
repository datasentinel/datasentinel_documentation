.. _pg_store_plans:


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

.. warning::
   | To be installed in the **postgres** database.
   
When it is installed, you have acces to 
 - Historical statistics of each plan for a query id     
 - Execution plans

See http://pgstoreplans.osdn.jp/pg_store_plans.html for more details.


**Installation**
****************

1. Download source files
************************

The extension can be downloaded here https://github.com/datasentinel/pg_store_plans

.. warning::
   | For a version < 10, download the version 1.3.1 https://github.com/ossc-db/pg_store_plans/archive/1.3.1.tar.gz

2. Compile and deploy
*********************

Ensure you have set the PATH variable to your PostgreSQL installation directory 

.. code-block:: bash

   export PATH=<<POSTGRESQL_DIRECTORY>>/bin:$PATH

.. note::
   | The **pg_config** command should be OK

- Then compile the extension

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

5. Create the extension
************************

- connect as a superuser

.. code-block:: bash

    CREATE EXTENSION pg_store_plans;
