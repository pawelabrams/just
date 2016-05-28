__all__ = ['echo', 'github']

from . import *

cmds = {
  'echo': echo.echo,
  'clone': github.clone,
}

__all__.append('cmds')