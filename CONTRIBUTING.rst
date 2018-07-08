Contributing guidelines
=======================

Feature Requests, Bug Reports, and Feedback. . .
------------------------------------------------

. . .should all be reported on the `GitHub Issue Tracker`_ .

.. _`GitHub Issue Tracker`: https://github.com/nmvalera/flask-web3/issues

Reporting issues
~~~~~~~~~~~~~~~~

- Describe what you expected to happen.
- If possible, include a `minimal, complete, and verifiable example`_ to help
- Describe what actually happened. Include the full traceback if there was an
  exception.

.. _minimal, complete, and verifiable example: https://stackoverflow.com/help/mcve

Setting-Up environment
----------------------

Requirements
~~~~~~~~~~~~

#. Having the latest version of ``git`` installed locally
#. Having Python 3.6 installed locally
#. Having ``virtualenv`` installed locally

   To install ``virtualenv`` you can run the following command

   .. code-block:: sh

       $ pip install virtualenv

#. Having ``docker`` and ``docker-compose`` installed locally
#. Having ``pip`` environment variables correctly configured

   Some of the package's dependencies of the project could be hosted on a custom PyPi server.
   In this case you need to set some environment variables in order to make ``pip`` inspect the custom pypi server when installing packages.

   To set ``pip`` environment variables on a permanent basis you can add the following lines at the end of your ``\.bashrc`` file (being careful to replace placeholders)

   .. code-block:: text

       # ~/.bashrc

       ...

       # Indicate to pip which pypi server to download from
       export PIP_TIMEOUT=60
       export PIP_INDEX_URL=<custom_pypi_protocol>://<user>:<password>@<custom_pypi_host>
       export PIP_EXTRA_INDEX_URL=https://pypi.python.org/simple

First time setup
~~~~~~~~~~~~~~~~

- Clone the project locally

- Create development environment using Docker or Make

  .. code-block:: sh

      $ make init

Project organisation
--------------------

The project

.. code-block:: text

    .
    ├── flask_web3/           # Main package source scripts (where all functional python scripts are stored)
    ├── docs/                    # Docs module containing all scripts required by sphinx to build the documentation
    ├── tests/                   # Tests folder where all test modules are stores
    ├── .coveragerc              # Configuration file for coverage
    ├── .gitignore               # List all files pattern excluded from git's tracking
    ├── .gitlab-ci.yml           # GitLab CI script
    ├── AUTHORS                  # List of authors of the project
    ├── CHANGES                  # Changelog listing every changes from a release to another
    ├── CONTRIBUTING.rst         # Indicate the guidelines that should be respected when contributing on this project
    ├── LICENSE                  # License of the project
    ├── Makefile                 # Script implement multiple commands to facilitate developments
    ├── README.rst               # README.md of your project
    ├── setup.cfg                # Configuration of extra commands that will be installed on package setup
    ├── setup.py                 # File used to setup the package
    └── tox.ini                  # Configuration file of test suite (it runs test suite in both Python 3.5 and 3.6 environments)

Coding
------

Development Workflow
~~~~~~~~~~~~~~~~~~~~

Please follow the next workflow when developing

- Create a branch to identify the feature or issue you will work on (e.g.
  ``feature/my-feature`` or ``hotfix/2287``)
- Using your favorite editor, make your changes, `committing as you go`_ and respecting the `AngularJS Commit Message Conventions`_
- Follow `PEP8`_ and limit script's line length to **120 characters**. See `<testing-linting_>`_
- Include tests that cover any code changes you make. See `<running-test_>`_ and `<running-coverage_>`_
- Update ``setup.py`` script with all dependencies you introduce. See `<adding-dependency_>`_ for precisions
- Write clear and exhaustive docstrings. Write docs to precise how to use the functionality you implement. See `<writing-docs_>`_
- Update changelog with the modifications you proceed to. See `<updating-changelog_>`_
- Your branch will soon be merged ! :-)

.. _committing as you go: http://dont-be-afraid-to-commit.readthedocs.io/en/latest/git/commandlinegit.html#commit-your-changes
.. _AngularJS Commit Message Conventions: https://gist.github.com/stephenparish/9941e89d80e2bc58a153
.. _PEP8: https://pep8.org/

Testing
~~~~~~~

.. _running-test:

Running tests
`````````````

Run test suite in by running

.. code-block:: sh

    $ make test

.. _running-coverage:

Running coverage
````````````````

Please ensure that all the lines of source code you are writing are covered in your test suite.
To generate the coverage report, please run

.. code-block:: sh

    $ make coverage

Read more about `coverage <https://coverage.readthedocs.io>`_.

Running the full test suite with ``tox`` will combine the coverage reports from all runs.

.. _testing-linting:

Testing linting
```````````````

To test if your project is compliant with linting rules run

.. code-block:: sh

    $ make test-lint

To automatically correct linting errors run

.. code-block:: sh

    $ make lint

Running full test suite
```````````````````````

Run test suite in multiple distinct python environment with following command

.. code-block:: sh

    $ make tox

.. _writing-docs:

Writing documentation
~~~~~~~~~~~~~~~~~~~~~

Write clear and exhaustive docstrings in every functional scripts.

This project uses sphinx to build documentations, it requires docs file to be written in ``.rst`` format.

To build the documentation, please run

.. code-block:: sh

    $ make docs

Precisions
~~~~~~~~~~

.. _updating-changelog:

Updating changelog
``````````````````

Every implemented modifications on the project from a release to another should be documented in the changelog ``CHANGES.rst`` file.

The format used for a release block is be the following

.. code-block:: text

    Version <NEW_VERSION>
    ---------------------

    Released on <NEW_VERSION_RELEASED_DATE>, codename <NEW_VERSION_CODENAME>.

    Features

    - Feature 1
    - Feature 2
    - Feature 3

    Fixes

    - Hotfix 1 (``#134``)
    - Hotfix 2 (``#139``)

    .. _#134: https://github.com/nmvalera/flask-web3/issues/134
    .. _#139: https://github.com/nmvalera/sandbox/flask-web3/issues/139

Be careful to never touch the header line as well as the release's metadata sentence.

.. code-block:: text

    Version <NEW_VERSION>
    ---------------------

    Released on <NEW_VERSION_RELEASED_DATE>, codename <NEW_VERSION_CODENAME>.

.. _adding-dependency:

Adding a new dependency
```````````````````````

When adding a new package dependency it should be added in ``setup.py`` file in the ``install_requires`` list

The format should be ``dependency==1.3.2``.

When adding a dev dependency (e.g. a testing dependency) it should be added in
    - ``setup.py`` file in the ``extra_requires`` ``dev`` list
    - ``tox.ini`` file in the ``[testenv]`` ``deps``

Makefile commands
-----------------

``Makefile`` implements multiple handful shell commands for development

make init
~~~~~~~~~

Initialize development environment including
    - venv creation
    - package installation in dev mode

make clean
~~~~~~~~~~

Clean the package project by removing some files such as ``.pyc``, ``.pyo``, ``*.egg-info``

make test-lint
~~~~~~~~~~~~~~

Check if python scripts are compliant with `PEP8`_ rules

make lint
~~~~~~~~~

Automatically correct `PEP8`_ mistakes contained in the project.

make coverage
~~~~~~~~~~~~~

Run the test suite and computes test coverage.
It creates an html report that is automatically open after the commands terminates

make tox
~~~~~~~~

Run the test suites in multiple environments

make docs
~~~~~~~~~

Build documentation from the ``docs`` folder using sphinx.
It generates a build of the documentation in html format located in ``docs/_build/html``.