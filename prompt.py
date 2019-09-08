# python clone of tagtime http://messymatters.com/tagtime/

# set cron job with $crontab -e
# * * * * * DISPLAY=:1 python3 /path/to/prompt.py 2> /tmp/err
# this fires once a minute 
# set debugging = True first to make sure cron job fires
# check /tmp/err for problems if it doesn't fire

# or use a cron alternative as desired. 
# just needs to fire every minute or so.

import pymsgbox
import datetime
import numpy
import time 

debugging = False
avg_delay = 30 # minutes

time_path = "/home/zephyr/workspace/biohacking/flow/time.txt"
log_path  = "/home/zephyr/workspace/biohacking/flow/log.txt"
prompt    = 'What are you doing right at this moment?'

if debugging == False:
	# check if we're due for a log
	curr_time = int(time.time())
	with open(time_path, "r") as f:
		data = int(float(f.read().split("\n")[0]))
		if data > curr_time:	
			exit()

# prompt user
response = pymsgbox.prompt(prompt)

# record response as follows: 
# Sep 7 18:10 | response
ts = datetime.datetime.now().strftime("%b %d %H:%M") 
with open(log_path, "a") as myfile:
    myfile.write(str(ts) + " | " + response + "\n")

# select next time we should prompt user
next_delay = numpy.random.exponential(avg_delay)*60
next_time  = str(curr_time + next_delay)
with open(time_path, "w") as f:
	f.write(next_time)






