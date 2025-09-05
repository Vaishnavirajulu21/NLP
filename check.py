words = "this is a beautiful bird i have ever seen in my life"

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

# Tokenization
tokens = words.strip().split()
print("tokens:", tokens)

# Stopword removal
sr = stopwords.words('english')
cleared_token = [token for token in tokens if token.lower() not in sr]

print("cleared tokens:", cleared_token)
