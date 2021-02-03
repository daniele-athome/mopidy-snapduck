Mopidy-Snapduck
===============

Mopidy extension that controls its own instance of the [Snapcast client](https://github.com/badaix/snapcast).

In a [multi-room, multi-Mopidy configuration](https://www.home-assistant.io/blog/2016/02/18/multi-room-audio-with-snapcast/)
the sound card of a room speaker is either owned by Snapcast client or by the local Mopidy instance. This extension will
start `snapclient` when Mopidy is stopped and stops it when Mopidy is playing.

## Installation

Install by running:

```
sudo python3 -m pip mopidy-snapduck
```

## Configuration

TODO
