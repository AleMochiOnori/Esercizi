# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza, instead of printing just the name of the pizza. For each pizza, you should have one line of output containing a simple statement like I like pepperoni pizza.
# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

frasi: list = ["mi piace tanto la ", "vorrei avere una ", "vorrei ordinare la "]
pizzas: list = ['margherita', 'diavola' , "rossa con i wusstel/salsiccia"]


for f,i in zip(frasi,pizzas) :
    print(f"{f} Pizza {i}")
print(f"Mi piace molto la pizza margerita ma ogni tanto per cambiare prendo anche la {pizzas[-2]} e la", pizzas[-1])        



# 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
# • Add a line at the end of your program, stating what these animals have in common. You could print a sentence, such as Any of these animals would make a great pet!

animalLove: list = [" is one of my favourite pets."," is the best friend of the human being and i think that's true because i love them even more than cats."," can be a pet for arguable people that want exotic pets. i don't raccomand though."]
pets :list = ['Cat', 'Dog' , "Shark"]
for a,i in zip(pets,animalLove) :
    print(f"{a}{i}")
print(f"I really like either {pets[0]} and {pets[1]} {pets[2]} non lo è e mi fa paura")    


# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.


for i in range(1,21):
    print(i)



# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)




My_list: list = [*range(1, 1000000,1)]
print(My_list)





# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.


minimun: int = min(My_list)
maximum : int = max(My_list)
sum : int = sum(My_list)
print(sum)





# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.




My_list: list = [*range(1, 1000000,1)]
print(My_list)

