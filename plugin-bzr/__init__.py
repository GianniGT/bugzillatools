# This file is part of bugzillatools
# Copyright (C) 2010-2011 Benon Technologies Pty Ltd
#
# bugzillatools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Mark bugzilla bugs fixed using --fixes argument

If the --fixes argument to `bzr commit` points to a bugzilla installation,
the bug will be marked fixed using the credentials stored in your
bazaar.conf.
"""

import bzrlib.api
import bzrlib.commands
import bzrlib.trace

from . import hooks

# plugin setup
# TODO use bzlib version info
bzr_plugin_name = 'bugzilla'
version_info = (0, 6, 0, 'dev', 0)

if version_info[3] == 'final':
    version_string = '%d.%d.%d' % version_info[:3]
else:
    version_string = '%d.%d.%d%s%d' % version_info
__version__ = version_string

COMPATIBLE_BZR_VERSIONS = [
    (2, 0, 0),
    (2, 1, 0),
    (2, 2, 0),
    (2, 3, 0),
]

bzrlib.api.require_any_api(bzrlib, COMPATIBLE_BZR_VERSIONS)

if __name__ != 'bzrlib.plugins.bugzilla':
    bzrlib.trace.warning(
        'Not running as bzrlib.plugins.bugzilla; things may break.')

# install the get_command hook
bzrlib.commands.Command.hooks.install_named_hook(
    'get_command',
    hooks.get_command_hook,
    'bugzilla plugin - extend cmd_commit'
)
