"""FERENGI's main configuration"""

from homeinfo.lib.config import Configuration

__all__ = ['config']


class FerengiConfig(Configuration):
    """HIPSTER's main config parser"""

    @property
    def core(self):
        self.load()
        return self['core']

    @property
    def db(self):
        self.load()
        return self['db']


config = FerengiConfig('/etc/ferengi.conf')
