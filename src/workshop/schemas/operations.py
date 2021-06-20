from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBaseSchema(BaseModel):
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]


class OperationSchema(OperationBaseSchema):
    id: int

    class Config:
        orm_mode = True


class OperationCreateSchema(OperationBaseSchema):
    pass


class OperationUpdateSchema(OperationBaseSchema):
    pass
