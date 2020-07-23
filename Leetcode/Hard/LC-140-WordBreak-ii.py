def main():

    def helper(s, wordDict, cache):
        if not s:
            return []
        if s in cache:
            return cache[s]

        result = []

        for word in wordDict:
            if s.startswith(word):
                if s == word:
                    result.append(word)
                else:
                    helperResult = helper(s[len(word):], wordDict, cache)
                    for nextWords in helperResult:
                        result.append(word + " " + nextWords)

        cache[s] = result

        return result
    def wordBreak( s, wordDict):
        return helper(s, wordDict, {})

    s = "fastracecars"
    wordDict = ["fast", "cars", "car","race","astra","run"]
    print(wordBreak(s, wordDict))
if __name__ == '__main__':
    main()