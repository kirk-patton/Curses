import curses
import time
import math


def main(stdscr, x, y, height=2, width=10):
    (max_y, max_x) = stdscr.getmaxyx()
    begin_x = x
    begin_y = y

    win = curses.newwin(height,
                        width,
                        begin_y,
                        begin_x)
    # Box it
    win.box()

    # Put some text
    string = 'Hello'
    (max_y, max_x) = win.getmaxyx()
    str_y = int(math.ceil(max_y / 2))
    str_x = int(math.ceil(max_x / 2 - int(len(string) / 2)))
    win.addstr(str_y, str_x, string)
    win.refresh()
    time.sleep(.5)

    # Clear the old window
    win.clear()
    win.refresh()

    # Grow
    win.resize(max_y + 2, max_x + 2)
    string = 'Resize'
    (max_y, max_x) = win.getmaxyx()
    str_y = int(math.ceil(max_y / 2))
    str_x = int(math.ceil(max_x / 2 - int(len(string) / 2)))
    win.addstr(str_y, str_x, string)

    # Box it
    win.box()
    win.refresh()
    time.sleep(.5)

    string = 'Move   '
    win.addstr(str_y, str_x, string)
    win.refresh()
    move_it(stdscr,win)


def move_it(stdscr,win):
    (max_y, max_x) = stdscr.getmaxyx()
    (win_y, win_x) = win.getmaxyx()
    y_list = range(0, max_y - win_y, 2)
    x_list = range(0, max_x - win_x, 2)

    while True:
        for y in y_list:
            y_list.reverse()
            for x in x_list:
                x_list.reverse()
                win.mvwin(y,x)
                stdscr.clear()
                stdscr.refresh()
                win.refresh()
                time.sleep(.025)
      



if __name__ == '__main__':
    win = curses.wrapper(main, x=0, y=0, height=3, width=10)
