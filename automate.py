#A collection of commands to automate various Marvel Future Fight functions.
#This shit only works if you are running an emulator in fullscreen.

import os
import sys
import pyautogui as gui
import pytesseract as ocr
import time
import math
import datetime
from itertools import islice
from colorama import Fore, Style, init
from terminaltables import SingleTable
from mff_data import Enhancement, GoldCost, Specials, CTPs, Missions, Collections
try:
    from configparser import ConfigParser, SafeConfigParser
except ImportError:
    from ConfigParser import ConfigParser, SafeConfigParser
delay = 2

#COLORS
#Yellow = user input
#Cyan = begin and end
#Green = nice
#Red = not nice
#Magenta = error


class MFF_Automate:
    def __init__(self):
        """Initialising some variables."""

        self.conf = ConfigParser()

        #Find config file
        os.chdir(sys.path[0])
        if os.path.exists('config.ini'):
            self.conf.read('config.ini')
            self.conf.read('data.ini')
        else:
            raise FileNotFoundError('Config file, config.ini, was not found.')

        #Read delays from config
        self.image_location = self.conf.get('GENERAL', 'use_image_location')
        self.delay_loading_screen = int(
            self.conf.get('GENERAL', 'delay_loading_screen'))
        self.delay_orange_circle = int(
            self.conf.get('GENERAL', 'delay_orange_circle'))
        self.delay_game_startup = int(
            self.conf.get('GENERAL', 'delay_game_startup'))
        self.delay_tab_in = int(self.conf.get('GENERAL', 'delay_tab_in'))

        #Warning text
        self.first_time = True
        self.Menu()

    def Menu(self):
        """Basic menu to show and select functions."""

        print(
            Fore.YELLOW +
            """MFF_Automate by PinkChode: choose the function you would like to use.
        1: AmplifyToFour()
        2: ISORoller()
        3: Shifters()
        4: Po10tial()
        5: DoMyDailies()
        6: RunThisMission()
        0: MiscCommands()""" + Style.RESET_ALL)
        selection = input()

        if selection == "1":
            self.AmplifyToFour()
        elif selection == "2":
            self.ISORoller()
        elif selection == "3":
            self.Shifters()
        elif selection == "4":
            self.Po10tialVerification()
        elif selection == "5":
            self.DoMyDailies()
        elif selection == "6":
            self.RunThisMission()
        elif selection == "0":
            self.MiscCommands()
        else:
            print(Fore.MAGENTA + "Wrong input, only enter the numbers listed")
            return
###
### 4-Slot Uru Amplification
###

    def AmplifyToFour(self):
        """Amplifies Urus to 4 Amplified Slots or higher."""

        mult = self.ValidateBooleanInput(
            'Do you want to amplify multiple gears (y) or just this one (n)? ',
            default='n')
        if mult == 'y' or mult == 'Y':
            print(
                Fore.YELLOW +
                'Which gears do you wish to amplify? (eg. 1234 or 134, no spaces)'
                + Style.RESET_ALL)
            gears = input()
            #Function validates the input and returns as a list
            gear_list = self.StringToListValidation(gears, 4)
            for gear in gear_list:
                if self.first_time == True:
                    self.FunctionStart()
                    self.first_time = False
                #Clicks on gears and calls the clicking function
                if gear == str(1):
                    pos_x = self.conf.get('URU_AMPLIFY', 'firstgear_x')
                    pos_y = self.conf.get('URU_AMPLIFY', 'firstgear_y')
                elif gear == str(2):
                    pos_x = self.conf.get('URU_AMPLIFY', 'secondgear_x')
                    pos_y = self.conf.get('URU_AMPLIFY', 'secondgear_y')
                elif gear == str(3):
                    pos_x = self.conf.get('URU_AMPLIFY', 'thirdgear_x')
                    pos_y = self.conf.get('URU_AMPLIFY', 'thirdgear_y')
                elif gear == str(4):
                    pos_x = self.conf.get('URU_AMPLIFY', 'fourthgear_x')
                    pos_y = self.conf.get('URU_AMPLIFY', 'fourthgear_y')
                else:
                    print(Fore.MAGENTA + "This wasn't supposed to happen")
                    return
                time.sleep(1)
                gui.click(int(pos_x), int(pos_y))
                self.AmplifyClicker(gear)
            #Output and tab back to terminal
            print(Fore.GREEN + 'Finished amplifying!')
            self.FunctionEnd()
        else:
            self.FunctionStart()
            self.AmplifyClicker()
            #Output and tab back to terminal
            print(Fore.GREEN + 'Finished amplifying!')
            self.FunctionEnd()

    def AmplifyClicker(self, gear_number=0):
        """Does the actual clicking to amplify."""

        #Find buttons
        if self.image_location == str(True):
            x1, y1 = gui.locateCenterOnScreen(
                'images/uru_amplification_button.png')
            x2, y2 = gui.locateCenterOnScreen('images/amplify_button.png')
        elif self.image_location == str(False):
            x1 = self.conf.get('URU_AMPLIFY', 'uru_amplification_button_x')
            y1 = self.conf.get('URU_AMPLIFY', 'uru_amplification_button_y')
            x2 = self.conf.get('URU_AMPLIFY', 'amplify_button_x')
            y2 = self.conf.get('URU_AMPLIFY', 'amplify_button_y')
        else:
            print(self.image_location + 'error')
            return

        #Navigating to amplify page
        time.sleep(self.delay_orange_circle)
        gui.click(int(x1), int(y1))
        time.sleep(self.delay_orange_circle)

        #Loop declarations
        found = False
        tries = 0

        #Loops until 4 or 5 slots amplified
        while found == False:
            gui.click(int(x2), int(y2))
            time.sleep(self.delay_orange_circle)
            tries += 1
            #Image location method
            if self.image_location == str(True):
                if gui.locateCenterOnScreen('images/4_amplified.png'):
                    found = True
                    amps = 4
                elif gui.locateCenterOnScreen('images/5_amplified.png'):
                    found = True
                    amps = 5
            #OCR method
            elif self.image_location == str(False):
                image = gui.screenshot(
                    'ocr/uru_amp.png',
                    region=(int(self.conf.get('URU_AMPLIFY', 'amps_x')),
                            int(self.conf.get('URU_AMPLIFY', 'amps_y')), 391,
                            42))
                string = ocr.image_to_string(image, lang="mff")
                string = string[-1]
                if string == str(4):
                    found = True
                    amps = 4
                elif string == str(5) or string == "S" or string == "s":
                    found = True
                    amps = 5
        #Calculate gold spent and output
        gold = "{:,d}".format(tries * 30000)
        #If multiple gears
        gear_text = ""
        if gear_number != 0:
            gear_text = f"Gear {gear_number} "
        print(
            Fore.GREEN +
            f'Amplified {gear_text}to {amps} slots in {tries} attempts! ({gold} Gold)'
        )
        self.Logging('URU AMPLIFICATION', '1-3', tries - 1)
        self.Logging('URU AMPLIFICATION', str(amps), 1)
        #Close button
        if self.image_location == str(True):
            x3, y3 = gui.locateCenterOnScreen('images/uru_close_button.png')
        else:
            x3 = int(self.conf.get('URU_AMPLIFY', 'close_button_x'))
            y3 = int(self.conf.get('URU_AMPLIFY', 'close_button_y'))
        gui.click(x3, y3)

###
###
###

    def AmplifyToFive(self):
        """Runs "Chain Amplification" until you get 5 slots amplified."""
        print('i')

