import flet as ft

class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        #valori letti dalla page e modificabili
        self.testo_casellaTesto = None
        self.valore_dd = None

    def read_casellaTesto(self, e):
        """
        legge e memorizza nella classe controller il testo inserito dall'utente in casella_testo
        """
        self.testo_casellaTesto = self._view.casella_testo.value
        print(f"testo letto: {self.testo_casellaTesto} - {type(self.testo_casellaTesto)}")


    #DROPDOWN
    def fill_dropdown(self):
        lista_opzioni = ["a", (1, 2), "b", 14, 8.24, ["carote", "banane", 25]]
        for o in lista_opzioni:
            self._view.dropdown.options.append(ft.dropdown.Option(key= o,
                                                                  text=o,
                                                                  data= o,
                                                                  on_click=self.read_dropdown))
    def read_dropdown(self, e):
        self.valore_dd = e.control.data
        print(f"valore letto: {self.valore_dd} - {type(self.valore_dd)}")

    #ALTERNATIVA dropdown
    def fillDD(self):
        lista_opzioni = ["a", (1, 2), "b", 14, 8.24, ["carote", "banane", 25]]
        for o in lista_opzioni:
            self._view.dd.options.append(ft.dropdown.Option(o))

    def readDD(self, e):
        print(self._view.dd.value)



    def fill_listView(self):
        lista_elementi = ["a", (1, 2), "b", 14, 8.24]
        for el in lista_elementi:
            self._view.lv.controls.append(ft.Text(f"{el}"))



    def read_casellaTesto_intero(self):
        valore = self._view._txtInDurata.value
        try:
            valore = int(valore)
            self.valore = valore
            print(f"durata: {self.valore} {type(valore)}")
            return True
        except ValueError:
            self._view.create_alert("inserire valore valido")
            return False

    # template funzione controller handle creazione grafo
    def handle_creaGrafo(self, e):
        self._view.lv_result.controls.clear()
        self._view.update_page()

        self._model.build_graph()

        self._view.lv_result.controls.append(ft.Text(self._model.grafo))

        self._view.update_page()

