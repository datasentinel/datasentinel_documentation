**********************************
On-premises platform installation
**********************************

.. raw:: html

   <h3>Prerequisites</h3>

You need to have a linux machine **Red Hat or centos 7**:

    - >= 8 CPUS 
    - >= 16 GB RAM
    - >= 50 GB STORAGE
    - Nginx web server preinstalled


.. note::
   | The platform is composed of several components packaged in a single file **install-datasentinel-platform.tar.gz** (size 550 MB)
   | All the components are packaged under the user **datasentinel**
   | Installation less than 5 minutes

.. image:: architecture.png
   :scale: 100 %
   :align: center

1. Uncompress
*************

.. code-block:: bash

   tar xvzf {{ downloaded file name }}.tar.gz

2 files are created

- init_datasentinel.sh
- datasentinel-platform.tar.gz

2. Install
**********

| Run the shell script

.. code-block:: bash

   ./init_datasentinel.sh


.. warning:: 
   The script must be run as root


.. raw:: html

   <h3>The script does several actions</h3>


- Creation of a user and group **datasentinel**
- Creation of a directory **/datasentinel**
- **datasentinel-platform.tar.gz** decompression to install all components
- **bash_profile** and **crontab** entries creation
- Services deployment for automatic restart
- Start all components

.. caution::
   | nginx uses a self-signed certificate located in **/etc/nginx/certs** directory
   | You can change it with your own certificate.

.. caution::
   | The port 443 must be opened and accessible.
   | Also, be careful with your firewall configuration (selinux, firewalld) if any

.. note:: 
   | At the end of the script, the datasentinel repository should be UP and RUNNING.
   | 
   | You should be able to connect to the user interface.
   | Open a brower and type **https://<<your-hostname>>**
   | The login is **datasentinel**
   | The password is given by datasentinel team

3. Components
*************

Datasentinel uses the following components:

- Nginx web server (Preinstalled)
- Datasentinel backend APIs
- Timeseries database influxdb
- Grafana Frontend (with a postgreSQL database)
- Datasentinel Frontend application

.. note:: 
   | Each component is restarted automatically with a system service 
   | located on **/usr/lib/systemd/system**

4. Components management
************************

Start

.. code-block:: bash

    systemctl start datasentinel_influxdb datasentinel_postgresql datasentinel_grafana datasentinel_backend nginx

Stop

.. code-block:: bash

    systemctl stop datasentinel_influxdb datasentinel_postgresql datasentinel_grafana datasentinel_backend nginx

Status details

.. code-block:: bash

    systemctl status datasentinel_influxdb datasentinel_postgresql datasentinel_grafana datasentinel_backend nginx

.. raw:: html

   <h3>An alias is present when connected as datasentinel to check all components availibility</h3>

.. code-block:: bash

   status_datasentinel

Output

.. code-block:: bash

   datasentinel_backend.service                                       loaded active running   Datasentinel backend APIs
   datasentinel_dispatcher.service                                    loaded active running   Datasentinel dispatcher
   datasentinel_influxdb.service                                      loaded active running   InfluxDB service
   datasentinel_grafana.service                                       loaded active running   Grafana daemon
   datasentinel_postgresql.service                                    loaded active running   PostgreSQL 10 database server
   nginx.service                                                      loaded active running   The nginx HTTP and reverse proxy server

4. Useful log files
********************

.. note:: 
   | Log files are located in the directory **/datasentinel/log** except the nginx log file


+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Log file                              | Information                                                                                      |
+=======================================+==================================================================================================+
| /var/log/https_datasentinel.log       | Nginx log access                                                                                 |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| backend_apis.log                      | API calls                                                                                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| backend_to_influx.log                 | Log data copied to influxdb database                                                             |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| dispatcher.log                        | Agentless feature log file                                                                       |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| compute.log                           | Internal metrics compute done by datasentinel                                                    |
+---------------------------------------+--------------------------------------------------------------------------------------------------+
| grafana.log                           | Grafana log access                                                                               |
+---------------------------------------+--------------------------------------------------------------------------------------------------+

