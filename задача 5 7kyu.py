def solution(full_text, search_text):
    return full_text.count(search_text)
    # return (len(full_text.split(search_text))-1) if search_text !="" else len(list(full_text))+1
    # return sum((len(i)) for i in search_text if i in full_text)

    c = []
#     # for i in search_text:
# #     # if search_text in full_text:
# #     #     return len(search_text)
#

    # if search_text in full_text:
    #     c.append(search_text)
    #
    # return len(c)
#
print(solution('abcdeb', 'b'))
print(solution('abc', 'b'))
print(solution('abbcbqbb', 'bb'))

# a = 'abbqbbcdbbqe'
# b = 'bb'
#
# if b in a[:]:
#     print('da')
# else:
#         print('net')