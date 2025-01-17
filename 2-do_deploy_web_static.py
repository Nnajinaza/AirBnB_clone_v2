#!/usr/bin/python3
"""distributes an archive to your web servers"""
from fabric.api import *
import os.path


env.hosts = ["54.84.80.138", "54.144.143.183"]


def do_deploy(archive_path):
    """functio that distributes an archive to your web servers"""
    if os.path.isfile(archive_path):
        p1 = archive_path.split("/")
        p2 = p1[-1].split(".")

        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(p2[0]))

        data = "/data/web_static/releases"
        sudo("tar -xzf /tmp/{} -C {}/{}/".format(p1[-1], data, p2[0]))
        sudo("rm /tmp/{}".format(p1[-1]))

        path = "mv /data/web_static/releases"
        path2 = "/data/web_static/releases"
        sudo("{}/{}/web_static/* {}/{}/".format(path, p2[0], path2, p2[0]))

        sudo("rm -rf {}/{}//web_static".format(path2, p2[0]))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}/{}/ /data/web_static/current".format(path2, p2[0]))

        print("New version deployed!")
        return True

    else:
        return False
