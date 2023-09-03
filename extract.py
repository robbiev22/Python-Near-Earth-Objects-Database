"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # an empty collection for storing the NearEarthObject instances
    neos = []
    # opens the provided file containing the NEO data
    with open(neo_csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # iterates over the rows in the file and extracts the
        # relevant features
        for row in reader:
            # creates an NearEarthObject instance and appends it to
            # the collection
            neos.append(NearEarthObject(designation=row[3], name=row[4],
                diameter=row[15], hazardous=row[7]))
    
    return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # an empty collection for storing the CloseApproach instances
    cas = []
    # opens the provided file containing the NEO data
    with open(cad_json_path, 'r') as file:
        data = json.load(file)
        # iterates over the rows in the file and extracts the
        # relevant features
        for row in data['data']:
            # creates and appends the CloseApproach object to the
            # collection
            cas.append(CloseApproach(designation=row[0], time=row[3],
             distance=row[4], velocity=row[7]))
    
    return cas
