f = open("zipf.data", "r+")
r = open("zipf_ara.data", "w")
count = 1
for i in f:
    frequence = int(i.split()[0])
    r.write(i.split()[0] + ' ' + str(count) + ' ' + str(count*frequence) + '\n')
    count += 1


