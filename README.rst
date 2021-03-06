Microsoft Azure CLI 2.0 - Preview
==================================

.. image:: https://img.shields.io/pypi/v/azure-cli.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/azure-cli

.. image:: https://img.shields.io/pypi/pyversions/azure-cli.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/azure-cli

.. image:: https://travis-ci.org/Azure/azure-cli.svg?branch=master
    :target: https://travis-ci.org/Azure/azure-cli

A great cloud needs great tools; we're excited to introduce *Azure CLI 2.0 - Preview*, our next generation multi-platform command line experience for Azure.

Installation
===============

Upgrading
^^^^^^^^^

If you already have the CLI installed, run the following to update:

.. code-block:: console

   $ az component update

If you don't have the CLI installed, see below.

Install with pip
^^^^^^^^^^^^^^^^

For those familiar with pip, use the following:

.. code-block:: console

   $ pip install --user azure-cli

You may need to modify your PATH to include the directory ``az`` is installed to:

**On Linux:**

.. code-block:: console

   $ export PATH=$PATH:~/.local/bin

Permanently include this change by modifying your rc file:

.. code-block:: console

   $ echo "PATH=\$PATH:~/.local/bin" >> ~/.bashrc

**On OS X:**

.. code-block:: console

   export PATH=$PATH:~/Library/Python/X.Y/bin

Where X.Y is your Python version.

Permanently include this change by modifying your rc file:

.. code-block:: console

   $ echo "PATH=\$PATH:~/Library/Python/X.Y/bin" >> ~/.bash_profile

**On Windows:**

Add ``%APPDATA%\Python\PythonXY\Scripts`` to your PATH.
Where XY is your Python version.

Enable tab completion with ``source az.completion.sh``.

Some prerequisites may be required. See our `Preview Install Guide <https://github.com/Azure/azure-cli/blob/master/doc/preview_install_guide.md>`__.

If you run into an ``AttributeError: 'X509' object has no attribute '_x509'`` error, downgrade your version of the requests library from 2.12.1 to 2.11.1.
Use ``pip install requests==2.11.1``.

NOTE: If in a virtual environment, you can simply use ``pip install azure-cli`` and the CLI will be installed into that virtual environment.

Install with apt-get
^^^^^^^^^^^^^^^^^^^^

A Debian/Ubuntu package is also available. Install as follows:

.. code-block:: console

    $ echo "deb https://apt-mo.trafficmanager.net/repos/azure-cli/ wheezy main" | sudo tee /etc/apt/sources.list.d/azure-cli.list
    $ sudo apt-key adv --keyserver apt-mo.trafficmanager.net --recv-keys 417A0893
    $ sudo apt-get install apt-transport-https
    $ sudo apt-get update && sudo apt-get install azure-cli

Install with Docker
^^^^^^^^^^^^^^^^^^^

We also maintain a Docker image preconfigured with the Azure CLI.

Tagged Docker images are available.
See our `Docker tags <https://hub.docker.com/r/azuresdk/azure-cli-python/tags/>`__ for available versions.

.. code-block:: console

   $ docker run -v ${HOME}:/root -it azuresdk/azure-cli-python:<version>

Run the latest automated Docker build with the command below.
All command modules are included in this version as the image is built directly from the Git repository.

.. code-block:: console

   $ docker run -v ${HOME}:/root -it azuresdk/azure-cli-python:latest

For installation steps for common platforms, as well as dependency troubleshooting, please take a look at our `installation guide <http://github.com/Azure/azure-cli/blob/master/doc/preview_install_guide.md>`__.


Install with interactive install script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For OSX and Linux, you can install using curl: 

.. code-block:: console

   $ curl -L https://aka.ms/InstallAzureCli | bash

or using wget:

.. code-block:: console

   $ wget -q -O - https://aka.ms/InstallAzureCli | bash

Some prerequisites may be required. See our `Preview Install Guide <https://github.com/Azure/azure-cli/blob/master/doc/preview_install_guide.md>`__.

If you run into an ``AttributeError: 'X509' object has no attribute '_x509'`` error, downgrade your version of the requests library from 2.12.1 to 2.11.1.
With the default install location, use ``/usr/local/az/bin/pip install requests==2.11.1``.

