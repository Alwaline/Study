import re

def srh_word(string):
    return re.findall(pattern=r'\b[-a-zA-Zа-яА-ЯёЁ]+\b', string=string)


def main():
    put = input()

    mch = srh_word(put)
    
    print(len(mch))
    
if __name__ == '__main__':
    main()