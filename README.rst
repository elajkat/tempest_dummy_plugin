Dummy plugin for tempest
=======================

This is a demonstarion for how to write a tempest test plugin.
This feature is available from tag 6 in tempest, see.:
http://docs.openstack.org/developer/tempest/plugin.html

How to use
----------
An example how I used it:

- In tempest repo install a venv for tempest::

  $ tox -evenv

- Activate the venv and install the tempest_dummy_plugin to the venve::

  $ . .tox/venv/bin/activate
  (venv)$ pyton setup.py install

- You can check the test listing to see if the tests are detected::

  $ testr list-tests | grep dummy


Configuration
-------------
Add the following lines to the end of tempest.conf::

  [dummy_config_options]

  funny_cfg_option = funny

And you can reach the options in the old way from your testcases.
