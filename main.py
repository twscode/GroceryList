
import tkinter as tk

def main():

  # Read current ingredients from input file.-Mariah Walker
  current_ingredients = []
  with open('current_ingredients.txt') as current_ingredients_file:
    content = current_ingredients_file.read()
    for line in content.split('\n'):
        current_ingredients.append(line)

  # Read recipes from input file and seperate the diet name, recipe name, and ingredients.-Mariah Walker
  recipes = []
  diets = []
  with open('recipes.txt') as recipes_file:
    content = recipes_file.read()
    for line in content.split('\n'):
        recipe = line.split(';')
        recipes.append(recipe)
        if (recipe[0] not in diets):
          diets.append(recipe[0])


  current_ingredients_file.close()
  recipes_file.close()
  
  # Create recipe object instances based on the data read from the input files.-Mariah Walker 
#recipe_info = []
#for recipe in recipes:
#  if(recipe[0] == 'Keto'):
#    recipe_info.append(KetoRecipe(recipe[1], recipe[2]))
#  elif(recipe[0] == 'Low Carb'):
#   recipe_info.append(LowCarbRecipe(recipe[1], recipe[2]))
#  elif(recipe[0] == 'Vegan'):
#    recipe_info.append(VeganRecipe(recipe[1], recipe[2]))
#  elif(recipe[0] == 'Paleo'):
#    recipe_info.append(PaleoRecipe(recipe[1], recipe[2]))

#Create derived classes for each diet type using inheritance, and polymorphism-Theodore Wimberly
chosen_recipe=[]    

class Recipes:
  def __init__(self, diet, meal):
      self.__diet = diet
      self.__meal = meal

