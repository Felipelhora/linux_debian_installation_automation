from src.config import config
import os
import curses
import getpass
import time




class Menu():
    def __init__(self):
        self.options_to_run = {}
    
    def clear_terminal(self):
        
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


    # def print_menu(self, stdscr, selected_row_idx, selected_options, menu_options):
    #     stdscr.clear()
    #     h, w = stdscr.getmaxyx()
    #     for idx, row in enumerate(menu_options):
    #         x = w//2 - len(row)//2
    #         y = h//2 - len(menu_options)//2 + idx

    #         if idx == selected_row_idx:
    #             stdscr.attron(curses.color_pair(1))
    #             stdscr.addstr(y, x, row)
    #             stdscr.attroff(curses.color_pair(1))
    #         else:
    #             stdscr.addstr(y, x, row)

    #         if selected_options[idx]:
    #             stdscr.addstr(y, x - 2, "[X]")
    #         else:
    #             stdscr.addstr(y, x - 2, "[ ]")
    #     stdscr.refresh()

    # def main(self, stdscr):
    #     curses.curs_set(0)
    #     curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #     current_row = 0
    #     selected_options = [False] * len(self.options["menu_options"])
    #     while True:
    #         self.print_menu(stdscr, current_row, selected_options, self.options["menu_options"])
    #         key = stdscr.getch()
    
    #         if key == curses.KEY_UP and current_row > 0:
    #             current_row -= 1
    #         elif key == curses.KEY_DOWN and current_row < len(self.options["menu_options"]) - 1:
    #             current_row += 1
    #         elif key == curses.KEY_ENTER or key in [10, 13]:
    #             if current_row == len(self.options["menu_options"]) - 1:
    #                 break
    #             selected_options[current_row] = not selected_options[current_row]

    #     stdscr.clear()
    #     selected_items = [self.options["menu_options"][i] for i, selected in enumerate(selected_options) if selected]
    #     stdscr.addstr(0, 0, f"Selected items: {', '.join(selected_items)}")
    #     stdscr.refresh()
    #     stdscr.getch()
    #     os.system("clear")

    def print_menu(self, stdscr, selected_row_idx, selected_options, menu_options):
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        for idx, row in enumerate(menu_options):
            x = w // 2 - len(row) // 2
            y = h // 2 - len(menu_options) // 2 + idx

            if idx == selected_row_idx:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row)

            # Exibe o status de seleção
            if selected_options[idx]:
                stdscr.addstr(y, x - 2, "[X]")
            else:
                stdscr.addstr(y, x - 2, "[ ]")
        stdscr.refresh()

    def main(self, menu_items):
        stdscr = curses.initscr()
        curses.curs_set(0)

        # Verifica se o terminal suporta cores
        if curses.has_colors():
            curses.start_color()
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

        current_row = 0
        selected_options = [False] * len(menu_items)

        while True:
            self.print_menu(stdscr, current_row, selected_options, menu_items)
            key = stdscr.getch()

            # Navegação no menu
            if key == curses.KEY_UP:
                current_row = (current_row - 1) % len(menu_items)  # Círculo para cima
            elif key == curses.KEY_DOWN:
                current_row = (current_row + 1) % len(menu_items)  # Círculo para baixo
            elif key == curses.KEY_ENTER or key in [10, 13]:
                # Alterna a seleção do item atual
                selected_options[current_row] = not selected_options[current_row]
            elif key == 27:  # ESC para sair
                break

        stdscr.clear()
        selected_items = [menu_items[i] for i, selected in enumerate(selected_options) if selected]
        stdscr.addstr(0, 0, f"Selected items: {', '.join(selected_items)}")
        stdscr.refresh()
        stdscr.getch()
        curses.endwin()












   

    def __choise_options(self, options:list) -> str:
        text_options = ""
        number_options = len(options)
        for option in options:
            text_options = f"{text_options}\n{option}"
        return [f"{text_options}\n", number_options]
    

    def menu_maker(self, list_menu:list):
        while True:
            menu_options = self.__choise_options(list_menu)
            print (menu_options[0])
            choice = input(config["text_language"]["menu"]["choice_option"])
            self.clear_terminal()
            try:
                if int(choice) > 0 and int(choice) <= menu_options[1]:
                   return int(choice)
                else:
                    self.clear_terminal()
                    print ('\n\n####################################\n')
                    print ('----> ',config["text_language"]["menu"]['error_menu'], f' ** {choice} **' ,' <----')
                    print ('\n####################################\n')
                    time.sleep(1)
                    continue    
            except:
                self.clear_terminal()
                print ('\n\n####################################\n')
                print ('----> ',config["text_language"]["menu"]['error_menu'], f' ** {choice} **' ,' <----')
                print ('\n####################################\n')
                time.sleep(1)
                continue


    def menu_main(self):
        return self.menu_maker(config["text_language"]["menu"]["options"]['first_menu_options'])
       

    def menu_create_commands(self, options_list:list) -> int:
        return self.menu_maker(options_list)
        


    def get_password(self):
        return getpass.getpass(prompt=config["text_language"]["menu"]["enter_pass"])
    

    