#!/usr/bin/python3
"""
script to deploy the static files on the server
"""


from fabric.api import *
import os


env.hosts = ['54.160.81.105', '34.227.90.3']
env.user = 'ubuntu'
env.key = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    function to deploy the files to the servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")

        filename = os.path.basename(archive_path)

        archive_folder = f"/data/web_static/releases/{filename.split('.')[0]}"

        #run(f"sudo rm -rf {archive_folder}/")

        run(f"sudo mkdir -p {archive_folder}/")

        run(f"sudo tar -xzf /tmp/{filename} -C {archive_folder}/")

        run(f"sudo rm /tmp/{filename}")

        run(f"sudo mv {archive_folder}/web_static/* {archive_folder}/")

        run(f"sudo rm -rf {archive_folder}/web_static")

        run("sudo rm -rf /data/web_static/current")

        run(f"sudo ln -s {archive_folder}/ /data/web_static/current")

        print("New version deployed!")
        return True
    except Exception as e:
        return False
