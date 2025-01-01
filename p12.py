def length(words):
    return max(len(word)for word in words)
words_list=input("enter a list of words separated by spaces:").split()
print("length of lpngest word:",length(words_list))