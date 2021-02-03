from __future__ import unicode_literals

import logging

import os.path

from mopidy.core import CoreListener

import pykka

logger = logging.getLogger(__name__)


class SnapduckFrontend(pykka.ThreadingActor, CoreListener):
    def __init__(self, config, core):
        super().__init__()
        self.snapcast_path = config['snapduck']['snapclient_path']
        self.snapcast_args = config['snapduck']['snapclient_args']
        self.core = core

    def on_start(self):
        pass

    def on_stop(self):
        pass

    def track_playback_paused(self, tl_track, time_position):
        pass

    def track_playback_started(self, tl_track):
        pass

    def track_playback_resumed(self, tl_track, time_position):
        pass

    def track_playback_ended(self, tl_track, time_position):
        pass
