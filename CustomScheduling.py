import os
import traceback
from ContDeploy import ScheduledDeployment

if __name__ == "__main__":

    try:
        currentPath = os.path.dirname(os.path.abspath(__file__)) 
        scheduleScr = ScheduledDeployment(currentPath, 'cont_deploy.yml')
        scheduleScr.scheduleTime()
        scheduleScr.watch_schedule()
    except:
        exception = traceback.format_exc()
    
        if 'Completed' not in exception:
            print exception
        else:
            print 'Completed.'
