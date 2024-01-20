from textSummarizer.config.configuration import ConfigManager
from transformers import pipeline, AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        apipeline = pipeline('summarization', model = self.config.model_ckpt, tokenizer=tokenizer)
        print("Dialogue:")
        print(text)

        output = apipeline(text, **gen_kwargs)[0]["summary_text"]
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