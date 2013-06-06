# -*- coding: utf-8 -*-
'''
© 2012-2013 j$ startship enterprise
Authored by: Justin $
Licensed under CDDL 1.0
'''

import sys
from Tkinter import *
from miner import *

class textbox_handler:
  def __init__(self, text):
    self.data = []
    self.text = text #text is your tk text widget.
  def write(self, s):
    self.text.insert(END, s)
  def print_out(self):
    for line in data:
        self.text.insert('end',line)

class mywidgets:

	def selectall(self, event):
		event.widget.tag_add("sel","1.0","end")

	def __init__(self,root):
		bframe=Frame(root)
		tframe=Frame(root)
		tframe.pack(side=TOP)
		bframe.pack(side=BOTTOM)
		self.itemfr(tframe)
		self.txtfr(bframe)
		root.bind_class("Text","<Control-a>", self.selectall)
		return

	def gettrans(self):
		item_id = self.ItemEntry.get()
		m = miner()
		m.getItemTrans(item_id)
		return

	def getitems(self):
		seller_id = self.SellerEntry.get()
		cat_id = self.CatEntry.get()
		m = miner()
		m.getSellerItems(seller_id, cat_id)

	def getcats(self):
		m = miner()
		m.getCategories()


	def itemfr(self,frame):

		self.ItemLabel = Label(frame,text="Item ID #")
		self.ItemLabel.pack(side=LEFT)
		self.ItemEntry = Entry(frame,text="enter ebay item id")
		self.ItemEntry.pack(side=LEFT)
		self.TButton = Button(frame, text="ItemTransactions", command=self.gettrans)
		self.TButton.pack(side=LEFT)

		self.SellerLabel = Label(frame,text="Seller ID")
		self.SellerLabel.pack(side=LEFT)
		self.SellerEntry = Entry(frame,text="seller id")
		self.SellerEntry.pack(side=LEFT)

		self.CatLabel = Label(frame,text="Category #")
		self.CatLabel.pack(side=LEFT)
		self.CatEntry = Entry(frame,text="enter category")
		self.CatEntry.pack(side=LEFT)
		self.IButton = Button(frame, text="Get Seller Items", command=self.getitems)
		self.IButton.pack(side=LEFT)

		self.CButton = Button(frame, text="Get Ebay Categories #s", command=self.getcats)
		self.CButton.pack(side=LEFT)



	def txtfr(self,frame):
		
		#define a new frame and put a text area in it
		textfr=Frame(frame)
		self.text=Text(textfr,height=50,width=200,background='white')
		
		# put a scroll bar in the frame
		scroll=Scrollbar(textfr)
		self.text.configure(yscrollcommand=scroll.set)
		self.exit = Button(frame, text="exit", command=frame.quit)
		self.exit.pack(side=BOTTOM,padx=20,pady=10)

		#pack everything
		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT,fill=Y)
		textfr.pack(side=TOP, fill=X)
		return
def main():
	root = Tk()
	s=mywidgets(root)
	sys.stdout = textbox_handler(s.text)
	root.title('ebay-miner')
	root.mainloop()
main()
