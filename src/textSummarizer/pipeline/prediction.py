from textSummarizer.config.configuration import ConfigManager
from transformers import pipeline, AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_evaluation_config()
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        self.gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        self.pipeline = pipeline('summarization', model = self.config.model_ckpt, tokenizer=tokenizer)

    def predict(self, text):
        print("Dialogue:")
        print(text)

        output = self.pipeline(text, **self.gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output
    
if __name__ == '__main__':
    text = """Joey: Hey! How You doing?
    Rachel: Im doing good. Wanna share your sandwhich with me.
    Joey: Wo wo wo! Joey doesn't share his food.
    """
    pred = PredictionPipeline()
    summary = pred.predict(text)
    print(summary) 