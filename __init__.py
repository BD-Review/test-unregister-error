# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Test Unregister Error",
    "author": "BD",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 0),
    "location": "",
    "warning": "",
    "doc_url": "https://github.com/BD-Review/test-unregister-error/",
    "tracker_url": "https://github.com/BD-Review/test-unregister-error/issues",
    "endpoint_url": "https://raw.githubusercontent.com/BD-Review/test-unregister-error/main/endpoint.json",
    "category": "Generic"
}



def register():
    pass


def unregister():
    raise ValueError
