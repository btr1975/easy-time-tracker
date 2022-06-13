Installs as a linux style cli
=============================


Using help
----------

.. code-block:: bash

   (venv) user@main-pc:~/some-directory$ ett -h
   usage: ett [-h] {start,stop,output,gui} ...

   easy-time-tracker

   optional arguments:
     -h, --help            show this help message and exit

   commands:
     Valid commands: a single command is required

     {start,stop,output,gui}
                           CLI Help
       start               Start the clock
       stop                Stop the clock
       output              Output completed records
       gui                 Start the GUI

Example help for start
----------------------

.. code-block:: bash

   (venv) user@main-pc:~/some-directory$ ett start -h
   usage: ett start [-h] [-d DESCRIPTION] [-p PEOPLE [PEOPLE ...]] [--project PROJECT]

   optional arguments:
     -h, --help            show this help message and exit
     -d DESCRIPTION, --description DESCRIPTION
                           Description of the time
     -p PEOPLE [PEOPLE ...], --people PEOPLE [PEOPLE ...]
                           List of people
     --project PROJECT     Project

Example start Simple GUI
----------------------

.. code-block:: bash

   (venv) user@main-pc:~/some-directory$ ett gui
