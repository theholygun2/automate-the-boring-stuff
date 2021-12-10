spam = [6,'bananas','tofu','cats']
spam2 = ['6','bananas','tofu','cats']


def yogs(list1):
    in_list = list1
    answer = ''
    for index, item in enumerate(list1):
        answer += item + ', '

    return answer

def yogs2(list1):
    in_list = list1

    if in_list: #Does this list has value?
        in_list = list(map(str, in_list)) #if its has value
        answer = ''
        for i in range(0, len(list1) - 1):

            answer += in_list[i] + ', '
        answer += 'and ' + in_list[-1]
        return answer
    else: #if it does't have value
        return 'Bitch there\'s no value'

print(yogs2(spam))


print(yogs(spam2))
