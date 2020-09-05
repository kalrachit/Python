def expression (s, i):
    st=[]
    for x in s:
        if x != None:
            if x not in st:
                print(x)
                st.index()
                st.insert(1, x)
            elif x in st:
                print(x)
                print(st.index(x))
                st.insert(st.index(x)+1,x)
    print(st)
    for x in st:
        print(st.index(x))

exp = "aaabbaac"
h = 1
expression(exp, h)
