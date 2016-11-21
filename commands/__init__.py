__all__ = ['echo', 'install', 'github', 'download', 'check']

from . import *
from __main__ import config

cmds = {
  'echo': echo.echo,
  'apt': install.install,
  'install': install.install,
  'clone': github.clone,
  'download': download.download,
  'check': check.check
}

if config.has_section('aliases'):
    for alias, command in config.items('aliases'):
        try:
            cmds[alias] = cmds[command]
        except KeyError:
            pass

__all__.append('cmds')