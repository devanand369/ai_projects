import os

os.chdir('./Dataset/test')

i = 1
for file in os.listdir():
    src = file
    dst = 'joker' + '_' + str(i) + '.jpg'
    os.rename(src, dst)
    i += 1
