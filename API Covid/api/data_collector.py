import pandas as pd
from sodapy import Socrata


def consulta_datos(limite, Departamento):
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr",limit = limite, departamento= Departamento)
    results_df = pd.DataFrame.from_records(results,columns=['ciudad_de_ubicaci_n','departamento','edad','tipo','estado','pa_s_de_procedencia'])
    return results_df