###
### ISO-8
###

    def ISORoller(self):
        """Rolls repeatedly until a specific ISO set is rolled."""
        print(
            Fore.YELLOW +
            """Which of these ISO sets would be acceptable to you? (eg. 1234 or 134, no spaces)
        1: Hawk's Eye
        2: Overdrive
        3: Power of Angry Hulk
        4: I Am Also Groot.
        5: Stark Backing
        6: Binary Power
        7: Drastic Density Enhancement""" + Style.RESET_ALL)
        sets = input()

        self.FunctionStart()

        #Puts desired sets into a list
        set_list = self.StringToListValidation(sets, 7)

        #Rolls 10
        self.Click('ISO_SETS', 'auto_set_change')
        time.sleep(1)

        #Loop declarations
        tries = 0
        found = False

        while found == False:
            self.Click('ISO_SETS', 'roll_20_times')
            time.sleep(self.delay_orange_circle)
            time.sleep(
                10)  #It takes just over 10 seconds to auto roll 20 ISO sets
            image = gui.screenshot(
                'ocr/isoset.png',
                region=(int(self.conf.get('ISO_SETS', 'set_text_x')),
                        int(self.conf.get('ISO_SETS', 'set_text_y')),
                        int(self.conf.get('ISO_SETS', 'set_text_length')),
                        int(self.conf.get('ISO_SETS', 'set_text_height'))))
            string = ocr.image_to_string(image, lang="mff")
            tries += 1

            for iso_set in set_list:
                if iso_set == str(1) and self.conf.get('ISO_SETS',
                                                       'hawks_eye') in string:
                    print(Fore.GREEN + "Rolled Hawk's Eye successfully in " +
                          str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(2) and self.conf.get(
                        'ISO_SETS', 'overdrive') in string:
                    print(Fore.GREEN + "Rolled Overdrive successfully in " +
                          str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(3) and self.conf.get(
                        'ISO_SETS', 'power_of_angry_hulk') in string:
                    print(Fore.GREEN +
                          "Rolled Power of Angry Hulk successfully in " +
                          str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(4) and self.conf.get(
                        'ISO_SETS', 'i_am_also_groot') in string:
                    print(
                        Fore.GREEN + "Rolled I Am Also Groot. successfully in "
                        + str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(5) and self.conf.get(
                        'ISO_SETS', 'stark_backing') in string:
                    print(Fore.GREEN + "Rolled Stark Backing successfully in "
                          + str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(6) and self.conf.get(
                        'ISO_SETS', 'binary_power') in string:
                    print(Fore.GREEN + "Rolled Binary Power successfully in " +
                          str(tries) + " x20 attempts.")
                    found = True
                elif iso_set == str(7) and self.conf.get(
                        'ISO_SETS', 'drastic_density_enhancement') in string:
                    print(Fore.GREEN +
                          "Rolled Drastic Density Enhancement successfully in "
                          + str(tries) + " x20 attempts.")
                    found = True
        self.FunctionEnd()

###
###
###

    def TrackingRun(self):
        print('i')

###
### Shifters
###

    def Shifters(self):
        """Select which mode to run a shifter function on"""
        print(Fore.YELLOW +
              f"""Which gamemode would you like to find Shifters in?
        1. X-Force Epic Quest ({Fore.RED}Colossus{Fore.YELLOW})
        2. First Family Epic Quest ({Fore.MAGENTA}Victorious{Fore.YELLOW})
        3. Special Missions ({Fore.GREEN}Gwenpool{Fore.YELLOW}/{Fore.CYAN}Inferno{Fore.YELLOW}/{Fore.GREEN}Vulture{Fore.YELLOW})"""
              + Style.RESET_ALL)
        gamemode = input()
        if gamemode == "1":
            self.Colossus()
        elif gamemode == "2":
            self.Victorious()
        elif gamemode == "3":
            self.Specials()
        else:
            print(Fore.MAGENTA + "Wrong input, only enter the numbers listed")
            return

    def Colossus(self, runs=[]):
        """Force closes Colossus missions until a shifter is found. Start on X-Force Epic Quest Menu"""

        #If running shifters only
        if len(runs) == 0:
            #Get inputs
            mission1 = self.ValidateIntegerInput(
                'How many "Chrome-Plated Comrade" missions do you want to run? ',
                0,
                3,
                default=3)
            mission2 = self.ValidateIntegerInput(
                'How many "Psy-Locked Out" missions do you want to run? ',
                0,
                3,
                default=3)
            mission3 = self.ValidateIntegerInput(
                'How many "Beginning of the Chaos" missions do you want to run? ',
                0,
                2,
                default=2)

            self.FunctionStart()
        else:
            mission1 = runs[0]
            mission2 = runs[1]
            mission3 = runs[2]

        #Keep the initial inputs for logging later
        entries_input = [mission1, mission2, mission3]
        attempts = [0, 0, 0]

        #Navigate to Epic Quest
        self.NavToQuest('xforce')

        nav = True
        while mission1 > 0:
            if nav:
                self.Click('SHIFTER', 'stupid_xmen')
                time.sleep(2)
                self.Click('SHIFTER', 'chrome_plated_comrade')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission1, nav = self.RegularCheckShifter(
                mission1, "Chrome-Plated Comrade", "xforce", "fantomex")
            attempts[0] += 1
        nav = True
        while mission2 > 0:
            if nav:
                self.Click('SHIFTER', 'stupid_xmen')
                time.sleep(2)
                self.Click('SHIFTER', 'psylocked_out')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission2, nav = self.RegularCheckShifter(
                mission2, "Psy-Locked Out", "xforce", "colossus")
            attempts[1] += 1
        nav = True
        while mission3 > 0:
            if nav:
                self.Click('SHIFTER', 'beginning_of_the_chaos')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission3, nav = self.ChaosCheckShifter(
                mission3, "Beginning of the Chaos", "xforce")
            attempts[2] += 1

        #Go back home when loop finished
        time.sleep(0.3)
        self.Click('COORDS', 'home')

        #Logging
        self.Logging('CHROME-PLATED COMRADE', 'true', entries_input[0])
        self.Logging('CHROME-PLATED COMRADE', 'false',
                     attempts[0] - entries_input[0])
        self.Logging('PSY-LOCKED OUT', 'true', entries_input[1])
        self.Logging('PSY-LOCKED OUT', 'false', attempts[1] - entries_input[1])
        self.Logging("BEGINNING OF THE CHAOS", 'true', entries_input[2])
        self.Logging("BEGINNING OF THE CHAOS", 'false',
                     attempts[2] - entries_input[2])

        if len(runs) == 0:
            self.FunctionEnd()

    def Victorious(self, runs=[]):
        """Force closes Victorious missions until a shifter is found. Start on First Family Epic Quest Menu"""

        #If running shifters only
        if len(runs) == 0:
            #Get inputs
            mission1 = self.ValidateIntegerInput(
                'How many "Latverian Champion" missions do you want to run? ',
                0,
                3,
                default=3)
            mission2 = self.ValidateIntegerInput(
                'How many "In the Shadow of Doom" missions do you want to run? ',
                0,
                3,
                default=3)
            mission3 = self.ValidateIntegerInput(
                '''How many "Doom's Day" missions do you want to run? ''',
                0,
                2,
                default=2)

            self.FunctionStart()
        else:
            mission1 = runs[0]
            mission2 = runs[1]
            mission3 = runs[2]

        #Keep the initial inputs for logging later
        entries_input = [mission1, mission2, mission3]
        attempts = [0, 0, 0]

        #Navigate to Epic Quest
        self.NavToQuest('f4')

        nav = True
        while mission1 > 0:
            if nav:
                self.Click('SHIFTER', 'twisted_world')
                time.sleep(2)
                self.Click('SHIFTER', 'latverian_champion')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission1, nav = self.RegularCheckShifter(
                mission1, "Latverian Champion", "f4", "human_torch")
            attempts[0] += 1
        nav = True
        while mission2 > 0:
            if nav:
                self.Click('SHIFTER', 'twisted_world')
                time.sleep(2)
                self.Click('SHIFTER', 'in_the_shadow_of_doom')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission2, nav = self.RegularCheckShifter(
                mission2, "In the Shadow of Doom", "f4", "victorious")
            attempts[1] += 1
        nav = True
        while mission3 > 0:
            if nav:
                self.Click('SHIFTER', 'dooms_day')
                time.sleep(self.delay_orange_circle)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            mission3, nav = self.DoomCheckShifter(mission3, "Doom's Day", "f4")
            attempts[2] += 1

        #Go back home when loop finished
        time.sleep(0.3)
        self.Click('COORDS', 'home')

        #Logging
        self.Logging('LATVERIAN CHAMPION', 'true', entries_input[0])
        self.Logging('LATVERIAN CHAMPION', 'false',
                     attempts[0] - entries_input[0])
        self.Logging('IN THE SHADOW OF DOOM', 'true', entries_input[1])
        self.Logging('IN THE SHADOW OF DOOM', 'false',
                     attempts[1] - entries_input[1])
        self.Logging("DOOM'S DAY", 'true', entries_input[2])
        self.Logging("DOOM'S DAY", 'false', attempts[2] - entries_input[2])

        if len(runs) == 0:
            self.FunctionEnd()

    def Specials(self, data=[]):
        """Force close specials until shifter found."""

        specials = Specials()

        if len(data) == 0:
            #Find names of special mission groups
            group_names = []
            for group in specials:
                group_names.append(group[0])

            #Format this in an print
            group_text = "In which set of Special Missions is the specific mission you want to run?\n"
            for i, group_name in enumerate(group_names, 1):
                group_name[2] = self.TypeToColour(group_name[2])
                group_text += f"\t{i}: {group_name[0]} ({getattr(Fore, group_name[2])}{group_name[1]}{Fore.YELLOW})\n"
            group_text = group_text.rstrip()
            group_text += '\n'
            group_selection = self.ValidateIntegerInput(
                group_text, 1, len(group_names))

            #Find names of the missions and format in print
            mission_data = specials[group_selection - 1]
            mission_text = f"Which mission in the {mission_data[0][0]} Special Mission set would you like to run?\n"
            for i, mission in enumerate(islice(mission_data, 1, None), 1):
                mission[2] = self.TypeToColour(mission[2])
                mission_text += f"\t{i}: {mission[0]} ({getattr(Fore, mission[2])}{mission[1]}{Fore.YELLOW})\n"
            mission_text = mission_text.rstrip()
            mission_text += "\n"
            mission_selection = self.ValidateIntegerInput(
                mission_text, 1,
                len(mission_data) - 1)
            head = mission_data[0][1].lower()

            #How many entries?
            entries = self.ValidateIntegerInput(
                f'How many "{mission_data[mission_selection][0]}" missions do you want to run? ',
                1,
                20,
                default=20)

            #Use Hidden Tickets?
            use_tickets = self.ValidateBooleanInput(
                'Do you wish to use Hidden Tickets? If you have none, enter either. ',
                default='y')

            #Real shit starting
            self.FunctionStart()
        else:
            group_selection = data[0]
            mission_selection = data[1]
            head = data[2]
            use_tickets = data[3]
            entries = data[4]

            mission_data = specials[group_selection - 1]

        #Saving for logging
        entries_input = entries
        attempts = 0

        #Navigate to Special Missions
        self.NavToQuest("specials")

        #Loop
        nav = True
        while entries > 0:
            if nav:
                gui.click(
                    self.Get("SHIFTER", "special_set_left_x") +
                    (group_selection - 1) * self.Get("SHIFTER",
                                                     "special_set_dist_x"),
                    self.Get("SHIFTER", "special_set_left_y"))
                time.sleep(0.3)
                gui.click(
                    self.Get("SHIFTER", "special_mission_left_x") +
                    (mission_selection - 1) * self.Get(
                        "SHIFTER", "special_mission_dist_x"),
                    self.Get("SHIFTER", "special_mission_left_y"))
                time.sleep(0.3)
                self.Click('SHIFTER', 'special_mission_4')
                time.sleep(self.delay_orange_circle)
                self.Click('SHIFTER', 'special_mission_next')
                time.sleep(0.1)
                self.Click('SHIFTER', 'special_mission_next')
                time.sleep(0.3)
            self.CheckForBoost(4)
            time.sleep(0.2)
            self.Click('COORDS', 'start')
            time.sleep(0.3)
            if use_tickets == 'y' or use_tickets == 'Y':
                self.Click('SHIFTER', 'hidden_ticket_use')
            elif use_tickets == 'n' or use_tickets == 'N':
                self.Click('SHIFTER', 'hidden_ticket_dont_use')
            entries, nav = self.RegularCheckShifter(
                entries, mission_data[mission_selection][0], "specials", head)
            attempts += 1

        #Go back home when loop finished
        time.sleep(0.3)
        self.Click('COORDS', 'home')

        #Logging
        self.Logging('SPECIAL MISSIONS', 'true', entries_input)
        self.Logging('SPECIAL MISSIONS', 'false', attempts - entries_input)

        if len(data) == 0:
            self.FunctionEnd()

    def TypeToColour(self, char_type):
        if char_type == "Combat":
            char_type = "RED"
        elif char_type == "Speed":
            char_type = "GREEN"
        elif char_type == "Blast":
            char_type = "CYAN"
        else:
            char_type = "MAGENTA"
        return char_type

    def RegularCheckShifter(self, entries, mission, quest, head):
        """Takes screenshots and runs image matching to check if a shifter appears"""

        found = False
        while found == False:
            try:
                self.Locate(head, box='head')
            except:
                try:
                    self.Locate('basic_atk', box='basic_atk')
                except:
                    pass
                else:
                    found = True
                    print(
                        Fore.RED +
                        f'Shifter Not Found! Remaining "{mission}" entries: {entries}'
                    )
                    self.ForceClose()
                    self.NavToQuest(quest)
                    return entries, True

            else:
                found = True
                entries -= 1
                print(
                    Fore.GREEN +
                    f'Shifter Found! Remaining "{mission}" entries: {entries}')
                self.CheckForRetry()
                time.sleep(1)
                self.Click('COORDS', 'entries_used')
                time.sleep(0.4)
                self.Click('COORDS', 'retry_right')
                time.sleep(7.5)
                if entries == 0:
                    self.Click('COORDS', 'home')
                    time.sleep(1)
                    self.NavToQuest(quest)
                return entries, None

    def ChaosCheckShifter(self, entries, mission, quest):
        found = False
        while found == False:
            try:
                self.Locate('colossus', box='head')
            except:
                try:
                    self.Locate('domino', box='head')
                except:
                    try:
                        self.Locate('fantomex', box='head')
                    except:
                        pass
                    else:
                        found = True
                        print(
                            f'{Fore.GREEN}Fantomex{Fore.RED} Found! Remaining "{mission}" entries: {entries}'
                        )
                        self.ForceClose()
                        self.NavToQuest(quest)
                        return entries, True
                else:
                    found = True
                    print(
                        f'{Fore.GREEN}Domino{Fore.RED} Found! Remaining "{mission}" entries: {entries}'
                    )
                    self.ForceClose()
                    self.NavToQuest(quest)
                    return entries, True
            else:
                found = True
                entries -= 1
                print(
                    f'{Fore.RED}Colossus{Fore.GREEN} Found! Remaining "{mission}" entries: {entries}'
                )
                self.CheckForRetry()
                time.sleep(1)
                self.Click('COORDS', 'entries_used')
                time.sleep(0.4)
                self.Click('COORDS', 'retry_right')
                time.sleep(7.5)
                if entries == 0:
                    self.Click('COORDS', 'home')
                    time.sleep(1)
                self.NavToQuest(quest)
                return entries, None

    def DoomCheckShifter(self, entries, mission, quest):
        found = False
        while found == False:
            try:
                self.Locate('victorious', box='head')
            except:
                try:
                    self.Locate('victorious', box='head_lower')
                except:
                    try:
                        self.Locate('basic_atk', box='basic_atk')
                    except:
                        pass
                    else:
                        found = True
                        print(
                            f'{Fore.RED}Shifter Not Found! Remaining "{mission}" entries: {entries}'
                        )
                        self.ForceClose()
                        self.NavToQuest(quest)
                        return entries, True
                else:
                    found = True
                    entries -= 1
                    print(
                        f'{Fore.GREEN}DOUBLE SHIFTER Found! Remaining "{mission}" entries: {entries}'
                    )
                    self.CheckForRetry()
                    time.sleep(1)
                    self.Click('COORDS', 'entries_used')
                    time.sleep(0.4)
                    self.Click('COORDS', 'retry_right')
                    time.sleep(7.5)
                    if entries == 0:
                        self.Click('COORDS', 'home')
                        time.sleep(1)
                    self.NavToQuest(quest)
                    return entries, None
            else:
                found = True
                entries -= 1
                print(
                    f'{Fore.GREEN}Shifter Found! Remaining "{mission}" entries: {entries}'
                )
                self.CheckForRetry()
                time.sleep(1)
                self.Click('COORDS', 'entries_used')
                time.sleep(0.4)
                self.Click('COORDS', 'retry_right')
                time.sleep(7.5)
                if entries == 0:
                    self.Click('COORDS', 'home')
                    time.sleep(1)
                self.NavToQuest(quest)
                return entries, None

    def ForceClose(self):
        #Open all apps view
        self.Click('SHIFTER', 'emu_apps')
        time.sleep(2)
        #Close MFF
        gui.moveTo(
            int(self.conf.get('SHIFTER', 'force_close_drag_from_x')),
            int(self.conf.get('SHIFTER', 'force_close_drag_from_y')))
        time.sleep(1)
        gui.dragTo(
            int(self.conf.get('SHIFTER', 'force_close_drag_to_x')),
            int(self.conf.get('SHIFTER', "force_close_drag_to_y")),
            0.25,
            button='left')
        time.sleep(2)
        #Re-open MFF
        self.Click('SHIFTER', 'app_icon')
        #Wait until game starts
        #time.sleep(self.delay_game_startup)
        found = False
        while found == False:
            try:
                self.Locate('x_button', box='x_button')
            except:
                try:
                    self.Locate('shop_button', box='shop_button')
                except:
                    pass
                else:
                    found = True
            else:
                found = True
        time.sleep(2)
        #Close ad - back button and cancel if no ad, twice just in case
        self.Click('SHIFTER', 'back_button')
        if self.conf.get(
                'SHIFTER', 'backbutton_lower'
        ) == "True":  #if the back button is lower than the config we click again slightly lower
            time.sleep(0.5)
            gui.click(
                self.Get('SHIFTER', 'back_button_x'),
                self.Get('SHIFTER', 'back_button_y') + 20)
        time.sleep(0.5)
        self.Click('SHIFTER', 'deadzone')
        time.sleep(0.5)
        self.Click('SHIFTER', 'back_button')
        if self.conf.get(
                'SHIFTER', 'backbutton_lower'
        ) == "True":  #if the back button is lower than the config we click again slightly lower
            time.sleep(0.5)
            gui.click(
                self.Get('SHIFTER', 'back_button_x'),
                self.Get('SHIFTER', 'back_button_y') + 20)
        time.sleep(0.5)
        self.Click('SHIFTER', 'deadzone')
        time.sleep(1)

    def NavToQuest(self, quest):
        #Navigate to Epic Quest
        self.Click('COORDS', 'enter')
        time.sleep(1)
        if quest == "xforce" or quest == "f4":
            self.Click('SHIFTER', 'epicquest')
            time.sleep(1)
            if quest == "xforce":
                self.Click('SHIFTER', 'xforce')
            elif quest == "f4":
                self.Click('SHIFTER', 'first_family')
        elif quest == "specials":
            gui.moveTo(
                int(self.conf.get('SHIFTER', 'epicquest_x')),
                int(self.conf.get('SHIFTER', 'epicquest_y')))
            time.sleep(1)
            gui.dragTo(
                int(self.conf.get('SHIFTER', 'special_mission_drag_to_x')),
                int(self.conf.get('SHIFTER', 'special_mission_drag_to_y')),
                1,
                button='left')
            time.sleep(0.3)
            self.Click('SHIFTER', 'epicquest')
        time.sleep(1)

###
### Potential
###

    def Po10tialVerification(self):
        """Takes the conditions of the potential enhancement"""

        value_list = Enhancement()
        gold_cost = GoldCost()

        #Mutant or not mutant?
        char_type = self.ValidateIntegerInput(
            "Is this character a regular character (input '0') or a mutant (input '1')? ",
            0,
            1,
            default=0)

        #Extra cost?
        cost = self.ValidateBooleanInput(
            "Does this character take bonus material to enhance Potential? ",
            default='n')
        if cost == 'y' or cost == "Y":
            value_list = value_list[1]
            cost = "Extra Cost"
        elif cost == 'n' or cost == "N":
            value_list = value_list[0]
            cost = "Regular Cost"

        #What level?
        level = self.ValidateIntegerInput(
            "What level of Potential is your character currently at? ", 1, 5)
        value_list = value_list[int(level) - 1]

        #What materials?
        if char_type == 0:
            char_type = 'Regular'
            mat1 = "Rank 1 Black Anti-Matter"
            mat2 = "Norn Stones of Chaos"
        else:
            char_type = 'Mutant'
            mat1 = "Phoenix Feathers"
            mat2 = "M'Kraan Crystals"
        material = self.ValidateIntegerInput(
            f"Do you want to enhance with {mat1} (input '0') or {mat2} (input '1')? ",
            0,
            1,
            default=0)
        if material == 0:
            value = value_list[0]
            material_name = mat1
        elif material == 1:
            value = value_list[1]
            material_name = mat2

        #What success rate?
        percent = self.ValidateFloatInput(
            "What percentage success rate do you want to enhance to, each try? ",
            10,
            100,
            2,
            default=self.conf.get('POTENTIAL', 'default_percent'))

        #Current success rate?
        current_rate = self.ValidateFloatInput(
            "What is the current percentage success rate displayed? ",
            0,
            50,
            2,
            default=0)

        #Max number of rolls?
        max_rolls = self.ValidateIntegerInput(
            "What is the maximum number of enhancements you wish to try before the script stops? ",
            1,
            100,
            default=100)

        #Verification
        print(Fore.YELLOW + f"""Is this all correct? (y/n)
        Character Type: {char_type}
        Material Cost: {cost}
        Potential Level: {level} -> {str(int(level)+1)}
        Material To Use: {material_name}
        % Added Each Material: +{value}%
        Success Rate to Try: {percent}%
        Current Success Rate: {current_rate}%
        Maximum Rolls to Try: {max_rolls}
        """ + Style.RESET_ALL)
        verified = input()
        if verified == 'y' or verified == "Y":
            #Run the enhancement routine and return some results[0] attempts and results[1] material used
            print(Fore.CYAN + 'You now have ' + str(self.delay_loading_screen)
                  + ' seconds to tab into the game. CTRL+C to cancel.')
            time.sleep(self.delay_loading_screen)
            results = self.Po10tialEnhancement(value, percent, current_rate,
                                               material, max_rolls)
            #Calculating Gold Cost
            gold_per_enhance = gold_cost[int(level) - 1] * (
                math.floor(percent) + 1)
            gold = gold_per_enhance * results[0]
            gold = "{:,}".format(gold)
            #Results printed and logged
            if results[2] == True:
                print(
                    Fore.GREEN +
                    f"Enhancement Success in {results[0]} attempt(s). ({results[1]} {material_name}, {gold} Gold)"
                )
                self.Logging('POTENTIAL', 'success', 1)
                self.Logging('POTENTIAL', 'failure', results[0] - 1)
            else:
                print(
                    Fore.RED +
                    f"Enhancement stopped after {results[0]} attempt(s). ({results[1]} {material_name}, {gold} Gold)"
                )
                self.Logging('POTENTIAL', 'failure', results[0])
            self.FunctionEnd()
        else:
            print(Fore.MAGENTA + "Verification rejected, exiting")
            return

    def Po10tialEnhancement(self, mat_value, goal_value, current_value,
                            material_pos, max_rolls):
        """Handles the actual enhancement of the potential"""

        #Grab coordinates
        if material_pos == 0:
            mat_x = int(self.conf.get('POTENTIAL', 'middle_mat_x'))
            mat_y = int(self.conf.get('POTENTIAL', 'middle_mat_y'))
        else:
            mat_x = int(self.conf.get('POTENTIAL', 'right_mat_x'))
            mat_y = int(self.conf.get('POTENTIAL', 'right_mat_y'))

        #Set minimum goal value to slightly above 10% to avoid decimal inaccuracies
        if goal_value < 10.05:
            goal_value = 10.05

        #Loop declarations
        success = False  #If enhancement succeeded
        loop = False  #If loop to be broken
        attempts = 0  #Attempt counter
        running_value = current_value
        mat_used = 0
        while loop == False:
            #Loop until enough material selected
            while goal_value > running_value:
                gui.click(mat_x, mat_y)
                running_value += mat_value
                mat_used += 1
            attempts += 1
            #Once attempts matches max rolls, exit loop
            if attempts == max_rolls:
                loop = True
            #Once enough material, click Upgrade
            self.Click('POTENTIAL', 'upgrade')
            time.sleep(0.5)
            self.Click('COORDS', 'ok')
            #OCR to check for success
            time.sleep(1.5)
            image = gui.screenshot(
                'ocr/potential.png',
                region=(int(self.conf.get("POTENTIAL", "result_x")),
                        int(self.conf.get("POTENTIAL", "result_y")),
                        int(self.conf.get("POTENTIAL", "result_length")),
                        int(self.conf.get("POTENTIAL", "result_height"))))
            result = ocr.image_to_string(image, lang="mff")
            #Check success (we test "not failure" because sparkle effects fuck up OCR on success msg)
            if not self.conf.get("POTENTIAL", "failure_text") in result:
                success = True
                loop = True
            else:
                time.sleep(2)
                self.Click('POTENTIAL', 'upgrade')  #Click anywhere to cancel
                running_value = running_value / 2
                time.sleep(1)

        results = [attempts, mat_used, success]
        return results

###
###
###

    def DoMyDailies(self):
        """Runs all your dailies, ensuring Boost Points are active"""

        missions = Missions()
        missions_to_run = []

        #Inputs
        for mission in missions:
            user_input = self.ValidateIntegerInput(
                f'How many "{mission[0]}" missions do you want to run? ',
                0,
                mission[1],
                default=mission[1])  #temp 0, mission[1] usual
            missions_to_run.append(user_input)

        #Energy + BP Calculations
        energy = boost = 0
        for i, mission in enumerate(missions_to_run, 0):
            energy += mission * missions[i][2]
            boost += mission * missions[i][3]

        self.ValidateVerificationInput(
            f"""This will take {energy} Energy and {boost} Boost Points. \nMake sure you have sufficient resources and inventory space. \n"""
        )
        self.FunctionStart()

        #Do shifters first
        if self.conf.get('DAILIES_PREFS', 'colossus') == "1":
            if missions_to_run[5] + missions_to_run[6] + missions_to_run[9] > 0:
                self.Colossus(runs=[
                    missions_to_run[5], missions_to_run[6], missions_to_run[9]
                ])
                for i in [5, 6, 9]:
                    missions_to_run[i] = 0
        if self.conf.get('DAILIES_PREFS', 'victorious') == '1':
            if missions_to_run[12] + missions_to_run[13] + missions_to_run[14] > 0:
                self.Victorious(runs=[
                    missions_to_run[12], missions_to_run[13], missions_to_run[
                        14]
                ])
                for i in [12, 13, 14]:
                    missions_to_run[i] = 0
        if self.conf.get('DAILIES_PREFS', 'special_shifters') == '1':
            if missions_to_run[16] > 0:
                #Set/group
                group = self.Get('DAILIES_PREFS', 'special_mission_set')
                #Shifter name
                if group == 1:
                    head = 'vulture'
                elif group == 2:
                    head = 'inferno'
                else:
                    head = 'gwenpool'
                #Mission in set
                mission = self.Get('DAILIES_PREFS', 'special_mission_mission')
                #Use tickets or not
                if self.Get('DAILIES_PREFS',
                            'special_mission_use_tickets') == 1:
                    tickets = 'y'
                else:
                    tickets = 'n'
                self.Specials(
                    data=[group, mission, head, tickets, missions_to_run[16]])
                missions_to_run[16] = 0

        for i, mission in enumerate(missions_to_run, 0):
            if mission > 0:
                #Locate via status board
                time.sleep(1)
                self.Click('COORDS', 'board')
                time.sleep(1)
                try:
                    left, top = self.Locate(missions[i][4], confidence=0.8)
                except:
                    print(
                        Fore.RED +
                        f"Could not find {missions[i][0]} on Status Board. Ignoring."
                    )
                    mission = 0
                else:
                    gui.click(
                        left + self.Get('DAILIES_COORDS', 'board_x_shift'),
                        top + self.Get('DAILIES_COORDS', 'board_y_shift'))
                    #Navigate to mission
                    self.NavigateToMission(missions[i][0])
                    while mission > 0:
                        if missions[i][0] != 'Co-Op Play':
                            time.sleep(0.2)
                            self.CheckForBoost(4)
                            time.sleep(0.2)
                            self.Click('COORDS', 'start')
                            if missions[i][0] == 'Special Mission':
                                time.sleep(0.3)
                                if self.Get(
                                        'DAILIES_PREFS',
                                        'special_mission_use_tickets') == 1:
                                    self.Click('SHIFTER', 'hidden_ticket_use')
                                else:
                                    self.Click('SHIFTER',
                                               'hidden_ticket_dont_use')
                            time.sleep(0.2)
                            self.CheckForRetry()
                            time.sleep(1)
                            self.Click('COORDS', 'entries_used')
                            time.sleep(0.4)
                            self.Click('COORDS', 'retry_right')
                            mission -= 1
                            print(
                                Fore.GREEN +
                                f"Mission Complete! Remaining {missions[i][0]} entries: {mission}"
                            )
                            time.sleep(7.5)
                        else:
                            time.sleep(1)
                            try:
                                self.Locate('coop_reward', box='coop_button')
                            except:
                                self.Click('DAILIES_COORDS', 'coop_char')
                                time.sleep(0.5)
                                self.Click('COORDS', 'enter')
                                a, b = self.CheckForNext()
                                time.sleep(2)
                                gui.click(a, b)
                                time.sleep(7.5)
                            else:
                                self.Click('COORDS', 'enter')
                                time.sleep(0.2)
                                self.Click('DAILIES_COORDS', 'coop_acquire')
                                time.sleep(1)
                                self.Click('COORDS', 'centre')
                                time.sleep(0.5)
                                self.Click('DAILIES_COORDS', 'coop_ok')
                                mission -= 1
                                print(
                                    Fore.GREEN +
                                    f"Reward Acquired! Remaining {missions[i][0]} rewards: {mission}"
                                )
                                time.sleep(7.5)

                    self.Click('COORDS', 'home')
                    time.sleep(1)
        self.FunctionEnd()

    def NavigateToMission(self, mission):
        if mission == "Memory Mission":
            time.sleep(0.5)
            mission_value = self.Get('DAILIES_PREFS', "memory_mission")
            gui.click(
                self.Get("DAILIES_COORDS", "memory_mission_left_x") +
                (mission_value - 1) * self.Get("DAILIES_COORDS",
                                               "memory_mission_dist_x"),
                self.Get("DAILIES_COORDS", "memory_mission_left_y"))
            time.sleep(0.3)
            self.Click('DAILIES_COORDS', 'memory_mission_4')
            time.sleep(self.delay_orange_circle)
            self.Click('DAILIES_COORDS', 'memory_mission_next')
            time.sleep(0.1)
            self.Click('DAILIES_COORDS', 'memory_mission_next')
            time.sleep(0.1)
        elif mission == "Dark Dimension":
            time.sleep(0.5)
            mission_value = self.Get('DAILIES_PREFS', "dark_dimension")
            if mission_value == 1:
                self.Click('DAILIES_COORDS', 'left')
            else:
                self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "Veiled Secret: Magneto's Might":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'left')
            time.sleep(self.delay_orange_circle)
        elif mission == "Veiled Secret: Rise Of The Phoenix":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "Mutual Enemy":
            time.sleep(self.delay_orange_circle)
        elif mission == "Stupid X-Men: Chrome-Plated Comrade":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'left')
            time.sleep(self.delay_orange_circle)
        elif mission == "Stupid X-Men: Psy-Locked Out":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "The Big Twin: Cutting Cable":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'left')
            time.sleep(self.delay_orange_circle)
        elif mission == "The Big Twin: Ending the Stryfe":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "Beginning of the Chaos":
            time.sleep(self.delay_orange_circle)
        elif mission == "New Faces: Inhuman Princess":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'left')
            time.sleep(self.delay_orange_circle)
        elif mission == "New Faces: Mean & Green":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "Twisted World: Latverian Champion":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'left')
            time.sleep(self.delay_orange_circle)
        elif mission == "Twisted World: In the Shadow of Doom":
            time.sleep(0.5)
            self.Click('DAILIES_COORDS', 'right')
            time.sleep(self.delay_orange_circle)
        elif mission == "Doom's Day":
            time.sleep(self.delay_orange_circle)
        elif mission == "Daily Mission":
            time.sleep(0.5)
            group_selection = self.Get('DAILIES_PREFS', 'daily_mission_set')
            mission_selection = self.Get('DAILIES_PREFS',
                                         'daily_mission_mission')
            gui.click(
                self.Get("SHIFTER", "special_set_left_x") +
                (group_selection - 1) * self.Get("SHIFTER",
                                                 "special_set_dist_x"),
                self.Get("SHIFTER", "special_set_left_y"))
            time.sleep(0.3)
            gui.click(
                self.Get("DAILIES_COORDS", "memory_mission_left_x") +
                (mission_selection - 1) * self.Get("DAILIES_COORDS",
                                                   "memory_mission_dist_x"),
                self.Get("DAILIES_COORDS", "memory_mission_left_y"))
            time.sleep(self.delay_orange_circle)
        elif mission == "Special Mission":
            time.sleep(0.5)
            group_selection = self.Get('DAILIES_PREFS', 'special_mission_set')
            mission_selection = self.Get('DAILIES_PREFS',
                                         'special_mission_mission')
            gui.click(
                self.Get("SHIFTER", "special_set_left_x") +
                (group_selection - 1) * self.Get("SHIFTER",
                                                 "special_set_dist_x"),
                self.Get("SHIFTER", "special_set_left_y"))
            time.sleep(0.3)
            gui.click(
                self.Get("SHIFTER", "special_mission_left_x") +
                (mission_selection - 1) * self.Get("SHIFTER",
                                                   "special_mission_dist_x"),
                self.Get("SHIFTER", "special_mission_left_y"))
            time.sleep(0.3)
            self.Click('SHIFTER', 'special_mission_4')
            time.sleep(self.delay_orange_circle)
            self.Click('SHIFTER', 'special_mission_next')
            time.sleep(0.1)
            self.Click('SHIFTER', 'special_mission_next')
            time.sleep(0.3)
        elif mission == "Co-Op Play":
            time.sleep(self.delay_orange_circle)

    def CheckForNext(self):
        loop = True
        while loop == True:
            try:
                a, b = self.Locate('coop_next', box='coop_next')
            except:
                pass
            else:
                loop = False
                return a, b
            time.sleep(5)

    def CheckForRetry(self):
        loop = True
        while loop == True:
            try:
                self.Locate('retry_button', box='retry_button')
            except:
                try:
                    self.Locate('retry_button_dark', box='retry_button')
                except:
                    pass
                else:
                    loop = False
                    return
            else:
                loop = False
                return
            time.sleep(5)

    def CheckForBoost(self, cost):
        if cost == 4:
            try:
                self.Locate('0_boost', box='boost', confidence=0.99)
            except:
                try:
                    self.Locate('1_boost', box='boost', confidence=0.97)
                except:
                    try:
                        self.Locate('2_boost', box='boost', confidence=0.97)
                    except:
                        try:
                            self.Locate(
                                '3_boost', box='boost', confidence=0.97)
                        except:
                            return
                        else:
                            self.WaitForBoost(90)
                    else:
                        self.WaitForBoost(180)
                else:
                    self.WaitForBoost(270)
            else:
                self.WaitForBoost(360)
        elif cost == 6:
            try:
                self.Locate('0_boost', box='boost', confidence=0.99)
            except:
                try:
                    self.Locate('1_boost', box='boost', confidence=0.97)
                except:
                    try:
                        self.Locate('2_boost', box='boost', confidence=0.97)
                    except:
                        try:
                            self.Locate(
                                '3_boost', box='boost', confidence=0.97)
                        except:
                            try:
                                self.Locate(
                                    '4_boost', box='boost', confidence=0.97)
                            except:
                                try:
                                    self.Locate(
                                        '5_boost',
                                        box='boost',
                                        confidence=0.97)
                                except:
                                    return
                                else:
                                    self.WaitForBoost(90)
                            else:
                                self.WaitForBoost(180)
                        else:
                            self.WaitForBoost(270)
                    else:
                        self.WaitForBoost(360)
                else:
                    self.WaitForBoost(450)
            else:
                self.WaitForBoost(540)

    def WaitForBoost(self, seconds):
        for remaining in range(seconds, 0, -1):
            remaining = str(datetime.timedelta(seconds=remaining))[3:]
            sys.stdout.write("\r")
            sys.stdout.write(
                Fore.RED +
                f"Inadequate Boost Points. {remaining} until next attempt.")
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write(
            "\rInadequate Boost Points. Retrying.                          \n")

