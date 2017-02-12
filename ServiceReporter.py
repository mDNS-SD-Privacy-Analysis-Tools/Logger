import requests
import json
from time import gmtime, strftime


class ServiceReporter(object):

    def __init__(self, config):
        self.config = config

    @staticmethod
    def make_string(data):
        try:
            return data.decode("utf-8")
        except AttributeError:
            return str(data)

    def report_service_instance_found(self, service_name, service_info):
        print("Service %s added, service info: %s" % (service_name, service_info))

        instance_name = str(service_info.name).replace('.' + str(service_info.type), '')
        service_name_full = str(service_info.type).replace('.local.', '')
        service_name_split = service_name_full.split('.')

        txt_param = []
        for key, value in service_info.properties.items():
            txt_entry = {
                "name": self.make_string(key),
                "content": self.make_string(value),
            }
            txt_param.append(txt_entry)

        request_dict = {
            "instance": instance_name,
            "service": service_name_split[0],
            "service_protocol": service_name_split[1],
            "domain": "local",
            "origin": self.config.server_origin,
            "server": service_info.server,
            "port": str(service_info.port),
            "time": strftime("%d-%m-%Y %H:%M:%S", gmtime()),
            "txtDataList": txt_param,
        }   

        self.execute_request(request_dict)

    def execute_request(self, request_dict):
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.config.server_url + self.config.rest_add_log, data=json.dumps(request_dict),
                          headers=headers)
        if r.status_code != requests.codes.ok:
            print("An error occured! while adding: " + request_dict)

