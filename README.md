Overview:

 This assignment was all about creating graphics in some language of our choice. I have decided to make a frog in pygame since I understand pygame the best. To do this I will just need some basic shapes and a background.
	Steps:
	
First thing to do is to import pygame and math
Then make a main method and initialize pygame.
Next I will set the Screen size and screen name.
The next thing to tackle is the background. The first thing to do for it is to set the size to the same size as my window so there isn't blank space, then I set its color and convert it. For color I’m thinking a blue ish since it’ll be a frog.
Next will be to send the background to a function to actually add the image but we’ll get to that later.
Then add a clock for framerate so that everything can be displayed and loaded correctly. Also I will mention now that we will make a while keepGoing loop as we tend to.
After that in the while loop we set the clock to have a tick of 30 for smooth working then a for loop that just makes it so that if the code is open then everything works and runs.
After that you blit the screen to correctly put the background and everything on it to correctly display on the screen. Same with adding a pygame flip so that again all the drawings and such display correctly.
The last part of the main method is to do a pygame.quit() outside the loop for it to end.
The (kinda) last thing to do is to do that if __name__ == __main__ then run main bit

Image Steps:


The first thing I will do is make a function that takes in the background.
Then I’ll add the head of the frog. To do this I will do a Pygame.draw.ellipse() and in the parentheses I’ll add its specifications. These go in the order of (background so it knows to write on it, (r,g,b), (x location, y location), (width, height), and how full it is).
The next shape to tackle is the eyes. Similarly to the ellipse it’ll use a pygame.draw.circle() and in it will be (background again, (r,g,b), (x,y), and the radius around the center of it). I will probably just repeat this but smaller to make the eyes. I will also just duplicate these eyes to make the second one. *Added* I added eyelids to make the frog look better. I already go over arcs later but know I added those here.
The next shape to make is the mouth. This looks to be the hardest part because of the arc requiring a lot to its name. So you do a pygame.draw.arc(background obvs, (r,g,b again), (x location, y location), (size), the degree of the starting point, math.pi divided by the degree of the ending point, then lastly how filled it is). *Post note* Yeah these were the hardest to get right.
The last thing to add to our frog is the iconic tongue. To do this we will add a box in the center of the mouth and a circle on the end for the tip of his tongue. To make the box we do pygame.draw.rect(background, (r,g,b), (starting x, starting y), (width, height), how filled the box is). The circle is the same as the eyes. *Added* I added a pink line down the center to add like dimension. To do this I did pyagme.draw.line(background, (r,g,b), (start x, start y), (end x, end y)).
Last note is for colors I will probably just do shades of green for the frog and pink for the tongue. 
*Added* I added a top hat for visual flair. To do that I just went and before everything else so it’d be in the back I put a black ellipse and a black square. Flair.

What I learned:
		The biggest thing I learned in the project is how much it sucks to line things up correctly. On a more serious note I realized how much the small details mattered. From the eyes being just to close or the angles of the arc being wrong. There are so many places that small things can screw up a project. It shows why double and even triple checking is important.

Instalation:
		It's Pygame so you’re fine running it.
