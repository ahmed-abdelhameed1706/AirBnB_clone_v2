#!/usr/bin/python3
"""
script to deploy the static files on the server
"""


from fabric.api import *
import os
from datetime import datetime


env.hosts = ['54.160.81.105', '34.227.90.3']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_pack():
    """
    function to pack the web_static folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"web_static_{time}.tgz"
    local("sudo mkdir -p versions")
    archive_path = local(f"sudo tar -cvzf versions/{filename} web_static")

    if archive_path:
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """
    function to deploy the files to the servers
    """
    if not os.path.exists(archive_path):
        return False

    filename = os.path.basename(archive_path)
    archive_folder = f"/data/web_static/releases/{filename.split('.')[0]}"
    try:
        put(archive_path, "/tmp/")

        run(f"sudo rm -rf {archive_folder}/")

        run(f"sudo mkdir -p {archive_folder}/")

        run(f"sudo tar -xzf /tmp/{filename} -C {archive_folder}/")

        run(f"sudo rm /tmp/{filename}")

        run(f"sudo mv {archive_folder}/web_static/* {archive_folder}")

        run(f"sudo rm -rf {archive_folder}/web_static")

        run("sudo rm -rf /data/web_static/current")

        run(f"sudo ln -s {archive_folder}/ /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception:
        return False

def deploy():
    """
    deployment function for web servers
    """
    pack = do_pack()

    if pack is None:
        return False

    deployment_status = do_deploy(pack)
    return deployment_status

