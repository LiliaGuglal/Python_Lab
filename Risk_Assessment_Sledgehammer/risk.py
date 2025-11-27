import threading
import random
import time

class Warehouse:
    def __init__(self, name, meds):
        self.name = name
        self.meds = meds
        self.lock = threading.Lock()

    def steal(self, amount):
        with self.lock:
            if self.meds <= 0: return 0
            
            if random.random() < 0.2: return -1 
            
            actual = min(amount, self.meds)
            
            if random.random() < 0.1: actual //= 2
            
            self.meds -= actual
            return actual

class Runner(threading.Thread):
    def __init__(self, name, warehouses):
        super().__init__()
        self.name = name
        self.warehouses = warehouses
        self.profit = 0
        self.caught = False
        self.step = 0 

    def run(self):
        for i in range(10):
            if self.caught: break
            
            w = random.choice(self.warehouses)
            res = w.steal(random.randint(10, 30))
            
            if res == -1:
                self.caught = True
            else:
                self.profit += res * 1.5
            
            self.step = i + 1 
            time.sleep(random.uniform(0.1, 0.4)) 

def run_clean_simulation():
    warehouses = [Warehouse(f"Склад_{i+1}", random.randint(150, 250)) for i in range(3)]
    runners = [Runner(f"Злодій_{i+1}", warehouses) for i in range(5)]

    print("=== ПОЧАТОК ОПЕРАЦІЇ ===")
    
    for r in runners:
        r.start()

    while any(r.is_alive() for r in runners):
        status_line = ""
        for r in runners:
            icon = "💀" if r.caught else "🏃"
            if r.step == 10 and not r.caught: icon = "✅"
            
            bar = "█" * r.step + "." * (10 - r.step)
            status_line += f"| {r.name} {icon} [{bar}] "
        
        print(f"\r{status_line}|", end="", flush=True)
        time.sleep(0.1)

    for r in runners:
        r.join()

    print("\n\n=== ПІДСУМКИ ===")
    total_profit = 0
    for r in runners:
        status = "❌ СПІЙМАНИЙ" if r.caught else "✅ ВТІК"
        print(f"{r.name}: {status} | Прибуток: {r.profit:.1f}")
        total_profit += r.profit
    
    print(f"\n💰 ЗАГАЛЬНИЙ КУШ: {total_profit:.1f}")
    print(f"📦 Залишки на складах: {[w.meds for w in warehouses]}")

if __name__ == "__main__":
    run_clean_simulation()