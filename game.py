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
        self.get_records()

    def draw_instructions():
        return

    def get_records(self):
        with open("records.txt", "r") as f:
            content = f.read()
            categories = content.split("\n\n")
            for categorie in categories:
                heading = categorie.split("_")
                number_of_pieces = heading[0]
                places = categorie.split("\n")
                i = 0
                self.records[int(number_of_pieces)] = {}
                for place in places:
                    i += 1
                    primero = place.find("[")
                    ultimo = place.find("]")
                    texto = place[primero + 1 : ultimo]
                    valores = texto.split(", ")
                    self.records[int(number_of_pieces)][i] = [int(valores[0]), float(valores[1])]
    
    def update_records(self):
        content = ""
        for key, value in self.records.items():
            for key2, value2 in value.items():
                content += f"{key}_{key2} = {value2}\n"
            content += "\n"
        final_content = content.rstrip("\n")
        with open("records.txt", "w", encoding="utf-8") as f:
            f.write(final_content)
        self.get_records()
        

