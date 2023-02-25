a='hrudayesh'
l='guntur'
# with open('dat.txt','w') as mfile:
#     mfile.write(f'my name is {a}\nmy location is {l}')
with open('dat.txt','r') as file:
    l=file.readlines()
print(l[0])