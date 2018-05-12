import sys
import tty
import termios
import argparse
import os

CTRL_C = 3
CTRL_H = 8
DELETE = 127
RETURN = 13

def getch():
    fd = sys.stdin.fileno() # 標準入力のファイルディスクリプタを取得
    old = termios.tcgetattr(fd) # fdの端末属性(?)を取得
    """
    #include <termios.h>
    struct termios {
        tcflag_t c_iflag;
        tcflag_t c_oflag;
        tcflag_t c_cflag;
        tcflag_t c_lflag;
        cc_t     c_cc[NCCS];
    };
    """

    try:
        # 標準入力のモード切り替え
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        # fdの属性を元に戻す
        termios.tcsetattr(fd, termios.TCSANOW, old)

    return ch


def addch(buff, ch):
    buff.append(ch)

def delch(buff):
    buff.pop()

def newline(buff):
    buff.clear()
    
def main():
    while(True):
        ch = ord(getch())
        if(ch == CTRL_C):
            break
        elif(ch == RETURN):
            print()          
        else:
            sys.stdout.write(chr(ch))
            sys.stdout.flush()
        if(args.code):
            print(ch)

def main2():
    buff = list()
    while(True):
        ch = ord(getch())
        if(ch == CTRL_C):
            break
        elif(ch == DELETE or ch == CTRL_H):
            delch(buff)
        elif(ch == RETURN):
            newline(buff)
            print()
        else:
            addch(buff, ch)
        sys.stdout.write("\r\033[K") # キャリッジリターン, エスケープシーケンスによる行削除(<ESC>[K)
        for c in buff:
            print(chr(c),end='')
        sys.stdout.flush()


    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", help="show unicode typed", action="store_true")
    parser.add_argument("--two", help="switch the mode two", action="store_true")
    args = parser.parse_args()
    if(args.two):
        main2()
    else:
        main()
