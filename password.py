
dic = "0123456789abcdef!@a"
pwlen = 8

passwd = "aabb"

max_case = pow(len(dic),pwlen)
print(max_case)

def change(a, x):
    s = []
    while a>0:
        a, r = divmod(a, x)
        s.insert(0, r)
    return s


for i in range(0, max_case):
    result = change(i, len(dic))
    result2 = [dic[i] for i in result]

    # result2 = []
    # for i in result:
    #     result2.append(dic[i])

    cur = "".join(result2)
    if  cur == passwd:
        print(cur)
        break


# password = "937610"
#
# for i in range(0,1000000):
#     current = '%04d' % i
#     if password == current:
#         print(current)

