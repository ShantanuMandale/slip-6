pip install nltk
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
nltk.download('punkt')

def remove_stop_words(input_text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(input_text)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    filtered_text = ' '.join(filtered_words)
    return filtered_text


file_path = 'path/to/your/text/file.txt'
with open(file_path, 'r') as file:
    passage = file.read()


filtered_passage = remove_stop_words(passage)


print("Original Passage:\n", passage)
print("\nPassage after removing stop words:\n", filtered_passage)

