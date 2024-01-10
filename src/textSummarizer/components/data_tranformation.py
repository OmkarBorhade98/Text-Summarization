from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk
import json
import os
from textSummarizer.entity import DataTransformationConfig

class DataTranformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation= True)
        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length =128, truncation= True)
        return{
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def convert(self):
        dataset_path = self.config.dataset_path
        dataset_dict= os.path.join(dataset_path, 'dataset_dict.json')
        save_path = os.path.join(self.config.root_dir,"samsum_dataset")

        with open(dataset_dict, 'r') as file:
            json_data = json.load(file)
            for split in json_data['splits']:
                dataset_samsum = load_from_disk(os.path.join(self.config.dataset_path, split))
                dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched = True)
                dataset_samsum_pt.save_to_disk(os.path.join(save_path, split))