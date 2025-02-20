## my_playlist_functions

## Brandon Bennett
## 31/01/2021

## This file contains some useful functions for extracting
## information from files in my CSV-based playlist file format.



## Import module for handling csv files.
import csv

## Simple function for reading CSV files into a "datalist".

## Input is a file name (str), which is assumed to refer to a CSV file.

## The result returned will be a list of lists, where:
## Each element of the returned list corresponds to a line of the
## CSV file and usually represents a data record of some kind.
## Each line/record is a list of strings, which are the data
## for that record (one string per column).

def get_datalist_from_csv( filename ):
    ## Create a 'file object' f, for accessing the file
    with open( filename ) as f:
        reader = csv.reader(f)     # create a 'csv reader' from the file object
        datalist = list( reader )  # create a list from the reader
    return datalist


## Function to convert a string representation of
## a time duration into the number of seconds in that duration.

## Input string can be in any of the forms: "S", "M:S" or "H:M:S",
## where H, M and S are digits representing hours, minutes and
## seconds.
## It is expected (but not enforced) that M and S will consist
## of either 1 or 2 digits.
## Output is an int which is the equivalent time in seconds.

def time_string_to_seconds(s):
    parts = s.split(':')
    parts = [int(p) for p in parts]
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        return parts[0]*60 + parts[1]
    if len(parts) == 3:
        return parts[0]*60*60 + parts[1]*60 + parts[2]
    print( "!!! ERROR: time_string_to_seconds: incorrect format:", s)
    return False

def get_playlist_length(filename):
    data = get_datalist_from_csv(filename)
    tracks = data[1:]
    time_strings = [record[3] for record in tracks]
    print(time_strings)
    playtimes = [time_string_to_seconds(ts) for ts in time_strings]
    return sum(playtimes)



