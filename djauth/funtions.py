import json, csv
def gettupleList_from_csv(filepath):
    with open(filepath, 'rb') as fp:
        list_tuple= [tuple((line[0], line[0])) for line in csv.reader(fp, skipinitialspace=True)]
        return tuple(list_tuple)