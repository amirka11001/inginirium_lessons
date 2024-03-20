slovo = input()

slovocod1 = slovo[0:-1:2]
slovocod2 = slovo[1:int(len(slovo)):2]

if int(len(slovo)) % 2 != 0:
    slovocod2 = slovocod2 + str(".")

for i in range(0, len(slovo), 1):
    print(str(slovocod1[i]) + str(slovocod2[i]))
