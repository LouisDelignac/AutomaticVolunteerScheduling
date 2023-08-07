import configparser
import csv
from .Volunteer import Volunteer
from .Division import Division

# filename = 'ressources/sample.ini'
def get_config(filename: str) -> configparser.ConfigParser:
    """ Returns a ConfigParser object from a ini file """
    config = configparser.ConfigParser()
    config.read(filename)
    return config

# filename = 'data/volunteers.csv'
def data_to_volunteers(filename: str) -> list:
    """ Returns a list of Volunteer objects from a csv file """
    volunteers = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader: # reads the csv line by line
            # TODO: taille des tableaux "Disponibilités"
            volunteers.append(Volunteer(row['Prénom'], row['Nom'], row['Disponibilités [Créneaux]'].replace('h', '').split(';'), row['Préférences'].split(';')))
    return volunteers

# filename = 'data/divisions.csv'
def data_to_divisions(filename: str) -> list:
    """ Returns a list of Volunteer objects from a csv file """
    divisions = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader: # reads the csv line by line
            # TODO: taille des tableaux "Créneaux" et "Besoins humains"
            divisions.append(Division(row['Nom'], row['Créneaux'].replace('h', '').split(';'), row['Besoins humains']))
    return divisions