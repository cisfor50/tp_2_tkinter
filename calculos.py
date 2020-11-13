def promedioDisparo(x,y,z):
  resultado = (x + y + z) /3
  resultado = round(resultado, 2)
  return resultado

def mejorDisparo(disparo):
  
  auxMejorDisparo = min(disparo) #Menor número == más cercano al origen del plano.
  return auxMejorDisparo

