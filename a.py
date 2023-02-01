def identical(l1,l2):
    set_l1 = set(l1)
    set_l2 = set(l2)
    if len(l1) == len(set_l1) and len(l2) == len(set_l2):
        print(l1,"\n",l2)
    else:
        print("duplicate item found")

identical([1,2,3,4,5],[1,2,3,40,5,4])