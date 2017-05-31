from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
	"""docstring for Application"""
	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.Label1=Label(self,text='Today is Turesdy',fg='blue')
		self.Label1.pack()
		self.Button1=Button(self,text='Exit',command=self.quit,fg="red")
		self.Button1.pack()
		self.nameInput=Entry(self)
		self.nameInput.pack()
		self.alertButton=Button(self,text='Hello',command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name=self.nameInput.get() or 'God!'
		messagebox.showinfo('Message','Hello, %s' % name)
def main():
	root=Tk()
	root.geometry("400x350+500+200")
	app=Application(root)
	app.master.title('Date')
	app.mainloop()

if __name__=='__main__':
	main()