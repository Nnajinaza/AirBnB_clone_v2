#!/usr/bin/python3
""" Keep it clean!"""
from fabric.api import *
from fabric.context_managers import *

env.hosts = ["54.84.80.138", "54.144.143.183"]


def do_clean(number=0):
    """Clean everything"""

    if int(number) == 0 or int(number) == 1:
        number = 1
        with lcd("versions"):
            local("(ls -t | head -n {};ls)| grep -v test \
                 |sort|uniq -u|xargs rm -rf".format(number))

        with cd("/data/web_static/releases"):
            run("(ls -t | head -n {};ls)| grep -v test \
                |sort|uniq -u|xargs rm -rf".format(number))

    elif int(number) > 1:
        with lcd("versions"):
            local("(ls -t | head -n {};ls)| grep -v test \
                 |sort|uniq -u|xargs rm -rf".format(number))

        with cd("/data/web_static/releases"):
            run("(ls -t | head -n {};ls)| grep -v test \
                |sort|uniq -u|xargs rm -rf".format(number))

    else:
        pass
