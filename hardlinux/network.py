import psutil

def check_network():
    net_io = psutil.net_io_counters()
    used_net_mb = net_io.bytes_sent / (1024**2)
    used_net_mb = round(used_net_mb, 1)
    sent_mb = net_io.bytes_sent / (1024**2)
    sent_mb = round(sent_mb, 1)
    recv_mb = net_io.bytes_recv / (1024**2)
    recv_mb = round(recv_mb, 1)
    total_mb = sent_mb + recv_mb

    if total_mb < 50:
        status = "* Status: Network activity is normal — no excessive traffic detected."
        recommendation = "* Recommendation: No action needed — network usage is within safe limits."
    elif total_mb < 500:
        status = "* Status: Network under moderate usage — data transfer within expected range."
        recommendation = "* Recommendation: Review active applications if sustained — ensure downloads or cloud syncs are intended."
    elif total_mb < 2000:
        status = "* Status: High network activity detected — monitor background processes or apps."
        recommendation = "* Recommendation: Identify high-traffic applications, close unnecessary programs, or schedule large transfers during off-peak hours."
    else:
        status = "* Status: Excessive network usage — potential unauthorized activity or runaway processes."
        recommendation = "* Recommendation: Investigate unknown processes, check for malware or unauthorized connections, consider firewall monitoring, and limit bandwidth-heavy applications."
    
    print()
    print("------> Network: ")
    print(f"-Network usage = {used_net_mb} Mb")
    print(f"-Data sent = {sent_mb} Mb")
    print(f"-Data received = {recv_mb} Mb")
    print(f"-Total data = {total_mb} Mb")
    print(status)
    print(recommendation)
