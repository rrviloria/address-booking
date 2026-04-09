from ..core.service import CreateService
from .models import User


class UserService(CreateService):
    """User service with only create functionality
    """
    model = User
