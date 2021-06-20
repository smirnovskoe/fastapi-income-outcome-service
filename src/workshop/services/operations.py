from typing import List, Optional

from fastapi import (
    Depends,
    HTTPException,
    status)
from sqlalchemy.orm import Session

from ..database import get_session
from ..models.operations import OperationModel
from ..schemas.operations import OperationKind, OperationCreateSchema, OperationUpdateSchema


# logic

class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> OperationModel:
        operation = self.session.query(OperationModel).filter_by(id=operation_id).first()

        if not operation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
            )

        return operation

    def get_list(self, kind: Optional[OperationKind] = None) -> List[OperationModel]:
        query = self.session.query(OperationModel)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def get(self, operation_id: int) -> OperationModel:
        return self._get(operation_id)

    def create(self, operation_data: OperationCreateSchema) -> OperationModel:
        operation = OperationModel(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdateSchema) -> OperationModel:
        operation = self._get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()

