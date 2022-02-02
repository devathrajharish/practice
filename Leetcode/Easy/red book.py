# Complete a function that returns a list have excat same length.

#  output : ['Firstly is healthy', 'this', 'first', 'Next is you bad', 'second is', 'how are you','Python']


import collections


def main():
    def return_word_len_n(output):
        dicts = collections.defaultdict(list)
        result = []
        z  = ''
        # if len(output) == 0 or n==0 or n not in [len(x.split(' ')) for x in output]:
        #     return None

        for x in output:
            if len(x.split(' ')) < len(z):
                z = x
            if x.split(' ')[0] in dicts:

            # dicts[x] = len(x.split(' '))
                dicts[x.split(' ')[0]].append(x)
            else:
                dicts[x.split(' ')[0]] = [x]
        
        return dicts.get('python')
    output = ['Firstly is healthy', 'this', 'first', 'Next is you bad', 'second is', 'how are you','Python', 'Firstly is Naughty']
    print(return_word_len_n(output))
if __name__ == '__main__':
    main()
