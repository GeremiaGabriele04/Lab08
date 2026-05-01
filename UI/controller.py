import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._idMap = {}
        self.fillIDMap()
        self._choiceNerc = "Nessuna Opzione"

    def handleWorstCase(self, e):
        maxY = self._view._txtYears.value
        maxH = self._view._txtHours.value
        nerc = self._idMap[self._view._ddNerc.value]
        if maxY == "" or maxH == "":
            self._view.create_alert("Inserire entrambi i valori!")
            return

        risultati = self._model.worstCase(nerc, int(maxY), int(maxH))
        self._view._txtOut.controls.append(ft.Text("Di seguito il numero totale di persone coivolte e gli eventi:"))
        self._view._txtOut.controls.append(ft.Text(risultati[1]))
        for e in risultati[0]:
            self._view._txtOut.controls.append(ft.Text(e))

        self._view.update_page()




    def fillDD(self):
        nercList = self._model.listNerc

        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(key=n.value, text=n.value))
        self._view.update_page()

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v



