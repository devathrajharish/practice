import random
def k_largest(input, k):
    a = []
    input.sort(reverse = True)
    for i in range(k):
        if i == k: break
        a.append(input[i])
    return a

def main():
    n = random.randint(4, 100)
    inputs = random.sample(range(1,1001), n)
    print(inputs)
    k = random.randint(2,3)
    print(k_largest(inputs, k))

if __name__ == '__main__':
    main()
