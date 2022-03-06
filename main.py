import tkinter
import game

window = tkinter.Tk()
window.title("Connect 4")
window.geometry("650x600")

display = game.grid

def sendColumn(column):
    display = game.main("X", column)["Grid"]

chooseOne = tkinter.Button(window, text="1", bg="white", command=lambda: sendColumn(1))
chooseOne.place(x=150, y=50, height=30, width=40)
chooseTwo = tkinter.Button(window, text="2", bg="white", command=lambda: sendColumn(2))
chooseTwo.place(x=200, y=50, height=30, width=40)
chooseThree = tkinter.Button(window, text="3", bg="white", command=lambda: sendColumn(3))
chooseThree.place(x=250, y=50, height=30, width=40)
chooseFour = tkinter.Button(window, text="4", bg="white", command=lambda: sendColumn(4))
chooseFour.place(x=300, y=50, height=30, width=40)
chooseFive = tkinter.Button(window, text="5", bg="white", command=lambda: sendColumn(5))
chooseFive.place(x=350, y=50, height=30, width=40)
chooseSix = tkinter.Button(window, text="6", bg="white", command=lambda: sendColumn(6))
chooseSix.place(x=400, y=50, height=30, width=40)
chooseSeven = tkinter.Button(window, text="7", bg="white", command=lambda: sendColumn(7))
chooseSeven.place(x=450, y=50, height=30, width=40)

window.mainloop()