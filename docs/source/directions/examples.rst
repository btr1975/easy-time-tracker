Installs as a linux style cli
=============================


Using help
----------

.. code-block:: bash

   (venv) user@main-pc:~/some-directory$ ett -h
   usage: ett [-h] {start,stop,output} ...

   easy-time-tracker

   optional arguments:
     -h, --help           show this help message and exit

   commands:
     Valid commands: a single command is required

     {start,stop,output}  CLI Help
       start              Start the clock
       stop               Stop the clock
       output             Output completed records

Example help for start
----------------------

.. code-block:: bash

   (venv) user@main-pc:~/some-directory$ ett start -h
   usage: ett start [-h] [-d DESCRIPTION] [-p PEOPLE [PEOPLE ...]]

   optional arguments:
     -h, --help            show this help message and exit
     -d DESCRIPTION, --description DESCRIPTION
                           Description of the time
     -p PEOPLE [PEOPLE ...], --people PEOPLE [PEOPLE ...]
                           List of people
