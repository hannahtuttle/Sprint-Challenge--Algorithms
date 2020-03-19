'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0

    def inner(word):
        nonlocal count
        if len(word) == 0:
            return 0
        if len(word) == 1:
            return 0
        if len(word) > 1:

            arr = list(word)
            word1 = ''
            print(word)
            if arr[0] == 't' and arr[1] == 'h':
                count += 1
                word1 = word[2:]
            elif arr[0] == 't' and arr[1] == 't':
                word1 = word[1:]
            elif arr[0] == 't' and arr[1] != 'h':
                word1 = word[2:]
            elif arr[0] != 't':
                word1 = word[1:]
            print(word1)
            print(count)
        return inner(word1)
    inner(word)
    return count



# count_th('thistleth')
print(count_th("thhtthht"))