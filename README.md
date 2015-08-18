Say Fromage: Duplicate Photo Script
====================================

Prereqs
-------

None

Install
-------

This assumes that `py` is '2.7' and that `virtualenv` is installed.

    $ virtualenv ~/ENV/dps
    $ source ~/ENV/dps/bin/activate
    $ pip install -r requirements.txt


Configuration
-------------

There is a local configuration file `config.py` which has a few adjustable
parameters. Adjust these as you see fit.


Running
-------

Run the script as follows:

    $ pyhton duplication_photos.py

This will read its parameters from `config.py`.

You can overide some of the parameters like this:

    $ pyhton duplication_photos.py -b 100 -x 10

where [-b START_BATCH] [-x HOW_MANY_BATCHES] [-i ENABLE_INPUT]

The above line means start from batch 200 and create 10 batches.