Usage
=====
.. code-block:: console

    $ az [ group ] [ subgroup ] [ command ] {parameters}


Getting Started
=====================

After installation, use the ``az configure`` command to help setup your environment and get you logged in.

.. code-block:: console

   $ az configure

For usage and help content, pass in the ``-h`` parameter, for example:

.. code-block:: console

   $ az storage -h
   $ az vm create -h

Highlights
===========

Here are a few features and concepts that can help you get the most out of the Azure CLI 2.0 Preview

.. image:: doc/assets/AzBlogAnimation4.gif
    :align: center
    :alt: Azure CLI 2.0 Highlight Reel
    :width: 600
    :height: 300

    


The following examples are showing using the ``--output table`` format, you can change your default using the ``$ az configure`` command.

Tab Completion
^^^^^^^^^^^^^^

We support tab-completion for groups, commands, and some parameters

.. code-block:: console

   # looking up resource group and name
   $ az vm show -g [tab][tab]
   AccountingGroup   RGOne  WebPropertiesRG
   $ az vm show -g WebPropertiesRG -n [tab][tab]
   StoreVM  Bizlogic
   $ az vm show -g WebPropertiesRG -n Bizlogic

Querying
^^^^^^^^

You can use the ``--query`` parameter and the JMESPath query syntax to customize your output.

.. code-block:: console

   $ az vm list --query '[].{name:name,os:storageProfile.osDisk.osType}'
   Name                    Os
   ----------------------  -------
   storevm                 Linux
   bizlogic                Linux
   demo32111vm             Windows
   dcos-master-39DB807E-0  Linux

Creating a new Linux VM
^^^^^^^^^^^^^^^^^^^^^^^
The following block creates a new resource group in the 'westus' region, then creates a new Ubuntu VM.  We automatically provide a series of smart defaults, such as setting up SSH with your  ``~/.ssh/id_rsa.pub`` key.  For more details, try ``az vm create -h``.

.. code-block:: console

   $ az resource group create -l westus -n MyGroup
   Name     Location
   -------  ----------
   MyGroup  westus

   $ az vm create -g MyGroup -n MyVM --image ubuntults
   MacAddress         ResourceGroup    PublicIpAddress    PrivateIpAddress
   -----------------  ---------------  -----------------  ------------------
   00-0D-3A-30-B2-D7  MyGroup          52.160.111.118     10.0.0.4

   $ ssh 52.160.111.118
   Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.19.0-65-generic x86_64)

   System information as of Thu Sep 15 20:47:31 UTC 2016

   System load: 0.39              Memory usage: 2%   Processes:       80
   Usage of /:  39.6% of 1.94GB   Swap usage:   0%   Users logged in: 0

   jasonsha@MyVM:~$

More Samples and Snippets
^^^^^^^^^^^^^^^^^^^^^^^^^
For more usage examples, take a look at our `GitHub samples repo <http://github.com/Azure/azure-cli-samples>`__.

Reporting issues and feedback
=======================================

If you encounter any bugs with the tool please file an issue in the `Issues <https://github.com/Azure/azure-cli/issues>`__ section of our GitHub repo.

Before posting an issue, please review our list of `Common Issues <https://github.com/Azure/azure-cli/issues?q=label%3AFAQ+is%3Aclosed>`__. These are issues we have closed because we cannot address them within the CLI due to platform or language limitations. 

To provide feedback from the command line, try the ``az feedback`` command.

Contribute Code
===================================

This project has adopted the `Microsoft Open Source Code of Conduct <https://opensource.microsoft.com/codeofconduct/>`__.

For more information see the `Code of Conduct FAQ <https://opensource.microsoft.com/codeofconduct/faq/>`__ or contact `opencode@microsoft.com <mailto:opencode@microsoft.com>`__ with any additional questions or comments.

If you would like to become an active contributor to this project please
follow the instructions provided in `Microsoft Azure Projects Contribution Guidelines <http://azure.github.io/guidelines.html>`__


License
=======

`MIT <https://github.com/Azure/azure-cli/blob/master/LICENSE.txt>`__
