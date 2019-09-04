def find_three_common(word_str, k):
    """
        Takes a long string find a 3 most common words and return them
    """
    word_list = word_str.split()
    print(word_list[:4])

    hist = histogram(word_list)
    print(hist)

    # sorted_x = sorted(x.items(), key=lambda kv: kv[1])
    sorted_values = sorted(hist.items(), key=lambda kv: kv[1], reverse=True)
    print("sorted values: ", sorted_values)
    k_list = []
    for i in range(k):
        k_list.append(sorted_values[i][0])

    print("k list: ", k_list)


def histogram(list_words):

    hist = {}

    for word in list_words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1

    return hist


words = "hi hello bye hi hi say bye sukhrob sukhrob sukhrob"
k = 4
find_three_common(words, k)
