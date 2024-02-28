from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image,ImageOps , ImageDraw
import requests
import time
import json


class  BitcoinTracker:
    ################# colori ###############
    co0 = "#444466"  
    co1 = "#feffff"  
    co2 = "#6f9fbd"  
    sfondo = "#484f60" 
    #######################################
    def __init__(self, root=Tk()):
        self.root = root
        self.root.title("Bitcoin Price Tracker")
        self.root.geometry("320x350")
        self.root.resizable(False, False)
        self.root.iconphoto(False, PhotoImage(file="bitcoin.png"))
        self.root.config(bg=self.sfondo)

        # titolo
        title = Label(self.root, text="Bitcoin Price Tracker", font=("times new roman", 30, "bold"), bg="gray", fg="black").place(x=0, y=0, relwidth=1)

        ################# Frames ####################
        ttk.Separator(self.root, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)
        
        self.frame1 = Frame(self.root, width=320, height=50, bg=self.co1, pady=0, padx=0, relief="flat",)
        self.frame1.grid(row=1, column=0)
        
        self.frame2 = Frame(self.root, width=320, height=300, bg=self.sfondo, pady=12, padx=0, relief="flat",)
        self.frame2.grid(row=2, column=0, sticky=NW)
        
        style = ttk.Style(self.frame1)
        style.theme_use("clam")
        
        self.img = Image.open('bitcoin.png')
        self.img = self.img.resize((30, 30))
        self.img = ImageTk.PhotoImage(self.img)
        self.l_icon1 = Label(self.frame1,image=self.img, compound=LEFT,  bg=self.sfondo, fg="white",font=('Ivy 10 bold'), anchor="nw", relief=FLAT)
        self.l_icon1.place(x=10, y=10)

        self.l_nome = Label(self.frame1, text="Bitcoin Price Tracker", height=1, padx=0, relief="flat", anchor="center", font=('Arial 20 '), bg=self.co1, fg=self.co2)
        self.l_nome.place(x=50, y=5)

        self.l_prezzo_usd = Label(self.frame2, text="", width=14, height=1, padx=0, relief="flat", anchor="center", font=('Arial 30 '), bg=self.sfondo, fg=self.co1)
        self.l_prezzo_usd.place(x=0, y=50)
        
        self.l_prezzo_euro = Label(self.frame2, text="", height=1, padx=0, relief="flat", anchor="center", font=('Arial 12 '), bg=self.sfondo, fg=self.co1)
        self.l_prezzo_euro.place(x=10, y=130)
        
        self.l_prezzo_reais = Label(self.frame2, text="",height=1, padx=0, relief="flat", anchor="center", font=('Arial 12 '), bg=self.sfondo, fg=self.co1)
        self.l_prezzo_reais.place(x=10, y=160)
        
        
    def info(self):
        api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,BRL"

        # -- HTTP request
        r=requests.get(api_link)
        
        # -- convertire i dati in un dizionario
        self.dati=r.json()
        
        # -- USD
        self.valore_usd = float(self.dati["USD"])
        self.valore_in_usd = "${:,.3f}".format(self.valore_usd)
        self.l_prezzo_usd["text"] = self.valore_in_usd
        
        # -- Euro
        self.valore_euro = float(self.dati["EUR"])
        self.valore_in_euro = "{:,.3f}".format(self.valore_euro)
        self.l_prezzo_euro["text"] = "In euro é : € " + self.valore_in_euro
        
        # -- Reais
        self.valore_reais = float(self.dati["BRL"])
        self.valore_in_reais = "{:,.3f}".format(self.valore_reais)
        self.l_prezzo_reais["text"] = "In reais é : R$ " + self.valore_in_reais
    
        self.frame2.after(1000, self.info)


if __name__ == "__main__":
    BitcoinTracker().info()
    mainloop()