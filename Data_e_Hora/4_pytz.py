#COMANDO PARA INSTALAR A BIBLIOTECA DE TERCEIRO PYTZ DIGITANDO NO TERMINAL: pip install pytz
#MANIPULANDO DATAS COM DIVERSOS FUSOS HORÁRIOS
import pytz
from datetime import datetime


data = datetime.now(pytz.timezone("Europe/Oslo"))
print(data)
