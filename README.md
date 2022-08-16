# Python_Pygame_TestTubeGame


## Description
  This is a copy of a game that I saw on my phone and decided I wanted to make.
  It will feature the game and also perhaps an algorithym capable of solving the game on its own.
  
## Features
  * A liquid sorting game with up to ten colours
  * A variable number of test tubes and colours depending on player choice
  * A variable number of undos depending on player choice
  * Difficulty settings
  
 ## Tools used
 > This was my first time using python for a graphics game, so I tried out a library called pygame. I also used a build tool known as pybuilder. Finally, in order to make executables for MacOS and Windows, I used Py2app and PyInstaller, respectively.

## Building and Running

### Building
1. Pull this repository from Github: ``git clone https://github.com/MiracleSheep/Javascript_Discord_PollBot.git``
2. Navigate to the pulled repository
3. Install pybuilder; ``pip install pybuilder``
4. Build the project: ``pyb``
5. Find the distribution in ``Target/dist/``
6. The main file is TestTubeGame. Execute that to start the program.
  
  

#### Current Status: Finished

### Known Bugs
* Lightly tapping a trackpad can sometimes be too fast for the game to register the click, a full press is required
* The test tube image is not a transparent png. This is because pygame kept rendering the transparent parts of the image as black, and after trying convert_alpha() and set_colourkey() the background appeared blue and green. 

