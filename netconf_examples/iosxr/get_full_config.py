import xmltodict
import xml.dom.minidom
from ncclient.xml_ import to_ele
import logging
from ncclient import manager


logging.basicConfig(level=logging.DEBUG)

with manager.connect(host='192.168.243.21',
                     port=830,
                     username='username',
                     password='password',
                     hostkey_verify=False,
                     device_params={'name': 'iosxr'}) as session:

    full_config = session.get_config(source='running').data_xml
    print(full_config)
