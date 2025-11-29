## Servo-Online

# CONECTIONS

POWER -> GND  
GND -> GND  
DATA -> GPIO28  

# DOCS

Servo Online is a project i've been working on lately (Sorry for the terrible name). The project first oringinated from a school project in
whichwe had to make a mars base, at the time i had no current project and wanted to make the top a swiveling telescope room and decided to 
use a servo and a pi pico 2w

# TECH STACK

For this project i used, micropython and the micropython-servo library to make things a bit easier, as for the other libraries they come
packaged with micropython. As for the microcontroller I used the Rpi Pico 2W although i think the code will also run on the pico w. Before
running this project make sure micropython and the micropython-servo are both installed on the pico before running it it wont explode the
components or anything it just wont work. Of course you can just build your own servo library but if you want an easy plug and play approach i
would recomend just to use the micropython-servo library.

# EXAMPLES

Mind you in the demo the web page has the title mars base servo control because it was originaly for controlling the top of the mars base :)


<img width="2940" height="1912" alt="image" src="https://github.com/user-attachments/assets/b968e25b-0065-4652-b1be-fba264fd676e" />
