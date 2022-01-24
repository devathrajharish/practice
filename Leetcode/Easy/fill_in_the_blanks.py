def main():
    def fill_in_the_blanks(blanks):
        
        for x in range(1, len(blanks)):

            if blanks[x] == None:
                blanks[x] = blanks[x-1]
            
        return blanks

    blanks = [None,None, 3,4,5,None,None,None,5]
    print(fill_in_the_blanks(blanks))
if __name__ == '__main__':
    main()