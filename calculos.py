def promedio_disparo(disparos):
  total = 0
  for x in disparos:
    total += x
  resultado = round(total /len(disparos), 2)
  return resultado

def mejor_disparo(disparo):  
  mejor_disparo = min(disparo) 
  return mejor_disparo

