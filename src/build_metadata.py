import os
import pandas as pd

def build_metadata(root_dir="data/OCT2017"):
    records = []
    for split in ["train", "val", "test"]:
        split_path = os.path.join(root_dir, split)
        if not os.path.exists(split_path):
            continue
        for cls in os.listdir(split_path):
            cls_path = os.path.join(split_path, cls)
            if not os.path.isdir(cls_path):
                continue
            for fname in os.listdir(cls_path):
                if fname.endswith(('.jpeg', '.jpg', '.png')):
                    rel_path = os.path.join("data", "OCT2017", split, cls, fname).replace("\\", "/")
                    records.append({
                        "filename": fname,
                        "class": cls,
                        "split": split,
                        "filepath": rel_path
                    })
    return pd.DataFrame(records)

df = build_metadata()
df.to_csv("data/metadata.csv", index=False)
print("metadata.csv regenerated. Total images:", len(df))
