# Python_Pygame_TestTubeGame


## Description
  This is a copy of a game that I saw on my phone and decided I wanted to make. That is all.
  
## Features
  * A liquid sorting game with up to ten colours
  * A variable number of test tubes and colours depending on player choice
  * A variable number of undos depending on player choice
  * Difficulty settings
  

#### Current Status: Finished

### Known Bugs
* Lightly tapping a trackpad can sometimes be too fast for the game to register the click, a full press is required
* The test tube image is not a transparent png. This is because pygame kept rendering the transparent parts of the image as black, and after trying convert_alpha() and set_colourkey() the background appeared blue and green. 

