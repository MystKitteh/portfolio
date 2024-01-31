import spacy
# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

bing = open('bing.txt', 'r', encoding='utf8')
words = bing.read()
wordstrings = str(words)
# print(wordstrings)

bingWords = nlp(wordstrings)
for token in bingWords:
    # if token.pos_ == "VERB":
    print(token.text, "---->", token.pos_, ":::::", token.lemma_)

claude = open('claude.txt', 'r', encoding='utf8')
words = claude.read()
wordstrings = str(words)
print(wordstrings)

claudeWords = nlp(wordstrings)
for token in claudeWords:
    if token.pos_ == "VERB":
        print(token.text, '---->', token.pos_, ':::::', token.lemma_)

chatGPT = open('chatGPT.txt', 'r', encoding='utf8')
words = chatGPT.read()
wordstrings = str(words)
print(wordstrings)

chatGPTWords = nlp(wordstrings)
for token in chatGPTWords:
    if token.pos_ == "VERB":
        print(token.text, '---->', token.pos_, ':::::', token.lemma_)
