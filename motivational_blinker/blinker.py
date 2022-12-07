import PySimpleGUI as sg
import time
import random


# Create the window
with open("/home/nitish/PycharmProjects/pythonProject/tsr/blink_it/motivations.txt", "r") as fp:
    text = fp.read()

text = [i for i in text.splitlines() if i.strip()]

t1 = time.time()
# Create an event loop
while True:
    event = False
    t2 = time.time()
    if int(t2 - t1) % 180 ==0:
        layout = [[sg.Text(random.choice(text), size=(50, 10), text_color="white",
                           background_color="black", auto_size_text=False, border_width=10)], [sg.Button("OK")]]
        window = sg.Window("blinker", layout)
        event, values = window.read()
        t1 = t2
        if event == "OK":
            window.close()
            continue
