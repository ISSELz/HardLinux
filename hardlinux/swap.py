import psutil

def check_swap():
    swap = psutil.swap_memory()
    total_swap = round(swap.total / (1024**3), 2)
    used_swap = round(swap.used / (1024**3), 2)
    free_swap = round(swap.free / (1024**3), 2)
    percent = swap.percent 
    
    if total_swap == 0:
        status = "* Status: No swap configured — low-RAM systems may freeze under heavy load."
        recommendation = "* Recommendation: Create a swap file or partition to safeguard against memory spikes; even 2–4 GB improves system stability."
    else:
        if percent < 20:
            status = "* Status: Swap usage is minimal — system has sufficient RAM."
            recommendation = "* Recommendation: No action needed; performance is normal."
        elif percent < 60:
            status = "* Status: Swap is being used — memory pressure detected."
            recommendation = "Recommendation: Monitor running applications; consider closing memory-heavy programs to reduce swap usage."
        else:
            status = "* Status: Swap heavily used — system performance may be degraded."
            recommendation = "* Recommendation: Consider freeing RAM, reducing running applications, or increasing swap size; monitor for potential system slowdowns."

    print()
    print("------> Swap memory: ")
    print(f"-Total swap = {total_swap} Gb")
    print(f"-Used swap = {used_swap} Gb")
    print(f"-Free swap = {free_swap} Gb")
    print(f"-Percent = {percent} %")
    print(status)
    print(recommendation)
    
