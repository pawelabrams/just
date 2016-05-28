__all__ = ['echo']

from . import *

cmds = {
  'echo': echo.echo,
}

__all__.append('cmds')