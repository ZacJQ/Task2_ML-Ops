from fastapi import FastAPI, HTTPException
from transformers import GPT2LMHeadModel , GPT2TokenizerFast
from pydantic import BaseModel  
import json

model_name = "COMP0087-GROUP8-22-23/GPT2-poem-baseline"

tokenizer = GPT2TokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

app = FastAPI()

class Input_user(BaseModel):
    user_input: str


@app.get("/home")
async def home_page()-> None:
    return {"detail": "Welcome to the home page"}


@app.get("/")
async def input_page():
    return {"detail": "Page is working and up \n Head to the /generate page"}



@app.post("/generate")
async def generate_poem(input: Input_user) -> str:
    # text = "The quick brown fox"
    try:
        print(input)
        text = input.user_input
        print(text)
        input_ids = tokenizer.encode(text, return_tensors='pt')

        sample_outputs = model.generate(input_ids,
                                        do_sample = True,
                                        max_length = 100,
                                        temperature = 1.2,
                                        )
        sample_outputs_text = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)
        print(type(sample_outputs_text))
        print(sample_outputs_text)
        return json.dumps({"output": sample_outputs_text})
    except HTTPException as e:
        print("Error - ", e)
        return json.dumps({"Error": e})