from ..core.service import (
    CreateService,
    RetrieveService,
    UpdateService,
    DeleteService,
)
from .models import Address


class AddressService(CreateService, RetrieveService, UpdateService, DeleteService):
    """Address service with CRUD functionalities"""

    model = Address
