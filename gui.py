import tkinter as tk
import movie_recommender
from time import sleep

window=tk.Tk()
window.title("Recommender !!!")
window.geometry('1250x600')
lbl=tk.Label(window,text="Movie Recommender System",font=("Ariel Bold",60))
lbl.pack()
lb1=tk.Label(window,text="Enter The Movie Name: ",font=("Ariel Bold",20))
lb1.place(x=200,y=100)
txt=tk.Entry(window,width=50)
txt.place(x=450,y=100)
txt.focus()
l1=tk.Label(window,text="You May Also Like ....",font=("Ariel Bold",20))
l1.place(x=200,y=150)
yaxis=200
textFList=[]
myText=[]


for i in range(0,7):
    myText.append(None)
    myText[i]=tk.StringVar()


for i in range(0,7):
    l=tk.Label(window,textvariable=myText[i],font=("Ariel Bold",15))
    l.place(x=400,y=yaxis)
    textFList.append(l)
    yaxis=yaxis+60

def clicked():
       i=0
       moviename = txt.get()
       movie_recommender.movieprint(moviename)
       print(moviename)
       print(len(movie_recommender.recomendations))
       for movie in movie_recommender.recomendations:
          myText[i].set(movie)
          i=i+1
        
       movie_recommender.recomendations.clear()



btn = tk.Button(window,text="Show Movie",command=clicked)
btn.place(x=950,y=100)

window.mainloop()
