from random import randint
# repeat = True
# while repeat:
#     print("You rolled",randint(1,6))
#     print("Do you want to roll again?")
#     repeat = ("y" or "yes") in input().lower()
#     if repeat==False:
#         print('Enter Vslid input')
#         repeat = True

repeat = True

while True:
    print('you rolled ',randint(1,6))

    print('Enter yes to roll again and NO to stop')
    if ('y' or 'yes') in input().lower():
        repeat=True
        continue
    elif ('n' or 'no') in input().lower():
        continue
    break
    