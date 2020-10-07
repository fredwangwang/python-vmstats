python-vmstats
==============

Python script using pyVmomi to get VM statistics

## Sample Usage: 

`python3 py-vminfo.py -H vcenter.example.com -P 8443 -u admin -p password -m vm-name-1 -m vm-name-2 -k -i 5 -r 20`

to collect vm stats for 5 minutes rolling average every 20 seconds

## The script has the following parameters:

```
usage: py-vminfo.py [-h] -H HOST [-P PORT] -u USER [-p PASSWORD] -m VM [-k] [-i INTERVAL] [-r REPEAT]

Process args for retrieving all the Virtual Machines

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Remote host to connect to
  -P PORT, --port PORT  Port to connect on
  -u USER, --user USER  User name to use when connecting to host
  -p PASSWORD, --password PASSWORD
                        Password to use when connecting to host
  -m VM, --vm VM        On eor more Virtual Machines to report on
  -k, --skip-ssl-validation
                        skip ssl certificate check
  -i INTERVAL, --interval INTERVAL
                        Time interval in minutes to average the vSphere stats over
  -r REPEAT, --repeat REPEAT
                        Time in seconds to wait and retrieve data again. Perform one time statistics if not provided
```


