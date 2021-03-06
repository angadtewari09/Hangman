#Command line version of hangman using PYTHON
import random

def hangman():
  
    attempts =0
    max_attempts = 4
    print("\t")
    print("********"+ "\t"+"WELCOME TO THE COMMAND LINE VERSION OF HANGMAN GAME !"+ "\t"+"********")
    print("\n")
    num = int(input("Enter 1 to start the game and  to exit the game" + "\t"))
    
    if (num == 1):
        print("LETS SATRT PLAYING !" +"\n")
        
        words = ['lyncher' ,'choice' , 'batman' , 'superman' , 'hulk' , 'apple' , 'doctor' , 'orange' , 'python' , 'javascript' , 'laptop' , 'computer' , 'internet']
        random_word = random.choice(words)
        
        
        #The actual word is converted into underscores
        word_taken = []
        word_taken = list(random_word)
        hidden_word = []
        
        for i in word_taken :
            hidden_word.append("_")
     
        print("     ---------")
        print("     |     |")
        if attempts > 0:
            print("     |     O")
        else:
            print("     |     ")
                
        if attempts > 1:
            print("     |     /\ ")
        else:
            print("     |     ")        
           
        if attempts > 2:
            print("     |     |")
        else:
            print("     |     ") 
                
        if attempts > 3:
            print("     |     /\ ")
        else:
            print("     |     ")     
           
        print("     |     ") 
        print("--------------   ")
        Game_Over = False
        while not Game_Over: 

            moves = max_attempts - attempts
            print ("Number of attempts still left are: ", moves ,".")
            print("\n")
            
            hide = ' '.join(hidden_word) 
            print ("The current word is : " , hide)
            print("\n")
            
            letter_guessed = input("Please guess a letter:")
            print("\n")

            if letter_guessed in word_taken:
                print("You guessed corectly!", letter_guessed ," is present in the word")
                for i in range( len(word_taken) ):
                    character = word_taken[i]
                    if character == letter_guessed:
                        hidden_word[i] = word_taken[i]
                        word_taken[i] = "_"
                        
            else:
                print("WRONG ANSWER !The letter guessed is not in the word !")
                attempts = attempts + 1
                print("You have only" , max_attempts-attempts," attempts remaining!")
            
            
            print("\n")    
            print("     ---------")
            print("     |     |")

            if attempts > 0:
                print("     |     O")
            else:
                print("     |     ")
                
            if attempts >1:
                print("     |     /\ ")
            else:
                print("     |     ")        
            
            if attempts >2:
                print("     |     |")
            else:
                print("     |     ") 
                
            if attempts >3:
                print("     |     /\ ")
            else:
                print("     |     ")     
           
            print("     |     ") 
            print("--------------   ") 
            print("\n")
            
            
            if ( max_attempts == attempts ):
              print("YOU LET THE HANGMAN DIE!")
              print("Try again later!")
              Game_Over = True
              
        
        
    else: 
        print("GOODBYE SEE YOU SOON!")
        return 0
        
hangman()    
    