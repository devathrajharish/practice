# Complete a function that returns a list have excat same length.

#  output : ['Firstly is healthy', 'this', 'first', 'Next is you bad', 'second is', 'how are you','Python']


import collections


def main():
    def return_word_len_n(output,n):
        dicts = collections.defaultdict(list)
        result = []
        if len(output) == 0 or n==0 or n not in [len(x.split(' ')) for x in output]:
            return None

        for x in output:
            if len(x.split(' ')) in dicts:

            # dicts[x] = len(x.split(' '))
                dicts[len(x.split(' '))].append(x)
            else:
                dicts[len(x.split(' '))] = [x]

        
        return dicts.get(n)

    output = ['Firstly is healthy', 'this', 'first', 'Next is you bad', 'second is', 'how are you','Python']
    print(return_word_len_n(output, n))
if __name__ == '__main__':
    main()
