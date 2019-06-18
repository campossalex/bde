#!/usr/bin/python
import time
import datetime
import pytz
import numpy
import random
import gzip
import zipfile
import sys
import argparse
from faker import Faker
from random import randrange
from tzlocal import get_localzone
local = get_localzone()
from time import sleep
from random import randint

#todo:
# allow writing different patterns (Common Log, Apache Error log etc)
# log rotation


def convertLines(lines):
    head = lines[0]
    del lines[0]
    infoDict = {}
    for line in lines: #Going through everything but the first line
        infoDict[line.split(",")[0]] = [tuple(line.split(",")[1:])]
    return infoDict

def read_file(filename):
    thefile = open(filename, "r")
    lines = []
    for i in thefile:
        lines.append(i.rstrip("\n\r"))
    thefile.close()
    return lines

class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

parser = argparse.ArgumentParser(__file__, description="Fake Apache Log Generator")
parser.add_argument("--output", "-o", dest='output_type', help="Write to a Log file, a gzip file or to STDOUT", choices=['LOG','GZ','CONSOLE'] )
parser.add_argument("--log-format", "-l", dest='log_format', help="Log format, Common or Extended Log Format ", choices=['CLF','ELF'], default="ELF" )
parser.add_argument("--num", "-n", dest='num_lines', help="Number of lines to generate (0 for infinite)", type=int, default=1)
parser.add_argument("--prefix", "-p", dest='file_prefix', help="Prefix the output file name", type=str)
parser.add_argument("--sleep", "-s", help="Sleep this long between lines (in seconds)", default=0.0, type=float)

args = parser.parse_args()

log_lines = args.num_lines
file_prefix = args.file_prefix
output_type = args.output_type
log_format = args.log_format

faker = Faker()

timestr = time.strftime("%Y%m%d-%H%M%S")
otime = datetime.datetime.now()

#outFileName = 'access_log_'+timestr+'.log' if not file_prefix else file_prefix+'_access_log_'+timestr+'.log'
outFileName = 'access.log' if not file_prefix else file_prefix+'_access_log_'+timestr+'.log'

for case in switch(output_type):
    if case('LOG'):
        f = open('/www/' + outFileName,'w')
        break
    if case('GZ'):
        f = gzip.open(outFileName+'.gz','w')
        break
    if case('CONSOLE'): pass
    if case():
        f = sys.stdout


product_catalog = convertLines(read_file("product_catalog.csv"))

response=["200","404","500","301"]

verb=["GET","PUT"]

resources=["/home","/item/id?skuID=","/item/id?skuID=","/item/id?skuID=","/cart/add_item.jsp?skuID=","/cart/rm_item.jsp?skuID=","/checkout/productid?skuID=","/search/product.jsp?skuID="]

ualist = [faker.firefox, faker.chrome, faker.safari, faker.internet_explorer, faker.opera]

flag = True
while (flag):
#    if args.sleep:
#        increment = datetime.timedelta(seconds=args.sleep)
#    else:
#        increment = datetime.timedelta(seconds=random.randint(30, 300))
#    otime += increment

    otime = datetime.datetime.now()
    otime -= datetime.timedelta(seconds=10800)
    ip = faker.ipv4()
    dt = otime.strftime('%d/%b/%Y:%H:%M:%S')
    tz = datetime.datetime.now(local).strftime('%z')
    vrb = numpy.random.choice(verb,p=[0.7,0.3])
    uri = numpy.random.choice(resources,p=[0.2,0.1,0.1,0.1,0.15,0.1,0.05,0.2])
    if uri.find("skuID")>0:
	product_key = random.choice(product_catalog.keys())
        uri += str(product_key)

    resp = numpy.random.choice(response,p=[0.9,0.04,0.02,0.04])
    byt = int(random.gauss(5000,50))
    referer = faker.uri()
    useragent = numpy.random.choice(ualist,p=[0.5,0.3,0.1,0.05,0.05] )()
    if log_format == "CLF":
        f.write('%s - - [%s %s] "%s %s HTTP/1.0" %s %s\n' % (ip,dt,tz,vrb,uri,resp,byt))
    elif log_format == "ELF": 
        f.write('%s - - [%s %s] "%s %s HTTP/1.0" %s %s "%s" "%s"\n' % (ip,dt,tz,vrb,uri,resp,byt,referer,useragent))
    f.flush()

    #log_lines = log_lines - 1
    #flag = False if log_lines == 0 else True
    if args.sleep:
	sleep(randint(100, 1500) / 1000)
#        time.sleep(randint(1, 2))