class Keto1(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Mac and Cheese [1]') 
      def show_ingredients():  
        print('\nHere are the ingredients you will need: Cauliflower,Olive Oil,Shredded Cheddar Cheese,Butter,Black Pepper')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == '1':
            Keto1.show_ingredients()
            break
            user_done = True
            break
          elif user_choice == '2':
            Keto2.show_ingredients()
            break
            user_done = True
          else:
            print("\nNot a valid option")
            Keto1.get_ingredients()
            break    

class Keto2(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Fruit Salad [2]')
      def show_ingredients():   
        print('\nHere are the ingredients you will need: Grapes,Blueberry,Strawberry,Melon')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == '1':
            Keto1.show_ingredients()
            user_done = True
          elif user_choice == '2':
            Keto2.show_ingredients
            user_done = True
            break
          else:
            print("\nNot a valid option")
            Keto2.get_ingredients()
            break             

class Vegan1(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Roasted Corn [1]') 
      def show_ingredients():  
        print('\nHere are the ingredients you will need: Corn,Olive Oil,Black Pepper,Onions,Salt')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == '1':
            Vegan1.show_ingredients()
            break
            user_done = True
            break
          elif user_choice == '2':
            Vegan2.show_ingredients()
            break
            user_done = True
          else:
            print("\nNot a valid option")
            Vegan1.get_ingredients()
            break            

class Vegan2(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Tomato Soup [2]') 
      def show_ingredients():  
        print('\nHere are the ingredients you will need: Onions,Garlic,Tomatoes,Coconut,Olive Oil,Jalapeño')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == '1':
            Vegan1.show_ingredients()
            break
            user_done = True
            break
          elif user_choice == '2':
            Vegan2.show_ingredients()
            break
            user_done = True
          else:
            print("\nNot a valid option")
            Vegan1.get_ingredients()
            break                

class Low_Carb(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Pesto Chicken [1]') 
      def show_ingredients():  
        print('\nHere are the ingredients you will need: Chicken Breast,Basil,Pine Nuts,Parmesan Cheese,Olive Oil')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == 'Y' or user_choice == 'y':
            Low_Carb.show_ingredients()
            break
          elif user_choice =='N' or user_choice == 'n':
            print("\nThat's the only recipe we have for now. Retry when you are ready to make a grocery list")
            break
          else:
            print("\nNot a valid option")
            Low_Carb.get_ingredients()
            break    


class Paleo(Recipes):
      def __init__(self, diet, meal):
        Recipes.__init__(diet)
        Recipes.__init__(meal)
      def show_meal():
        print('Shrimp Scampi [1]') 
      def show_ingredients():  
        print('\nHere are the ingredients you will need: Shrimp,Ghee,Garlic,White Wine,Butter,Black Pepper')
      def get_ingredients():
        user_choice= input()
        user_done = False
        while user_done == False:
          if user_choice == 'Y' or user_choice == 'y':
            Paleo.show_ingredients()
            break
          elif user_choice =='N' or user_choice == 'n':
            print("\nThat's the only recipe we have for now. Retry when you are ready to make a another grocery list")
            break
          else:
            print("\nNot a valid option")
            Paleo.get_ingredients()
            break                                               
#Created functions for ingredients buttons-Theodore Wimberly
diet_storage =0
def click_button():
  user_food.append('Basil')
def click_button2():
  user_food.append('Black Pepper')
def click_button3():
  user_food.append('Butter')
def click_button4():
  user_food.append('Cauliflower')
def click_button5():
  user_food.append('Cheddar Cheese')
def click_button6():
  user_food.append('Chicken Breast')
def click_button7():
  user_food.append('Coconut')
def click_button8():
  user_food.append('Garlic')
def click_button9():
  user_food.append('Ghee') 
def click_button10():
  user_food.append('Jalapeño')
def click_button11():
  user_food.append('Nuts')
def click_button12():
  user_food.append('Olive Oil')
def click_button13():
  user_food.append('Onions')
def click_button14():
  user_food.append('Parmesan Cheese')
def click_button15():
  user_food.append('Pine')
def click_button16():
  user_food.append('Shrimp')
def click_button17():
  user_food.append('Tomatoes')
def click_button18():
  user_food.append('White Wine')
def click_button19():
  user_recipes.append('Keto')
def click_button20():
  user_recipes.append('Low Carb')
def click_button21():
  user_recipes.append('Paleo') 
def click_button22():
  user_recipes.append('Vegan')
  
main()

print('===================== Grocery List Generator =====================\n')
print('Are you ready to begin? [Y/N]')
user_answer_1= input()
if user_answer_1 == 'Y' or user_answer_1 == 'y':
  print("\nLet's get started!" )
  print("Choose your current ingredients/diet from the windows above:" )  
else:
  print('Retry when you are ready to make a grocery list')
  exit()



user_food=[]
user_food.clear()
user_recipes=[]
user_recipes.clear()


#Create a recipe base class-Marcus Cusaac
class Recipe:
    def __init__(self, recipe_name, ingredients):
      self._recipe_name = recipe_name
      self._ingredients = ingredients
    def get_recipe_name(self):
       return self._recipe_name
    def get_required_ingredients(self):
      return self._ingredients

#Create derived classes for each diet type using inheritance, and polymorphism-Marcus Cusaac

class KetoRecipe(Recipe):
  def __init__(self,recipe_name,ingredients):
    Recipe.__init__(recipe_name, ingredients)
    self.diet_name = "Keto"
  def get_diet_name(self):
    return self._diet_name

class VeganRecipe(Recipe):
  def __init__(self,recipe_name,ingredients):
    Recipe.__init__(recipe_name, ingredients)
    self.diet_name = "Vegan"
  def get_diet_name(self):
    return self._diet_name

class LowCarbRecipe(Recipe):
  def __init__(self,recipe_name,ingredients):
    Recipe.__init__(recipe_name, ingredients)
    self.diet_name = "Low Carb"
  def get_diet_name(self):
    return self._diet_name

class PaleoRecipe(Recipe):
  def __init__(self,recipe_name,ingredients):
    Recipe.__init__(recipe_name, ingredients)
    self.diet_name = "Paleo"
  def get_diet_name(self):
    return self._diet_name

#Created ingredients buttons-Theodore Wimberly
def ingredient_button(label):
  label.config(text=str(ingredient_button))
root = tk.Tk()
root.title("Ingredients")
label = tk.Label(root, text= 'Click the ingredients that you have below. Click DONE when you are done.' ,fg="red")
label.pack()

button = tk.Button(root, text='Basil', width=15, command=click_button)
button.pack(side='top')

button2 = tk.Button(root, text='Black Pepper', width=15, command=click_button2)
button2.pack(side='top')

button3 = tk.Button(root, text='Butter', width=15, command=click_button3)
button3.pack(side='top')

button4 = tk.Button(root, text='Cauliflower', width=15, command=click_button4)
button4.pack(side='top')

button5 = tk.Button(root, text='Cheddar Cheese', width=15, command=click_button5)
button5.pack(side='top')

button6 = tk.Button(root, text='Chicken Breast', width=15, command=click_button6)
button6.pack(side='top')

button7 = tk.Button(root, text='Coconut', width=15, command=click_button7)
button7.pack(side='top')

button8 = tk.Button(root, text='Garlic', width=15, command=click_button8)
button8.pack(side='top')

button9 = tk.Button(root, text='Ghee', width=15, command=click_button9)
button9.pack(side='top')

button10 = tk.Button(root, text='Ginger', width=15, command=click_button10)
button10.pack(side='top')

button11 = tk.Button(root, text='Jalapeño', width=15, command=click_button11)
button11.pack(side='top')

button12 = tk.Button(root, text='Olive Oil', width=15, command=click_button12)
button12.pack(side='top')

button13 = tk.Button(root, text='Onions', width=15, command=click_button13)
button13.pack(side='top')

button14 = tk.Button(root, text='Parmesan Cheese', width=15, command=click_button14)
button14.pack(side='top')

button15 = tk.Button(root, text='Pine Nuts', width=15, command=click_button15)
button15.pack(side='top')

button16 = tk.Button(root, text='Shrimp', width=15, command=click_button16)
button16.pack(side='top')

button17 = tk.Button(root, text='Tomatoes', width=15, command=click_button17)
button17.pack(side='top')

button18 = tk.Button(root, text='White Wine', width=15, command=click_button18)
button18.pack(side='top')

label = tk.Label(root, text= 'Click your diet from the list below. Click DONE when you are done:' ,fg="red")

button_done = tk.Button(root, text='DONE', width=15, command=root.destroy)
button_done.pack(side='bottom')
root.mainloop()

#Created diet buttons-Theodore Wimberly
def recipe_button(label):
  label.config(text=str(ingredient_button))
root = tk.Tk()
root.title("Diet")
label = tk.Label(root, text= 'Click the diet that you are currently on below. Click DONE when you are done:' ,fg="red")
label.pack()

button = tk.Button(root, text='Keto', width=15, command=click_button19)
button.pack(side='top')

button2 = tk.Button(root, text='Low Carb', width=15, command=click_button20)
button2.pack(side='top')

button3 = tk.Button(root, text='Paleo', width=15, command=click_button21)
button3.pack(side='top')

button4 = tk.Button(root, text='Vegan', width=15, command=click_button22)
button4.pack(side='top')

button_done = tk.Button(root, text='DONE', width=15, command=root.destroy)
button_done.pack(side='bottom')
root.mainloop()

#Wrote code to prompt the user to input what food they currently have, what is their diet, and what recipes do they want to make?-Theodore Wimberly
print("\nHere is the food you currently have:")
print(" ")
i = 0
while i< len(user_food):
  print(user_food[i])
  i= i+1
print(" ")  
print("Here is the diet you chose:")
print(" ")
print(user_recipes[-1])
print(" ")
print("Here are some "+ user_recipes[-1]+ " recipes for you to try:")
print(" ")
if user_recipes[-1] == 'Keto':
  Keto1.show_meal()
  Keto2.show_meal()
  print(" ")
  print("Which recipe would you like to make (1 or 2)?")
  Keto1.get_ingredients()   
elif user_recipes[-1] == 'Vegan': 
  Vegan1.show_meal()
  Vegan2.show_meal()
  print(" ")
  print("Which recipe would you like to make (1 or 2)?")
  Vegan1.get_ingredients()
elif user_recipes[-1] == 'Low Carb':
  Low_Carb.show_meal()
  print(" ")
  print("Would you like to make this recipe?[Y/N]")
  Low_Carb.get_ingredients()    
elif user_recipes[-1] == 'Paleo':
  Paleo.show_meal()
  print(" ")
  print("Would you like to make this recipe?[Y/N]")
  Paleo.get_ingredients()    
print(" ")  
print("Thank you for using grocery list generator, hit ENTER to exit.")
input()

#top = Tk()  
#sb = Scrollbar(top)  
#sb.pack(side = RIGHT, fill = Y)  
  
#mylist = Listbox(top, yscrollcommand = sb.set )  
  
#for line in range(30):  
    #mylist.insert(END, "Number " + str(line))  
  
#mylist.pack( side = LEFT )  
#sb.config( command = mylist.yview )  
