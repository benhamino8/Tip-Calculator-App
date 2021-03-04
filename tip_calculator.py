'''
Tip Calculator Project
JTC
Created by Benjamin A Horst
3.4.21
'''

print()
print("*************************************************************************************************************")
print()
print("Welcome to the TIP CALCULATOR 3000!")
print("The ultimate tip calculator on the market!")
print("Just answer the next few questions & I will do all the tip calculating for you!!!")
print()
print("*************************************************************************************************************")
print()

'''
I am using a while loop below because I want the code to continue to run until the user inputs correct inputs as per my parameters below (positive float or integer). I found the try/except functions from the link below. 

- The purpose of the Try function is to 'try' that block of code for errors or specifically in this case if the input is less than 0. 
- The purpose of the Except function is to handle errors or specifically in this case if the input was not a float.
- in both the Try & Except blocks of code, the code 'continues' to loop until the input is > than 0 & a float or integer. Once the input is correct, the loop 'breaks'

# https://stackoverflow.com/questions/51086375/python-input-validation-positive-float-or-int-accepted
'''

q1 = "What is the total cost of the bill excluding tax? "
while True: 
    food_cost = input(q1)
    try: 
       food_cost = float(food_cost) #I want this to be a float so people could put in decimals

       if food_cost < 0: #the amount cannot be a negative
           q1 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words. Only numbers! Please input your total bill amount again. "
           continue
       correct_user_input = True        
      
    except ValueError: #this prevents the code from giving an error & stopping if the user inputs a word/letters instead of numbers
        correct_user_input = False 
        q1 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words. Only numbers! Please input your total bill amount again. "
        continue
    
    if correct_user_input:
        break

print()
print("*************************************************************************************************************")
print()

q2 = "How many people are splitting the bill? "
while True: 
    head_count = input(q2)
    try: 
       head_count = int(head_count) #int here because I do not want fractions of people

       if head_count <= 0: #I do not want 0 or less than 0 people
           q2 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words. Only numbers! Please input the number of people who will be splitting the bill again. "
           continue
       correct_user_input = True        
      
    except ValueError:
        correct_user_input = False 
        q2 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words. Only numbers! Please input the number of people who will be splitting the bill again. "
        continue
    
    if correct_user_input:
        break

print()
print("*************************************************************************************************************")
print()

q3 = "What percent would you like to tip (please input a whole number - i.e. 20 percent is input as '20'? "
while True: 
    tip = input(q3)
    try: 
       tip = float(tip) #I want tip to be a float since it is currency

       if tip < 0: #tip can be 0 but not less than 0
           q3 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words or percent sign. Only numbers! Decimals are allowed. Please input the percent tip you would like to leave, again. "
           continue
       correct_user_input = True        
      
    except ValueError:
        correct_user_input = False 
        q3 = "Your response was not in a calculable format. Please ensure you are inputting positive numbers only. And no words or percent sign. Only numbers! Decimals are allowed. Please input the percent tip you would like to leave, again. "
        continue
    
    if correct_user_input:
        break

print()
print("*************************************************************************************************************")
print()

tip_percent = tip/100 #this converts the percent input by the user to a decimal for calculation purposes
tip_amount = food_cost * tip_percent # this calculates the tip amount

tax_percent = 10 # this is the fixed tax as noted in the project description
tax = (food_cost * .10) #this calculates the tax amount

'''
* I used this rounding() function because I wanted my outputs to round to the nearest two decimal number since the output is a currency. However, this did not add 0's when the was not decimals to round and so I had to also use the format() function which is also noted here. I found this code at the below link:

https://stackoverflow.com/questions/20457038/how-to-round-to-2-decimals-with-python#:~:text=Just%20use%20the%20formatting%20with,rounding%20down%20to%202%20decimals.&text=You%20can%20use%20the%20round%20function.&text=You%20can%20use%20the%20string%20formatting%20operator%20of%20python%20%22%25%22.

This code works by applying the round() function to the user input variable (1st arguement) & including the amount of decimals I want (2nd argument)

** I used the format() function because I wanted my outputs to always have two decimals (so I used the {:.2f} python format). I did this because my outputs are US$ currency. This was included because the rounding() function would not add 0's in the event there was nothing to round. I found this code at the below link: 

# https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,number%20with%20two%20decimal%20places.

This code works by applying the python format {:.2f} to the selected variable.
'''

