
def mergeAlternately(word1, word2) -> str:
    word = ""
    for i in range(min(len(word1), len(word2))):
        word = word + word1[i] + word2[i]

    if len(word1) < len(word2):
        word = word + word2[len(word1):]
    else:
        word = word + word1[len(word2):]
    return word


word1 = "abc"
word2 = "pqr"
print(mergeAlternately(word1,word2))