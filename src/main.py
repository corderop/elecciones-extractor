from elecciones.types import Type, ValuesTypes
from elecciones.utils import get_last_advance, get_participation, get_results
from gsheet.tools import send_information_to_gsheet
from gsheet.types import SheetTypes


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
    congress_data = fetch_congress_data()
    senate_data = fetch_senate_data()

    send_information_to_gsheet(
        sheet_name=SheetTypes.CONGRESO_AVANCES,
        data=congress_data[ValuesTypes.PARTICIPATION],
    )
    send_information_to_gsheet(
        sheet_name=SheetTypes.CONGRESO_RESULTADOS,
        data=congress_data[ValuesTypes.RESULTS],
    )
    send_information_to_gsheet(
        sheet_name=SheetTypes.SENADO_RESULTADOS,
        data=senate_data[ValuesTypes.RESULTS],
    )


loop()
