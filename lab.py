# import curses
# import os

# def print_menu(stdscr, selected_row_idx, selected_options, menu_options):
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

# def main(stdscr):
#     curses.curs_set(0)
#     curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

#     config = {
#         "menu_options": [
#             "Option 1",
#             "Option 2",
#             "Option 3",
#             "Option 4",
#             "Exit"
#         ]
#     }

#     current_row = 0
#     selected_options = [False] * len(config["menu_options"])

#     while True:
#         print_menu(stdscr, current_row, selected_options, config["menu_options"])
#         key = stdscr.getch()
 
#         if key == curses.KEY_UP and current_row > 0:
#             current_row -= 1
#         elif key == curses.KEY_DOWN and current_row < len(config["menu_options"]) - 1:
#             current_row += 1
#         elif key == curses.KEY_ENTER or key in [10, 13]:
#             if current_row == len(config["menu_options"]) - 1:
#                 break
#             selected_options[current_row] = not selected_options[current_row]

#     stdscr.clear()
#     selected_items = [config["menu_options"][i] for i, selected in enumerate(selected_options) if selected]
#     stdscr.addstr(0, 0, f"Selected items: {', '.join(selected_items)}")
#     stdscr.refresh()
#     stdscr.getch()
#     os.system("clear")

# if __name__ == "__main__":
#     curses.wrapper(main)



options = {"menu_options" : 
                                                    [
                                                            "PYTHON", "TERMINAL"
                                                    ]}

print (len(options["menu_options"]))