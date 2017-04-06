"""FERENGI's main configuration"""

from configparserplus import ConfigParserPlus

__all__ = ['config']


class FerengiConfig(ConfigParserPlus):
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
