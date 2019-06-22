**********************
Extension
**********************

| Datasentinel needs a special extension to be installed in each postgresql server. 
| This little extension is to be added to the **pg_stat_statements** extension.

How to install the extension
****************************

.. note::
   The examples are done on a standard postgresql installation on a server running **centos** operating system

1. Install the libraries and headers for C language
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Version 9.6

.. code-block:: bash

   $ yum install -y https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-centos96-9.6-3.noarch.rpm
   $ yum install -y postgresql96-devel postgresql96-contrib

- Version 10

.. code-block:: bash

   $ yum install -y https://yum.postgresql.org/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm
   $ yum install -y postgresql10-devel postgresql10-contrib

- Version 11

.. code-block:: bash

   $ yum install -y https://download.postgresql.org/pub/repos/yum/11/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
   $ yum install -y yum install centos-release-scl
   $ yum install -y postgresql11-devel postgresql11-llvmjit llvm-toolset-7

2. Get the extension source files from `Datasentinel application <https://app.datasentinel.io>`_
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3. Compile and deploy the extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Version 9.6

.. code-block:: bash

   $ export PATH=/usr/pgsql-9.6/bin:$PATH

- Version 10

.. code-block:: bash

   $ export PATH=/usr/pgsql-10/bin:$PATH

- Version 11

.. code-block:: bash

   $ export PATH=/usr/pgsql-11/bin:$PATH

- All

.. code-block:: bash

   $ cd datasentinel/src
   $ make
   $ make install

4. Modify postgresql.conf
^^^^^^^^^^^^^^^^^^^^^^^^^
- Add the following lines

.. code-block:: bash

    shared_preload_libraries = 'pg_stat_statements,datasentinel'
    track_activity_query_size = 2048
    pg_stat_statements.track = all

5. Restart postgresql
^^^^^^^^^^^^^^^^^^^^^
 - Version 9.6

.. code-block:: bash

   $ systemctl restart postgresql

- Version 10

.. code-block:: bash

   $ systemctl restart postgresql-10

- Version 11

.. code-block:: bash

   $ systemctl restart postgresql-11

6. Create the extensions in the instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    psql
    CREATE EXTENSION pg_stat_statements;
    CREATE EXTENSION datasentinel;
    exit;

.. note::

   | To verify that the extension is correctly installed, you can execute the following sql
   |    *select query, pid, datasentinel_queryid(pid) from pg_stat_activity*
   