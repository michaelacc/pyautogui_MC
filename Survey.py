import pyautogui as pg
import time
import webbrowser

points=0

answer = pg.prompt(
"""
What team do you prefer?

a) The Minnesota Vikings
b) The Celevland Browns
c) I don't like sports

"""
)

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3




answer = pg.prompt(
"""
What do you sleep in?

a) A nightgown
b) A tee shirt
c) A silk suit

"""
)

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3


answer = pg.prompt(
"""
Who do you dislike

a) Gary Anderson 
b) Stven
c) Mandy Mendoza 

"""
)

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3


answer = pg.prompt(
"""
What would you do for halloween?

a) Do a couples coustume  
b) Hanging chad
c) I always wear suits

"""
)





#END OF SURVEY
pg.alert("You are...")

#Marshall
if points < 5:
    pg.alert("Marshall Erkison")
    webbrowser.open("https://i.pinimg.com/736x/a8/bf/29/a8bf29719cc3b7c9cd547ba3c1ff71db--funny-happy-birthday-meme-funny-happy-birthdays.jpg")
#Ted
if points == 5:
    pg.alert("Ted Mosby")
    webbrowser.open("https://img.buzzfeed.com/buzzfeed-static/static/2016-05/10/17/campaign_images/webdr09/how-compatible-are-you-and-ted-mosby-2-18518-1462915869-0_dblbig.jpg")
#Barney
if points >=6:
    pg.alert("Barney Stinston")
    webbrowser.open("https://www.youtube.com/watch?v=C19US6rqqAo")

