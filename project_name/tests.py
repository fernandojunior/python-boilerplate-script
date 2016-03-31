import subprocess
import pytest  # noqa
from script_name import hello_world


def cmd(s):
    return subprocess.check_output(s.split()).strip()


def test_hello_world():
    assert(hello_world == "Hello World")


def test_script():
    assert(cmd('python script_name.py ' + hello_world))