###
### RunThisMission
###

    def RunThisMission(self):
        """Run this mission x times"""

        boost_cost = story_mission = None #Define first

        #How many times?
        runs = self.ValidateIntegerInput(
            "How many times do you want to run this mission? ",
            1,
            100,
            default=10)

        #Boost?
        boost = self.ValidateBooleanInput(
            "Do you wish to wait for Boost Points to recharge before running this mission? ",
            default='n')
        if boost == 'y':
            boost_cost = self.ValidateIntegerInput(
                'How many Boost Points does it take to run this mission once? ',
                4,
                6,
                default=6)
            if boost_cost == 5:
                self.Exit(
                    "no mission costs 5 Boost Points, only 4 and 6 are valid inputs"
                )

        #Story? (to determine retry button position)
        if boost == 'n' or boost == 'y' and boost_cost == 6:
            story_mission = self.ValidateBooleanInput(
                "Is this a Story Mission? ", default='n')

        self.FunctionStart()

        while runs > 0:
            if boost == 'y':
                self.CheckForBoost(boost_cost)
            self.Click('COORDS', 'enter')
            self.CheckForRetry()
            runs -= 1
            time.sleep(1)
            self.Click('COORDS', 'entries_used')
            time.sleep(0.4)
            if story_mission == 'y':
                self.Click('COORDS', 'retry_left')
            else:
                self.Click('COORDS', 'retry_right')
            print(Fore.GREEN + f"Mission Success! Remaining runs: {runs}")
            time.sleep(5)
            time.sleep(self.delay_orange_circle)

        self.FunctionEnd()

