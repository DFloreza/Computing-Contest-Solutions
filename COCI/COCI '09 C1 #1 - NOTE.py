# COCI '09 Contest #1 Note
# Dexter Floreza
userNoteOrder = []
ascendingNoteOrder = ["1","2","3","4","5","6","7","8"]
descendingNoteOrder = ["8", "7", "6", "5","4","3","2","1"]
a,b,c,d,e,f,g,h = [str(x) for x in input().split()]

userNoteOrder.append(a)
userNoteOrder.append(b)
userNoteOrder.append(c)
userNoteOrder.append(d)
userNoteOrder.append(e)
userNoteOrder.append(f)
userNoteOrder.append(g)
userNoteOrder.append(h)

if userNoteOrder == ascendingNoteOrder:
    print("ascending")

elif userNoteOrder == descendingNoteOrder:
    print("descending")

else:
    print("mixed")

