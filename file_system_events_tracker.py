import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/raveendraguturi/Downloads"

#event handler class
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey! {event.src_path} has been created!")

    def on_deleted(self,event):
        print(f"Oops! someone deleted {event.src_path}!")

    def on_moved(self,event):
        print(f" look! {event.src_path} has been modified!")

    def on_modified(self,event):
        print(f"look! someone moved {event.src_path} to {event.dest_path!")



#initilazie event handler
event_handler = FileEventHandler()

#initilaize observer
observer = Observer()

#schedule the observer
observer.schedule(event_handler, from_dir, recursive= True)


#start the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()