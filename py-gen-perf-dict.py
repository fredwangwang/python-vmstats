import argparse
import atexit
import getpass
import json

from pyVim.connect import SmartConnect, SmartConnectNoSSL, Disconnect


def GetArgs():
    """
    Supports the command-line arguments listed below.
    """
    parser = argparse.ArgumentParser(description='Process args for retrieving all the Virtual Machines')
    parser.add_argument('-H', '--host', required=True, action='store', help='Remote host to connect to')
    parser.add_argument('-P', '--port', type=int, default=443, action='store', help='Port to connect on')
    parser.add_argument('-u', '--user', required=True, action='store', help='User name to use when connecting to host')
    parser.add_argument('-p', '--password', required=False, action='store', help='Password to use when connecting to host')
    parser.add_argument('-k', '--skip-ssl-validation', required=False, action='store_true', help='skip ssl certificate check')
    args = parser.parse_args()
    return args


def main():
    args = GetArgs()
    si = None
    if args.password:
        password = args.password
    else:
        password = getpass.getpass(prompt="Enter password for host {} and user {}: ".format(args.host, args.user))
    try:
        if args.skip_ssl_validation:
            si = SmartConnectNoSSL(host=args.host,
                                   user=args.user,
                                   pwd=password,
                                   port=int(args.port))
        else:
            si = SmartConnect(host=args.host,
                              user=args.user,
                              pwd=password,
                              port=int(args.port))
    except IOError as e:
        pass
    if not si:
        print('Could not connect to the specified host using specified username and password')
        return -1

    atexit.register(Disconnect, si)
    content = si.RetrieveContent()

    # Get all the performance counters
    perf_dict = {}
    perf_list = content.perfManager.perfCounter
    for counter in perf_list:
        counter_full = "{}.{}.{}".format(counter.groupInfo.key, counter.nameInfo.key, counter.rollupType)
        perf_dict[counter_full] = {'key': counter.key, 'summary': counter.nameInfo.summary}
    with open('perf_dict.json', 'w') as out:
        json.dump(perf_dict, out, indent=2)


# Start program
if __name__ == "__main__":
    main()
