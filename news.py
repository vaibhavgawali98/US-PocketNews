import requests
from tkinter import*
from urllib.request import urlopen
from PIL import ImageTk,Image 
import io
import webbrowser

class NewsApp:

    def __init__(self):
        #fetch data
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=a966f7928b0f4951899c1444b9ea26be').json()
        self.load_gui()
        self.load_news_item(0)


    def load_gui(self):

        self.root = Tk()
        self.root.title('Insta  Read')
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.config(background='black')
        #load first news item

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self,index):
        self.clear()
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        except:
            img_url = 'https://png.pngtree.com/png-vector/20190820/ourmid/pngtree-no-image-vector-illustration-isolated-png-image_1694547.jpg'
            raw_data = urlopen(img_url).read()
            
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)


        label = Label(self.root,image=photo)
        label.pack()


        heading = Label(self.root,text=self.data['articles'][index]['title'],fg='white',bg='black',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))

        details = Label(self.root,text=self.data['articles'][index]['description'],fg='white',bg='black',wraplength=350,justify='center')
        details.pack(pady=(2,20))
        details.config(font=('verdana',12))     

        frame = Frame(self.root,bg='black')
        frame.pack(expand=True,fill=BOTH)

        if index != 0:
            prev = Button(frame,text='Prev',width=16,height=3,command= lambda : self.load_news_item(index+1))
            prev.pack(side=LEFT)


        read = Button(frame,text='Read More',width=16,height=3,command= lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        if index != len(self.data['articles'])-1:
            nextt = Button(frame,text='Next',width=16,height=3,command= lambda : self.load_news_item(index-1))
            nextt.pack(side=LEFT)

        self.root.mainloop() 

    def open_link(self,url):
        webbrowser.open(url)    


app = NewsApp()