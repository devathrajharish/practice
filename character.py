MAX_WIDTH = 80
width = int(input("Enter the width"))
if width < MAX_WIDTH:

    with open("GettysburgAddress.txt", "r") as f_in:
        words_in = [word.strip('\n').split(' ') for word in f_in.readlines()]
        # words_out = " ".join(words_in)
    with open("outt.txt", "w") as f_out:
        count = 0
        for i in range(len(words_in)):
            for ele in words_in[i]:
                if (count == width or "." in ele):
                    count = 0
                    f_out.write(" " +ele+ "\n")
                    if("." in ele):
                        f_out.write("\n")
                else:
                    f_out.write(" " + ele)
                    count = count + 1
    f_out.close()
else:
    print("Enter number less than 80")

