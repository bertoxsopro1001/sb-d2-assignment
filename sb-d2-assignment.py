from random import randint

First_input = int(input("Enter First Combination :"))
Second_input = int(input("Enter First Combination :"))
Third_input = int(input("Enter First Combination :"))

first_result_combination = randint(0,9)
second_result_combintaion = randint(0,9)
third_result_combination = randint(0,9)

User_input = [First_input,Second_input,Third_input]
result = [first_result_combination,second_result_combintaion,third_result_combination]



if User_input == result:
    print(f"{result} You win! ")

elif sorted(User_input) == sorted(result):
    print(f"{result} Partial win! ")
else:
    print(f" you lose ! {result}  ")
