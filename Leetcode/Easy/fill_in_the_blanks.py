# Can you do the following without using subquery?: {1,None,1,2,None} --> [1,1,1,2,2] 
# Ensure you take care of case input[None] which means None object

def main():
    def fill_in_the_blanks(blanks):
        
        for x in range(1, len(blanks)):

            if blanks[x] == None:
                blanks[x] = blanks[x-1]
            
        return blanks

    blanks = [1,None, 3,4,5,None,None,None,5]
    print(fill_in_the_blanks(blanks))
if __name__ == '__main__':
    main()