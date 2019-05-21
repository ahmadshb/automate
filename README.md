#Future Fight Commands

##Setup

###Dependencies

To set up you will need:

* Python 3 (https://www.python.org/downloads/)
* pyautogui (`pip install pyautogui`)
* Tesseract (https://github.com/UB-Mannheim/tesseract/wiki)
* pytesseract (`pip install pytesseract`)

*Note: If you are getting errors with pytesseract (`pytesseract.pytesseract.TesseractNotFoundError`), ensure tesseract is installed to PATH.*

This is designed to work for the game fullscreen in any emulator, though you can customise it to work with other layouts through the config file, `config.ini`.

#### Tesseract OCR

> **Add to PATH**

As mentioned before if you are given an error that says something about Tesseract not being in your "path", you may have to add it manually:

1. Find where Tesseract OCR installed to on your PC (eg. `C:/Program Files (x86)/Tesseract-OCR`)
2. In the Windows search bar type in "environment variables" and click the option that says "Edit the system environment variables"
3. A window called "System Properties" should open, click the button in the bottom right that is labelled "Environment Variables".
4. In the top half of the "Environment Variables" window that is labelled "User variables for [username]", click the row that has the variable name "Path" and click "Edit..."
5. A new window should appear called "Edit environment variable". Click "New" on the right hand side and in the text field that appears, paste in the location of your Tesseract OCR folder. You don't need to point it towards the executable file, just the folder it is contained in.
6. Click OK on everything and close those windows. You don't need to restart your computer but you will need to restart the command prompt so it recognises your changes to PATH.

> **Trained Data File**

This isn't completely necessary but it would help quite a bit. It's not perfect since it's auto-generated but it can sort of recognise most text in the font MFF uses.

1. Find where Tesseract OCR installed to on your PC (eg. `C:/Program Files (x86)/Tesseract-OCR`)
2. Go into the "tessdata" subfolder and drop in the "mff.traineddata" file. There should be some other .traineddata files in there so you know you're in the right place.

###Folder Setup

Create or allocate a folder to store all the relevant files in. This folder should contain:

* automate.py
* config.ini
* a subfolder named "ocr"

Without all 3 of these things the script will not work.

### Running the Script

1. Open terminal (command prompt or cmd)
2. Use the command `cd` to navigate to your folder where you have stored the files (eg. `cd iMuffles/mff/script`)
3. Use the command `python` to run the script in the terminal (eg. `python automate.py`)

###Determining Screen Coordinates 

A big part of this program will be entering the screen coordinates of various objects for your screen layout.



##Functions



####Config - General

>**delay_loading_screen**

* Accepts: Integer
* Default: 5

The upper bound time, in seconds, it takes for a loading screen to finish (the ones that display fullscreen loading artwork). The script does not detect exactly when a loading screen will end, so guess a time that is a safe amount higher than the average observed time.

Loading screen times are typically determined by the speed of your device, not your internet connection.

>**delay_orange_circle**

* Accepts: Integer
* Default: 3

The upper bound time, in seconds, it takes for a spinning orange circle to finish (the ones that appear over the game). The script does not detect exactly when an orange circle will end, so guess a time that is a safe amount higher than the average observed time.

Orange circle times are typically determined by your internet connection, not the speed of your device.

>**delay_game_startup**

* Accepts: Integer
* Default: 30

The upper bound time, in seconds, it takes for the game to boot up after a force close, from clicking on the app icon to the homepage. The script does not detect exactly when the game loads, so guess a time that is a safe amount higher than the average observed time.

Game startup times are typically determined by both internet connection and the speed of your device.

>**use_image_location**

* Accepts: `True`/`False`
* Default: True

A `True` or `False` setting that determines whether the script will try to recognise buttons by image. If `True`, the script will require less setup, but it will run slower and there's a chance it won't work with resizing and such. If `False`, you will have to enter/verify **all** the coordinates of various buttons manually.

##Uru Functions

###Amplify

There are 2 functions here - `AmplifyToFour()` and `AmplifyToFive()` - and they do exactly what you think they do. Both commands should be run from a character's gear's Uru page, and have the option to enhance just that gear, or multiple of the character.

`AmplifyToFour()` continuously rolls amplifications until 4 or 5 slots are amplified, then either stops or moves to the next gear.

`AmplifyToFive()` makes use of the "Chain Amplification" inbuilt function, but keeps doing x10 chains until 5 slots are amplified.

####Config for Uru Amplify

###Upgrade

`UruUpgrade()` is a simple function. Open a stack of Uru's enhancement page and this function will run until the stack cannot be upgraded anymore. This can also be handled using macro but it is a bit more intelligent here because it will stop once the stack is empty.

####Config for Uru Upgrade

##Repeat Functions

##ISO-8 Functions

##Force Close Functions

### Colossus

