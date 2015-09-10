"""
Author: Sujayyendhiren Srinivasamurthi
Email: sujayy1983@gmail.com
Description: Schedule deployment with this script/application
"""
import sys
import yaml
import time
import schedule
import traceback
import subprocess

class ScheduledDeployment(object):

    def __init__(self, scriptPath, script):
        """Initialize scripts"""
        try:
            self.confFile = scriptPath + '/conf/' + script 
            confFD = open(self.confFile, 'r')
            self.separator = '\n+++++++++++++++++++++++++\n'
            self.configs = yaml.load(confFD)
            self.time = self.configs['TIME']
            self.commands = self.configs['SHELL_EXECUTE']
            self.output = ''
        except:
            traceback.print_exc(file=sys.stdout)
            sys.exit(-1)

    def execute_shell_handler(self):
        """Execute shell handler."""
        try:
            count = 1
            for commandInfo in self.commands:
                command = commandInfo['COMMAND'].split(' ')
                process = subprocess.Popen( command, cwd=commandInfo['SCRIPT_PATH'] ,stdout=subprocess.PIPE)
                out, err = process.communicate()
                self.output += self.separator + "Output" + str(count) + self.separator + str(out) + "\nError:\n" + str(err) + "\n"
                count+=1
        except:
            traceback.print_exc(file=sys.stdout)
            sys.exit(-1)

        print self.output
        raise Exception('Completed')

    def scheduleTime(self):    
        """Set schedule"""
        schedule.every().day.at(self.time).do(self.execute_shell_handler)

    def schedule_later(self, seconds, scriptPath, scriptName):
        """Schedule for later"""
        pass

    def watch_schedule(self):
        """Keep waching for desired schedule."""
        while(True):
            schedule.run_pending()
            time.sleep(15)
