#!/usr/bin/env python3

# Author ID: drussell6

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    fs = output[0].decode("utf-8").strip()
    return fs