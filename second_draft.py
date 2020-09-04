from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

class Root(Tk):
	def __init__(self):
		super(Root, self).__init__()
		self.title("Python Tkinter Dialog Widget")
		self.minsize(640, 400)

		self.labelFrame = ttk.LabelFrame(self, text = "Open File")
		self.labelFrame.grid(column = 0, row = 1, padx = 0, pady = 0)
		
		
		#Player Display Frames
		
		self.display1Frame = ttk.LabelFrame(self, text = "Player 1")
		self.display1Frame.grid(column = 0, row = 2, padx = 0, pady = 0)

		self.display2Frame = ttk.LabelFrame(self, text = "Player 2")
		self.display2Frame.grid(column = 4, row = 2, padx = 0, pady = 0)
		
		self.display3Frame = ttk.LabelFrame(self, text = "Player 3")
		self.display3Frame.grid(column = 0, row = 8, padx = 0, pady = 0)
		
		self.display4Frame = ttk.LabelFrame(self, text = "Player 4")
		self.display4Frame.grid(column = 4, row = 8, padx = 0, pady = 0)
		
		self.energyFrame = ttk.LabelFrame(self, text = "Energy Expended")
		self.energyFrame.grid(column = 1, row = 13, padx = 0, pady = 0) 
		
		
		self.vicky = ImageTk.PhotoImage(Image.open("vicky.jpg").resize((100, 100)))
		self.gaby = ImageTk.PhotoImage(Image.open("gaby.jpg").resize((100, 100)))
		self.rachel = ImageTk.PhotoImage(Image.open("rachel.jpg").resize((100, 100)))
		self.manny = ImageTk.PhotoImage(Image.open("manny.jpg").resize((100, 100)))
		
		
		
		self.button()
		self.displays()


	def button(self):
		self.button = ttk.Button(self.labelFrame, text = "Browse A File",command = self.fileDialog)
		self.button.grid(column = 1, row = 1)
		
	def Xcalculate_energy(self, mass, velocity, velocity0, time, distance):
		Ex = ( (mass/2.2) * ( (velocity - velocity0) / time ) ) * distance * (786.8/1000)
		return Ex
		
	def Ycalculate_energy(self, mass, velocity, velocity0, time, distance):
		Ey = ( (mass/2.2) * ( (velocity - velocity0) / time ) ) * distance * (786.8/1000)
		return Ey
		

		
		
	def displays(self):
		#Energy Expended Display
		#self.energy = ttk.Label(self.energyFrame, text= "Energy Expended")
		energy_entry = ttk.Entry(self.energyFrame, textvariable = StringVar(), font=('calibre',10,'normal'))
		#self.energy.grid(column=2, row=13)
		energy_entry.grid(column=1, row=14)
	
		#Player Displays
		  
		self.display1 = ttk.Label(self.display1Frame, image=self.vicky)
		self.display1.grid(column=0, row=2)
   
   
		self.health1 = ttk.Label(text="Health:") #19/19
		health1_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		health1_entry.grid(column=0, row=4)
		self.health1.grid(column=0, row=3)
		
		self.calories1 = ttk.Label(text="KCal:") #1750/1750
		self.calories1.grid(column=0, row=5)
		calories1_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		calories1_entry.grid(column=0, row=6)
		#####################################
		
		self.display2 = ttk.Label(self.display2Frame, image=self.manny)
		self.display2.grid(column=4, row=2)
		self.health2 = ttk.Label(text="Health: ") #20/20
		self.calories2 = ttk.Label(text="KCal: ") #2000/2000
		self.health2.grid(column=4, row=3)
		self.calories2.grid(column=4, row=5)
		
		health2_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		health2_entry.grid(column=4, row=4)
		calories2_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		calories2_entry.grid(column=4, row=6)
		#######################################
		
		self.display3 = ttk.Label(self.display3Frame, image=self.rachel)
		self.display3.grid(column=0, row=8)
		self.health3 = ttk.Label(text="Health:") #21/21
		self.calories3 = ttk.Label(text="KCal:") #2250/2250
		self.health3.grid(column=0, row=9)
		self.calories3.grid(column=0, row=10)
		
		health3_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		health3_entry.grid(column=0, row=10)
		calories3_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		calories3_entry.grid(column=0, row=12)
		######################################
		
		self.display4 = ttk.Label(self.display4Frame, image=self.gaby)
		self.display4.grid(column=4, row=8)
		self.health4 = ttk.Label(text="Health:") #23/23
		self.calories4 = ttk.Label(text="KCal:") #2750/2750
		self.health4.grid(column=4, row=9)
		self.calories4.grid(column=4, row=10)
		
		health4_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		health4_entry.grid(column=4, row=10)
		calories4_entry = ttk.Entry(textvariable = StringVar() ,font=('calibre',10,'normal')) 
		calories4_entry.grid(column=4, row=12)
		#########################################

	def fileDialog(self):

		self.filename = filedialog.askopenfilename(initialdir =  "/user", title = "Select A File", filetypes =
		(("jpeg files","*.jpg"),("all files","*.*")) )
		self.label = ttk.Label(self.labelFrame, text = "")
		self.label.grid(column = 1, row = 2)
		#self.label.configure(text = self.filename)

		img = Image.open(self.filename)
		img = img.resize((500, 340))
		photo = ImageTk.PhotoImage(img)

		self.label2 = Label(image=photo)
		self.label2.image = photo 
		self.label2.grid(column=1, row=7)
		
root = Root()
root.mainloop()