from data.Volunteer import Volunteer
from data.Division import Division
from data.data import data_to_volunteers, data_to_divisions, get_config
from data.Solver import Solver

volunteers = data_to_volunteers('ressources/volunteers.csv')
divisions = data_to_divisions('ressources/divisions.csv')

config = get_config('ressources/sample.ini')

shifts = []
for d in range(int(config.get('Days', 'days'))):
    for s in config.get('Days', 'day' + str(d + 1)).split('_'):
        shifts.append(s)
print(shifts)

solver = Solver(len(volunteers), len(shifts), len(divisions))

# if not config.getboolean('constraints', 'is_multitasking'):
#     solver.DisableMultitasking()
# if config.get('constraints', 'max_tasks') != '':
#     solver.LimitDifferentTasks(config.getint('constraints', 'max_tasks'))
# if config.get('constraints', 'break') != '':
#     solver.AddBreaks(config.getint('constraints', 'break'))
# if config.getboolean('constraints', 'is_distribute_tasks_evenly'):
#     solver.DistributeShiftsEvenly()
