from ServiceReporter import ServiceReporter


class ServiceListener(object):

    def __init__(self, config):
        self.serviceReporter = ServiceReporter(config)

    def remove_service(self, zeroconf, type, name):
        print("Service %s removed" % (name,))

    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        if info is not None:
            self.serviceReporter.report_service_instance_found(name, info)
