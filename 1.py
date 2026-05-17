import os
import numpy as np
from PIL import Image

input_dir = r"C:\Users\User\Desktop\2 курс\информатика\np-20260429T194436Z-3-001\np\1\lunar_images"
output_dir = r"C:\Users\User\Desktop\2 курс\информатика\np-20260429T194436Z-3-001\np\1_res"

for filename in os.listdir(input_dir):   
    img = Image.open(input_dir + filename)
    data = np.array(img)

    min_val = data.min()
    max_val = data.max()

    updated_data = ((data - min_val) * 255.0 / (max_val - min_val))
    updated_data = np.clip(updated_data, 0, 255).astype(np.uint8)

    name, ext = os.path.splitext(filename)
    out_path = os.path.join(output_dir, f"{name}_better{ext}")
    Image.fromarray(updated_data).save(out_path)
