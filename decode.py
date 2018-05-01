import sys
import os
import json
import codecs




def main():
    with codecs.open('data2.json', 'w',encoding="utf-8") as ff:

        with codecs.open('data_corrected.json', 'r',encoding="unicode-escape") as f:
            # line2 = str(line2)
            line =  f.read()
            print(line)
            ff.write(line)


if __name__ == '__main__':
    main()
