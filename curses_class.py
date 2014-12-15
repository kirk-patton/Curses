#!/usr/bin/env python2.7
import curses
import math
import time


class Window():
    '''
        Define a windows common methods
    '''
    def __init__(self, stdscr, y=0, x=0, height=0, width=0):
        self.stdscr = stdscr
        (self.max_y, self.max_x) = self.stdscr.getmaxyx()
        self.begin_x = x
        self.begin_y = y
        self.height = height
        self.width = width
        self.border = 1

        self.win = curses.newwin(self.height,
                                 self.width,
                                 self.begin_y,
                                 self.begin_x)

    def resize(self, y, x):
        # Resize the window
        self.height = y
        self.width = x

        # Remove the contents of the old window
        self.win.clear()
        self.win.border(0)
        self.win.refresh()

        self.win.resize(y, x)
        if self.border:
            self.win.border()
            self.win.refresh()


    def header(self, text='Enter Some Text'):
        # top.addstr(int(math.ceil(max_y / 2)),
        #                       int(math.ceil(max_x / 2)), 'Hello Top')
        self.win.addstr(3, 10, text)


def main(stdscr):
    wait = 1
    top = Window(stdscr, 0, 0, 10, 40)
    top.header('Foo')
    top.win.border()
    top.win.refresh()
    time.sleep(wait)
    top.resize(50,30)
    time.sleep(wait)

if __name__ == '__main__':
    curses.wrapper(main)
