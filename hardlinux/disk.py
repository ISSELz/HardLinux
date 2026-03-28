import psutil 

def check_disk():
    disk = psutil.disk_usage("/")
    total_disk = round(disk.total / 2**30, 2)
    used_disk = round(disk.used / 2**30, 2)
    percent = disk.percent

    if percent < 60:
        status = "* Status : Disk utilization is within optimal limits — sufficient free space available."
        recommendation = "* Recommendation: No immediate action required — maintain current storage practices."
    elif percent < 80:
        status = "* Status: Disk usage is increasing — storage consumption should be monitored."
        recommendation = "* Recommendation: Review stored data, remove redundant files, and consider organizing large directories."
    elif percent > 90:
        status = "* Status: Disk nearing capacity — risk of performance degradation."
        recommendation = "* Recommendation: Clear temporary files, uninstall unused applications, and offload large data to external storage."
    else:
        status = "* Status: Disk capacity critically high — immediate action required."
        recommendation = "* Recommendation: Free up space urgently — delete unnecessary files, empty trash, and consider expanding storage capacity."

    print()
    print("------> Disk : ")
    print(f"-Disk total = {total_disk} Gb")
    print(f"-Disk usage = {used_disk} Gb")
    print(f"-Percent = {percent} %")
    print(status)
    print(recommendation)

