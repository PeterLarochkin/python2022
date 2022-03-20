from pyfiglet import Figlet
from time import strftime
from time import localtime


def date(format='%Y %d %b, %A',font='graceful' ):
    text_to_render = strftime(format, localtime())
    return Figlet(font).renderText(text_to_render)
