from __future__ import unicode_literals

import logging

import subprocess
import shlex

from mopidy.core import CoreListener

import pykka

logger = logging.getLogger(__name__)


class SnapduckFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super().__init__()
        self.snapcast_path = config["snapduck"]["snapclient_path"]
        self.snapcast_args = config["snapduck"]["snapclient_args"] or ""
        self.core = core
        self.process = None

    def on_start(self):
        self.start_snapclient()

    def on_stop(self):
        self.stop_snapclient()

    def start_snapclient(self):
        if not self.process:
            logger.debug("Starting snapclient")
            self.process = subprocess.Popen(shlex.split(self.snapcast_path + " --logsink=stdout " + self.snapcast_args))

    def playback_state_changed(self, old_state, new_state):
        if new_state == "stopped":
            self.start_snapclient()
        else:
            self.stop_snapclient()

    def stop_snapclient(self):
        if self.process:
            logger.debug("Stopping snapclient")
            self.process.terminate()
            try:
                self.process.wait(1)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
