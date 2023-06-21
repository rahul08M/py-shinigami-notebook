import psutil    # import psutil library

CPU_PERCENTAGE_THRESHOLD = 90    # Define constant CPU_PERCENTAGE_THRESHOLD with value 90
MEMORY_PERCENTAGE_THRESHOLD = 90    # Define constant MEMORY_PERCENTAGE_THRESHOLD with value 90
DISK_PERCENTAGE_THRESHOLD = 90    # Define constant DISK_PERCENTAGE_THRESHOLD with value 90


def monitor_system():    # Function to monitor system performance
    
    cpu_percentage = psutil.cpu_percent(interval=1)    # get the cpu usage for 1 second
    if cpu_percentage > CPU_PERCENTAGE_THRESHOLD:    # check if cpu usage is greater than threshold
        print("High CPU Usage", f"CPU usage is {cpu_percentage}%")    # print message on console

    device_memory = psutil.virtual_memory()    # get the system memory usage
    memory_percentage = device_memory.percent    # get the percentage of memory usage
    if memory_percentage > MEMORY_PERCENTAGE_THRESHOLD:    # check if memory usage is greater than threshold
        print("High Memory Usage", f"Memory usage is {memory_percentage}%")    # print message on console

    disk = psutil.disk_usage("/")    # get the disk usage
    disk_percentage = disk.percent    # get the percentage of disk usage
    if disk_percentage > DISK_PERCENTAGE_THRESHOLD:    # check if disk usage is greater than threshold
        print("High Disk Usage", f"Disk usage is {disk_percentage}%")    # print message on console


while True:    # Run the program continuously
    monitor_system()    # monitor system performance
