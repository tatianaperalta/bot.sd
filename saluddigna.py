import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

data = pd.read_csv("candidatos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['Whatsapp']
candidatos = data_dict['Candidato']
consultores = data_dict['Consultor']

combo = zip(celulares,candidatos,consultores)
first = True
for celulares,candidatos,consultores in combo:
    time.sleep(2)
    web.open("https://web.whatsapp.com/send?phone=" + celulares)
    if first:
        time.sleep(5)
    time.sleep(5)
    pg.typewrite('Hola ' + candidatos + ', ' + '¿como estas? \n')
    pg.typewrite('Soy ' + consultores +' consultora de Page Group, una firma de reclutamiento especializado.\n')
    pg.typewrite('Te escribo ya que actualmente tengo una posición la cual creo que podría llamarte la atención. Por esta misma razón me gustaría poder platicar contigo.\n')
    pg.typewrite('La vacante es como Tecnico Radiologo para la empresa Salud Digna.\n' 'Ofrecemos un salario competitivo + prestaciones superiores+ Bono de reubicación si lo requiere el candidato.\n')
    pg.typewrite('Si te interesa por favor compárteme tu CV y una hora a la que podamos conversar.\n' + 'Saludos !')
    pg.press('enter')
    time.sleep(5)
    pg.hotkey('ctrl', 'w')
    time.sleep(5)