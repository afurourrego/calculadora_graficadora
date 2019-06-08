import Pyro4
import os

@Pyro4.expose
class Calculadora():
    def calcular(self, texto):
        try:
            resultado = str(eval(texto))
        except:
            resultado = "ERROR"
        return resultado

    def lanzar_grafo(self):
        os.system('python D:\GtiHub\calculadora_graficadora\grafos.py')



demonio=Pyro4.Daemon()
uri = demonio.register(Calculadora)
dns = Pyro4.locateNS()
dns.register("calcu.com", uri)
demonio.requestLoop()

# python -m Pyro4.naming
