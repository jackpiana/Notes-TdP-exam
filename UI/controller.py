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

    def fill_dropdown(self):
        lista_opzioni = ["a", (1, 2), "b", 14, 8.24]
        for o in lista_opzioni:
            self._view.dropdown.options.append(ft.dropdown.Option(key= o,
                                                                  text=o,
                                                                  data= o,
                                                                  on_click=self.read_dropdown))

    def read_dropdown(self, e):
        self.valore_dd = e.control.data
        print(f"valore letto: {self.valore_dd} - {type(self.valore_dd)}")


    def fill_listView(self):
        lista_elementi = ["a", (1, 2), "b", 14, 8.24]
        for el in lista_elementi:
            self._view.lv.controls.append(ft.Text(f"{el}"))














    def read_casellaTesto_intero(self):
        durata = self._view._txtInDurata.value
        try:
            durata = int(durata)
            self.durata = durata*60*1000
            print(f"durata: {self.durata} {type(durata)}")
            return True
        except ValueError:
            self._view.create_alert("inserire valore valido")
            return False
