from .Division import Division

class Volunteer:
    id = 0

    def __init__(self, name: str, surname: str, availability: list[bool], preference: list[Division]): # TODO: list division si possible
        self.id = Volunteer.id
        Volunteer.id += 1
        self.name = name                
        self.surname = surname  
        self.availability = availability    
        self.preference = preference    

    def __repr__(self):
        timeSlotsStr = '|'
        for i in self.availability:
            timeSlotsStr += ' X|' if i else '  |'
        delimiter = ', '
        preferenceStr = delimiter.join(self.preference)
        return '_' * 52                                              + '\n' \
            + self.name + ' ' + self.surname                         + '\n' \
            + "| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|" + '\n' \
            + timeSlotsStr                                           + '\n' \
            + "preferences : " + preferenceStr                       + '\n' \
            + '_' * 52                                    
            # + ' | '.join([f'{i:02}:00' for i in list(range(8, 24)) + list(range(0, 3))]) + '\n' \
            # + ' | '.join([f'  {i}  ' for i in list(map(lambda b: 'X' if b else ' ', self.availability))]) + '\n' \
    
