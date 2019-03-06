import slate 

with open('../../data/chapter5/EN-FINAL Table 9.pdf','rb') as f:
    doc = slate.PDF(f)

for page in doc[:2]:
    print(page)