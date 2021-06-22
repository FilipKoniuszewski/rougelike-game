import sys
import os
import random
import ui


def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def Attack_chances(attacker,defender):
    tab_poss = []
    for x in range(2):
        random_value = random.randrange(1,101)
        tab_poss.append(random_value)
    if  tab_poss[0] <= defender["DodgeChance"]:
        ui.information_board(f"{attacker} attacked but {defender} managed to dodge")        
    else :
        if tab_poss[1] <= attacker["CriticalChance"]:
           ui.Information_board(f"{attacker} managed to do Critical attack and dealed 50 damage to {defender}")
           defender["HP"] -= (attacker["BaseDamage"]*2)  
        else:
            defender["HP"] -= attacker["BaseDamage"]
            ui.information_board(f"{attacker} managed to attack and dealed 20 damage to defender")

