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


Configuration
=============

Various parameters can be tweaked to your convenience. You can alter any of
them in your project's ``conf.py`` file, they're simple Python variables.

You can assign any value to these settings, however you should respect their
typing, the extension could crash otherwise.

Here's an exhaustive list of every parameter:

- ``dust_days_limit`` (default: ``30``), the number of days a document can live
  since its last reviewing without emitting warnings,
- ``dust_emit_warnings`` (default: ``True``), controls whether the extension emits a
  warning when a document needs reviewing,
- ``dust_include_output`` (default: ``True``), controls whether to include an HTML
  output in the monitored documents,
- ``dust_output_format`` (default: ``"Written on {written_on}, proofread on {proofread_on}"``),
  the content of the HTML output, needs to include two format variables:
  ``written_on`` and ``proofread_on``, which will get replaced by the result of
  ``strftime``-formatting ``written-on`` and ``proofread-on`` values,
- ``dust_datetime_format`` (default: ``"%d %B %Y"``), the format datetimes
  (``written-on`` and ``proofread-on`` values) take in HTML output; and,
- ``dust_node_classes`` (default: ``['note']``), a list of Sphinx admonition
  classes to apply to the node used to generate HTML.
