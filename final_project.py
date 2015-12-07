"""
Jonathan Stewart
Python 3200K
Fall 2015
Final Project
"""
from collections import namedtuple
from datetime import datetime

def get_slope(slope):
    """creates a factor based on the slope of the yard"""
    if slope <= 10:
        slopefactor = 1
    elif slope > 11 and slope <= 15:
        slopefactor = 1.05
    elif slope > 15 and slope <= 20:
        slopefactor = 1.13
    elif slope > 20 and slope <= 25:
        slopefactor = 1.20
    elif slope > 25:
        slopefactor = 0
    return slopefactor

def get_shade(shade):
    """creates a factor based on how much of the yard is covered in shade"""
    if shade <= 10:
        shadefactor = 1
    elif shade > 10 and shade <= 15:
        shadefactor = 1.1
    elif shade > 15 and shade <= 20:
        shadefactor = 1.2
    elif shade > 20 and shade <= 30:
        shadefactor = 1.3
    elif shade > 30 and shade <= 40:
        shadefactor = 1.4
    elif shade > 40 and shade <= 50:
        shadefactor = 1.5
    elif shade > 50 and shade <= 60:
        shadefactor = 1.6
    elif shape > 60:
        shadefactor = 0
    return shadefactor

def get_distance(distance):
    """creates a factor based on the distance that the address is away
from the shop"""
    if distance <= 5:
        distancefactor = 1
    elif distance > 5 and distance <= 10:
        distancefactor = 1.1
    elif distance > 10 and distance <= 15:
        distancefactor = 1.15
    elif distance > 15 and distance <= 20:
        distancefactor = 1.2
    elif distance > 20 and distance <= 25:
        distancefactor = 1.25
    elif distance > 25 and distance <= 30:
        distancefactor = 1.3
    elif distance > 30 and distance <= 35:
        distancefactor = 1.35
    elif distance > 35 and distance <= 40:
        distancefactor = 1.4
    elif distance > 40 and distance <= 45:
        distancefactor = 1.45
    elif distance > 45 and distance <= 50:
        distancefactor = 1.5
    elif distance > 50:
        distancefactor = 0
    return distancefactor

# makes named tuple (make it easier to keep up with all data (header)
Yard = namedtuple('Yard',
                  ['address', 'sq_ft', 'turf_type', 'slope', 'shade', 'distance'],
                  )

#opens csv file and stores it in 'f'
f = open("addresses.csv", 'r')
data = f.readlines()
f.close()

# asks for address
add = raw_input("What address are you interested in? ")

# iterates through file to find address
yard = None
for line in data:
    line = line.strip().split(',')
    if line[0].lower() == add.lower():
        print line[0]
        address, sq_ft, turf_type, slope, shade, distance = line
        sq_ft = float(sq_ft)
        slope = get_slope(float(slope))
        shade = get_shade(float(shade))
        distance = get_distance(float(distance))
        yard = Yard(address, sq_ft, turf_type, slope, shade, distance)
        price = (yard.sq_ft * .01) * (distance) * (slope) * (shade)
        if price == 0:
            report = open("report.txt", "a")
            report.write("{} - The property at {} may not be cost effective to treat.\n".format(datetime.now().isoformat(' ').split('.')[0], add))
            report.close()
            print "This yard may not be cost effective to treat"
        else:
            report = open("report.txt", "a")
            report.write("{} - The property at {} should be priced at ${}.\n".format(datetime.now().isoformat(' ').split('.')[0],
                                                                                     add, ("{0:.2f}".format(price))))
            report.close()
            print "$" + ("{0:.2f}".format(price))

if yard is None:
    report = open("report.txt", "a")
    report.write("{} - Address not found\n".format(datetime.now().isoformat(' ').split('.')[0]))
    report.close()
    print "The address you entered does not match any records."
    

# multiplies factors and square footage
##price = (yard.sq_ft * .01) * (distance) * (slope) * (shade)
##if price == 0:
##    print "This yard may not be cost effective to treat"
##else:
##    print price
        


# create text file, then write a report to it
##report = open("report.txt", "w")
##
##report.write("The property at {} should be priced at ${}.\n".format(add, price))
##
##report.close()



