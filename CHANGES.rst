Changelog for dust
==================

1.1 (unreleased)
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
