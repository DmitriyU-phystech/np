import os
import numpy as np
import matplotlib.pyplot as plt

input_dir = r"C:\Users\User\Desktop\2 курс\информатика\np-20260429T194436Z-3-001\np\2\signals"
output_dir = r"C:\Users\User\Desktop\2 курс\информатика\np-20260429T194436Z-3-001\np\2_res"

for filename in os.listdir(input_dir):
     data = np.loadtxt(os.path.join(input_dir, filename))
     smoothed = np.zeros_like(data)

     for i in range(len(data)):
         start = max(0, i - 9)
         smoothed[i] = np.mean(data[start:i+1])

     fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

     ax1.plot(data, 'b-', linewidth=0.5)
     ax1.set_title('Исходные данные')
     ax1.set_ylabel('Значение')
     ax1.grid(True, alpha=0.3)
    
     ax2.plot(smoothed, 'r-', linewidth=1.0)
     ax2.set_title('Сглаженные данные')
     ax2.set_ylabel('Значение')
     ax2.grid(True, alpha=0.3)
    
     plt.tight_layout()
    
     name = os.path.splitext(filename)[0]
     save_path = os.path.join(output_dir, f"{name}_two_plots.png")
     plt.savefig(save_path, dpi=150)
     plt.close()