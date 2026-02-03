import time
import random
import sys
from codecarbon import EmissionsTracker

sys.setrecursionlimit(200000)

# --- 1. ALGORİTMALAR ---

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# --- 2. ÖLÇÜM FONKSİYONU ---

def run_benchmark(algorithm_func, data, algorithm_name, input_size):
    print(f"--- {algorithm_name} Çalışıyor (Veri Boyutu: {input_size}) ---")
    
    data_copy = data.copy()
    tracker = EmissionsTracker(measure_power_secs=0.01, save_to_file=False)
    
    tracker.start() 
    start_time = time.time()
    
    # Algoritmayı çalıştır
    if algorithm_name == "QuickSort":
        algorithm_func(data_copy) 
    else:
        algorithm_func(data_copy)
        
    end_time = time.time()
    emissions = tracker.stop() 
    
    # --- SONUÇ HESAPLAMA ---
    
    energy_kwh = tracker.final_emissions_data.energy_consumed
    energy_joules = energy_kwh * 3_600_000 
    
    duration = end_time - start_time
    
    print(f"Süre (T): {duration:.6f} saniye")
    print(f"Enerji (E): {energy_joules:.8f} Joule")
    print("-" * 30)
    
    return duration, energy_joules


if __name__ == "__main__":
    sizes = {
        "Düşük": 1000,
        "Orta": 10000,
        "Yüksek": 50000  
    }

    results = []

    for size_label, size in sizes.items():
        print(f"\n>>> Veri Üretiliyor: {size_label} ({size} eleman)...")
        random_data = [random.randint(0, 100000) for _ in range(size)]
        
        # MergeSort Testi
        t_merge, e_merge = run_benchmark(merge_sort, random_data, "MergeSort", size)
        
        # QuickSort Testi
        t_quick, e_quick = run_benchmark(quick_sort, random_data, "QuickSort", size)
        
        results.append({
            "Boyut": size_label,
            "N": size,
            "MergeSort_Time": t_merge,
            "MergeSort_Energy": e_merge,
            "QuickSort_Time": t_quick,
            "QuickSort_Energy": e_quick
        })

    print("\n=== GENEL SONUÇ TABLOSU ===")
    print(f"{'Boyut':<10} {'N':<10} {'Algoritma':<15} {'Süre (s)':<15} {'Enerji (J)':<15}")
    for r in results:
        print(f"{r['Boyut']:<10} {r['N']:<10} {'MergeSort':<15} {r['MergeSort_Time']:<15.5f} {r['MergeSort_Energy']:<15.8f}")
        print(f"{r['Boyut']:<10} {r['N']:<10} {'QuickSort':<15} {r['QuickSort_Time']:<15.5f} {r['QuickSort_Energy']:<15.8f}")