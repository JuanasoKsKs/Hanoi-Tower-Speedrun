import os

records = {
    3 : {
        "primero" : 2,
        "segundo" : 2,
    },
    4 : {
        "primero" : 2,
        "segundo" : 2,
    }
}


class Game():
    def __init__(self):
        self.won = False
        self.records = {}
        self.started = False

    def draw_instructions():
        return

    def get_records(self):
        with open("records.txt", "r") as f:
            content = f.read()
            categories = content.split("\n\n")
            for categorie in categories:
                number_of_pieces = categorie[0]
                places = categorie.split("\n")
                i = 0
                self.records[str(number_of_pieces)] = {}
                for place in places:
                    i += 1
                    primero = place.find("[")
                    ultimo = place.find("]")
                    texto = place[primero + 1 : ultimo]
                    valores = texto.split(", ")
                    self.records[str(number_of_pieces)][i] = [int(valores[0]), int(valores[1])]

            return self.records

