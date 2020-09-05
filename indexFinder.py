
def countofexpression(x, h):
    count = 0
    s={}
    temp = x[0]
    insert = False
    for y in range(len(x)):

        if x[y] != None:
            if temp == x[y]:
                count += 1
            else:
                if temp is not s.keys():
                    print(temp)
                    print(s)
                    count = 0
                else:
                    insert = True
                count = 0
                count += 1
                temp = x[y]
            if insert:
                s.update([{temp: str(count)}])
                insert = False
            else:
                s.update({temp : str(count)})
                insert = False
    def printexp(s, h):
        append = False
        st = ""
        for keys in s:
            for x in s[keys]:
                if int(x) >= h:
                    append = True
            if append == True:
                for n in range(h):
                    st+=keys
                append = False
            else:
                for x in range(int(s.get(keys))):
                    st += keys
        return st
    print(s)
    express = printexp(s, h)
    return express
exp = "aaabaac"
h=1
print(countofexpression(exp, h))