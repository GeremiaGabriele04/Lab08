from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._bestValue = 0
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        self.loadEvents(nerc)
        self._listEvents.sort(key=lambda x: x.date_event_began)
        self._solBest = []
        self._bestValue = 0

        self.ricorsione([], maxY, maxH, 0)
        return self._solBest, self._bestValue

    def ricorsione(self, parziale, maxY, maxH, pos):
        ore_tot = sum((e.date_event_finished - e.date_event_began).total_seconds() / 3600 for e in parziale)
        persone_tot = sum(e.customers_affected for e in parziale)

        if len(parziale) > 0:
            anni = [e.date_event_began.year for e in parziale]
            if max(anni) - min(anni) > maxY:
                return
        else:
            anni = []

        if ore_tot > maxH:
            return

        # Aggiorno best
        if persone_tot > self._bestValue:
            self._bestValue = persone_tot
            self._solBest = parziale.copy()

        # Esplorazione
        for i in range(pos, len(self._listEvents)):
            e = self._listEvents[i]

            parziale.append(e)
            self.ricorsione(parziale, maxY, maxH, i + 1)
            parziale.pop()


    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc