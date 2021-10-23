from janome.tokenizer import Tokenizer

t = Tokenizer(wakati=True)

# for token in t.tokenize('すもももももももものうち'):
#   print(token)

tokens = t.tokenize("すもももももももものうち")
print(list(tokens))
