#!/usr/bin/env python

import sys
import time
import httplib
import argparse

appliance_ip = '192.168.10.70'


def runParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--backend', type=str, help='Full path to "*.tgz" file')
    parser.add_argument('-appl', '--appliance', type=str, help='IP address of Appliance')

    return parser


def updateFirmware(backend_path):
#    backend_path = build
    with open(backend_path, 'rb') as firwareBlob:
        print '-- Uploading firmware "%s" to %s Appliance' % (backend_path, appliance_ip)
        conn = httplib.HTTPConnection(appliance_ip)
        conn.request("POST", "/app/createUpdateFile/", firwareBlob)
        response = conn.getresponse()
        if response.status != 200:
            print >> sys.stderr, 'Firmware upload update failed:', response.status, response.reason
            sys.exit(2)
        conn.close()
        conn = httplib.HTTPConnection(appliance_ip)
        conn.request("GET", "/app/runUpdate/")
        response = conn.getresponse()
        if response.status != 200:
            print >> sys.stderr, 'Firmware update failed:', response.status, response.reason
            sys.exit(2)
        conn.close()
        for attempt in xrange(5):
            print '--   Waiting for appliance %s.. attempt %s' % (appliance_ip, attempt + 1)
            time.sleep(5)
            try:
                conn = httplib.HTTPConnection(appliance_ip)
                conn.request("GET", "/app/getAppInfo2")
                response = conn.getresponse()
                if response.status != 200:
                    print >> sys.stderr, 'Firmware post update check failed:', response.status, response.reason
                    sys.exit(2)
                conn.close()
                print 'Backend "' + backend_path + '" has been uploaded to Appliance successfully. \n'
                break
            except:
                pass


if __name__ == "__main__":

    options = runParser()
    optSpace = options.parse_args(sys.argv[1:])

    B_name = optSpace.backend
    appliance_ip = optSpace.appliance

    updateFirmware(B_name)