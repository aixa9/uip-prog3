import kivy
kivy. require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Calculador(BoxLayout):
	def Borrar(self, operacion):
			self.num.text = operacion[:-1]

	def elim(self, operacion):
			self.num.text = operacion[:0]


	def Calculos(self, operacion):
		try:
			self.num.text = str( eval(operacion))
			print (operacion)
			print (self.num.text)
		except:
			self.num.text = 'Error de sintaxis'

class CalculadorApp(App):
	title = "Calculadora"
	def build(self):
		return Calculador()

if __name__ in ('__main__', '__android__'):
	CalculadorApp().run()

#integrantes:
#YESELKA TYRRELL
#ALBERTO JUAREZ
