class Tempo:
    def __init__(self):
        self.horas = 0
        self.minutos = 0
        self.segundos = 0
        self.dife_hora = 0
        self.dife_min = 0
        self.dife_seg = 0

    def set_medidas_tempo(self, aux_hora, aux_min, aux_seg):
        if (0 <= aux_hora < 25) and (0 <= aux_min < 61) and (0 <= aux_seg < 61):
            self.horas = aux_hora
            self.minutos = aux_min
            self.segundos = aux_seg
            return "Hora Valida"
        return "Hora Invalida"

    def converte_tempo_segundos(self):
        return 3600 * self.horas + 60 * self.minutos + self.segundos

    def converte_segundos_tempo(self, tempo1, tempo2):
        diferenca = tempo1 - tempo2
        self.dife_hora = diferenca // 3600
        self.dife_min = (diferenca - (self.dife_hora * 3600)) // 60
        self.dife_seg = diferenca % 60

    def get_dife_hora(self):
        return self.dife_hora

    def get_dife_min(self):
        return self.dife_min

    def get_dife_seg(self):
        return self.dife_seg


# Exemplo de uso
tempo = Tempo()
print(tempo.set_medidas_tempo(10, 20, 30))  # Saída esperada: Hora Valida
print(tempo.converte_tempo_segundos())  # Saída esperada: 37230
tempo.converte_segundos_tempo(7200, 3600)
print(tempo.get_dife_hora())  # Saída esperada: 1
print(tempo.get_dife_min())  # Saída esperada: 0
print(tempo.get_dife_seg())  # Saída esperada: 0
