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
	def __init__(self,root):
		frame=Frame(root)
		frame.pack()
		self.itemfr(frame)
		self.txtfr(frame)
		return

	def mine(self):
                item_id = self.entry.get()
                m = miner()
                m.getItemTrans(item_id)
		
	def itemfr(self,frame):
                self.entry = Entry(frame,text="enter ebay item id")
		self.entry.pack(side=LEFT,padx=10,pady=12)

		self.button = Button(frame, text="MINE", command=self.mine)
		self.button.pack(side=LEFT,padx=15,pady=10)

		self.exit = Button(frame, text="exit", command=frame.quit)
		self.exit.pack(side=BOTTOM,padx=20,pady=10)

	def txtfr(self,frame):
		
		#define a new frame and put a text area in it
		textfr=Frame(frame)
		self.text=Text(textfr,height=50,width=200,background='white')
		
		# put a scroll bar in the frame
		scroll=Scrollbar(textfr)
		self.text.configure(yscrollcommand=scroll.set)
		
		#pack everything
		self.text.pack(side=LEFT)
		scroll.pack(side=RIGHT,fill=Y)
		textfr.pack(side=TOP)
		return
def main():
	root = Tk()
	s=mywidgets(root)
	sys.stdout = textbox_handler(s.text)
	root.title('ebay-miner')
	root.mainloop()
main()
