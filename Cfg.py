import configparser as cp
from utils import read_file


class Cfg(object):

    def __init__(self):
        self.config = cp.ConfigParser()
        self.config.read('config/settings.cfg')

        # SERVER
        self.server_url = self.config['SERVER']['url']
        self.server_origin = self.config['SERVER']['origin']

        # REST
        self.rest_status = self.config['REST']['status']
        self.rest_add_log = self.config['REST']['add_log']

        # LOGGING
        self.logging_ignored_services = read_file(self.config['LOGGING']['ignoredServices'])
