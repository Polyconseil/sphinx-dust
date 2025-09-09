from importlib import metadata

from .directive import setup  # pylint: disable=unused-import

__version__ = metadata.version('sphinx-dust')
