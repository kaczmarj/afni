import subprocess
import sys

def test_3dAllineate():
   cp = subprocess.run('cd pytest_tests/test_dirs/3dAllineate && tcsh runit',
                       check=True,
                       close_fds=True,
                       shell=True)