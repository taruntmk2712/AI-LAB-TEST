#Vaccum cleaner
import random

class Environment(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = {'A': '0', 'B': '0'}

        # randomize conditions in locations A and B
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print (Environment.locationCondition)
        # Instantiate performance measurement
        Score = 0
        # place vacuum at random location
        vacuumLocation = random.randint(0, 1)
        # if vacuum at A
        if vacuumLocation == 0:
            print ("Vacuum is randomly placed at Location A.")
            # and Location A is Dirty.
            if Environment.locationCondition['A'] == 1:
                print ("Location A is Dirty.")
                # suck the dirt  and mark it clean
                Environment.locationCondition['A'] = 0;
                Score += 1
                print ("Location A has been Cleaned.")
                # move to B
                print ("Moving to Location B...")
                Score -= 1
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned.")
            else:
                # move to B
                Score -= 1
                print ("Moving to Location B...")
                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print ("Location B is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print ("Location B has been Cleaned.")

        elif vacuumLocation == 1:
            print ("Vacuum cleaner randomly placed at Location B.")
            # and B is Dirty
            if Environment.locationCondition['B'] == 1:
                print ("Location B is Dirty.")
                # suck and mark clean
                Environment.locationCondition['B'] = 0;
                Score += 1
                print ("Location B has been Cleaned.")
                # move to A
                Score -= 1
                print ("Moving to Location A...")
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned.")
            else:
                # move to A
                print ("Moving to Location A...")
                Score -= 1
                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print ("Location A is Dirty.")
                    # suck and mark clean
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print ("Location A has been Cleaned.")
        # done cleaning
        print (Environment.locationCondition)
        print ("Performance Measurement: " + str(Score))


theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)


'''
{'A': 1, 'B': 1}
Vacuum is randomly placed at Location A.
Location A is Dirty.
Location A has been Cleaned.
Moving to Location B...
Location B is Dirty.
Location B has been Cleaned.
{'A': 0, 'B': 0}
Performance Measurement: 1


{'A': 0, 'B': 1}
Vacuum is randomly placed at Location A.
Moving to Location B...
Location B is Dirty.
Location B has been Cleaned.
{'A': 0, 'B': 0}
Performance Measurement: 0



{'A': 1, 'B': 1}
Vacuum cleaner randomly placed at Location B.
Location B is Dirty.
Location B has been Cleaned.
Moving to Location A...
Location A is Dirty.
Location A has been Cleaned.
{'A': 0, 'B': 0}
Performance Measurement: 1



{'A': 0, 'B': 0}
Vacuum cleaner randomly placed at Location B.
Moving to Location A...
{'A': 0, 'B': 0}
Performance Measurement: -1

'''
