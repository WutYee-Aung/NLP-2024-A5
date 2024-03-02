from flask import Flask, render_template, request, jsonify
import torch
from util_2 import *
# from models import MultiHeadAttentionLayer

app = Flask(__name__)

data = pickle.load(open('app/model/data.pkl', 'rb'))
word2id     = data['word2id']
max_mask    = data['max_mask']
max_len     = data['max_len']

tokenizer = BERT_Tokenizer(word2id)

# Initialize your attention model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model  = BERT()
model.load_state_dict(torch.load('app/model/s_bert.pt', map_location=device))
model.eval()


# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling translation requests
@app.route('/translate', methods=['POST'])
def translate():
        sentence_a = request.form.get('input_sentence1')
        sentence_b = request.form.get('input_sentence2')
        similarity = calculate_similarity(model, tokenizer, sentence_a, sentence_b, device)
        print(similarity)
        return render_template('index.html',sent_a=sentence_a,sent_b=sentence_b,similarity_score=similarity)

if __name__ == '__main__':
    app.run(debug=True)
