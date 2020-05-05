import psutil
import os


def monitor():
    print()
    p = psutil.Process(os.getpid())
    print("Uso de CPU ", end='')
    print((f"{p.cpu_percent(interval=15)}%"))
    print()
    print(f"CPU núcleos {p.cpu_affinity()}")
    print()
    print(f"Uso de memória {(p.memory_percent() * 100)}%")
    print()
    print(f"PIDS (processos rodando no sistema) {len(psutil.pids())}")
    print()
