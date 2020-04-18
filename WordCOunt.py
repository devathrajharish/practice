def add_word(wc_list, str):
    # break the string into list of words
    str = str.lower().split()
    str2 = []

    for i in str:

        # checking for the duplicates
        if i not in str2:
            str2.append(i)

    for i in range(0, len(str2)):
        wc_list.append([str2[i], str.count(str2[i])])
        print(wc_list)

    return wc_list
def printTable(wc_list):
    print('\n')
    print('Sort alphabetically')
    print('{0:10}             {1}'.format("Word", "Freq"))
    print('{0:10}             {1}'.format("----------", "----"))
    for word, count in sorted(wc_list):
        print('{0:10}             {1}'.format(word, count))
    print('{0:10}             {1}'.format("----------", "----"))
    print("\n")
    print('Sort by Frequency')
    print('{0:10}             {1}'.format("Word", "Freq"))
    print('{0:10}             {1}'.format("----------", "----"))
    wc_list.sort(key=lambda x : x[1], reverse=True)
    for word, count in wc_list:
        print('{0:10}             {1}'.format(word, count))
    print('{0:10}             {1}'.format("----------", "----"))


def main():

    wc_list = []
    str = ''
    while True:
        sentence = input('Enter your string: ')
        print(sentence.split(" "))

        if sentence == "":
            count = add_word(wc_list, str)
            printTable(count)
            break
        else:
            str = str + " " + sentence
            print(str)


main()

