from enum import Enum

ELECCIONES_23J_ENDPOINT = "https://descargas.generales23j.es/descargas/csv/data"

GRANADA = "18"


class Type(Enum):
    CONGRESO = "2"
    SENADO = "3"


class Actions(Enum):
    GET_ENVIO = "getEnvio"
    GET_AVANCES_MUNICIPIOS = "getAvancesMunicipios"
    GET_ESCRUTINIO_MUNICIPIOS = "getEscrutinioMunicipios"


class ValuesTypes(Enum):
    LAST_ADVANCE = "last_advance"
    PARTICIPATION = "participation"
    RESULTS = "results"
