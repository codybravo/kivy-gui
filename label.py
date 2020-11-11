from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from data import New
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase
from kivymd.icon_definitions import md_icons


class MenuScreen(Screen):
	pass
	
		
class MathScreen(Screen):
	pass
		
class SimtrapScreen(Screen):
	a = ObjectProperty()
	b = ObjectProperty()
	n = ObjectProperty()
	d = ObjectProperty()
	exp = ObjectProperty()
	out1 = ObjectProperty()
	out2 = ObjectProperty()
	correction = StringProperty()
	dialog = None
	
	def showa(self):
		if not self.dialog:
			self.dialog = MDDialog(text="Please fill the form properly")
		self.dialog.open()	
	
	def validation(self):
		if self.a.text != "" and self.b.text != "" and self.n.text != "" and self.exp.text != "":
			self.on_submit()
		else:
			self.showa()
						
	def on_submit(self):
		with open("data.txt","w") as f:
			f.write("")
		if self.d.text == "":
			self.d.text = "4"
			
		self.exp.text = self.exp.text.replace("x","self.x")
		self.out1.text,self.out2.text = New(self.a.text,self.b.text,self.n.text,self.exp.text,"data.txt",self.correction,self.d.text).add() 
		self.exp.text = self.exp.text.replace("self.x","x")

class Tab(FloatLayout, MDTabsBase):
	pass
	
class WindowManager(ScreenManager):
	pass 
	
#at = MenuScreen().on_submit() 
#print(at)






class NewApp(MDApp):
	
	def build(self):
		#theme for all screen
		self.theme_cls.primary_palette = "Red"
		#self.theme_cls.primary_hue = "A700"
		self.theme_cls.theme_style = "Light"
		
		lb = Builder.load_file("lb.kv")
		return lb
		

	
		
		
		

		
		
if __name__=="__main__":	
	NewApp().run()