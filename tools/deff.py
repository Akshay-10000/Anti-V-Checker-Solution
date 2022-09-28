deff = list(open('vinfo.txt','r').readlines())

for i in deff:
    xyz = open('vhash.txt','a').writelines(i[0:64]+'\n')
    abc = open('vrinfo.txt','a').writelines(i[65:len(i)])