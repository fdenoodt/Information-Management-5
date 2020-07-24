import datetime
import csv
import subprocess

##

date_time = datetime.datetime.now()
print(date_time, type(date_time))
##
date_time.strftime('%a, %d %b %Y %H:%M:%S')

##

speedtest_cmd = "speedtest-cli --simple"
process = subprocess.Popen(speedtest_cmd.split(), stdout=subprocess.PIPE)
process_output = process.communicate()[0]

##
print(process_output)


##
print(process_output, type(process_output))

##

process_output = process_output.split()
# and we add the date and time 
process_output.append(date_time)

##

process_output
##

