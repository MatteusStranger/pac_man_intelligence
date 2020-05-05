import psutil
import os
from tools.user_interaction import write_text


def monitor():
    print()
    p = psutil.Process(os.getpid())
    print("Uso de CPU ", end='')
    cpu = p.cpu_percent(interval=15)
    print((f"{cpu}%"))
    write_text(f"Uso de CPU {cpu}%")
    print()
    cpu = p.cpu_affinity()
    print(f"CPU núcleos {cpu}")
    write_text(f"Cores {cpu}%")

    print()
    mem = (p.memory_percent() * 100)
    print(f"Uso de memória {mem}%")
    write_text(f"Uso de memória {mem}%")
    print()
    pid = len(psutil.pids())
    print(f"PIDS (processos rodando no sistema) {pid}")
    write_text(f"Processos em execução {pid}")
    print()
