import os
import pandas as pd

def build_metadata(root_dir="data/OCT2017"):
    data = []
    for split in ['train', 'val', 'test']:
        for label in ['cnv', 'dme', 'drusen', 'normal']:
            folder = os.path.join(root_dir, split, label)
            for filename in os.listdir(folder):
                if filename.lower().endswith(".jpeg"):
                    filepath = os.path.join(folder, filename)
                    data.append({
                        'filepath': filepath.replace("\\", "/"),  # for Windows compatibility
                        'class': label.lower(),
                        'split': split
                    })

    df = pd.DataFrame(data)
    df.to_csv("data/metadata.csv", index=False)
    print(f"[INFO] Saved metadata.csv with {len(df)} rows")

if __name__ == "__main__":
    build_metadata()
