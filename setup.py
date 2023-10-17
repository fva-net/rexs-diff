import os
import sys
from cx_Freeze import setup, Executable

# run with `python setup.py build`

buildOptions = dict(
    include_files = [
        # 'Sample_Data/',
        # 'settings.cfg'
        'README.md'
    ],
    silent_level = 0
)
def find_data_file(filename):
    if getattr(sys, 'frozen', False):
        # The application is frozen
        datadir = os.path.dirname(sys.executable)
    else:
        # The application is not frozen
        # Change this bit to match where you store your data files:
        datadir = os.path.dirname(__file__)

    return os.path.join(datadir, filename)

setup(
    name = "Rexs Model Differention",
    version = "1",
    description = "",
    options= {'build_exe': buildOptions},
    executables = [
        Executable(
            script="main.py",
            target_name="REXSMatching",
            base=None
        )
    ]
)