food_cost_rounded = float(round(food_cost, 2)) # *
food_cost_formatted = "{:.2f}".format(food_cost_rounded) # **

tip_percent_rounded = float(round(tip_percent, 2)) # *
tip_amount_rounded = float(round(tip_amount, 2)) # *
tip_amount_formatted = "{:.2f}".format(tip_amount_rounded) # **

tax_rounded = float(round(tax, 2)) # *
tax_formatted = "{:.2f}".format(tax_rounded) # **
print()
print()
print()
print()
print("Here is a summary of everything you told me: ")

print()

print(f"The total food cost is ${food_cost_formatted}.")
print(f"The total number of people splitting the bill is {head_count}.")
print(f"The tip percent is {tip}% and the total tip amount is ${tip_amount_formatted}.")
print(f"The tax is {tax_percent}%.")
print(f"The total tax amount due is ${tax_formatted}.")
print()
print()


print("Above are all of the numbers you have inputted. If everything above is correct, calculated below is the total cost and the cost per person:")
total_bill = food_cost_rounded + tip_amount_rounded + tax_rounded
total_bill_rounded = float(round(total_bill, 2)) # *
total_bill_formatted = "{:.2f}".format(total_bill_rounded) # **

cost_per_person = total_bill / head_count
cost_per_person_rounded = float(round(cost_per_person, 2)) # *
cost_per_person_formatted = "{:.2f}".format(cost_per_person_rounded) # **

print()
print()
print()
print()

print(f"The total cost of the bill is ${total_bill_formatted}.")
print(f"The total cost per person is ${cost_per_person_formatted}.")
print()
print()
print()
print()
print()
print("*************************************************************************************************************")
print()
print()

# I used the below conditional if/elif statements with a number of logic to add some humor to this project. The responses change based on the amount of the bill per person.

if int(cost_per_person) < 5:
    print(f"Whoa! Only ${cost_per_person_formatted}! What a cheap meal! I hope you don't get sick... lol!")

elif int(cost_per_person) >= 5 and int(cost_per_person) < 15:
    print(f"What a reasonably priced meal. It's hard to get a decent meal for less than ${cost_per_person_formatted} these days.")

elif int(cost_per_person) >= 15 and int(cost_per_person) < 25:
    print(f"Seems like a pretty average priced meal. I hope you weren't on a date! Your partner is really going to think you are cheap only spending ${cost_per_person_formatted}! Hahaha!")

elif int(cost_per_person) >= 25 and int(cost_per_person) < 50:
    print(f"I hope you don't spend this much every day! ${cost_per_person_formatted} is no small amount of money to be spending on a meal all the time! What would your parents think?") 

elif int(cost_per_person) >= 50 and int(cost_per_person) < 100:
    print(f"Sheesh... pricey meal dontcha think?? ${cost_per_person_formatted} is a lot! The food better have been good!") 

elif int(cost_per_person) >= 100 and int(cost_per_person) < 300:
    print(f"Dang! You are a baller! You really spent ${cost_per_person_formatted}?!?! I hope this included wine!") 

elif int(cost_per_person) >= 500:
    print(f"WHOOAAAAA... you are a BOSS!!! ${cost_per_person_formatted}?!?! Really!? This is my number - 555-555-5555. I'm really cool & attractive. Call me! I want to go out with you!") 

print()
print()
print("*************************************************************************************************************")
print()
print()
print()
print()
print("Thanks for using the TIP CALCULATOR 3000!! I hope it worked well for you. Please come back again and for any problems or bugs, please email here: ben@aol.com")
print()
print()
print()
print()