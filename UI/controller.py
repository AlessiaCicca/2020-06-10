import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        genere = self._view.dd_genere.value
        if genere is None:
            self._view.create_alert("Selezionare un genere")
            return
        grafo = self._model.creaGrafo(genere)
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                      f"{self._model.getNumEdges()} archi."))
        for nodo in grafo.nodes:
            self._view.dd_attore.options.append(ft.dropdown.Option(
                text=nodo))
        self._view.update_page()
    def handle_simili(self, e):
        attore = self._view.dd_attore.value
        if attore is None:
            self._view.create_alert("Selezionare un attore")
            return
        raggiungibili=self._model.analisi(attore)
        self._view.txt_result.controls.append(ft.Text(f"Attori simili a: {attore}"))
        for (nodi,cognome) in raggiungibili:
            self._view.txt_result.controls.append(ft.Text(f"{nodi}"))
        self._view.update_page()


    def fillDD(self):
        generi=self._model.generi
        for genere in generi:
            self._view.dd_genere.options.append(ft.dropdown.Option(
                text=genere))
