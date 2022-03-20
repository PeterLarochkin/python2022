from .figdate import date
import argparse
import locale
if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, "ru_RU")
    parser = argparse.ArgumentParser()
    parser.add_argument("-format", default="%Y %d %b, %A", type=str)
    parser.add_argument("-font", default="graceful", type=str)
    args = parser.parse_args()
    print(date(args.format, args.font))
    