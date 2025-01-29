# history 29/1/25 - 30 min

# solution 1
def is_anagram(s, t):
    my_list ={}
    if (len(s)!=len(t)):
        return False
    # create hash 
    for each in list(s):
        if each in my_list:
            my_list[each]=my_list[each]+1
        else:
            my_list[each]=1
    # check with hash
    for each in list(t):
        if each in my_list and (my_list[each]>0):
            my_list[each]=my_list[each]-1
        else:
            return False

    return True


def is_anagram_executor():
    print("is_anagram")
    print(is_anagram("one","noe"),True)
    print(is_anagram("anagram","nagaram"),True)
    print(is_anagram("rat","car"),False)
    print(is_anagram("rats","car"),False)
    print(is_anagram("rat_s","s_tar"),True)
    print(is_anagram("rat_s#@","s_t@#ar"),True)
    print(is_anagram("",""),True)

    