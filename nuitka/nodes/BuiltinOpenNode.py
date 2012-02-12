#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Part of "Nuitka", an optimizing Python compiler that is compatible and
#     integrates with CPython, but also works on its own.
#
#     If you submit patches or make the software available to licensors of
#     this software in either form, you automatically them grant them a
#     license for your part of the code under "Apache License 2.0" unless you
#     choose to remove this notice.
#
#     Kay Hayen uses the right to license his code under only GPL version 3,
#     to discourage a fork of Nuitka before it is "finished". He will later
#     make a new "Nuitka" release fully under "Apache License 2.0".
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, version 3 of the License.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#     Please leave the whole of this copyright notice intact.
#
""" Node the calls to the 'open' builtin.

This is a rather two sided beast, as it may be read or write. And we would like to be able
to track it, so we can include files into the executable, or write more efficiently.
"""

from .NodeBases import CPythonExpressionChildrenHavingBase


class CPythonExpressionBuiltinOpen( CPythonExpressionChildrenHavingBase ):
    kind = "EXPRESSION_BUILTIN_OPEN"

    named_children = ( "filename", "mode", "buffering" )

    def __init__( self, filename, mode, buffering, source_ref ):
        CPythonExpressionChildrenHavingBase.__init__(
            self,
            values     = {
                "filename"  : filename,
                "mode"      : mode,
                "buffering" : buffering
            },
            source_ref = source_ref
        )

    getFilename = CPythonExpressionChildrenHavingBase.childGetter( "filename" )
    getMode = CPythonExpressionChildrenHavingBase.childGetter( "mode" )
    getBuffering = CPythonExpressionChildrenHavingBase.childGetter( "buffering" )

    def computeNode( self ):
        # Note: Quite impossible to predict without further assumptions.
        return self, None, None