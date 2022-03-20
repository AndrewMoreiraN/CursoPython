from caneta import Caneta
from escritor import Escritor
from maquina_de_escrever import MaquinaDeEscrever

escritor = Escritor('Andrew')
caneta = Caneta('Bic')
maquina_de_escrever = MaquinaDeEscrever()

escritor.ferramenta = maquina_de_escrever
escritor.ferramenta.escrever()
