.. _system_stats:

*************
system_stats
*************

**SYSTEM_STATS** is an extension to monitor system activity.

.. note::
   | This extension is **OPTIONAL** and is only used if you choose the agentless mode. 
   | Datasentinel automatically takes it into account if it is installed

.. warning::
   | To be installed in the **postgres** database.
   | You need to grant the role monitor_system_stats to the monitoring user.
   |
   | Example: GRANT **monitor_system_stats** to datasentinel;
   

.. raw:: html

Installation 
************
   
- See https://github.com/EnterpriseDB/system_stats for more details and how to install this extension.

Monitored metrics 
*****************

- System information
- CPU load
- CPU usage
- Memory usage
- Network usage
- Swap usage
- IOs statistics
- File-systems usage
