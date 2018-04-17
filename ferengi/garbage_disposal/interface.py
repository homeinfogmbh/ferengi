"""Interface to the AHA web scraper."""

from aha import LocationNotFound, AhaDisposalClient

from ferengi.garbage_disposal.config import LOGGER
from ferengi.garbage_disposal.exceptions import NoInformation


def _fix_street(street):
    """Fixes the street name."""

    street = street.replace('str.', 'straße')
    return street.replace('Str.', 'Straße')


def get_dispsal(address):
    """Returns the respective disposal dictionary."""

    aha_client = AhaDisposalClient(district=address.city or 'Hannover')

    try:
        pickup_information = aha_client.by_address(
            _fix_street(address.street), address.house_number)
    except LocationNotFound as location_not_found:
        LOGGER.warning('Location not found: %s.', location_not_found)
        raise NoInformation()

    if pickup_information is None:
        LOGGER.warning('No disposal information for address: %s.', address)
        raise NoInformation()

    return pickup_information.to_dict()
