.. _extension:

**********************
datasentinel extension
**********************

.. note::
   | The extension is **OPTIONAL**, only required if you plan to use the sessions sampling feature every second.
   | 
   | The role of this extension is to get the queryid (**pg_stat_statements**) from active sessions (**pg_stat_activity**)

.. warning::
   | To be installed in the **postgres** database.
   
.. raw:: html

   <h3>Installation</h3>

.. note::
   The examples are done with a standard postgresql installation on a server running **centos 7** operating system

1. Install the libraries
************************

- Version < 9.6  (Example done with 9.4)

.. code-block:: bash

   yum install -y https://download.postgresql.org/pub/repos/yum/9.4/redhat/rhel-7-x86_64/pgdg-centos94-9.4-3.noarch.rpm
   yum install -y postgresql94-devel postgresql94-contrib

- Version 9.6

.. code-block:: bash

   yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
   yum install -y postgresql96-devel postgresql96-contrib

- Version 10

.. code-block:: bash

   yum install -y https://yum.postgresql.org/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm
   yum install -y postgresql10-devel postgresql10-contrib

- Version 11

.. code-block:: bash

   yum install -y https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   yum install -y centos-release-scl
   yum install -y postgresql11-devel postgresql11-llvmjit llvm-toolset-7

- Version 12

.. code-block:: bash

   yum install -y https://download.postgresql.org/pub/repos/yum/12/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   yum install -y centos-release-scl
   yum install -y postgresql12-devel postgresql12-llvmjit llvm-toolset-7

- All (to compile the extension)

.. code-block:: bash

   yum install -y gcc

2. Download source files
************************

- Download the source files from the user interface (Agents submenu)

.. note::
   You can also copy directly copy the file **datasentinel-extension.tar.gz** from the directory **/datasentinel/download**

3. Compile and deploy
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

   cd datasentinel_extension/src
   make
   make install

.. note::
   Once the extension is compiled in one server, you can manually copy the files below on others servers

.. code-block:: bash

   # example done with a standard postgresql 10 installed version
   /usr/bin/mkdir -p /usr/pgsql-10/lib
   /usr/bin/mkdir -p /usr/pgsql-10/share/extension
   cp datasentinel.so /usr/pgsql-10/lib/
   chmod 755 /usr/pgsql-10/lib/datasentinel.so
   cp datasentinel.control /usr/pgsql-10/share/extension/
   chmod 644 /usr/pgsql-10/share/extension/datasentinel.control
   cp datasentinel--1.0.sql /usr/pgsql-10/share/extension/
   chmod 644 /usr/pgsql-10/share/extension/datasentinel--1.0.sql


4. Modify postgresql.conf
*************************

- Add the following lines

.. code-block:: bash

    shared_preload_libraries = 'pg_stat_statements,datasentinel'
    track_activity_query_size = 2048
    pg_stat_statements.track = all

5. Restart postgresql
*********************

- Version 9.6

.. code-block:: bash

   systemctl restart postgresql

- Version 10

.. code-block:: bash

   systemctl restart postgresql-10

- Version 11

.. code-block:: bash

   systemctl restart postgresql-11

- Version 12

.. code-block:: bash

   systemctl restart postgresql-12

6. Create the extensions
************************

- connect as a superuser

.. code-block:: bash

    CREATE EXTENSION pg_stat_statements;
    CREATE EXTENSION datasentinel;
   
.. note::

   | To check the extension is correctly installed, you can execute the following sql
   |    
   |    *select query, pid, datasentinel_queryid(pid) from pg_stat_activity*
   