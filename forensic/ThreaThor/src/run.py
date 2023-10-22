#!/usr/bin/env python3

import os
port = 27545
command = 'socat -d -d tcp-l:' + str(port) + ',reuseaddr,fork EXEC:"python3 -u chall.py" '
os.system(command)