###
### Misc Commands
###

    def MiscCommands(self):
        """Random collection of commands"""

        #Which command to run
        print(Fore.YELLOW + """Which command would you like to run?
        1: DailyReset()
        2: WeeklyReset()
        3: CTPLookup()
        4: BAMCalculator()
        5: EQCollectionLookup()""" + Style.RESET_ALL)
        command = input()

        if command == "1":
            self.DailyReset()
        elif command == "2":
            self.WeeklyReset()
        elif command == "3":
            self.CTPLookup()
        elif command == "4":
            self.BAMCalculator()
        elif command == "5":
            self.EQCollectionLookup()
        else:
            print(Fore.MAGENTA +
                  "Wrong input, must be one of the numbers listed.")
            return

    def DailyReset(self):
        """Returns how long until daily reset."""
        current_time = datetime.datetime.utcnow()
        reset_hour = 15
        daily_reset = datetime.datetime(
            year=current_time.year,
            month=current_time.month,
            day=current_time.day,
            hour=reset_hour,
            minute=00,
            second=0,
            microsecond=0)

        if current_time.hour > reset_hour:
            daily_reset = daily_reset + datetime.timedelta(days=1)
        time_remaining = daily_reset - current_time

        total_seconds = int(time_remaining.total_seconds())
        hours, remainder = divmod(total_seconds, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        str = Fore.CYAN + 'Time Until Daily Reset: {}{} Hours, {} Minutes, {} Seconds'.format(
            Fore.GREEN, hours, minutes, seconds)
        print(str)

    def WeeklyReset(self):
        """Returns how long until weekly reset."""
        current_time = datetime.datetime.utcnow()
        reset_hour = 1
        day_deficit = 0

        if current_time.weekday() < 4:
            day_deficit = 4 - current_time.weekday()
        elif current_time.weekday() > 3:
            day_deficit = 11 - current_time.weekday()

        weekly_reset = datetime.datetime(
            year=current_time.year,
            month=current_time.month,
            day=current_time.day,
            hour=reset_hour,
            minute=00,
            second=0,
            microsecond=0) + datetime.timedelta(days=day_deficit)
        time_remaining = weekly_reset - current_time

        total_seconds = int(time_remaining.total_seconds())
        days, remainder = divmod(total_seconds, 60 * 60 * 24)
        hours, remainder = divmod(remainder, 60 * 60)
        minutes, seconds = divmod(remainder, 60)

        str = Fore.CYAN + 'Time Until Weekly Reset: {}{} Days, {} Hours, {} Minutes, {} Seconds'.format(
            Fore.GREEN, days, hours, minutes, seconds)
        print(str)

    def CTPLookup(self):
        """Lookup the max stats of a chosen CTP"""

        ctps = CTPs()

        #Which CTP?
        ctp = self.ValidateIntegerInput(
            """Which CTP would you like to look up the max stats for?
        1: Authority
        2: Energy
        3: Destruction
        4: Refinement
        5: Transcendence
        6: Patience
        7: Regeneration
        8: Rage\n""", 1, 8)

        #Output
        ctps = ctps[ctp - 1]
        output = Fore.CYAN + f"C.T.P. of {Fore.GREEN}{ctps[0]}\n"
        output += Fore.CYAN + f"Acquired From: {Fore.GREEN}{ctps[1]}\n"
        output += Fore.CYAN + "Stats at Maximum Rolls:\n"
        output += Fore.GREEN + ctps[2]
        print(output)

    def BAMCalculator(self):
        """Get amount of R1BAM and Gold needed for specified amounts of higher rank"""

        #Get input
        print(
            Fore.YELLOW +
            "Enter the number to calculate, of each higher rank BAM, in the format <r6> <r5> <r4> <r3> <r2>. Use a 0 if you wish to craft none of that rank."
            + Style.RESET_ALL)
        user_input = input()

        #Format into list then int, bams[0] = r6, bams[1] = r5 ... bams[n] = r{6-n}
        user_input = user_input.split()
        bams = []
        for bam in user_input:
            try:
                bams.append(int(bam))
            except:
                print(Fore.MAGENTA + "Wrong input, only numbers are allowed.")
                return
        if len(bams) != 5:
            print(
                Fore.MAGENTA +
                "Wrong input, there must be 5 numbers with spaces in between.")
            return

        #Calculate
        r1 = (bams[0] * 800) + (bams[1] * 400) + (bams[2] * 200) + (
            bams[3] * 100) + (bams[4] * 50)
        gold = (bams[0] * 5500000) + (bams[1] * 2562500) + (
            bams[2] * 1125000) + (bams[3] * 437500) + (bams[4] * 125000)
        gold = "{:,}".format(gold)

        #Output
        r2t = r3t = r4t = r5t = r6t = ""
        if bams[4] > 0:
            r2t = f"• {Fore.GREEN}{bams[4]}{Fore.CYAN} Rank 2 \n"
        if bams[3] > 0:
            r3t = f"• {Fore.GREEN}{bams[3]}{Fore.CYAN} Rank 3 \n"
        if bams[2] > 0:
            r4t = f"• {Fore.GREEN}{bams[2]}{Fore.CYAN} Rank 4 \n"
        if bams[1] > 0:
            r5t = f"• {Fore.GREEN}{bams[1]}{Fore.CYAN} Rank 5 \n"
        if bams[0] > 0:
            r6t = f"• {Fore.GREEN}{bams[0]}{Fore.CYAN} Rank 6 \n"

        output = Fore.CYAN + "Black Anti-Matter to Craft:\n"
        output += f"{r2t}{r3t}{r4t}{r5t}{r6t}"
        output += Fore.CYAN + "Basic Materials Required:\n"
        output += Fore.GREEN + f"{Fore.CYAN}• {Fore.GREEN}{str(r1)}{Fore.CYAN} Rank 1 Black Anti-Matter \n• {Fore.GREEN}{gold}{Fore.CYAN} Gold"
        print(output)

    def EQCollectionLookup(self):
        """Prints some info about Epic Quest Collections."""

        collections = Collections()

        #Which Epic Quest?
        quest = self.ValidateIntegerInput(
            f"""In which Epic Quest is the collection you wish to look up?
        1: Sorcerer Supreme ({Fore.CYAN}Doctor Strange{Fore.YELLOW})
        2: Rise of the X-Men ({Fore.RED}Wolverine{Fore.YELLOW})
        3: X-Force ({Fore.GREEN}Deadpool{Fore.YELLOW})
        4: First Family ({Fore.RED}Mister Fantastic{Fore.YELLOW})\n""", 1, 4)

        collections = collections[quest - 1]

        #Which collection?
        text = "Which Collection do you wish to look up?\n"
        for i, collection in enumerate(collections, 1):
            text += f"\t{i}: {collection[0][0]}\n"
        collection = self.ValidateIntegerInput(text, 1, i)

        collections = collections[collection - 1]

        #Print info
        name = collections[0][0]
        text = f"{Fore.CYAN}Collection Name: {Fore.GREEN}{name}\n"
        text += f"{Fore.CYAN}Reward: {Fore.GREEN}{collections[0][1]}\n"
        collections[0] = ["Item Name", "Quantity", "Location"]
        table = SingleTable(collections, title=name)
        text += Fore.GREEN + table.table
        print(text)


###
### General Functions
###

    def StringToListValidation(self, string, max):
        """Validates string input and returns as list."""

        #Length check
        if not 1 <= len(string) <= max:
            print(Fore.MAGENTA +
                  'Input not accepted: input must be between 1 and ' +
                  str(max) + ' characters.')
            return

        #Range check
        string_list = list(string)
        for string in string_list:
            if not 1 <= int(string) <= max:
                print(Fore.MAGENTA +
                      'Input not accepted: input must be numbered from 1 to ' +
                      str(max) + '.')
                return

        #Remove duplicate numbers if any
        string_list = set(
            [x for x in string_list if string_list.count(x) >= 1])

        #Sort
        string_list = sorted(string_list)

        return string_list

    def Logging(self, category, data_point, increment):
        """Logs data to data.ini"""

        self.safe_conf = SafeConfigParser()

        #Find config file
        os.chdir(sys.path[0])
        if os.path.exists('data.ini'):
            self.safe_conf.read('data.ini')
        else:
            raise FileNotFoundError('Data file, data.ini, was not found.')

        temp = self.safe_conf.get(category, data_point)
        temp = int(temp)
        temp += increment
        temp = str(temp)
        self.safe_conf.set(category, data_point, temp)
        with open('data.ini', 'w') as configfile:
            self.safe_conf.write(configfile)

        print(
            Fore.CYAN +
            f'Logging +{increment} to "{data_point}" under category "{category}".'
        )

        time.sleep(1)

    def ChangePrefs(self, category, data_point, new_value):
        """Changes data in config.ini"""

        self.conf.set(category, data_point, new_value)
        with open('config.ini', 'w') as configfile:
            self.safe_conf.write(configfile)

    def Get(self, category, data_point):
        """Easy way to get an integer from config"""

        return int(self.conf.get(category, data_point))

    def Click(self, category, value):
        """Clicks in a spot based on ini values"""

        x_value = value + "_x"
        y_value = value + "_y"

        gui.click(
            int(self.conf.get(category, x_value)),
            int(self.conf.get(category, y_value)))

    def Locate(self, image_name, box=None, confidence=0.9):

        #Coords
        if box == None:
            left = 0
            top = 0
            width = 1920
            height = 1080
        else:
            left = self.Get('IMAGE_MATCHING', f'{box}_left')
            top = self.Get('IMAGE_MATCHING', f'{box}_top')
            width = self.Get('IMAGE_MATCHING', f'{box}_width')
            height = self.Get('IMAGE_MATCHING', f'{box}_height')

        a, b, c, d, = gui.locateOnScreen(
            f'images/{image_name}.png',
            region=(left, top, width, height),
            grayscale=True,
            confidence=confidence)
        return a, b

    def ValidateIntegerInput(self, prompt, min, max, default=None):
        """Basic validation for a number input"""

        #Print prompt and get input
        if default != None:
            print(Fore.YELLOW + prompt + f"({min}-{max})" +
                  f" [Default = {default}]" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + prompt + f"({min}-{max})" + Style.RESET_ALL)
        user_input = input()

        if user_input == "" and default != None:
            user_input = default
        elif user_input == "" and not default != None:
            self.Exit("no default value exists for this prompt")
        else:
            #Try to convert to integer
            try:
                user_input = int(user_input)
            except ValueError:
                self.Exit("must be an integer.")

            if not max >= user_input >= min:
                self.Exit(f"must be between {min} and {max}")

        return user_input

    def ValidateFloatInput(self, prompt, min, max, decimals, default=None):
        """Basic validation of a float input. Default as string for now"""

        #Print prompt and get input
        if default != None:
            print(Fore.YELLOW + prompt +
                  f"({min}-{max}, no % sign, max {decimals} decimals)" +
                  f" [Default = {default}]" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + prompt +
                  f"({min}-{max}, no % sign, max {decimals} decimals)" +
                  Style.RESET_ALL)
        user_input = input()

        if user_input == "" and default != None:
            user_input = default
        elif user_input == "" and not default != None:
            self.Exit("no default value exists for this prompt")

        #Type check
        try:
            user_input = float(user_input)
        except ValueError:
            self.Exit(
                "enter no characters except numbers and optionally a decimal point"
            )

        #Range/decimal check
        if not min <= user_input <= max and round(user_input,
                                                  decimals) == user_input:
            self.Exit(
                "must be to 2 decimal places at most and between 10 and 100")
        user_input = round(user_input, decimals)

        return user_input

    def ValidateBooleanInput(self, prompt, default=None):
        """Basic validation for a y/n input"""

        #Print prompt and get input
        if default != None:
            print(Fore.YELLOW + prompt + "(y/n)" + f" [Default = {default}]" +
                  Style.RESET_ALL)
        else:
            print(Fore.YELLOW + prompt + "(y/n)" + Style.RESET_ALL)
        user_input = input()

        if user_input == "" and default != None:
            user_input = default
        elif user_input == "" and not default != None:
            self.Exit("no default value exists for this prompt")
        else:
            if user_input not in ['y', 'Y', 'n', 'N']:
                self.Exit("must be y or n")

        return user_input

    def ValidateVerificationInput(self, prompt):

        #Print prompt and get input
        print(Fore.YELLOW + prompt + "(y to proceed)" + Style.RESET_ALL)
        user_input = input()

        if user_input == "y" or user_input == "Y":
            return
        else:
            self.Exit('verification rejected')

    def FunctionStart(self):
        print(Fore.CYAN + 'You now have ' + str(self.delay_loading_screen) +
              ' seconds to tab into the game. CTRL+C to cancel.')
        time.sleep(self.delay_loading_screen)

    def FunctionEnd(self):
        gui.hotkey('alt', 'tab', interval=0.1)
        print(Fore.CYAN + "Function ended. Press ENTER to exit.")
        input()

    def Exit(self, exit_msg):
        print(
            Fore.MAGENTA + "Bad input: " + exit_msg + ". Press ENTER to exit.")
        input()
        raise SystemExit

init()
MFF_Automate()