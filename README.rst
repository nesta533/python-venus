========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-venus/badge/?style=flat
    :target: https://readthedocs.org/projects/python-venus
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/nesta533@hotmail.com/python-venus.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/nesta533@hotmail.com/python-venus

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/nesta533@hotmail.com/python-venus?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/nesta533@hotmail.com/python-venus

.. |requires| image:: https://requires.io/github/nesta533@hotmail.com/python-venus/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/nesta533@hotmail.com/python-venus/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/nesta533@hotmail.com/python-venus/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/nesta533@hotmail.com/python-venus

.. |version| image:: https://img.shields.io/pypi/v/venus.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/venus

.. |commits-since| image:: https://img.shields.io/github/commits-since/nesta533@hotmail.com/python-venus/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/nesta533@hotmail.com/python-venus/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/venus.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/venus

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/venus.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/venus

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/venus.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/venus


.. end-badges

VENUS created by Abel Hui Wang

* Free software: BSD license

Installation
============

::

    pip install venus

Documentation
=============

https://python-venus.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
