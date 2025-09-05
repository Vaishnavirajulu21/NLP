# handling url
import urllib.request 
from bs4 import BeautifulSoup # handling or parsing a html file
import matplotlib.pyplot as plt # for visualization
import csv
import nltk #toolkit
nltk.download('stopwords') # i,or,was extracted
from nltk.corpus import stopwords 

#fetch from website
headers = {"User-Agent": "Mozilla/5.0"}
req = urllib.request.Request("https://en.wikipedia.org/wiki/India",headers=headers)
response =  urllib.request.urlopen(req)
html = response.read()
#print("html file loaded successfully")

#to extract the text
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip=True) #If True, strings will be stripped before being concatenated.
#print("text:",text)

#tokenization
tokens = text.split()

#convert into lower case
tokens = [t.lower() for t in tokens]

#Remove punctuation and numbers
tokens = [t for t in tokens if t.isalpha()] # tokens: ['this', 'is', 'a', 'beautiful', 'bird', 'i', 'have', 'ever', 'seen', 'in', 'my', 'life']
# tokened = len(tokens)
# print("tokens:",tokened)
# print("tokens:",tokens)

# stopwords removal using loop
sr = stopwords.words('english')  #is,are,at are -extracted using stopwords
cleaned_token = []
for token in tokens:
    if token  not in sr :
        cleaned_token.append(token) #cleared tokens: ['beautiful', 'bird', 'ever', 'seen', 'life']]

# cleaned_tokened = len(cleaned_token)       
# print("cleaned_token:",cleaned_tokened)
# print("cleared_token:",cleaned_token)

# frequency distribution

freq = nltk.FreqDist(cleaned_token)

# for key,val in freq.items():
#     print(str(key)+":"+str(val))



# to get top100
top_100 = freq.most_common(100)

#to  write csv file
with open('top_100_words.csv','w',newline="", encoding='utf-8')as f:
    writer = csv .writer(f)
    writer.writerow(["words","count"]) # header or heading
    writer.writerows(top_100)

print("✅ Top 100 words saved to 'top_100_words.csv'")

#visualization
freq.plot(20)

plt.show()




