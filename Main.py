from data.Volunteer import Volunteer
from data.Division import Division
from data.data import data_to_volunteers, data_to_divisions

volunteers = data_to_volunteers('ressources/volunteers.csv')
divisions = data_to_divisions('ressources/divisions.csv')

print(divisions[0])
