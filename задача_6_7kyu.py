def solve(st):
     # return "".join(sorted(st.lower())) in "abcdefghijklmnopqrstuvwxyz"
    st = st.lower()
    st = list(st) and sorted(st)

    st_check = 'abcdefghijklmnopqrstuvwxyz'
    st_check = list(st_check)
    for i in range(len(st_check)-len(st)+1):
        if st_check[i:i+len(st)] == st:
            return True
    return False

print(solve('def'))
print(solve('bcdef'))

# https://www.codewars.com/kata/5ce6728c939bf80029988b57

# print(solve('abc'))
# print(solve('dabc'))
# print(solve('abd'))
# print(solve('cdefghijklmn'))


# a = 'ijklmnopq'
# a = a.lower()
# a = list(a) and sorted(a)
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet = list(alphabet)
# for i in range(len(alphabet)-len(a)+1):
#     if alphabet[i:i+len(a)] == a:
#         print(range(len(alphabet)-len(a)+1))
#         print(alphabet[i:i+len(a)])
#         print('True')
