import torch


# hyperparameters

## embedding layer
## convert each character in your input seuqnece into a dense vector

## Transformer decoder block

## output layer



class GPT(torch.nn.Module):
    def __init__(self, vocab_size, d_model, max_seq_len):
        super(GPT, self).__init__()
        self.embedding = torch.nn.Embedding(vocab_size, d_model)
        self.pos_embedding = torch.nn.Embedding(max_seq_len, d_model)
    
    def forward(self, x):
        pass
    

class TransformerBlock(torch.nn.Module):
    def __init__(self, d_model, num_heards, dropout=0.1):
        pass
    
    def forward(self, x):
        pass