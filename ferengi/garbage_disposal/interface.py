"""Interface to the AHA web scraper."""

from typing import Iterator

from aha import LocationNotFound, AhaDisposalClient, PickupSolution
from mdb import Address

from ferengi.garbage_disposal.config import LOGGER
from ferengi.garbage_disposal.exceptions import NoInformation


__all__ = ['get_disposals']


def get_disposals(address: Address) -> Iterator[PickupSolution]:
    """Returns the respective disposal dictionary."""

    aha_client = AhaDisposalClient(district=address.city or 'Hannover')

    try:
        for pickup_solution in aha_client.by_address(address):
            yield pickup_solution
    except LocationNotFound as location_not_found:
        LOGGER.warning('Location not found: %s.', location_not_found)
        raise NoInformation() from None
