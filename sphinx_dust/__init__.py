import pkg_resources

from .directive import setup  # pylint: disable=unused-import


__version__ = pkg_resources.get_distribution('sphinx-dust').version
