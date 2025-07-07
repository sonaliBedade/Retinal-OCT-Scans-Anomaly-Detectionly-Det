import os
import random
import shutil
from pathlib import Path

# Set paths
BASE_DIR = Path("data/OCT2017")
NORMAL_DIR = BASE_DIR / "train" / "normal"
VAL_DIR = BASE_DIR / "val" / "normal"

# Ensure val/normal directory exists
VAL_DIR.mkdir(parents=True, exist_ok=True)

# Get all image paths
all_images = list(NORMAL_DIR.glob("*.jpeg"))
print(f"Total normal images: {len(all_images)}")

# Shuffle
random.seed(42)
random.shuffle(all_images)

# Compute 15% split
split_idx = int(0.15 * len(all_images))
val_images = all_images[:split_idx]

# Move images to val/normal
for img_path in val_images:
    dest_path = VAL_DIR / img_path.name
    shutil.move(str(img_path), str(dest_path))

print(f"Moved {len(val_images)} images to validation set.")
