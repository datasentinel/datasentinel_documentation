******************
Sessions workload
******************

.. note::

    | Datasentinel agent performs sampling of active sessions at regular intervals

**With this sampling feature**

- Quickly identify the most consuming sessions and/or queries
- Point precisely the root cause of your slowdowns
- Identify the most consumed resources (CPU, IOs, others)
- .../...

.. raw:: html 

    <h4>Datasentinel allows 2 levels of granularity</h4>

- **low** : a sampling is done every 10 seconds (**default**)
- **high** : a sampling is done every second (needs datasentinel extension. See how to :ref:`extension`)

.. note::

    | You can modify the granularity at the agent level with the :doc:`../agent/CLI` (datasentinel set collection-rate **high or low**)

.. note::

    | The **high** level is more precise but generates more data to upload.


.. raw:: html 

    <h4>The dedicated dashboard displays the information in a multi-dimensional way with Time selection, Time zooming and Tag filtering</h4>

.. image:: ../images/sessions_workload.png
   :alt: Sessions workload
   :width: 100%
   :align: center
