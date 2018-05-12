import curses
import curses.ascii

def main(stdscr):
    stdscr.clear()
    while(True):
        key = stdscr.getch()
        if(key == curses.ascii.CAN):
            break;
        else:
            stdscr.addch(key)
        stdscr.refresh()

if __name__ == '__main__':
    curses.wrapper(main)
