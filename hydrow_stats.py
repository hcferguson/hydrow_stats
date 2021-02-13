#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" A simple script to reformat the statistics for a hydrow workout into csv."""

__author__ = "Henry C. Ferguson"
__version__ = "0.2.0"
__license__ = "MIT"

import requests
import re
import json
import sys
import argparse


def fetch_json_data(url):
    """ Return the JSON data from a hydrow workout html file """
    # Fetch the html
    response = requests.get(url)
    # Search for the JSON data within the html
    pattern = re.compile('{"dataManager":.*}}}')
    result = pattern.findall(response.text)
    data = json.loads(result[0])
    return data

def parse_json_data(data,sep='\t'):
    """ Extract the data from json into a dictionary and a string """
    # Set up the dictionary
    keys = ['date','rower','meters','duration','split','spm',
            'watts','calories','resistance','instructor','workout']
    workout = {}

    # Pointers to portions of the data
    metadata = data['props']['pageProps']['workout']
    stats = data['props']['pageProps']['workout']['workoutStats']

    # Put the data in the dictionary
    workout['workout']    = metadata['workoutVideo']['name']
    workout['instructor'] = metadata['workoutVideo']['instructorName']
    workout['category']   = metadata['workoutVideo']['categoryName']
    workout['rower']      = metadata['rower']['screenName']
    workout['date']       = metadata['startTime']
    workout['calories']   = stats['calories']
    workout['duration']   = stats['elapsedTime']
    workout['resistance'] = stats['hydrowResistance']
    workout['meters']     = stats['meters']
    workout['split']      = stats['splitTime']
    workout['spm']        = stats['strokesPerMinute']
    workout['watts']      = stats['watts']

    # Format the string
    workout_string = sep.join([str(workout[k]) for k in keys])

    return workout, workout_string

if __name__ == "__main__":
    """ Usage format_hydro_stats.py url -sep separator """
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Extract hydrow workout data from web page.')
    parser.add_argument('url', 
        help='The URL of the workout (obtain by emailing yourself the workout from the hydrow app)')
    parser.add_argument('--sep', dest='separator', default='\t',
        help='separator between fields (default is tab. "--sep ," to change this to a comma)')
    args = parser.parse_args()
    url = args.url
    sep = args.separator

    # Get the data
    data = fetch_json_data(url)
    workout, workout_string = parse_json_data(data,sep=sep)
    
    print(workout_string)
