import psutil
import shutil

title = "* HardLinux — Your System Health Doctor *"
terminal_width = shutil.get_terminal_size().columns
print(title.center(terminal_width))

from hardlinux.memory import check_memory
check_memory()

from hardlinux.swap import check_swap
check_swap()

from hardlinux.cpu import check_cpu
check_cpu()

from hardlinux.network import check_network
check_network()

from hardlinux.disk import check_disk
check_disk()

#Health score
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")
swap = psutil.swap_memory()

memory_score = abs(memory.percent - 100)
cpu_score = abs(psutil.cpu_percent(interval=1) - 100)
swap_score = abs(swap.percent - 100)
disk_score = abs(disk.percent - 100)
health_score = (memory_score + cpu_score + swap_score + disk_score) / 4
health_score = round(health_score, 1)

print()
print(f"------> Health score = {health_score} % ")
