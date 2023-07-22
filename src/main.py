from elecciones.types import Type, ValuesTypes
from elecciones.utils import get_last_advance, get_participation, get_results


def fetch_congress_data():
    last_advance = get_last_advance(election_type=Type.CONGRESO)
    return {
        ValuesTypes.LAST_ADVANCE: last_advance,
        ValuesTypes.PARTICIPATION: get_participation(advance=last_advance),
        ValuesTypes.RESULTS: get_results(
            election_type=Type.CONGRESO, advance=last_advance
        ),
    }


def fetch_senate_data():
    last_advance = get_last_advance(election_type=Type.SENADO)
    return {
        ValuesTypes.LAST_ADVANCE: last_advance,
        ValuesTypes.RESULTS: get_results(
            election_type=Type.SENADO, advance=last_advance
        ),
    }


def loop():
    fetch_congress_data()
    fetch_senate_data()


loop()
