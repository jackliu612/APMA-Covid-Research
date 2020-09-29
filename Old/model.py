from mesa import Agent, Model

class Person(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)

class Student(Person):
    """An student with unique id."""
    def __init__(self, unique_id, major, model):
        super().__init__(unique_id, model)
        self.major = major
    
    def scheduleMaker(self, classes, meals):
        """
        Creates a schedule for the student with sleep, dorm, class, recreation, and dining times
        Schedule is stored in an array of length 144
        classes and meals are integers denoting how many are in a day
        Weekend schedules are defined as classes = 0
        """
        schedule = []
        diningCount = 0
        breakfastTime = int(self.random.random()*30)+36
        lastMealTime = breakfastTime
        classCount = 0
        returnTime = int(self.random.random()*24)+120
        i = 0
        while i < 144:
            if i < breakfastTime:
                schedule.append('dorm')
                i += 1
            elif i == breakfastTime:
                diningCount += 1
                for x in range(3):
                    schedule.append('dining')
                    i += 1
            elif i < 120:
                if classCount < classes and self.random.random() < 0.2:
                    classCount += 1
                    for x in range(6):
                        schedule.append('class')
                        i += 1
                if diningCount < meals and self.random.random() < 0.2 and i - lastMealTime > 24:
                    for x in range(4):
                        schedule.append('dining')
                        i += 1
                schedule.append('other')
                i += 1
            elif i <= returnTime:
                schedule.append('other')
                i+= 1
            else:
                schedule.append('dorm')
                i += 1
        return schedule

class Staff(Person):
    """An student with unique id."""
    def __init__(self, unique_id, major, model):
        super().__init__(unique_id, model)
        self.major = major
    
    def scheduleMaker(self, classes, meals):
        """
        Creates a schedule for the student with sleep, dorm, class, recreation, and dining times
        Schedule is stored in an array of length 144
        Weekend schedules are defined as classes = 0
        """
        schedule = []
        return schedule

class SchoolModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        # Create agents
        for i in range(self.num_agents):
            a = Student(i, "Engineer", self)