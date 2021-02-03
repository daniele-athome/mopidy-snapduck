import pathlib

import pkg_resources

from mopidy import config, ext

__version__ = pkg_resources.get_distribution("Mopidy-Snapduck").version


class Extension(ext.Extension):

    dist_name = "Mopidy-Snapduck"
    ext_name = "snapduck"
    version = __version__

    def get_default_config(self):
        return config.read(pathlib.Path(__file__).parent / "ext.conf")

    def get_config_schema(self):
        schema = super().get_config_schema()
        schema["snapclient_path"] = config.Path(optional=True)
        schema["snapclient_args"] = config.String(optional=True)
        return schema

    def setup(self, registry):
        from .frontend import SnapduckFrontend

        registry.add("frontend", SnapduckFrontend)
