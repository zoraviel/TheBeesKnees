import csv

def convert_to_dict(filename):
    datafile = open(filename, newline='')
    my_reader = csv.DictReader(datafile)
    list_of_dicts = list(my_reader)
    datafile.close()
    return list_of_dicts
