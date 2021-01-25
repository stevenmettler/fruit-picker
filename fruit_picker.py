#!/usr/bin/python

import sys
import csv
import pandas as pd
from collections import Counter

csv_name = sys.argv[1]

# read csv
with open(csv_name) as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    data_read = [row for row in reader]

df = pd.read_csv(csv_name, sep=',', encoding="utf-8", skipinitialspace=True)

tuples = [tuple(x) for x in df.values]

# number of fruit total
print("Total number of fruit: %d\n" % len(tuples))

# total types of fruit
fruit_types = set()
for elem in tuples:
    fruit_types.add(elem[0])

print("Types of fruit: %d\n" % len(fruit_types))

# counts of individual fruits descending order
fruit_counts = Counter(elem[0] for elem in tuples)
print("The number of each type of fruit in descending order:")
for key, value in fruit_counts.most_common():
    print("%s: %d" % (key, value))

print("\n")

# groups of fruit, pair if identical tuples
fruit_type_tuples = []
fruits_expired = []
for elem in tuples:
    fruit_type_tuples.append(tuple(x for x in elem if isinstance(x, str)))
    if elem[1] > 3:
        fruits_expired.append((elem[0]))

# helper function to format fruit plurality in output


def format_output(num, fruit):
    if num > 1:
        return("%d %ss" % (num, fruit))
    elif num == 1:
        return("1 %s" % fruit)


print("The characteristics of each fruit type:")

fruit_characteristics = {}
# initialize data structure: dictionary with key, value as {(fruit_name, (characteristic1, characterisitic2)) : count}
for elem in fruit_type_tuples:
    # sort characteristics alphabetically so that there are no duplicates
    characteristics = tuple(sorted((elem[1], elem[2])))
    if not (elem[0], characteristics) in fruit_characteristics:
        fruit_characteristics[(elem[0], characteristics)] = 1
    else:
        fruit_characteristics[(elem[0], characteristics)] += 1

# print out list of fruit counts, names, characteristics
for fruit, characteristic in fruit_characteristics:
    count = fruit_characteristics[(fruit, characteristic)]
    print("%s: %s, %s" % (format_output(count, fruit),
                          characteristic[0], characteristic[1]))


# given a list of tuples where the first element of each tuple is always a fruit, compare the latter two elements in each tuple to see if equal
fruits_expired_counts = Counter(elem for elem in fruits_expired)
print("\n")
output = ""
for i, elem in enumerate(fruits_expired_counts):
    if i == len(fruits_expired_counts)-1:
        output += ("and %s are older than 3 days." %
                   format_output(fruits_expired_counts[elem], elem))
    else:
        output += ("%s, " % format_output(fruits_expired_counts[elem], elem))

print(output)
