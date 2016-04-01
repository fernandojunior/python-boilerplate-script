import os
import subprocess
import pytest  # noqa
from script_name import hello_world

path = os.path.dirname(os.path.abspath(__file__))


def cmd(s):
    return subprocess.check_output(s.split()).decode('utf-8').strip()


def test_hello_world():
    assert(hello_world == "Hello World")


def test_script():
    script = path + '/script_name.py'
    assert('Hello World' in cmd('python %s %s' % (script, hello_world)))
