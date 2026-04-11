from ..core.service import (CreateService, DeleteService, RetrieveService,
                            UpdateService)
from .models import Address


class AddressService(CreateService, RetrieveService, UpdateService, DeleteService):
    """Address service with CRUD functionalities"""

    model = Address
