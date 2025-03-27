# Contoh infinite loop
# while True:
#     num = int(input("Enter an integer: "))
#     print("The double of",num,"is",2 * num)

#Contoh untuk loop with condition at the top:
# n = int(input("Enter n: "))
# # initialize sum and counter
# sum = 0
# i = 1
# while i <= n:
#    print('i:', i)
#    sum = sum + i
#    i = i+2
# print("The sum is",sum)

#Contoh untuk loop with condition in the middle:
# vowels = "aeiouAEIOU"
# while True:
#     v = input("Enter a vowel: ")
#     # condition in the middle
#     if v in vowels:
#         break
#     print("That is not a vowel. Try again!")
# print("Thank you!")

#Contoh untuk loop with condition at the bottom:
import random as rd
while True:
    input("Press enter to roll the dice")
    # get a number between 1 to 6
    num = rd.randint(1, 6)
    print("You got", num)
    option = input("Roll again?(y/n) ")

    # condition
    if option == 'n':
        break