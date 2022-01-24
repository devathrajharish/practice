def main():
    def no_of_friends(friends):
        dicts = {}
        for x in friends:
            if len(x) == 1:
                dicts[x[0]] = 0
            else:
                if x[0] in dicts:
                    dicts[x[0]] += 1 
                else: 
                    dicts[x[0]] = 1
        return dicts

    friends = [[5,2], [4,1],[1,3],[3], [4,2],[4,3]]
    print(no_of_friends(friends))
if __name__ == '__main__':
    main()