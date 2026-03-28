import psutil

def check_cpu():
    
    cpu_percent = psutil.cpu_percent(interval=1)

    print()
    print("------> CPU :")

    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                print(f"-{line.strip()}")
                break

    print(f"-CPU usage : {cpu_percent} % ")
    if cpu_percent < 10:
        status = "* Status : CPU is idle — no active workload detected."
        recommendation = "* Recommendation : System resources are underutilized; workload can be increased if needed."
    elif cpu_percent <= 60:
        status = "* Status : Processor activity is stable and healthy."
        recommendation = "* Recommendation : No optimization needed — CPU operating within normal parameters."
    elif cpu_percent <= 85:
        status = "* Status : CPU under increased load — monitor active processes."
        recommendation = """* Recommendations :
- Review active processes and consider closing non-essential applications. 
- Reduce parallel workloads if performance degradation is observed. """
    else:
        status = "* Status : CPU heavily loaded — immediate optimization recommended."
        recommendation = """* Recommendations :
- Immediate action required — terminate high CPU-consuming processes.
- Investigate potential runaway or inefficient processes.
- Check for infinite loops or misbehaving programs. """

    print()
    print(status)
    print(recommendation) 

