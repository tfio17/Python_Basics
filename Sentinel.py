#
#
## Tom
#
#
#
#
## Sentinel Loop
#

Another = [2,4,6,8,10,12,999,12,45,56]

a = 0
for i in Another:
    if i == 999:
        break
    else:
        a = a + i

print(a)
