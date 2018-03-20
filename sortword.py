def sortedSentence(Sentence):
    words = Sentence.split(" ")
    words.sort()
    newSentence = " ".join(words)
    return newSentence

Sentence = "what is your name"
print("new sentence is:")
print(sortedSentence(Sentence))
