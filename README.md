# Energy Complexity Analysis: MergeSort vs. QuickSort
This project investigates the energy efficiency of sorting algorithms beyond traditional time complexity, focusing on Energy Complexity (E(n)). It specifically compares MergeSort and QuickSort on modern hardware to determine if the fastest algorithm is always the most "green".



**Project Overview**

Traditional analysis uses Big-O notation (O(nlogn)) for speed, but this study highlights that energy consumption is the product of Power (P) and Time (t). On an Apple M2 processor, results show that while QuickSort can be faster, it often draws more instantaneous power, making it less energy-efficient in high-volume scenarios.





**Key Findings**

**Time vs. Energy:** 

For N=50,000 elements, QuickSort was faster (0.083s vs 0.101s) but consumed ~50% more energy (3.75 J vs 2.50 J).



**Resource Intensity:** 

QuickSort exhibits a more aggressive processor load, whereas MergeSort maintains a stable energy profile.


**Hardware: Benchmarked** 

On an Apple M2 chip using the CodeCarbon library for real-time tracking.




**Installation & Usage**

**Install Dependencies:**

you need to install codecarbon library to execute this code. Execute "pip install codecarbon" on the terminal.


**Author:** Yusuf Taha ÖNCÜ
