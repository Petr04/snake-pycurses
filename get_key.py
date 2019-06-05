import curses

def main(stdscr):
	curses.curs_set(0)
	stdscr.clear()

	stdscr.timeout(1000)

	while True:
		ch = stdscr.getch()

		if ch == -1:
			stdscr.clear()
		elif ch == ord('q'):
			break
		else:
			stdscr.clear()
			stdscr.addstr(0, 0, '{} {}'.format(ch, chr(ch)))

if __name__ == '__main__':
	curses.wrapper(main)
