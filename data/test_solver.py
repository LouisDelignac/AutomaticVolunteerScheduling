from Solver import Solver
import time

num_volunteers = 10
num_shifts = 6                          # staff slot : 8h00 - 2h00 each day => 1 shift = 3h00
num_days = 1
num_divisions = 3                       # Sécurité, Bar, Logistique
all_volunteers = range(num_volunteers)
all_shifts = range(num_shifts)
all_days = range(num_days)
all_divisions = range(num_divisions)
div_human_needs = [
    [                                   # Jour 1
        [2, 0, 6],                      # Shift 1 (Sécurité, Bar, Logistique)
        [2, 0, 6],                      # Shift 2
        [2, 2, 4],                      # ...
        [2, 4, 0],
        [2, 6, 0],
        [4, 6, 0]
    ]
]
# TODO: Constraint when shift request = -1 => volunteer not available
shift_requests = [
    [[1, 1, 0, 0, -1, -1]],
    [[1, 1, 0, 0, 0, 0]],
    [[1, 1, 0, 0, 0, 0]],
    [[1, 1, 1, 1, 1, 1]],
    [[0, 0, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 1, 1]],
    [[0, 0, 0, 0, 1, 1]],
    [[0, 0, 0, 1, 1, 1]],
    [[0, 0, 0, 0, 0, -2]],
    [[0, 1, 1, 1, 1, 0]]
]
division_requests = [ # TODO: ça marche pas
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 1, 1],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [-5, 10, -5],
    [0, 1, 1]
]

start_time = time.time()

solver = Solver(num_volunteers, num_shifts, num_days, num_divisions)
solver.CreateModel()
solver.CreateVariables()
solver.DisableMultitasking()
solver.LimitDifferentTasks(2)
solver.DivisionRequirements(div_human_needs)
solver.VolunteerAvailability(shift_requests)
solver.DistributeShiftsEvenly()
solver.MaximizeDivisionRequests(division_requests)
solver.Solve()

end_time = time.time()
total_duration = end_time - start_time
print("Durée d'exécution:", total_duration, "secondes")