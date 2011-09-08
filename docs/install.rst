==================
Installation
==================

Pre-Requisites
===============

* `distribute <http://pypi.python.org/pypi/distribute>`_
* `pip <http://pypi.python.org/pypi/pip>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_
* `rvm <http://beginrescueend.com/>`_
  * `ruby 1.9.2-p290`

To install all of these system dependencies::

  curl -O http://python-distribute.org/distribute_setup.py
  python distribute_setup.py
  easy_install pip
  pip install virtualenv
  bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)
  rvm install ruby-1.9.2-p290


Creating the Virtual Environment
================================

First, create a clean base environment using virtualenv::

    virtualenv myproject
    cd myproject
    source bin/activate


Installing the Project
======================

Install the requirements and the project source::

	cd path/to/your/myproject/
    pip install -r requirements.txt
    pip install -e .


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp myproject/conf/local/example/* myproject/conf/local
    manage.py syncdb --migrate


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started:

    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
