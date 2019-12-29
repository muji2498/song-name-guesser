import random
import re
import ctypes
import easygui


def main():
    pass


if __name__ == '__main__':
    main()

score = 0


def song_gen():
    remove_lower = lambda text: re.sub('[a-z]', '- ', text)
    filename = 'name_SongArtist.txt'
    line_number = random.randint(1, 32)
    with open(filename, 'r') as filehandle:
        current_line = 1
        for line in filehandle:
            if current_line == line_number:
                fields = line.split(';')
                songtitle = fields[0]
                songtitle1 = remove_lower(songtitle)
                artist = fields[1]
                uppercase = songtitle1
                qlue = uppercase + ' by ' + artist
                # print(uppercase + ' by ' + artist)
                break
            current_line += 1

    global score
    guess = easygui.enterbox(qlue, "\nPlease Enter The Song Name")
    if guess == songtitle:
        score = score + 3
        text_field1 = username2, "Your Current Score Is", str(score), "Well Done!"
        ctypes.windll.user32.MessageBoxW(0, str(text_field1), 1)
        song_gen()
    else:
        guess1 = easygui.enterbox(qlue, "\nWRONG!!! Please Re-Enter The Song Name")
        if guess1 == songtitle:
            score = score + 1
            text_field2 = username2, "Your Current Score Is", str(score), "Well Done!"
            ctypes.windll.user32.MessageBoxW(0, str(text_field2), 1)
            song_gen()
        else:
            message = "HAHAHA Run Again!!", username2, "Your Score Is ", str(score), "Well Done!"
            message = str(message)
            ctypes.windll.user32.MessageBoxW(0, str(message), 0)
            scorename = 'ScoreName.txt'
            with open(scorename, 'a') as f:
                splitline = ';'
                write_1 = username2 + ':' + str(score) + splitline
                f.write(write_1)
            f.close()
            exit()


def highscore():
    scores_main = open("ScoreName.txt", "r").read().split(";")
    print(scores_main)
    # scores = []
    # for x in scores_main:
    #     scores = scores.append(x)
    # ctypes.windll.user32.MessageBoxW(0, scores_main, 1)


decision = easygui.enterbox("What would you like to run?\nRun HighScore = 1\nRun Game = 2")
decision = int(decision)
# decision = int(input("What Would You Like To Do?\nRun HighScore = 1\nRun Game = 2\n"))

if decision == 1:
    highscore()
if decision == 2:
    username1 = easygui.enterbox("Please Enter Your Name\n")
    username2 = easygui.enterbox("Please Re-Enter Your Name\n")
    if username1 == username2:
        welcome_message = "Welcome To The Game", username2
        ctypes.windll.user32.MessageBoxW(0, str(welcome_message), 1)
        song_gen()
    else:
        ctypes.windll.user32.MessageBoxW(0, "Please Run The Program Again", 1)
        exit()
    song_gen()
