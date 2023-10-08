#!/usr/bin/python3
"""
fab file to pack the web_static
"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """
    function to pack the web_static folder
    """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    local("sudo mkdir -p versions")
    filename = f"versions/web_static_{time}.tgz"
    archive_path = local(f"sudo tar -cvzf {filename} web_static")

    if archive_path.succeeded:
        return filename
    else:
        return None
