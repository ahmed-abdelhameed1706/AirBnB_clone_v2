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
    filename = f"web_static_{time}.tgz"
    local("sudo mkdir -p versions")
    archive_path = local(f"sudo tar -cvzf versions/{filename} web_static")

    if archive_path:
        return archive_path
    else:
        return None
