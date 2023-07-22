import requests

from config import ELECCIONES_PASSWORD, ELECCIONES_USER
from elecciones.types import ELECCIONES_23J_ENDPOINT, GRANADA, Actions, Type


def get_last_advance(election_type: Type):
    print("Fetching advance for:", election_type.name)

    url = f"{ELECCIONES_23J_ENDPOINT}/{Actions.GET_ENVIO.value}/{election_type.value}"

    response = requests.get(url, auth=(ELECCIONES_USER, ELECCIONES_PASSWORD))
    response.raise_for_status()

    return response.text


def get_participation(advance: str):
    print("Fetching participation for:", advance)

    url = f"{ELECCIONES_23J_ENDPOINT}/{Actions.GET_AVANCES_MUNICIPIOS.value}/{Type.CONGRESO.value}/{GRANADA}/{advance}"

    response = requests.get(url, auth=(ELECCIONES_USER, ELECCIONES_PASSWORD))
    response.raise_for_status()

    return response.text


def get_results(election_type: Type, advance: str):
    print("Fetching results for:", election_type.name, advance)

    url = (
        f"{ELECCIONES_23J_ENDPOINT}/{Actions.GET_ESCRUTINIO_MUNICIPIOS.value}/"
        f"{election_type.value}/{GRANADA}/{advance}"
    )

    response = requests.get(url, auth=(ELECCIONES_USER, ELECCIONES_PASSWORD))
    response.raise_for_status()

    return response.text
