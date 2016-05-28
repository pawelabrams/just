__all__ = ['echo', 'install', 'github']

from . import *

cmds = {
  'echo': echo.echo,
  'apt': install.install,
  'install': install.install,
  'clone': github.clone,
}

__all__.append('cmds')