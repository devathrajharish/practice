def main():
    def wordBreak(s, wordDict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

    s = "fastracecars"
    wordDict = ["fast", "cars", "car","race","astra","run"]
    print(wordBreak(s, wordDict))

if __name__ == '__main__':
    main()