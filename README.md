Planteamiento del problema --> "Hay que Falsear las notas de enfermeria para poder facturarlas en las fechas que son"
  La empresa adquirio un software de tercero para manejar su gestion general (financiera y asistencial), el cual no permite mactualizacion y/o gestion libre via front
  Debido a que es del Sector Salud hubo un gran problema con los soportes que amarran a las facturas para enviar a la EPS y Efectuar cobro; esto porque las auxiliares montan los soportes a destiempo

Analisis de la solucion --> Se entendió que habia que replicar las consultas front al back
  Primero se gestionó el requerimiento a través de un formato word que debian llenar para que a traves del sqlserver se hiciera la ejecucion del mismo,
  esta solucion se descontinuo rapidamente debido al grabn volumen de soportes que habian que montar (+1100), y estos debian pasar por el area de Sistemas para efectuarse en la App
  
Implementacion Interfaz Grafica --> Se entendio que la mejor opcion era generar un aplicativo que sustituyera la presencia en SQL del area de Sistemas
  En formato sprint (2 horas de desarrollo) Se les generó una vista basica que pudiera reemplazar al area (Debido a la urgencia del requerimiento),

Actualizacion a la IGv2 --> Se mejoró la experiencia de usuario para evitar errores y facilitar la gestion del mismo
  Se procedio con la mejora de la interfaz grafica ( cambiando ortografia, limpiando campos despues de creacion de notas( a excepcion de los campos mas traumaticos de encontrar),
  limitando el mensaje comprobatorio de notas)

Se compiló, y se entregó con su respectivo SaaS.


