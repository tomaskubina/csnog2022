from pygnmi.client import gNMIclient
import json

host = ('192.168.243.21', '50001')

with gNMIclient(target=host, username='username', password='password', insecure=True, debug=0) as gc:
    result = gc.get(path=[], encoding='json_ietf', datatype='config')
    print(json.dumps(result, indent=4))
