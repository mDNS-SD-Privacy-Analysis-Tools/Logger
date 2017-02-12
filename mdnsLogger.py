from time import sleep
from zeroconf import ServiceBrowser, Zeroconf, ZeroconfServiceTypes, BadTypeInNameException
from ServiceListener import ServiceListener
from Cfg import Cfg

config = Cfg()
while True:
    services = ZeroconfServiceTypes.find()
    zeroconf = Zeroconf()
    listener = ServiceListener(config)

    for service in services:
        str_service = str(service)
        if str_service not in config.logging_ignored_services:
            print("service found: " + str_service)
            try:
                browser = ServiceBrowser(zeroconf, str(service), listener)
            except BadTypeInNameException:
                pass
        else:
            print("ignoring: " + str_service)

    try:
        sleep(15)
    finally:
        zeroconf.close()
    try:
        sleep(15)
    except Exception:
        pass

