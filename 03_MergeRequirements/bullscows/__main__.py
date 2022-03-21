import string
from .bullscows import *
import sys
import urllib.request

if __name__ == "__main__":
    len_of_words = int(sys.argv[2]) if len(sys.argv) > 2 else 5    
    try:
        words = open(sys.argv[1], "r", encoding="utf8").read().split()
        words = list(filter(lambda word: len(word) == len_of_words, words))
        print(gameplay(ask=ask, inform=inform, words=words))
    except IOError:
        try: 
            req = urllib.request.Request(sys.argv[1])
            response = urllib.request.urlopen(req).read().decode("utf8")
            words = response.split()
            words = list(filter(lambda word: len(word) == len_of_words, words))
            print(gameplay(ask=ask, inform=inform, words=words))
        except urllib.error.URLError:
            print("Not valid path or url")