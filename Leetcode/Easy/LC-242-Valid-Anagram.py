def main():
    s = 'anagram'
    t = 'naargma'
    # method 1: using dictonary
    def anagram(s, t):

        ob1 = {}
        ob2 = {}
        for item in s:
            ob1[item] = s.count(item)
        for item in t:
            ob2[item] = t.count(item)

        return True if ob1 == ob2 else False
    print(anagram(s, t))

    #method 2 : brute force

    def anagram2(s, t):

        return True if sorted(s) == sorted(t) else False
    print(anagram2(s, t))
if __name__ == '__main__':
    main()