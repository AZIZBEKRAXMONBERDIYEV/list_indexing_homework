def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    s=list_num[0]
    a=list_num[-1]
    if s>a:
        i=s
    else:
        i=a

    return i
print(main([1,2,3,4,4,6,544,32,]))