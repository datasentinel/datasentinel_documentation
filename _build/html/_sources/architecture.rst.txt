.. _architecture:

*****************************
Which architecture to choose?
*****************************

.. note::

    | Datasentinel can be used **On-Premises** or in **SaaS** mode with or without an agent
    | Its flexibility alllows you to always find an architecture that suits you
    | 
    | It is also available on the `AWS Marketplace <https://aws.amazon.com/marketplace/pp/B08L436C4Q>`_

**The platform is made up of several components**

    - The timeseries database `InfluxDB <https://www.influxdata.com>`_ to store metrics
    - The visualization software  `Grafana <https://grafana.com>`_  with a PostgreSQL database as a backend
    - The Datasentinel platform composed of
        - Frontend and Backend application
        - API
        - Agents


**PostgreSQL target Prerequisites**
    - Version >= 9.4
    - Extension pg_stat_statements (See :ref:`extensions`)



1. On-Premises Architecture
***************************

To install the **On-premises** platform, it is preferable to have a dedicated machine running on **Linux Centos 7+** or equivalent.  

You can also deploy several platforms if needed.

The size of the machine will depend on the number of instances to monitor and the retention period.

See our :ref:`global_faq`

Default recommendation:

+---------------+--------------+--------------+--------------+
| Instances     | CPUs         | Memory       | Storage      |
+===============+==============+==============+==============+
| 1-25          | 4            | 16GB         | 50GB         |
+---------------+--------------+--------------+--------------+
| 25-50         | 8            | 32GB         | 100GB        |
+---------------+--------------+--------------+--------------+
| 51-100        | 8            | 64GB         | 200GB        |
+---------------+--------------+--------------+--------------+
| 101-150       | 16           | 64GB         | 350GB        |
+---------------+--------------+--------------+--------------+
| >151          | 32           | 128GB        | 500GB        |
+---------------+--------------+--------------+--------------+

You can use either the **Agent-based** or **AgentLess** or both methods to load metrics. See :ref:`agentless`

**Hybrid architecture example**

.. image:: images/on-premises.png
   :align: center
   :alt: PostgreSQL performance monitoring tool Datasentinel On-premises hybrid Architecture
   :width: 100%


.. note::
    | `Getting started with Datasentinel on-premises <https://www.datasentinel.io/blog/post/start/>`_ blog and complete documentation :ref:`on_prem_installation`


2. Saas Architecture
********************


.. note::

    | In **SaaS** mode, you have a dedicated machine hosted by Datasentinel



With this method, you need to install agents to upload the metrics.
See :ref:`agent-installation`

The agents can be configured to pass through a proxy server


.. note::
    | In some cases, it is possible to use the **Agentless** method to monitor instances. 
    |
    | To do so, the dedicated **SaaS** platform must have the ability to remotely connect to the instances
    | (Access authorization to be defined on managed instances provided by public cloud providers for example)

.. image:: images/saas-architecture.png
   :align: center
   :alt: PostgreSQL performance monitoring tool Datasentinel SaaS Architecture
   :width: 100%

.. note::
    | `Getting started with Datasentinel SaaS <https://www.datasentinel.io/blog/post/start_saas/>`_ blog

