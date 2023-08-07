from ortools.sat.python import cp_model

class Solver:

    def __init__(self, num_volunteers, num_shifts, num_days, num_divisions):
        # Initialize the solver with the parameters.
        self.num_volunteers = num_volunteers
        self.num_shifts = num_shifts
        self.num_days = num_days
        self.num_divisions = num_divisions

        # Create the lists by length of the parameters.
        self.all_volunteers = range(self.num_volunteers)
        self.all_shifts = range(self.num_shifts)
        self.all_days = range(self.num_days)
        self.all_divisions = range(self.num_divisions)

        # Default values for the constraints.
        self.multitasking = True
        self.max_tasks = num_divisions
        # TODO: breaks
        self.division_requirements = []
        self.availabilities = []
        self.even_distribution = False
        self.division_requests = []

    def CreateModel(self):
        """Create the model."""
        self.model = cp_model.CpModel()

    def CreateVariables(self):
        """Create the variables."""
        self.shifts = {}
        for v in self.all_volunteers:
            for d in self.all_days:
                for s in self.all_shifts:
                    for p in self.all_divisions:
                        self.shifts[(v, d, s, p)] = self.model.NewBoolVar('shift_n%id%is%ip%i' % (v, d, s, p))
    
    def DisableMultitasking(self):
        """Each volunteer is assigned to at most one division per shift.""" 
        for v in self.all_volunteers:
            for d in self.all_days:
                for s in self.all_shifts:
                    self.model.AddAtMostOne(self.shifts[(v, d, s, p)] for p in self.all_divisions)

    def LimitDifferentTasks(self, max_tasks: int):
        """Each volunteer works at most in max_tasks differents divisions during the event."""
        # TODO: à corriger, bizzarement on peut pas faire le max d'un string...
        self.max_tasks = max_tasks
        # for v in self.all_volunteers:
        #     for d in self.all_days:
        #         self.model.Add(sum(max(self.shifts[(v, d, s, p)] for s in self.all_shifts) for p in self.all_divisions) <= self.max_tasks)

    def AddBreaks(self, max_continuous_work_period: int):
        # TODO
        pass

    def DivisionRequirements(self, division_requirements: list[list[list[int]]]):
        """Each division needs a certain number of volunteers each shift."""
        self.division_requirements = division_requirements
        for d in self.all_days:
            for s in self.all_shifts:
                for p in self.all_divisions:
                    self.model.Add(sum(self.shifts[(v, d, s, p)] for v in self.all_volunteers) >= self.division_requirements[d][s][p])

    def VolunteerAvailability(self, availabilities: list[list[list[int]]]):
        """Each volunteer is only available at certain shifts."""
        # TODO
        self.availabilities = availabilities
        for v in self.all_volunteers:
            for d in self.all_days:
                for s in self.all_shifts:
                    for p in self.all_divisions:
                        self.model.Add(self.shifts[(v, d, s, p)] <= availabilities[s][d][s])

    def DistributeShiftsEvenly(self):
        """Try to distribute the shifts evenly, so that each volunteer works
        min_shifts_per_volunteer shifts. If this is not possible, because the total
        number of shifts is not divisible by the number of volunteers, some 
        volunteers will be assigned one more shift."""
        if self.division_requirements == []:
            raise Exception("Division requirements must be set before calling DistributeShiftsEvenly")
        self.even_distribution = True
        sum_shifts_available = sum(self.division_requirements[d][s][p] for d in self.all_days for s in self.all_shifts for p in self.all_divisions)
        min_shifts_per_volunteer = sum_shifts_available // self.num_volunteers
        if sum_shifts_available % self.num_volunteers == 0:
            max_shifts_per_volunteer = min_shifts_per_volunteer
        else:
            max_shifts_per_volunteer = min_shifts_per_volunteer + 1
        for v in self.all_volunteers:
            self.model.Add(sum(self.shifts[(v, d, s, p)] for d in self.all_days for s in self.all_shifts for p in self.all_divisions) >= min_shifts_per_volunteer)
            self.model.Add(sum(self.shifts[(v, d, s, p)] for d in self.all_days for s in self.all_shifts for p in self.all_divisions) <= max_shifts_per_volunteer)

    def MaximizeDivisionRequests(self, division_requests: list[list[list[int]]]):
        # Create an objective function to maximize the number of division requests that are fulfilled. TODO: doesn't work
        self.model.Maximize(sum(division_requests[d][p] * self.shifts[(v, d, s, p)] \
                            for v in self.all_volunteers for d in self.all_days for s in self.all_shifts for p in self.all_divisions))

    def Solve(self):
        solver = cp_model.CpSolver()
        status = solver.Solve(self.model)

        if status == cp_model.OPTIMAL:
            print('X   |', end="")
            for s in self.all_shifts:
                print(s, '|', end="")
            print()
            print('-' * (self.num_shifts*4-1))
            for v in self.all_volunteers:
                print(f'{v:3}', '|', end="")
                for s in self.all_shifts:
                    is_working = False
                    for p in self.all_divisions:
                        if solver.Value(self.shifts[(v, 0, s, p)]) == 1:
                            print(p, '|', end="")
                            is_working = True
                    if not is_working:
                        print('  |', end="")
                print()
        
        else:
            print('No optimal solution found !')

    def __repr__(self) -> str:
        # Return str with data, all constraints, if objective funtion is defined, si le solver a été appelé et s'il a trouvé une solution
        pass