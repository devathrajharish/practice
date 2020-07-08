# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# All the input string will only include lower case letters.
# The returned elements order does not matter.

def main():
    def concatenatedwords(words):
        mp = {}
        words = set(words)
        output = []

        def recur(word):
            if word in mp:
                return mp[word]

            for i in range(1, len(word)):
                word1 = word[:i]
                word2 = word[i:]

                if word1 in words and word2 in words:
                    mp[word] = True
                    return True

                if word1 in words and recur(word2):
                    mp[word2] = True
                    return True

                if word2 in words and recur(word1):
                    mp[word1] = True
                    return True

            return False

        for word in words:
            if recur(word) == True:
                output.append(word)

        return output

    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    print(concatenatedwords(words))


if __name__ == '__main__':
    main()