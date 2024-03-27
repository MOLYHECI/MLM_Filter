#!/bin/bash
conda activate mlm_filter
mkdir data
cd data
mkdir coco gqa ocr_vqa textvqa vg
cd ..
python download_dataset.py
