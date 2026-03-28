import psutil

def check_memory():
    mem = psutil.virtual_memory()

    #Human readable units :

    def fullmem(total_mem):
        if mem.total >= 2**30:
            fmem = (mem.total / 2**30)
            fmem = (round(fmem, 1), "Gb")
            return fmem
        elif mem.total >= 2**30:
            fmem = (mem.total / 2**20)
            fmem = (round(fmem, 1), "Mb")
            return fmem
        elif mem.total >= 2**10:
            fmem = (mem.total / 2**10)
            fmem = (round(fmem, 1), "Kb")
            return fmem
        else:
            fmem = (mem.total)
            fmem = (round(fmem, 1), "Bytes")
            return fmem

    def usedmem(used_mem):
        if mem.used >= 2**30:
            umem = (mem.used / 2**30)
            umem = (round(umem, 1), "Gb")
            return umem
        elif mem.used >= 2**20:
            umem = (mem.used / 2**20)
            umem = (round(umem, 1), "Mb")
            return umem
        elif mem.used >= 2**10 :
            umem = (mem.used / 2**10)
            umem = (round(umem, 1), "Kb")
            return umem
        else:
            umem = (mem.used, "Bytes")
            return umem
    
    full_value, full_unit = fullmem(mem.total)
    used_value, used_unit = usedmem(mem.used)

    #---

    print()
    print("------> Memory (RAM) usage: " )
    print(f"-Total memory = {full_value} {full_unit}")
    print(f"-Used memory = {used_value} {used_unit}")
    print(f"-Percent = {mem.percent} %" )
    print()

    health_score = max(0, 100 - mem.percent )
    if mem.percent <70 :
        status = "* Status : Healthy: Memory usage within safe limits."
        recommendation = "* Recommendation : No immediate action needed — memory usage is within safe limits."
    elif mem.percent <85:
        status = "* Status : Caution: Memory under moderate stress — monitor high-usage apps."
        recommendation = """* Recommandation :
-Close unnecessary or high-memory processes to free RAM.
-Consider checking background services for memory leaks.
-Monitor memory trends to prevent sudden overload.
-Suggest temporary swap usage increase if available."""
    else:
        status = "* Status : Critical: Memory critically high — immediate action required."
        recommendation = """* Recommandation:
-Immediate action required — close top RAM-consuming processes now.
-Consider restarting system if memory fragmentation is high.
-Investigate memory-intensive apps; check for leaks or runaway processes. """

    print(status)
    print(recommendation)



