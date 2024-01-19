from textSummarizer.logging import logger
from datasets import load_dataset, load_from_disk, load_metric
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from tqdm import tqdm 
import pandas as pd
from textSummarizer.entity import ModelEvaluationConfig
import os
from pathlib import Path


class ModelEvaluation:
    def __init__(self,config: ModelEvaluationConfig):
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i: i+batch_size]
            
    def calculate_metric_on_test_dataset(self, dataset, tokenizer: AutoTokenizer, model: AutoModelForSeq2SeqLM, 
                                         metric, batch_size: int = 16,
                                         device = 'cuda' if torch.cuda.is_available() else 'cpu',
                                         text_column= 'dialogue', summary_column = 'summary'):
        x_batches = list(self.generate_batch_sized_chunks(dataset[text_column], batch_size))
        y_batches = list(self.generate_batch_sized_chunks(dataset[summary_column], batch_size))

        for x_batch, y_batch in tqdm(zip(x_batches, y_batches), total = len(x_batches)):
            inputs = tokenizer(x_batch, max_length = 1024, padding = 'max_length', truncation = True, return_tensors = 'pt')
            summaries = model.generate(input_ids = inputs['input_ids'].to(device), attention_mask = inputs['attention_mask'].to(device),
                                     length_penalty = 0.8, num_beams = 8, max_length = 128)
            decoded_summaries = [tokenizer.decode(s, skip_special_tokens = True, clean_up_tokenization_spaces = True) for s in summaries]
            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]
            metric.add_batch(predictions=decoded_summaries, references=y_batch)
            
        score = metric.compute()
        return score
    
    def evaluate(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)

        datset = load_from_disk(os.path.join(self.config.dataset_path, 'test'))

        rouge_name = ['rouge1', 'rouge2', 'rougeL', 'rougeLsum']
        rouge_metric = load_metric('rouge')
        score  = self.calculate_metric_on_test_dataset(datset, tokenizer, model, rouge_metric, 8, device, 'dialogue', 'summary')

        rouge_dict = dict((rn, score[rn].mid.fmeasure) for rn in rouge_name)
        print(rouge_dict)
        df = pd.DataFrame([rouge_dict])
        print(df)
        df.to_csv(self.config.metric_file_name, index= 0)