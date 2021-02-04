from mopidy_snapduck import Extension


def test_get_default_config():
    ext = Extension()

    config = ext.get_default_config()

    assert "[snapduck]" in config
    assert "enabled = true" in config
    assert "snapclient_path = /usr/bin/snapclient" in config
    assert "snapclient_args =" in config


def test_get_config_schema():
    ext = Extension()

    schema = ext.get_config_schema()

    assert "snapclient_path" in schema
    assert "snapclient_args" in schema
