from abc import ABC, abstractmethod

from sqlmodel import Session, SQLModel, select


class Properties(ABC):
    """Abstract class for required Properties"""

    @property
    def model():
        raise NotImplementedError("Model property doesn't exist")


class BaseRetrieve(Properties, ABC):
    """Abstract class for Retrieve Service"""

    @abstractmethod
    def get(self):
        raise NotImplementedError("Get method not implemented")


class BaseCreate(Properties, ABC):
    """Abstract class for Create Service"""

    @abstractmethod
    def create(self):
        raise NotImplementedError("Create method not implemented")


class BaseUpdate(Properties, ABC):
    """Abstract class for Update Service"""

    @abstractmethod
    def update(self):
        raise NotImplementedError("Update method not implemented")


class BaseDelete(Properties, ABC):
    """Abstract class for Delete Service"""

    @abstractmethod
    def delete(self):
        raise NotImplementedError("Delete method not implemented")


class RetrieveService(BaseRetrieve):
    """Base retrieve service"""

    model: SQLModel = SQLModel

    def get(self, session: Session, filter: dict) -> list[SQLModel]:
        return session.exec(select(self.model).filter_by(**filter)).all()


class CreateService(BaseCreate):
    """Base create service"""

    model: SQLModel = SQLModel

    def create(self, session: Session, data: SQLModel) -> SQLModel:
        self.model.model_validate(data)
        session.add(data)
        session.commit()
        session.refresh(data)
        return data


class UpdateService(BaseUpdate):
    """Base update service"""

    model: SQLModel = SQLModel

    def update(self, session: Session, filters: dict, data: SQLModel) -> SQLModel:
        self.model.model_validate(data)
        db_data = session.exec(select(self.model).filter_by(**filters)).first()

        data = data.model_dump(exclude_unset=True)
        db_data.sqlmodel_update(data)

        session.add(db_data)
        session.commit()
        session.refresh(db_data)
        return db_data


class DeleteService(BaseDelete):
    """Base delete service"""

    model: SQLModel = SQLModel

    def delete(self, session: Session, filters: dict):
        db_data = session.exec(select(self.model).filter_by(**filters)).first()
        session.delete(db_data)
        session.commit()
