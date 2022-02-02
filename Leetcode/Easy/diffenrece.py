# Complete a function that returns a list containing all the mismatched
#  words (case sensitive) between two given input strings #
#  For example: # - string 1 : "Firstly this is the first string" # - 
# string 2 : "Next is the second string" # # -
#  output : ['Firstly', 'this', 'first', 'Next', 'second']


def main():
    def mismatched_words(string1,string2):

        a = string1.split(' ')
        b = string2.split(' ')
        dicts = {}
        for x in a:
            if x not in b:
                dicts[x] = 1
        
        for y in b:
            if y not in a:
                dicts[y] = 1
        
        return list(dicts.keys())



    string1 = "Firstly this is the first string"
    string2 = "Next is the second string"
    print(mismatched_words(string1, string2))
if __name__ == '__main__':
    main()