class Data:
    def __init__(self, aux_dia, aux_mes, aux_ano):
        self.dia = aux_dia
        self.mes = aux_mes
        self.ano = aux_ano

    def get_dia(self):
        return self.dia

    def get_mes(self):
        return self.mes

    def get_ano(self):
        return self.ano

    def valida_data(self):
        if (0 < self.dia < 32) and (0 < self.mes < 13) and (1900 < self.ano < 2040):
            return "Data Valida"
        return "Data Invalida"

    def determina_dia_semana(self):
        chave_mes = {
            1: 1, 2: 4, 3: 4, 4: 0, 5: 2, 6: 5,
            7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12: 6
        }

        chave_do_mes = chave_mes.get(self.mes, 0)
        chave_do_ano = (self.ano // 4 + self.ano % 7) % 7
        maior_multiplo_de_sete = 0
        for i in range(self.dia + chave_do_mes + chave_do_ano):
            if i % 7 == 0:
                maior_multiplo_de_sete = i

        formula = (self.dia + chave_do_mes + chave_do_ano) - maior_multiplo_de_sete
        dias_semana = {
            1: "Domingo", 2: "Segunda-feira", 3: "Terca-feira",
            4: "Quarta-feira", 5: "Quinta-feira", 6: "Sexta-feira", 0: "Sabado"
        }
        return dias_semana.get(formula, "")

    @staticmethod
    def calcula_dias_entre_datas(dia1, mes1, ano1, dia2, mes2, ano2):
        dia_total_ano = 0
        dia_total_mes = 0

        for i in range(ano1, ano2):
            if i % 4 == 0:
                dia_total_ano += 366
            else:
                dia_total_ano += 365

        if mes1 > mes2:
            for i in range(mes1, mes2, -1):
                dia_total_mes += 30
                if i % 2 == 0:
                    dia_total_mes += 1
        else:
            for i in range(mes2, mes1, -1):
                dia_total_mes += 30
                if i % 2 == 0:
                    dia_total_mes += 1

        if mes1 > mes2:
            dia_total_ano += dia_total_mes
        else:
            dia_total_ano -= dia_total_mes

        if dia1 > dia2:
            dia_total_ano += (dia1 - dia2)
        else:
            dia_total_ano += (dia2 - dia1)

        return dia_total_ano


# Exemplo de uso
data1 = Data(10, 2, 2024)
print(data1.valida_data())  # Saída esperada: Data Valida
print(data1.determina_dia_semana())  # Saída esperada: Segunda-feira

data2 = Data(20, 3, 2023)

print(Data.calcula_dias_entre_datas(data1.get_dia(), data1.get_mes(), data1.get_ano(),
                                    data2.get_dia(), data2.get_mes(), data2.get_ano()))  # Saída esperada: 39
