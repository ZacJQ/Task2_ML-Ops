from transformers import GPT2LMHeadModel , GPT2TokenizerFast

model_name = "COMP0087-GROUP8-22-23/GPT2-poem-baseline"

tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)


text = "The quick brown fox"
input_ids = tokenizer.encode(text, return_tensors='pt')

sample_outputs = model.generate(input_ids,
                                do_sample = True,
                                max_length = 100,
                                temperature = 1.2,
)

print("Output:", tokenizer.decode(sample_outputs[0], skip_special_tokens=True))


# https://huggingface.co/COMP0087-GROUP8-22-23/GPT2-poem-baseline

# COMP0087-GROUP8-22-23/GPT2-poem-baseline