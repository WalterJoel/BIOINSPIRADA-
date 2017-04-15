import matplotlib.pyplot as plt
import random

#Inicio Algoritmo Genetico
class A_Genetico:
	 num_individuos      = 0
	 poblacion           = [] #Matriz que representa un individuo o cromosoma
	 longitud_cromosoma  = 0
	 list_result_fitnes  = []
	 valores_x 			   = [] #Para la grafica
	 valores_y 			   = [] #Para la grafica
	 iteraciones         = 0
	 def __init__(self,num_indi,long_cromosoma,num_iteraciones):
		  self.num_individuos     = num_indi
		  self.longitud_cromosoma = long_cromosoma 
		  self.iteraciones        = num_iteraciones
	 #Obtengo en una matriz toda mi poblacion en binario
	 def generarPoblacion(self):
		  for x in range(self.num_individuos):
				self.poblacion.append([])
				#Generando cada gen aleatoriamente
				for y in range(self.longitud_cromosoma):
					 gen = random.randint(0,1) #Elijo un gen entre 0 y 1
					 self.poblacion[x].append(gen)
					 print gen
				print "otro: "
	 def funcionFitness(self,list_temp_indi,cont):
		  string = "".join(map(str, list_temp_indi)) #Convierto a string el individuo que recibo por parametro
		  valor_entero  = int(string, base=2)
		  #Aplicamos la funcion, en este caso x^2
		  valor_fitness = valor_entero*valor_entero
		  #Agrego a mi lista de resultados fitnes el valor obtenido
		  self.list_result_fitnes.append(valor_fitness)
		  #Agregando valores para la grafica
		  self.valores_x.append(cont)
		  self.valores_y.append(valor_fitness)
	 def cruzamiento(self):
		#Elijo una posicion K para el cruzamiento, a partir de alli hago el cruce
		pos_k = random.randint(1,self.longitud_cromosoma-2)
		cont = 0
		list_temp_padre = []
		list_temp_madre = []
		#Itero hasta la pos k
		while cont < pos_k:
			list_temp_padre.append(self.poblacion[0][cont])
			list_temp_madre.append(self.poblacion[1][cont])
			cont = cont + 1
		# Ahora cont = K
		cont = pos_k
		while cont < self.longitud_cromosoma:
			#Aqui invierto las colas del indiv1 al indiv2
			list_temp_padre.append(self.poblacion[1][cont])
			list_temp_madre.append(self.poblacion[0][cont])
			cont = cont + 1
		print pos_k
		print list_temp_padre
		print list_temp_madre
		#Despues de hacer el cruzamiento, pasamos los cambios a la poblacion
		self.poblacion[0] = list_temp_padre
		self.poblacion[1] = list_temp_madre
	#Ordenar a todos los individuos segun su funcion Fitness ascendentemente
	 def seleccionRanking(self):
	 	cont = 1
		#Recorro todos los individuos
		for x in range(self.num_individuos):
			#Evaluo a cada individuo de acuerdo a la funcion fitness
			self.funcionFitness( self.poblacion[x],cont )
			cont = cont+1
		# Como en la lista `list_result_fitness tengo todos los resultados de una poblacion
		# Solo me queda ordenar esa lista y tengo mi Ranking
		self.list_result_fitnes.sort() 
		print "\n\n SELECCION POR RANKING RESULTADOS: "
		print self.list_result_fitnes
	 def mutacion(self):	
		#Calculo la cantidad de genes que voy a mutar segun el porcentaje
		cant_mutar = 0.0
		cont       = 0
		cant_mutar = (self.porcentaje_mutacion*self.num_individuos) / 100.0
		pos_random_indiv = random.randint(0,self.num_individuos-1) #Porque los individuos estan en la matriz poblacion
		while cont < cant_mutar:
			#ELige la posicion random entre las pos 0 y el num_individuos
			pos_random_gen   = random.randint(0,self.longitud_cromosoma-1) #Randon para el gen del individuo
			#Cambio el gen 
			if self.poblacion[pos_random_indiv][pos_random_gen] == 0:
				self.poblacion[pos_random_indiv][pos_random_gen] = 1
			else :
				self.poblacion[pos_random_indiv][pos_random_gen] = 1
			cont = cont + 1
	 #print self.poblacion
	 def mostrarGrafica(self):
		#Grafica para mostrar como cambia el genetico 
		print "valores: "
		print self.valores_x
		print "\n"
		print self.valores_y
		plt.plot(self.valores_x,self.valores_y)
		plt.title('Genetico Evolucion')
		plt.xlabel('x label')
		plt.ylabel('y label')
		plt.show()
	 def bucle(self):
	 	print "Poblacion 0: *****"
		self.generarPoblacion()
		self.seleccionRanking()
		cont = 1
		while cont<self.iteraciones:
			#limpio la lista del ranking
			self.Remove_List()
			self.cruzamiento()
			#self.Mutacion()
			print "Poblacion: ",cont, " *****"
			self.seleccionRanking()
			cont = cont+1
		self.mostrarGrafica()

	 def Remove_List(self):
		for x in self.list_result_fitnes[:]:
			self.list_result_fitnes.remove(x)
	 
def main():
	 obj = A_Genetico(2,4,2) 	#longitud del cromosoma 4 = maximo 31
	 obj.bucle()
main()




