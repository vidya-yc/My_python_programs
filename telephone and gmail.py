import re
p=re.compile('\d{3}[-|\.|\s]\d{3}[-|\.|\s]\d{4}')
r=p.findall('345-766-9087 , 879-0987,345 656 8754,67589,546.768.1234 is an American number')
print(r)

a=re.compile('\w+\d+\w*@gmail\.com')
t=a.findall('mail id is vid123@gmail.com ,1234e@gmail.in,vgfh4323hf@gmail.com')
print(t)

