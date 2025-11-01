import flet as ft
from UI.view import View
from model.modello import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    # TODO
    def HandlerCerca(self, e):
        self._view.lista_auto_ricerca.controls.clear()
        modello = self._view.txt_modello.value.strip()
        automobili = self._model.cerca_automobili_per_modello(modello)

        if modello == '':
            self._view.show_alert("❌ Il campo 'Modello' non può essere vuoto per effettuare la ricerca")
            return

        if not automobili:
            self._view.show_alert(f'❌ Nessuna automobile trovata con il modello {modello}')
        else:
            for auto in automobili:
                automobile = ft.Text(auto)
                self._view.lista_auto_ricerca.controls.append(automobile)
            self._view.show_alert(f'✅ Ricerca del modello: {modello} effettuata con successo!')

        self._view.txt_modello.value = ""
        self._view.txt_modello.update()
        self._view.update()

    def HandlerMostra(self, e):
        self._view.lista_auto.controls.clear()
        automobili = self._model.get_automobili()

        if not automobili:
            self._view.show_alert(f'❌ Nessuna automobile trovata!')
        else:
            for auto in automobili:
                automobile = ft.Text(auto)
                self._view.lista_auto.controls.append(automobile)
            self._view.show_alert('✅ Aggiunta delle automobili effettuata con successo!')


        self._view.update()

