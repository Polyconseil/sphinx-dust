Changelog for dust
==================

1.2.6 (unreleased)
------------------

- Nothing changed yet.


1.2.5 (2025-09-09)
------------------

- Replace pkg_resources with importlib.metadata.


1.2.4 (2018-08-31)
------------------

- Add a per document ``dust-days-limit`` configuration.


1.2.3 (2017-08-21)
------------------

- Emit a warning when providing a proofread-on value in the future


1.2.2 (2017-06-19)
------------------

- Add a new setting to choose the admonition node classes
- Add several settings to control dust's HTML output


1.2.1 (2017-05-17)
------------------

- Stop using the deprecated 'make_admonition', use 'BaseAdmonition' instead


1.2 (2017-05-16)
----------------

- Sphinx 1.6 compatibility.


1.1 (2016-09-21)
----------------

- The package used to install under ``dust`` which could conflict with
  the "Dust" package. It now installs under ``sphinx_dust``. You must
  update the ``extensions`` list accordingly in your Sphinx
  configuration.
- Fix CSS class. The styling was fine with the default Sphinx theme,
  but incorrect with ReadTheDocs theme.
- Fix outdated document calculation


1.0 (2016-08-31)
----------------

- Emit warnings when a document hasn't been proofread in a while
