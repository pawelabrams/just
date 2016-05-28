__all__ = ['echo', 'install', 'github', 'download', 'check']

from . import *

cmds = {
  'echo': echo.echo,
  'apt': install.install,
  'install': install.install,
  'clone': github.clone,
  'download': download.download,
  'check': check.check
}

__all__.append('cmds')