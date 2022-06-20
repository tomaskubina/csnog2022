# CSNOG 2022
This repository contains slides shared at CSNOG 2022 conference. It also contains several Python3 source code files to demonstrate 
way how to work with NETCONF and gNMI API by using Python libraries.  
  
Package [ncclient](https://github.com/ncclient/ncclient) was used for NETCONF testing and [gNMI](https://github.com/nokia/pygnmi) was used for gNMI protocol testing.

## How to use this repository
1. Install client libraries:
```bash
$ pip3 install -r requirements.txt
```
2. Enter folder with NETCONF or gNMI examples and select folder with scripts per OS platform. For example:
```bash
$ cd netconf_examples/iosxr
```
3. Open script based on RPC call type, change IP & port number and OS type if needed. Also update when needed content of request based on your network topology.
For NETCONF connection, modify parameters in connect() function:
```python
with manager.connect(host='192.168.243.21',
                     port=830,
                     username='username',
                     password='password',
                     hostkey_verify=False,
                     device_params={'name': 'iosxr'}) as session:
```  
For gNMI connection, modify parameters in gNMIclient() constructor and host variable:
```python
host = ('192.168.243.21', '50001')

with gNMIclient(target=host, username='username', password='password', insecure=True, debug=0) as session:
```
4. Enable NETCONF / gNMI on your device following vendor documentation.
5. Run script.
```python
$ python3 get_full_config.py
```
6. Enjoy data from your device! And test other RPC calls for NETCONF or gNMI.
