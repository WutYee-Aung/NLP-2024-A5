# NLP-2024-A5
 
# Student Information

Name : Wut Yee Aung - st124377

# Task1
I trained the BERT model by using a Haprry Potter book which I used in A2.
- No of sentences = 5754
- Vocab size = 7765

# Task3

My model is showing 0.99 consine similarity score for all sentence although these sentences are similar or not.

The pre-trained model "paraphrase-distilroberta-base-v1" from the SentenceTransformer library was chosen due to encountered issues accessing the Hugging Face model hub. A proxy error during attempts to connect to the hub prompted the adoption of SentenceTransformer.

# Comparison of "Model from scratch" to "Pretrained Model"

Similar sentence
- sentence_a = 'Your contribution helped make it possible for us to provide our students with a quality education.'
- sentence_b = "Your contributions were of no help with our students' education."

|Model            | Cosine Similarity |
|-----------------|-------------------|
|S-BERT Scratch   | 0.9979            |
|Pretrained Model | 0.7502            |

Difference sentence
- sentence_a = 'My name is Wut Yee'.
- sentence_b = 'Birds are flying'

|Model            | Cosine Similarity |
|-----------------|-------------------|
|S-BERT Scratch   | 0.9915            |
|Pretrained Model | 0.04583           |

# Hyperparameter for BERT

- batch_size   = 6
- max_mask     = 5
- max_len      = 1000
- No of encoded layers = 6
- No of heads in Multi-Head Attention  = 8
- Embedded Dim  = 768
- num_epoch = 500

# Hyperparameter for S-BERT
- num epoch = 1


My model doesn't work properly due to small training dataset size and a limited number of training epochs. Due to limitation of resource, can't train the higher performance model.

# Acknowledgment

I would like to express Min Bannyar's support in understanding the S-BERT model and assisting in the development of S-BERT from the initial scratch-built BERT model.