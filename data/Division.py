# Author:  Delignac Louis
# Purpose: This file contains the Division class.
#          A division has a list of time slots that a volunteer can work.
#          A division also has a number of volunteers that can work per hour in that division.
# Warning: If a time slot is False, then the number of volunteers that can work must be 0.
class Division:
    def __init__(self, name: str, timeSlots: list[bool], human_needs: list[int]):
        self.name = name                      
        self.timeSlots = timeSlots            
        self.human_needs = human_needs    
    
    def __repr__(self):
        timeSlotsStr = '|'
        numVolunteersStr = '|'
        for i in self.timeSlots:
            timeSlotsStr += ' X|' if i else '  |'
        for i in self.human_needs:
            numVolunteersStr += ' ' + str(i) + '|'
        return '_' * 52                                              + '\n' \
            + self.name                                              + '\n' \
            + "| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|" + '\n' \
            + timeSlotsStr                                           + '\n' \
            + numVolunteersStr                                       + '\n' \
            + '_' * 52