import flet as ft

"""
Documentazione flet https://flet.dev/docs/
"""

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP - EXAM NOTES"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        #ELEMENTI
        self._title = None
        self.testo = None
        self.casella_testo = None
        self.bottone = None
        self.dropdown = None
        self.lv = None
        self.row_loadingBar = None

    def load_interface(self):
        # INIZIALIZZAZIONE
        self._title = ft.Text("TdP - EXAM NOTES", color="blue", size=24)
        self._page.controls.append(self._title)

        #aggiunta elementi

        #testo libero
        self.testo = ft.Text("Questo è del testo, FEEEGA")
        self._page.controls.append(self.testo)

        #casella di testo modificabile
        self.casella_testo = ft.TextField(label="Casella di testo",
                                          hint_text= "** suggerimento **")
        #self._page.controls.append(self.casella_testo)

        #bottone
        self.bottone = ft.ElevatedButton(text="bottone leggi testo",
                                         on_click= self._controller.read_casellaTesto)
        #self._page.controls.append(self.bottone)

        #dropdown
        self.dropdown = ft.Dropdown(label="label")
        self._controller.fill_dropdown()
        #alternativa dropdown
        self.dd = ft.Dropdown(label="label")
        self._controller.fillDD()
        self.btnRead = ft.ElevatedButton(text="bottone leggi dd",
                                         on_click= self._controller.readDD)

        #self._page.controls.append(self.dropdown)

        #listview
        self.lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._controller.fill_listView()
        #self._page.controls.append(self.lv)

        #inserimento per righe ROW
        row1 = ft.Row([self.casella_testo, self.bottone])    #contiene la lista di controlli che compongono la row
        row2 = ft.Row([self.dropdown])
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(self.lv)

        #self.show_loading_bar()
        #*** funzione lenta***
        #self.remove_loading_bar():

        #AGGIORNARE PAGINA SEMPRE
        self._page.update()

    def create_alert(self, message):
        """
        manda a schermo un avviso per l'utente
        :param message: messaggio da lanciare
        """
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()


    """
    LOADING BAR
    chiama funzione lunga di cui si desidera mostrare il caricamento tra show/remove
    """
    def show_loading_bar(self):
        # progress bar
        progress_loading = ft.ProgressBar(width=400,
                                          height=20,
                                          color="blue",
                                          bgcolor="#eeeeee")

        self.row_loadingBar = ft.Row([progress_loading],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.controls.append(self.row_loadingBar)
        self._page.update()

    def remove_loading_bar(self):
        self._page.controls.remove(self.row_loadingBar)
        self._page.update()



    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller
