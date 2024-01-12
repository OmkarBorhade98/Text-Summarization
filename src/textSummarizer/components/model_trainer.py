from textSummarizer.logging import logger
from textSummarizer.entity import ModelTrainerConfig
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
import os

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
    
    def train(self):
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        logger.info(f'device : {device}')
        tokenizer = self.config.tokenizer_name
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)
        # load data 
        splits = ['train', ' test', 'validation']
        dataset_samsum_pt ={}
        for split in splits:
            dataset_samsum_pt[split] = load_from_disk(os.path.join(self.config.data_path, split))
        trainer_args = TrainingArguments(
            output_dir = self.config.root_dir,
            num_train_epochs = self.config.num_train_epochs, 
            warmup_steps = self.config.warmup_steps,
            per_device_train_batch_size = self.config.per_device_train_batch_size, 
            per_device_eval_batch_size = self.config.per_device_train_batch_size,
            weight_decay = self.config.weight_decay, 
            logging_steps = self.config.logging_steps,
            evaluation_strategy = self.config.evaluation_strategy, 
            eval_steps = self.config.eval_steps, 
            save_steps = self.config.save_steps,
            gradient_accumulation_steps = self.config.gradient_accumulation_steps
        )
        logger.info('Training Started')
        trainer = Trainer(model=model, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["train"], 
                  eval_dataset=dataset_samsum_pt["validation"])
        trainer.train()
        logger.info('Training Done')
        ## Save model
        model.save_pretrained(os.path.join(self.config.root_dir,"model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))