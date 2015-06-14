# Launches the server as a deamon

import deamon

from server import run_server
with deamon.DeamonContext():
    run_server()
    
