__all__ = ['echo', 'install', 'github', 'download']

from . import *

cmds = {
  'echo': echo.echo,
  'apt': install.install,
  'install': install.install,
  'clone': github.clone,
  'download': download.download,
}

__all__.append('cmds')