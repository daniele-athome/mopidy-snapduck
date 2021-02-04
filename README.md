Mopidy-Snapduck
===============

Mopidy extension that controls its own instance of the [Snapcast client](https://github.com/badaix/snapcast).

In a [multi-room, multi-Mopidy configuration](https://www.home-assistant.io/blog/2016/02/18/multi-room-audio-with-snapcast/)
the sound card of a room speaker is either owned by Snapcast client or by the local Mopidy instance. This extension will
start `snapclient` when Mopidy is stopped and stop it when Mopidy is playing.

## Installation

Install by running:

```
sudo python3 -m pip Mopidy-Snapduck
```

## Configuration

Before starting Mopidy, you must add configuration for Mopidy-Snapduck to your Mopidy configuration file::

```
[snapduck]
snapclient_path = /path/to/snapclient
snapclient_args = arguments_for_snapclient
```

The following configuration values are available:

* `snapduck/enabled`: If the snapduck extension should be enabled or not. Defaults to `true`.
* `snapduck/snapclient_path`: Path to the snapclient executable. Defaults to `/usr/bin/snapclient`.
* `snapduck/snapclient_args`: Arguments for snapclient. Defaults to none.

## ALSA

When using ALSA Mopidy will not release the sound card immediately after stopping, so it is recommended
to configure a dmix device to enable shared access between Mopidy and the Snapcast client.
