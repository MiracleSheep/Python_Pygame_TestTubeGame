#   -*- coding: utf-8 -*-
from os import path

from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.distutils")


name = "Python_Pygame_TestTubeGame"
default_task = "publish"


@init
def set_properties(project):
    pass

