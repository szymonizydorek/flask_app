import psutil, datetime

class SystemMonitorClass:
    def get_cpu_load(self):
        cpu_load = psutil.cpu_percent(interval=1)
        return f"{cpu_load}%" 
    
    def get_cpu_count(self):
        cpu_count = psutil.cpu_count()
        return f"{cpu_count}" 
    
    def get_cpu_times(self):
        cpu_load = psutil.cpu_percent(interval=1)
        return print(str(cpu_load)+ '%')
    
    '''
    def get_memory_info(self):
        return psutil.virtual_memory()
    
    def get_boot_time(self):
        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
        formatted_boot_time = boot_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_boot_time
    
    def get_disk_io_counters(self):
        io_counters = psutil.disk_io_counters()
     
       '''
if __name__ == "__main__":
    monitor = SystemMonitorClass()
    
    cpu_load2 = monitor.get_cpu_load()
    print(f"CPU Load: {cpu_load2}")  # Print CPU load   
    
    cpu_count2 = monitor.get_cpu_count()
    print(f"{cpu_count2}")