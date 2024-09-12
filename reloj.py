import time

class Cronometro:
    def __init__(self):
        self.tiempo_inicio = None
        self.tiempo_total = 0
        self.en_pausa = True

    def iniciar(self):
        if self.en_pausa:
            self.tiempo_inicio = time.time()
            self.en_pausa = False
        else:
            print("El cronómetro ya está en marcha.")

    def pausar(self):
        if not self.en_pausa:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            self.tiempo_total += tiempo_transcurrido
            self.en_pausa = True
        else:
            print("El cronómetro ya está pausado.")

    def reiniciar(self):
        self.tiempo_inicio = None
        self.tiempo_total = 0
        self.en_pausa = True

    def tiempo_actual(self):
        if not self.en_pausa:
            tiempo_transcurrido = time.time() - self.tiempo_inicio
            return self.tiempo_total + tiempo_transcurrido
        else:
            return self.tiempo_total

    def mostrar_tiempo(self):
        tiempo = self.tiempo_actual()
        horas, rem = divmod(tiempo, 3600)
        minutos, segundos = divmod(rem, 60)
        return "{:02}:{:02}:{:05.2f}".format(int(horas), int(minutos), segundos)
