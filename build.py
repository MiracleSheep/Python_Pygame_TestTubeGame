#   -*- coding: utf-8 -*-
from os import path

from pybuilder.core import use_plugin, init, task

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("copy_resources")

name = "Python_Pygame_TestTubeGame"
default_task = "publish"



@init
def set_properties(project):
    project.build_depends_on("pygame")
    project.build_depends_on("pyautogui")
    project.get_property("copy_resources_glob").append("assets/*.png")
    project.get_property("copy_resources_glob").append("assets/*.jpeg")
    project.set_property("copy_resources_target", "$dir_dist/scripts")
    # project.include_file("assets", "*.png")  # All included binary wheels from vendors
    # project.include_file("assets", "*.jpeg")  # All included binary wheels from vendors

    # project.install_file("assets", "assets/*.png")
    # project.install_file("assets", "assets/*.jpeg")




