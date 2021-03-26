### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

#line 22 - should be "==", so it compares card 1 to int 1.
#line 23 - should have colon (:) at the end of else statement 
  def check_for_ace(self, card):
    if card.value = 1: 
      return True
    else               
      return False

#line 31 - "dif" should be "def" and there needs to be a comma between card1 and card 2, to separate the arguments 
#line 32 - 'if statement' should be indented, as it will not be used inside the highest card function otherwise
#line 33 - card should be changed to card1, as it will not relate to the argument of card1 otherwise

dif highest_card(self, card1 card2): 
if card1.value > card2.value:        
  return card                                   
else:
  return card2
  
#line 41 - indentation needed for function, as othersie it will not be used inside the class
#line 39 - 'total' has to be made into a variable and value assigned to it by adding " = 0", otherwise the for loop will not see the word 'total' as a variable
#line 45 - string interpolaton is needed here to make the print statement run - f"You have a total of {total}".  The return statement also needs to be moved to the same indentation level as the for loop.

def cards_total(self, cards):          
  total                                
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```

