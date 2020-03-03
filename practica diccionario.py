newdict={"Personas":[
         {"Name":"Francisco",
          "Age":"12",
          },
         {"Name":"Federico",
          "Age":"25",
          }]
}
#se necesita crear una lista para anidar diccionarios
print("edad: ", newdict['Personas'][1]["Age"])
#accede al diccionario "personas" y al primer valor( en este caso, francisco y su edad)
#finalmente, se solicita el nombre del primer valor