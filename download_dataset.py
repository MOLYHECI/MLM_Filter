import os
from huggingface_hub import snapshot_download
import multiprocessing as mp

snapshot_download(repo_id="weizhiwang/mlm_filter_instructions", repo_type="dataset", local_dir='./data')

urls = ['http://images.cocodataset.org/zips/train2017.zip', 'https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip', 'https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip',
         'https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip', 'https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip']

commands = ['curl -o ./data/coco/train2017.zip http://images.cocodataset.org/zips/train2017.zip',
            'curl -o ./data/gqa/images.zip https://downloads.cs.stanford.edu/nlp/data/gqa/images.zip',
            'curl -o ./data/textvqa/train_val_images.zip https://dl.fbaipublicfiles.com/textvqa/images/train_val_images.zip',
            'curl -o ./data/vg/VG_100K.zip https://cs.stanford.edu/people/rak248/VG_100K_2/images.zip', 
            'curl -o ./data/vg/VG_100K_2.zip https://cs.stanford.edu/people/rak248/VG_100K_2/images2.zip'
            ]

def run_command(command):
    os.system(command)

if __name__ == "__main__":
    pool = mp.Pool()
    pool.map(run_command, commands)

