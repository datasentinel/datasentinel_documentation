******************
Release notes
******************

**Feb 01, 2021 (v2021.02)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. | Datasentinel introduces its new Live360° feature:
   | 
   | Thanks to direct connections, this feature provides precision and additional information on the context, which will offer you a valuable and indispensable help during your performance analyzes
   | - Current and blocking sessions
   | - Relations Explorer to view statistics in detail (tables, indexes, columns, extended statistics, ...)
   | - Disk and memory cache usage
   | - Generate execution plans from any query and analyze them thanks to our execution plan visualizer
   | - In progress reporting (Vacuum, analyze, create index, ...)
   |
   | See :ref:`live_360` Documentation
   |
   | View our demo video

   .. image:: ./images/youtubeLogo.png
      :alt: Live360 user
      :align: center
      :target: https://youtu.be/28xODT1j9GI


**Dec 09, 2020 (v2020.12)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. | Datasentinel can retrieve system metrics with the :ref:`agentless_feature` method if you install the :ref:`system_stats` extension 
2. | Easily display the most frequently used Tables or Indexes (By disk reads, Cache activity or any other metric)
3. | New version name convention


**May 11, 2020 (v1.6.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. | New **Agentless** version allowing you to monitor all kinds of PostgreSQL instances
   | - AWS RDS, Aurora 
   | - Microsoft Azure database, hyperscale, 
   | - Google Cloud SQL and other cloud providers. 
   | 
   | It can also be used in your own environment. (See which method to use :ref:`agentless`
   | 
   | Connections can be created either with the :ref:`connection_management`
   | or with the :ref:`connection_api`

.. _connection_management:

User interface connection management
************************************

.. image:: images/agentless.gif
   :alt: connection management
   :width: 100%
   :align: center

**March 30, 2020 (v1.5.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. | Added Reporting. (Here is an example :download:`pdf <features/workload_example.pdf>`)
   | :ref:`export workload`
   | You can also generate your report with :ref:`api`
2. The Datasentinel extension is no longer required. (Required only when you choose the **high** level of collection). See :doc:`features/sessions-workload`

.. raw:: html

   <h3>Fixes</h3>

- Fix pagination on some dashboards in the UI. 

.. _export workload:


Export your workload in PDF format
**********************************
    Select a PostgreSQL instance, a time window and the sections to export.  

.. image:: images/export_workload.gif
   :alt: Export workload in PDF format
   :width: 100%
   :align: center

**February 18, 2020 (v1.4.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. Added API to export metrics. See :ref:`api`
2. :ref:`export metrics`
3. Query statistics display the minum and maximum execution time
4. Session workload sampling can be low (every 10 seconds) or high (every second). Updatable with the :ref:`agent`

.. raw:: html

   <h3>Fixes</h3>

- Fix layout in the top queries dashboard 
- Fix tab layout in the instance dashboard 

.. _export metrics:


The metrics can now be downloaded directly from the UI
**********************************************************
    JSON or CSV format 

.. image:: images/feature_export_metrics.gif
   :alt: Download metrics
   :width: 100%
   :align: center

**January 14, 2020 (v1.3.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

:ref:`plan viewer`

:ref:`index usage`

.. raw:: html

   <h3>Fixes</h3>

- In the Top queries dashboard, labels display the sql text (truncated if needed) instead of the query md5 id.


.. _plan viewer:

1. Execution plan viewer
************************
The execution plans can be easily analyzed thanks to the plan viewer feature. 

    You can copy/paste an existing plan (format text or json) or view it directly in the execution plans dashboard

.. image:: images/execution_plan.gif
   :alt: PostgreSQL Execution plans
   :width: 100%
   :align: center


.. _index usage:

2. Index usage statistics
**************************

Index usage statistics are now available. You can see what are the most used indexes.

.. image:: images/index_statistics.gif
   :alt: PostgreSQL indexes usage statistics
   :width: 100%
   :align: center

.. raw:: html

   <h3>Fixes</h3>

- In the Top queries dashboard, labels display the sql text (truncated if needed) instead of the query md5 id.

**December 19, 2019 (v1.2.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. raw:: html

   <h3>Features</h3>

:ref:`starred instances`

:ref:`instance tags`

.. raw:: html

   <h3>Fixes</h3>

- When updating a user email, the user properties are lost
- Home page reload does not work properly in some cases

.. _starred instances:

1. Starred instances
********************
The postgresql instances can be starred. You can choose to see your starred instances only 

.. image:: images/feature_starred.gif
   :alt: Starred instances
   :width: 100%
   :align: center

.. _instance tags:


2. Instance tags:
******************
The instance tags can be displayed in the home page and in the instances dashboard. You can then easily filter by tag

.. image:: images/feature_tags.gif
   :alt: Starred instances
   :width: 100%
   :align: center

.. raw:: html

   <h3>Fixes</h3>



**November 12, 2019 (v1.1.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

1. Upgrade to grafana 6.4.4
2. Developer or data admin user profile. A developer profile has only access to sessions workload and queries

.. raw:: html

   <h3>Fixes</h3>

- Query id with unkonwn filters


**October 2019 (v1.0.0)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. raw:: html

   <h3>Features</h3>

- Sessions workload
- Sqls statistics
- Instances, databases statistics
- Powerfull filters
- Consolidated or detailed view of the activity
- Real time or past view with zooming feature on the desired periods
