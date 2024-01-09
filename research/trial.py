import os
from pathlib import Path


from datasets import load_dataset ,load_from_disk
apath = ('F:\\Project\\Text_Summarization\\artifacts\\data_ingestion\\samsum_dataset')

if(os.path.exists(apath)):
    load_from_disk(apath) 
else:
    print('path not exist')