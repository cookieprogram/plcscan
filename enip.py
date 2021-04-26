'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
Get the properties of a module in the specified slot

In this example, we're getting the slot 0 module
properties
'''
from pylogix import PLC

PLC_id_file = open("PLC_IDs.txt", 'a')

def Scan(host):
    plc_ip = host
    with PLC() as comm:
        comm.IPAddress = plc_ip
        prop = comm.GetModuleProperties(0)
        if prop.Value.ProductName:
            PLC_id_file.write("AB" + " | " + plc_ip + " | " + prop.Value.Vendor + " " + prop.Value.ProductName + '\n')
        print prop.Value.ProductName, prop.Value.Revision
