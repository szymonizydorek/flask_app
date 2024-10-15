import psutil, datetime

class SystemMonitorClass:
    def get_cpu_load(self):
        return psutil.cpu_percent(interval=1)
    
    def get_memory_info(self):
        return psutil.virtual_memory()
    
    def get_boot_time(self):
        boot_time_timestamp = psutil.boot_time()
        boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
        formatted_boot_time = boot_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_boot_time
    
    def get_disk_io_counters(self):
        io_counters = psutil.disk_io_counters()