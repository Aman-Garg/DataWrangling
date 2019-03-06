import slate 

with open('../../data/chapter5/EN-FINAL Table 9.pdf','rb') as f:
    doc = slate.PDF(f)

#this is not yet complete trying to find some other module
for page in doc[:2]:
    print(page)