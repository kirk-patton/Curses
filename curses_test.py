#!/usr/bin/env python2.7
import curses
import math
import time


def top_win(stdscr):
    (max_y, max_x) = stdscr.getmaxyx()
    begin_y = 0
    begin_x = 0
    height = int(math.ceil(max_y * .1))
    width = max_x
    top = curses.newwin(height, width, begin_y, begin_x)
    top.box()
    top.refresh()
    return top


def bottom_win(stdscr, top):
    (top_max_y, top_max_x) = top.getmaxyx()
    begin_y = top_max_y
    begin_x = 0
    height = (stdscr.getmaxyx())[0]
    width = top_max_x
    bottom = curses.newwin(height, width, begin_y, begin_x)
    bottom.box()
    bottom.refresh()
    return bottom


def top_stats(top):
    # write the stats to the top window
    (max_y, max_x) = top.getmaxyx()
    top.addstr(int(math.ceil(max_y / 2)),
               int(math.ceil(max_x / 2)), 'Hello Top')
    top.refresh()


def bottom_stats(bottom):
    pass


def main(stdscr):
    # The start of the program
    top = top_win(stdscr)
    bottom = bottom_win(stdscr, top)
    top_stats(top)
    bottom_stats(bottom)
    time.sleep(5)


if __name__ == '__main__':
    curses.wrapper(main)
