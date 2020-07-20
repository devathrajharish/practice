def main():
    def wordBreak(s, wordDict):
        if len(s) == 0:
            return True

        for x in wordDict:
            prefix = s[0:len(x)]
            result = False

            if prefix == x:
                result = wordBreak(s[len(x):], wordDict)
            if result:
                return True

        return False

    s = "fastracecars"
    wordDict = ["fast", "cars", "car","race","astra","run"]
    print(wordBreak(s, wordDict))

if __name__ == '__main__':
    main()