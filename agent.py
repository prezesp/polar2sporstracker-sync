from app import App
from PyIOKitMatchingHandler import IOKitMatchingHandler
import os
import time
import yaml

# read configuration
workdir = os.path.dirname(os.path.realpath(__file__))
config = yaml.load(open(workdir+'/config.yml'))
delay = int(config['SYNC_DELAY']) if 'SYNC_DELAY' in config else 80

# handle macOS launch event
handler = IOKitMatchingHandler()
handler.handle()

# gives your polar time to synchronize with web app after plugged in
time.sleep(delay)

app = App()
app.run()
