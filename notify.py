from datetime import datetime


def inter(word):
    now = datetime.now()
    current_time = now.strftime("%d.%m.%Y %H:%M:%S")
    current_time = current_time.replace(".", " ")
    current_time = current_time.replace(":", " ")
    current_time = current_time.split()
    print(word)
    word = word.split()
    word = str(word[-1:-3:-1])
    word = word.replace("[", "")
    word = word.replace("]", "")
    word = word.replace(".", " ")
    word = word.replace(":", " ")
    word = word.replace(",", "")
    word = word.replace("'", "")
    print(word)
    word = word.split()
    return (int(word[2]) - int(current_time[2])) * 60 * 60 * 24 + (
                int(word[3]) - int(current_time[3])) * 60 * 60 * 24 * 30 + (
                   int(word[4]) - int(current_time[4])) * 60 * 60 * 24 * 30 * 365 + (
                       int(word[0]) - int(current_time[0])) * 60 * 60 + (
                   int(word[1]) - int(current_time[1])) * 60
