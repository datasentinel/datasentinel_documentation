.. _live_360:

******************
Live 360°
******************

Datasentinel provides this module thanks to direct connections to PostgreSQL instances via the agents. 

.. image:: ../images/youtubeLogo.png
   :alt: Live360 user
   :align: center
   :target: https://youtu.be/28xODT1j9GI

.. note::

    | Live360° is the only module that connects directly to PostgreSQL instances. 
    | The other analysis dashboards retrieve data from the repository.

.. raw:: html 

    <h4>You can enable or disable this feature for each datasentinel user</h4>

.. image:: ../images/userLiveEnabled.png
   :alt: Live360 user
   :align: center


.. warning::

    | If you use local agents, you must have at least version **2.5.0** of the agent


.. raw:: html 

    <h4>Live360° allows you to </h4>

- Analyze :ref:`current_sessions`
- Quickly detect :ref:`blocking_sessions`
- :ref:`explorer` 
- :ref:`progress_reporting`
- View current settings
- Generate :ref:`execution_plans` from any query and analyze them thanks to our execution plan visualizer
- View the :ref:`disk_usage` consumed by the databases and relations
- Analyze the :ref:`cache_usage` to explore the shared buffers cache (needs the extension `pg_buffercache <https://www.postgresql.org/docs/12/pgbuffercache.html>`_)


.. _current_sessions:

Current sessions
================

You can choose your database or all , filter only active sessions and show queries.

.. image:: ../images/currentSessionsToolbar.png
   :alt: Live360 user
   :align: center

From left to right, the above indicators are
    - Number of active sessions
    - Number of connected sessions
    - Database activity graph : Are the sessions on CPU, waiting, ... ?
    - Number of currently blocked sessions 

You can explore the details of a session by clicking on it.

.. image:: ../images/currentSessions.gif
   :alt: PostgreSQL current sessions
   :width: 100%
   :align: center


.. _blocking_sessions:


Blocking sessions
=================

The screen shows you the blocking sessions as well as the blocked sessions.
The blockers are identified by a green padlock. You can explore the details of a session by clicking on it.

You can kill the sesion directly from the interface.

.. note::

    | To be able to kill a session, the user connected to the interface must have the privilege "read write" (See :ref:`user-management`)

.. image:: ../images/blockingSessions.gif
   :alt: PostgreSQL blocking sessions
   :width: 100%
   :align: center


.. _explorer:


Explore Relation statistics
============================

Select your database, the schema,  then choose the relation type between
    - Table
    - Index
    - Materialized view
    - Foreign table
    - View
    - Extended Statistics
    - Extension
    - Function / Proc
    - Sequence
    - TOAT table



Example of displayed elements for a table
    - Columns statistics
    - Partitions
    - Indexes
    - Constraints
    - Options
    - Extended statistics
    - TOAST

.. note::

    | To be able to view some internal statistics (pg_statistic_ext, pg_stats), the PostgreSQL user used by datasentinel needs to have specific rigths.
    | 
    | Example of grant: 
    | GRANT SELECT ON ALL TABLES IN SCHEMA pg_catalog TO datasentinel; 


.. image:: ../images/explorer.gif
   :alt: PostgreSQL relation statistics explorer
   :width: 100%
   :align: center


.. _execution_plans:

Execution plans
===============

Select your database and generate an execution plan from any query.

| You can choose the **ANALYZE** option to execute the query in order to have its overall and step by step execution time statistics.
| The output can be text or json
| The execution plan viewer makes it easy and quick to understand each step.

.. warning::

    | **ANALYZE** option is only available for SELECT statements

.. note::

    | When choosing **ANALYZE**, specify a timeout to set the maximum allowed execution time of the query


.. image:: ../images/executionPlans.gif
   :alt: PostgreSQL query execution plans
   :width: 100%
   :align: center

.. _progress_reporting:


Progress reporting
===================

Follow the progress of current operations

All versions:
    -  VACUUM

Since PostgreSQL 12
    - CREATE INDEX
    - CLUSTER or VACUUM FULL

Since PostgreSQL 13
    - ANALYZE 


.. image:: ../images/progress_reporting.gif
   :alt: PostgreSQL progress reporting
   :width: 100%
   :align: center


.. _disk_usage:


Disk usage
==========

Disk usage lets you explore the space consumed by relations.

You can choose to view the space used for each database or all

Result can be grouped by
    - relations
    - schemas
    - tablespaces

.. image:: ../images/diskUsage.gif
   :alt: PostgreSQL relation disk Usage
   :width: 100%
   :align: center

.. _cache_usage:


Cache usage
============

Cache usage lets you explore the space consumed by relations in memory (shared_buffers)

.. note::

    | To use this feature, you need to install the extension **pg_buffercache** in all databases of your instance

You can choose to view the space used for each database or all

.. image:: ../images/cacheUsage.gif
   :alt: PostgreSQL relation disk Usage with pg_buffercache extension
   :width: 100%
   :align: center

