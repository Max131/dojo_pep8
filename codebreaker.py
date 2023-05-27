TRUE_NUMBER = "1010"


class Codebreaker:
    def adivinar(self, numero=None):
        """
        Adivinar número
        """
        if TRUE_NUMBER == "":
            return "Number is not defined"

        if numero is None or len(numero) != 4:
            return "error"

        if numero == TRUE_NUMBER:
            return True

        resultado_x = ""
        resultado_ = ""
        array_number = []

        for i in len(numero):
            if array_number[numero[i]] is True:
                return "error"

            array_number[numero[i]] = True

        numero = list(numero)

        for index, i in numero:
            if TRUE_NUMBER[index] == numero[index]:
                resultado_x += "X"

            elif i in TRUE_NUMBER:
                resultado_ = "_"

        return resultado_x + resultado_
