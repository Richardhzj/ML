import random
import time

#The vacuum would have two location: A and B

def vacuum_world():
    # On each location, there will be two status:
    # 0 means clean square, and 1 means dirty
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': 0, 'B': 0}
    
    print("Initial Location Environment is: " + str(goal_state))
    print("Location state 0 means clean and 1 means dirty")
        
    print("Now randomly generate dirt in this world...")
    goal_state['A']=random.randint(0,1)
    
    goal_state['B']=random.randint(0,1)

    print("-------------------------------------------")
    print("now the world becomes: "+str(goal_state))
    
    # initial score is zero, each movement will cost 1 point, and after each suck will earn 5 points
    performance = 0
    
    # vacuum would randomly generate in one of the location
    # vacuum location: 0 is location A and 1 is location B
    vacuum_loc = random.randint(0,1)
    print("vacuum initializing...")

    # Vacuum first appear in location A
    if vacuum_loc == 0:
        print("vacuum first appear in location A")
        # location A is originally dirty
        if  goal_state['A'] == 1:
            print("Location A is dirty, now suck.")
            
            # suck the dirt and mark it as clean
            goal_state['A'] = 0
            #earn points for suck
            performance+=5 
            
            print("Earn 5 points from sucking... Now the point is: " + str(performance))
            print("Location A has been cleaned.")
            print("Now move to location B")
            
            # cost one point for movement
            performance-=1  
            print("Cost 1 point for moving right... Now the point is: " + str(performance))
            
            
            # after clean location A, move right to location B
            if goal_state['B'] == 1:
                print("Location B is dirty, now suck.")
                
                performance+=5 
                print("Earn 5 points from sucking... Now the point is: " + str(performance))                    
               
                # suck the dirt and mark it as clean
                goal_state['B'] = 0
                print("Location B has been Cleaned. ")
            else:
                print("No action,location B is already clean.")
                
        # location A is originally clean       
        elif goal_state['A'] == 0:
            print("No action,location A is already clean ")
            print("Now move to location B")
            # cost one point for movement
            performance-=1  
            print("cost 1 point for moving right... Now the point is: " + str(performance))
            
            # check if location B is clean
            if goal_state['B'] == 1:
                print("Location B is dirty, now suck.")
                #earn points for suck
                performance+=5 
                print("Earn 5 points from sucking... Now the point is: " + str(performance))
                
                goal_state['B'] = 0
                print("Location B has been cleaned.")
            else:
                print("no action, location B is already clean")

    else:
        # Vacuum first appear in location B
        print("vacuum first appear in location B")
        # Location B is Dirty.
        if goal_state['B'] == 1:
            print("Location B is dirty, now suck.")
            
            # suck the dirt and mark it as clean
            goal_state['B'] = 0
            #earn points for suck
            performance+=5 
            
            print("Earn 5 points from sucking... Now the point is:" + str(performance))
            print("Location B has been cleaned.")
            print("Now move to location A")
            
            # cost one point for movement
            performance-=1  
            print("Cost 1 point for moving left... Now the point is:" + str(performance))

            if goal_state['A'] == 1:
                print("Location A is dirty, now suck.")
                
                performance+=5 
                print("Earn 5 points from sucking... Now the point is:" + str(performance))                    
               
                # suck the dirt and mark it as clean
                goal_state['A'] = 0
                print("Location A has been cleaned. ")
            else:
                print("No action,location A is already clean.")

        else:
        # location B is originally clean       
            if goal_state['B'] == 0:
                print("No action,location B is already clean ")
                print("Now move to location A")
                # cost one point for movement
                performance-=1  
                print("cost 1 point for moving left... Now the point is:" + str(performance))
            
            # check if location A is clean
            if goal_state['A'] == 1:
                print("Location A is dirty, now suck.")
                #earn points for suck
                performance+=5 
                print("Earn 5 points from sucking... Now the point is:" + str(performance))
                
                goal_state['A'] = 0
                print("Location A has been cleaned.")
            else:
                print("no action, location B is already clean")

    # done cleaning
    print("Current State is: ")
    print(goal_state)
    print("All clean! Vacuum temporally stop working...")
    print("Performance Measurement: " + str(performance))

check_interval=int(input("please set the vacuum check interval(unit:second): "))
while 1:
    vacuum_world()
    time.sleep(check_interval)
    print("---------------------------------------------------------------------")
    print("after a while, this world may become dirty again, check it once more.")
    print("---------------------------------------------------------------------")
