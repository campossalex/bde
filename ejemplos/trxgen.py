#!/usr/bin/python

import random
import MySQLdb
from faker import Faker
import random
import time
import datetime
from pprint import pprint

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

start = random.randint(1, random.randint(10, 55))
print("sleep for ", start, " seconds")
#time.sleep(start)

conn = MySQLdb.connect(host= "localhost", user="root", passwd="cloudera", db="ecommerce")
cur = conn.cursor()

fake = Faker()

otime = datetime.datetime.now()
otime -= datetime.timedelta(seconds=10800)
dt = otime.strftime('%Y-%m-%d:%H:%M:%S')

product_catalog = convertLines(read_file("product_catalog.csv"))
product_key = random.choice(product_catalog.keys())
customer = convertLines(read_file("customer.csv"))
customer_key = random.choice(customer.keys())

sku = product_key
state = fake.state()
description = product_catalog[product_key][0][0]
quantity = random.randint(1,6)
randday = int(random.randint(1,30))
customer_id = customer_key
price = product_catalog[product_key][0][1]

cur.execute ("INSERT INTO ecommerce.Transaction VALUES (NULL, %s, %s, %s, %s, %s, %s, %s) ", (sku, description, quantity, dt, price, customer_id, state))
## commit
conn.commit()
