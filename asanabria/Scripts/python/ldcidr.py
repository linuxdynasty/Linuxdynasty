#!/usr/bin/python
# Brandon Sterne - CIDR Block Converter - 2007
import sys, re

def dec2bin(ip):
    d = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
    return  ''.join([d[int(dig)] for dig in oct(ip)]).zfill(8)

def bin2dec(ip):
    return int(ip, 2)

#def removeZeros(ip):
#    return re.sub("^[0]+", "", str(ip))
#def net_calc(ip):

def main():
    # get the CIDR block from the command line args
    try:
        cidrBlock = sys.argv[1]
    # if not specified on the CLI -> prompt the user for CIDR block
    except:
        cidrBlock = raw_input("CIDR Block: ")

    block = cidrBlock.split('/')
    #ipAddr = block[0].split(".")
    #print type(ipAddr)
    ipAddr = map(int, block[0].split("."))
    #print ipAddr
    subnet = int(block[1])
    print subnet
    ip = map(dec2bin, ipAddr)
    print ip
    print type(ip)
    print map(bin2dec, ip)
    for i in range(2**(32-subnet)):
        boo = dec2bin(i)
        print boo, "yah"
        iold = map(removeZeros, ip)
        print type(iold)
        print type(boo)
        iold.append(boo)
        print iold, map(bin2dec, iold)
        #inew = 
    #print ip
    # input validation returned an error
    #if not validateCIDRBlock(cidrBlock):
    #    printUsage()
    # print the user-specified CIDR block
    #else:
    #    printCIDR(cidrBlock)

if __name__ == "__main__":
    main()
