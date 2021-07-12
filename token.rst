.. _token:

*****
Token
*****

.. note::

    | A license key is required to use Datasentinel.
    | 
    | If you don't have one, you can ask for a  `Free 30-days Trial <https://www.datasentinel.io/#/freetrial>`_
    |
    
  
.. warning::

    | Agents need a valid token to authenticate and communicate with the platform
    |
    | Token needs to be updated before its expiration date.

Update the platform
*********************

| The update is done in the user interface

- Open tools menu

    .. image:: images/tools_icon.png
       :alt: Change token
       :align: left

- Click on **Global settings**

    .. image:: images/tools_menu.png
       :align: left

- Then copy/paste the new valid token

    .. image:: images/change_token.gif
       :alt: Change token
       :width: 100%
       :align: center

                                            
Update agents
*************

.. note::

    | Each agent automatically downloads and updates its token from the platform


The update can also be done with the CLI

- Example

.. code-block:: bash

   datasentinel set token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODM2OTUyNzcsImlhdCI6MTU3NjM1MTI3MiwiZGF0Y

- Output

.. code-block:: text

    Copyright 2020 (c) datasentinel- All rights reserved        www.datasentinel.io
    ================================================================================

    Token successfully set!


            Server
                    host : 51.158.120.108                                    
                    port : 443                                               



Check the token validity
************************

- Example

.. code-block:: bash

   datasentinel show token 

- Output

.. code-block:: text


               Token : eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODM2OTUyNzcsImlhdCI6MTU3NjM1MTI3MiwiZGF0YWJhc2UiOiJkcy1kYXRhIn0.UQRxutKrJv7WVAaHCN3Fh_wnXJLst54s93lADIP_n-Y

        Organization : ds-data                                           
     Expiration Date : 2020-03-08 19:21:17                               
