from distutils.core import setup
import py2exe
import math

setup(
     options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
     console = [{'script': "calculator_tk.py"}],
     zipfile = None,
)
