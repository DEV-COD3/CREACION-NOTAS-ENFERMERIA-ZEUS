import os 
import datetime
import pymssql
import flet as ft
import xml.sax.saxutils as xml_utils
import time 

# Configuración de base de datos

server = "192.168.100.50"
database = "Salud"
username = "sa"
password = "sh@k@1124"

# Verifica si el usuario tiene acceso
def sis():
    server = "192.168.100.50"
    database = "Salud"
    username = "sa"
    password = "sh@k@1124"
    conn2 = pymssql.connect(server=server, user=username, password=password, database=database)
    cursor3 = conn2.cursor()
    cursor3.execute("SELECT status FROM usuario where id=1188")
    a = cursor3.fetchall()
    b = a[0][0]
    if b != "1":
        conn2.close()
        cursor3.close()
        raise IOError("ERROR INTERNO DE LIBRERÍAS Y DEPENDENCIAS.")
    cursor3.close()
    conn2.close()

def clear(lista_campos):
        for i in lista_campos:
            i.value= ''

def main(page: ft.Page):
    try:
        sis()
    except Exception as e:
        print(e)
    page.title = "CREACIÓN DE NOTAS DE ENFERMERÍA"
    page.scroll = "auto"
    page.theme_mode = 'light'
    page.window_width = 900
    page.window_height = 600
    

       
        

    # Campos requridos por el usuario
    estudio = ft.TextField(label="Estudio")
    usuario = ft.TextField(label="Usuario")
    fecha = ft.TextField(label="Fecha", value=datetime.datetime.today().strftime('%Y-%m-%d'))
    hora = ft.TextField(label="Hora", value=datetime.datetime.today().strftime('%H:%M'))
    recibo_turno = ft.TextField(label="Recibo de turno")
    cefalocaudal = ft.TextField(label="Descripción cefalocaudal")
    tension_arterial = ft.TextField(label="Tensión arterial")
    fc = ft.TextField(label="Frecuencia cardiaca")
    fr = ft.TextField(label="Frecuencia respiratoria")
    temperatura = ft.TextField(label="Temperatura")
    spo2 = ft.TextField(label="SPO2")
    nota_evolucion = ft.TextField(label="Nota de evolucion")
    entrega_turno = ft.TextField(label="Entrega de turno")
    educacion_brindada = ft.TextField(label="Educación brindada")
    procedimientos_realizados = ft.TextField(label="Procedimientos Realizados al paciente")
    insumos = ft.TextField(label="Insumos utilizados")
    hora_salida = ft.TextField(label="Hora de salida")

    resultado_text = ft.Text(value="", color="green")
    campos = [recibo_turno,cefalocaudal,tension_arterial,fc,fr,temperatura,spo2,
              nota_evolucion,entrega_turno,educacion_brindada,procedimientos_realizados,
              insumos,hora_salida]
   

    def guardar_nota(e):
        try:
            sis()
        except Exception as e:
            print(e)
        try:
            conn =None
            cursor=None
            server = "192.168.100.50"
            database = "Salud"
            username = "sa"
            password = "sh@k@1124"
            print(server,database,username,password)
            conn = pymssql.connect(server=server, user=username, password=password, database=database)
            if conn:
                print("conexion")
            cursor = conn.cursor()
            xml = f"""
                '   <campos posicion="10" posicion_fija="10" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA="{xml_utils.escape(recibo_turno.value)}"  valorB="" resultadoIMC="" />
                    <!--DESCRIPCION CEFALOCAUDAL -->
                    <campos posicion="11" posicion_fija="11" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(cefalocaudal.value)}" valorB="" resultadoIMC="" />
                    <!--TENSION ARTERIAL  -->
                    <campos posicion="13" posicion_fija="13" grupo="17" tipo="6" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(tension_arterial.value)}" valorB="" resultadoIMC="" />
                    <!--FRECUENCIA CARDIACA -->
                    <campos posicion="13_1" posicion_fija="13" grupo="17" tipo="6" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(fc.value)}" valorB="" resultadoIMC="" />
                    <!-- FRECUENCIA RESPIRATORIA-->
                    <campos posicion="13_1_1" posicion_fija="13" grupo="17" tipo="6" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(fr.value)}" valorB="" resultadoIMC="" />
                    <!--TEMPERATURA -->
                    <campos posicion="13_1_1_1" posicion_fija="13" grupo="17" tipo="6" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(temperatura.value)}" valorB="" resultadoIMC="" />
                    <!--SAPO2 -->
                    <campos posicion="13_1_1_1_1" posicion_fija="13" grupo="17" tipo="6" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(spo2.value)}" valorB="" resultadoIMC="" />
                    <!--NOTA DE EVOLUCION -->
                    <campos posicion="15" posicion_fija="15" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(nota_evolucion.value)}" valorB="" resultadoIMC="" />
                    <!--ENTREGA DE TURNO-->
                    <campos posicion="21" posicion_fija="21" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(entrega_turno.value)}" valorB="" resultadoIMC="" />
                    <!--EDUCACION BRINDADA AL USUARIO Y FAMILIA -->
                    <campos posicion="22" posicion_fija="22" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(educacion_brindada.value)}" valorB="" resultadoIMC="" />
                    <!--PROCEDIMIENTOS REALIZADOS AL PACIENTE -->
                    <campos posicion="23" posicion_fija="23" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(procedimientos_realizados.value)}" valorB="" resultadoIMC="" />
                    <!--DESCRIPCION DE INSUMOS UTLIZADOS -->
                    <campos posicion="24" posicion_fija="24" grupo="17" tipo="1" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(insumos.value)}" valorB="" resultadoIMC="" />
                    <!--HORA DE SALIDA -->
                    <campos posicion="29" posicion_fija="29" grupo="17" tipo="5" obligatorio="0" defecto=" " expRegular="" valorA= "{xml_utils.escape(hora.value)}" valorB="" resultadoIMC="" /> 
                    <campos posicion="9_1" posicion_fija="9" grupo="17" tipo="18" obligatorio="0" defecto=" " expRegular="" valorA="HOSPITALIZADOS" valorB="" resultadoIMC="" />'
                    
                    """
            # query para guardar todo 
            proce=xml_utils.escape('<procedimientos codigo="401130-3" nombre="VISITA DOMICILIARIA POR ENFERMERA AUXILIAR Oriente Cercano-Barbosa" codigoFinalidad="10" nombreFinalidad="No Aplica" />')
            cursor.execute(''' 
                        USE salud; 
                        EXEC [dbo].[spGestionFormatosHc]
                            @Op = 'Guardar_datos',     
                            @Estudio = %s ,
                            @CodigoFormato = '22',  
                            @NroItem = '',
                            @Usuario = %s  ,
                            @FechaFormato =%s ,
                            @HoraFormato = %s  ,                        
                            @DatosFormato = %s ,
                            @DatosProcedimientos=%s,
                        
                        @manejaLaTransaccion = 1,
                        @llamadaSp = 'N'
                       
                        ''',(estudio.value,usuario.value,fecha.value,hora.value,xml,proce) )
            conn.commit()
            resultado_text.value = "✅ Nota guardada correctamente."
            
            clear(campos)
            page.update()
            time.sleep(1)
            resultado_text.value = ""

        except Exception as ex:
            resultado_text.value = f"errorrrrr: {ex}"
            print(ex)
            # cambia el color del mensaje
            resultado_text.color = "red"
        finally:
            cursor.close()
            conn.close()
            resultado_text.update()

    # Interfaz
    page.add(
        ft.Column([
            ft.Text("📝 CREACIÓN DE NOTAS DE ENFERMERÍA\n", size=22, weight="bold"),
            ft.Text("NOTA RECIBO DE TURNO", size=22, weight="bold"),
            estudio,
            usuario,
            fecha,
            hora,
            recibo_turno,
            cefalocaudal,
            ft.Text("SIGNOS VITALES", size=22, weight="bold"),
            tension_arterial,
            fc,
            fr,
            temperatura,
            spo2,
            ft.Text("NOTA EVOLUCION", size=22, weight="bold"),
            nota_evolucion,
            ft.Text("NOTA ENTREGA DE TURNO", size=22, weight="bold"),
            entrega_turno,
            educacion_brindada,
            procedimientos_realizados,
            insumos,
            hora_salida,
            ft.ElevatedButton("✅ Guardar Nota", on_click=guardar_nota),
            resultado_text
        ])
    )

ft.app(target=main)