# coding: utf-8
"""Find the path to LiteMORT dynamic library files."""
import os

from platform import system


def find_lib_path():
    """Find the path to LiteMORT library files.
    Returns
    -------
    lib_path: list(string)
       List of all found library path to LiteMORT
    """
    curr_path = os.path.dirname(os.path.abspath(os.path.expanduser(__file__)))
    dll_path = [curr_path, os.path.join(curr_path, '../../'),
                os.path.join(curr_path, 'compile'),
                os.path.join(curr_path, '../compile'),
                os.path.join(curr_path, '../../lib/')]
    if system() in ('Windows', 'Microsoft'):
        dll_path.append(os.path.join(curr_path, '../compile/Release/'))
        dll_path.append(os.path.join(curr_path, '../compile/windows/x64/DLL/'))
        dll_path.append(os.path.join(curr_path, '../../Release/'))
        dll_path.append(os.path.join(curr_path, '../../windows/x64/DLL/'))
        dll_path = [os.path.join(p, 'LiteMORT.dll') for p in dll_path]
    else:
        dll_path = [os.path.join(p, 'lib_LiteMORT.so') for p in dll_path]
    lib_path = [p for p in dll_path if os.path.exists(p) and os.path.isfile(p)]
    if not lib_path:
        dll_path = [os.path.realpath(p) for p in dll_path]
        raise Exception('Cannot find LiteMORT library in following paths: ' + '\n'.join(dll_path))

    return lib_path
