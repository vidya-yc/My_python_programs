import re
text='hello,how are you.'
print(re.sub('[,\.,\s]',':',text))
