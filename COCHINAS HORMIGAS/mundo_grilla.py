import pygame
import math
import random

class nodo():
  def __init__(self,x,y):
	self.pos_x  = x      #Coordenadas para el nodo
	self.pos_y  = y
	self.id     = 0
	self.cantidad_feromona = 0

class agente():
	#Recibe una posicion actual
	def __init__(self,pos_x,pos_actual_y):
		self.pos_actual_x  = pos_x
		self.pos_actual_y  = pos_y
		self.unidad_comida = 0

class mundoGrilla():
  # normal = 0,nido = 1, comida = 2 
  matriz = []
  def __init__(self,col,fil,num_agentes):
	self.total_agentes = num_agentes
	self.num_col  = col
	self.num_fil  = fil
	#Lleno la matriz de nodos
	for i in range(self.num_fil):
		self.matriz.append([])
		for j in range(self.num_col):
			self.matriz[i].append(nodo(i,j))
	#Creando una lista de agentes 
	for agente in range(self.total_agentes):
		nido_pos_x = random.randrange(0,self.num_col-1)
		nido_pos_y = random.randrange(0,self.num_fil-1)
		nuevo_agente = agente(nido_pos_x,nido_pos_y )
		self.list_agentes.append(nuevo_agente)

  def set_nodo_comida(self,x,y):  
	self.matriz[x][y].id = 2
  def posicionesComida(self):
	list_cantidades_comida = []
	total_posiciones = random.randrange(0,self.num_col-1)
	#Posiciones aleatorias
	temp_x = random.randrange(0,self.num_col-1)
	temp_y = random.randrange(0,self.num_fil-1)
	print total_posiciones
	for i in range(total_posiciones):
			#Indico que su ID es 2 para saber que son posiciones de comida
		self.matriz[temp_x][temp_y].id = 2
  def set_nodo_nido(self):
	while (1):
		#elegimos una posicion aleatoria para el nido
		self.nido_temp_x = random.randrange(0,self.num_col-1)
		self.nido_temp_y = random.randrange(0,self.num_fil-1)
		#Verificamos que la posicion aleatoria no sea de comida 
		if (self.matriz[nido_temp_x][nido_temp_y].id != 2):
			#Indicamos que su ID es 1 para saber que es el nido
			self.matriz[nido_temp_x][nido_temp_y].id = 1
			break
  #se verifica que un agente llega a la posicion comida
  def llego_posicion_comida(x,y,pos_agente):
  	if(self.matriz[x][y].id == 2):
  		#Aumentamos su unidad de comida en 1 del agente
  		self.list_agentes[pos_agente].unidad_comida +=1
  		return True
  	else:
  		return False
   def llego_posicion_nido(x,y,pos_agente):
   	 if(self.matriz[x][y].id == 1):
  		#Descontamos su unidad de comida en 1 del agente
  		self.list_agentes[pos_agente].unidad_comida -=1
  		return True
  	else:
  		return False


	def simularAccionPercepcion():
#Iteramos por cada agente
for agente in range(self.total_agentes):
#Un agente dara n movimientos 
for movimientos in range(self.num_col-1):
#0=quedarse, 1=arriba ,2=abajo,3=izquierda, 4=derecha
movimiento = random.randrange(0,4)
if(movimiento == 1): 
	list_cantidades_comida[agente].pos_actual_y +=1
	#Colocando la cantidad de feromona para esa posicion que se mueve
	self.matriz[self.nido_temp_x][self.nido_temp_y+1].cantidad_feromona = random.randrange(0,self.num_fil-1)
	#preguntando si llego al nido o a alguna posicion de comida
	self.llego_posicion_comida(self.nido_temp_x,self.nido_temp_y+1,agente)
	self.llego_posicion_nido(self.nido_temp_x,self.nido_temp_y+1,agente)
elif(movimiento ==2):
	list_cantidades_comida[agente].pos_actual_y -=1
	self.matriz[self.nido_temp_x][self.nido_temp_y-1].cantidad_feromona = random.randrange(0,self.num_fil-1)
	#preguntando si llego al nido o a alguna posicion de comida
	self.llego_posicion_comida(self.nido_temp_x,self.nido_temp_y-1,agente)
	self.llego_posicion_nido(self.nido_temp_x,self.nido_temp_y-1,agente)
elif(movimiento ==3):
	list_cantidades_comida[agente].pos_actual_x -=1
	self.matriz[self.nido_temp_x-1][self.nido_temp_y].cantidad_feromona = random.randrange(0,self.num_fil-1)
	#preguntando si llego al nido o a alguna posicion de comida
	self.llego_posicion_comida(self.nido_temp_x-1,self.nido_temp_y,agente)
	self.llego_posicion_nido(self.nido_temp_x-1,self.nido_temp_y,agente)
elif(movimiento ==4):
	list_cantidades_comida[agente].pos_actual_x +=1
	self.matriz[self.nido_temp_x+1][self.nido_temp_y].cantidad_feromona = random.randrange(0,self.num_fil-1)
	#preguntando si llego al nido o a alguna posicion de comida
	self.llego_posicion_comida(self.nido_temp_x+1,self.nido_temp_y,agente)
	self.llego_posicion_nido(self.nido_temp_x+1,self.nido_temp_y,agente)


def main():
	dim_x = input('Ingrese la dimension de X: ')
	dim_y = input('Ingrese la dimension de Y: ')
	total_agentes = input('Ingrese el numero de agentes: ')
	if(int(dim_y) >1 and int(dim_x) >1):
		#Inicializo toda la simulacion
		grilla = mundoGrilla(dim_x,dim_y,total_agentes)
		grilla.posicionesComida()
		grilla.set_nodo_nido()
		grilla.simularAccionPercepcion()
		grilla.dibujar()
	else:
		print 'Las dimensiones especificadas no son correctas para la simulacion'
	

main()

