from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

class HuggingFaceLLM:
    def query(self, prompt):
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=150)
        return tokenizer.decode(outputs[0], skip_special_tokens=True)

hf_llm = HuggingFaceLLM()
