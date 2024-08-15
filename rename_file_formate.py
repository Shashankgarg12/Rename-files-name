import os

a=1
x=os.listdir('File Handling/for51_question')

# os.chdir('File Handling/for51_question')
# print(os.getcwd())

for i in x:
    if i.endswith('.png'):
        os.rename(f'File Handling/for51_question/{i}',f'File Handling/for51_question/{a}.png')
        a +=1
        
# print(x)