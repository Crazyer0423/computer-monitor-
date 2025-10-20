"""
import ‘psutil’ library for system information gathering (cpu and memory info)
'time' library for program delay (activate time_sleep() function)
import notification module from 'plyer' library for desktop notification(notification.notify ())
import 'datetime' library to get date and time
"""
import psutil
import time
from plyer import notification
from datetime import datetime

# Define a function named "usage_monitor", and set thresholds for both cpu and memory usage.
def usage_monitor(cpu_threshold=50,mem_threshold=50):
# use while true to start a loop, keep the program running continuously
    while True:
        current_time = datetime.now().strftime("%H:%M:%S") # Obtain the current time and format it as a string in hour:minute:second
        cpu_usage = psutil.cpu_percent(interval=1) # use psutil to obtain the cpu usage for the pasted 1 second.
        mem = psutil.virtual_memory() # use psutil to obtain the usage info of memory
        mem_usage = mem.percent # extract the percentage of memory usage

        # compare the cpu usage and memory usage with their thresholds
        if cpu_usage > cpu_threshold or mem_usage > mem_threshold:
            # set content for title and message, including current time and the percentages of the usages
            title = f"({current_time}!OVERRIDE!)"
            message = f"CPU:{cpu_usage:.1f} ...MEM:{mem_usage:.1f}" # 1f to keep one decimal place

            # use notification module from plyer library to send desktop notification with the pre-set title and message
            notification.notify (
                title=title,
                message=message,
                timeout=10 # makes the desktop notification disappear in 10 seconds
            )
            # print warning message, use flush=ture to ensure the message is output immediately
            print(f"!WARNING! {title}{message}",flush=True)

        time.sleep(5) # pause for 5 second after each loop

if __name__=="__main__": # make sure that the program is only activated when the script is run directly
    print("Activating monitor",flush=True) # print the text to show the program is running
    # code for terminating the program. it will detect keyboard interrupt when ctrl+c is clicked, which wil stop the program
    # and print suspending monitor immediately
    try:
        usage_monitor(cpu_threshold=50,mem_threshold=50)
    except KeyboardInterrupt:
        print("Suspending monitor",flush=True)
