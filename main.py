from flask import Flask, request
import os
from transformers import GPT2LMHeadModel, GPT2Tokenizer
config = {
    "DEBUG": True
}


app = Flask(__name__)
app.config.from_mapping(config)
# cache = Cache(app)

tok = GPT2Tokenizer.from_pretrained('models/infobuzz')

# curl http://91.201.54.207/ -d "{\"Theme\":\"<input>\""}""
@app.route('/', methods=['POST'])
# @cache.cached()
def incoming_theme():
    text = request.get_json()
    out = GPT2LMHeadModel.from_pretrained('models/infobuzz') \
        .generate(tok.encode(text['Theme'], return_tensors='pt'), max_length=300, repetition_penalty=5.0, do_sample=True, top_k=5, top_p=0.95, temperature=1)

    return tok.decode(out[0])

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))