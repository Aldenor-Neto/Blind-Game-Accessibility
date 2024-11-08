import ui
import wx
import globalPluginHandler
import winsound
import os

from . import parOrImpar
from . import adivinheONumero

class GameMenuDialog(wx.Dialog):
    def __init__(self, parent, id=-1, title="Menu de Jogos"):
        super(GameMenuDialog, self).__init__(parent, id, title, size=(300, 200))
        self.InitUI()
    
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        title = wx.StaticText(self, label="Selecione um jogo")
        vbox.Add(title, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        self.btnParImpar = wx.Button(self, label="Par ou Ímpar")
        vbox.Add(self.btnParImpar, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.btnAdivinheNumero = wx.Button(self, label="Adivinhe o Número")
        vbox.Add(self.btnAdivinheNumero, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        self.btnClose = wx.Button(self, label="Fechar")
        vbox.Add(self.btnClose, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP | wx.BOTTOM, border=10)
        self.SetSizer(vbox)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def script_init(self, gesture):
        self.tocarSom()
        wx.CallLater(8600, lambda: self.mostrarMenu())

    def mostrarMenu(self):
        self.dialog = GameMenuDialog(None)
        self.dialog.btnParImpar.Bind(wx.EVT_BUTTON, self.iniciar_jogo_par_ou_impar)
        self.dialog.btnAdivinheNumero.Bind(wx.EVT_BUTTON, self.iniciar_jogo_adivinhe_o_numero)
        self.dialog.btnClose.Bind(wx.EVT_BUTTON, self.fechar_menu)
        self.dialog.ShowModal()

    def iniciar_jogo_par_ou_impar(self, event):
        self.pararSom()
        self.dialog.Destroy()
        jogo = parOrImpar.ParOrImpar()
        jogo.script_init(None)

    def iniciar_jogo_adivinhe_o_numero(self, event):
        self.pararSom()
        self.dialog.Destroy()
        jogo = adivinheONumero.AdivinheONumero()
        jogo.script_init(None)

    def fechar_menu(self, event):
        self.pararSom()
        self.dialog.Destroy()

    def tocarSom(self):
        caminho_som = os.path.join(os.path.dirname(__file__), "sounds", "bem vindo ao blind game.wav")
        try:
            winsound.PlaySound(caminho_som, winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print(f"Erro ao reproduzir o som: {e}")

    def pararSom(self):
        winsound.PlaySound(None, winsound.SND_ASYNC)

    __gestures = {
        "kb:NVDA+shift+J": "init"
    }
