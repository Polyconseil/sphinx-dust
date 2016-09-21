Dust
====

Dust is a Sphinx extension that emits warnings when a document hasn't
been proofread in a while.

It prevents your doc from accumulating dust!


Setting up
==========

Install dust from pip:

.. code-block:: shell

    $ pip install sphinx-dust

Then add it as an extension to your project's ``conf.py``:

.. code-block:: python

    # conf.py
    extensions = [
        'sphinx_dust',
    ]

Optionally, configure the value of ``dust_days_limit`` to your
convenience (defaults to 30):

.. code-block:: python

    # conf.py
    dust_days_limit = 30

If you only want to benefit from the generated note, configure the
``dust_emit_warnings`` attribute (defaults to ``True``):

.. code-block:: python

    # conf.py
    dust_emit_warnings = False


Using dust
==========

Dust introduces a new directive: ``reviewer-meta``.

It takes two arguments:

- ``written-on``, the date the document was redacted; and,
- ``proofread-on``, the date the document was proofread.

Both dates must respect the ``yyyy-mm-dd`` format.

Here it is in context:

.. code-block:: rst

    .. index.rst

    Rubik's Cube Tutorial
    ---------------------

    .. reviewer-meta::
        :written-on: 1974-05-19
        :proofread-on: 1974-06-20


This directive will be replaced by a note reading:

.. code-block:: rst

    .. note::

        Written on 19 May 1974, proofread on 20 June 1974


Running ``sphinx-build`` will output a warning if the number of days spanning
between ``written-on`` and ``proofread-on`` is greater than ``dust_days_limit``.
In this case, with ``dust_days_limit = 30``, Sphinx will emit a warning:

.. code-block:: shell

    /path/to/your/doc/index.rst:2: WARNING: This document hasn't been proofread for 32 days

Using Sphinx's ``-W`` option, warnings will be turned into errors, useful to
make CI builds fail and be notified of outdated docs.

The warning and note content are exported using sphinx.locale so you can translate
them in your language if you see fit.
