def main():

    print('=======================Grocery List Generator=======================\n')
    grocery_message()
    print ('\nHere is the food you currently have: \n' + '\n*print contents from current_ingredients txt file here* ')
    get_current_diet()
    print('\nHere are some popular recipes for you to try:  \n' + '\n*print recipes names only for current_diet from recipe txt file here*')
    get_current_recipe()
    print('\nHere are the ingredients you will need to buy to make those recipes: \n' + '\n*print ingredients from recipe txt file for each current_recipe*') 
    print('\nTime to go grocery shopping!')

def grocery_message():
    
    message = input('Are you ready to make your grocery list?(YES OR NO) ')
    if str(message).upper() != str('YES'):
        print('\nOh no! Start over when you are ready to make one.\n')
        grocery_message()
    else:
        print("\nOk let's get started! ")    
      

def get_current_diet():

    current_diet = input('\nWhich of the following popular diets is your current diet \n(Keto, Vegan, Low ' +  'Carb, Paleo, or None?) ')
    return current_diet
    
def get_current_recipe():    
    current_recipes = input('\nWhich of these recipes do you want to make? ')
    return current_recipes

main()
