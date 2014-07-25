"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Main.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True, 'includes': ['sip', 'PySide.QtCore','PySide.QtGui'], 'resources':'assets'}
setup(
    app=APP,
    name='Interstitail',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
