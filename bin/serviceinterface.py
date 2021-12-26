from subprocess import PIPE, run
import os

class ServiceManager():
    def __init__(self, service_name: str) -> None:
        self.service = service_name
        self.workingdir = os.getcwd()
        print(self.workingdir)

    def checkServiceStatus(self):
        status = run("{nssm} status {service}".format(
                    nssm = 'tools\\nssm.exe', 
                    service = self.service), 
                    stdout=PIPE, 
                    stderr=PIPE, 
                    universal_newlines=True, 
                    shell=True)
        result = status.stdout.replace("\x00", "")
        return result.replace("\n", "")

    def startService(self):
        command = run("{nssm} start {service}".format(
                    nssm = 'tools\\nssm.exe', 
                    service = self.service), 
                    stdout=PIPE, 
                    stderr=PIPE, 
                    universal_newlines=True, 
                    shell=True)
        
    def stopService(self):
        command = run("{nssm} stop {service}".format(
                    nssm = 'tools\\nssm.exe', 
                    service = self.service), 
                    stdout=PIPE, 
                    stderr=PIPE, 
                    universal_newlines=True, 
                    shell=True)