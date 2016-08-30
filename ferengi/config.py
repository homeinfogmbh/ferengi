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

    @property
    def facebook(self):
        self.load()
        return self['facebook']

    @property
    def guess_pic(self):
        self.load()
        return self['guess_pic']

    @property
    def news(self):
        self.load()
        return self['news']

    @property
    def quotes(self):
        self.load()
        return self['quotes']

    @property
    def weather(self):
        self.load()
        return self['weather']


config = FerengiConfig('/etc/ferengi.conf')
