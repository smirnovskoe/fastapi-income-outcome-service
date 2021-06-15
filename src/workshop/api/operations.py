from typing import List, Optional

from fastapi import APIRouter, Depends

from ..schemas.operations import OperationSchema, OperationKind, OperationCreateSchema
from ..services.operations import OperationService

router = APIRouter(
    prefix='/operations',
)


# handlers

@router.get('/', response_model=List[OperationSchema])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationService = Depends()
):
    return service.get_list(kind=kind)


@router.get('/{operation_id}', response_model=OperationSchema)
def get_operation(
        operation_id: int,
        service: OperationService = Depends()
):
    return service.get(operation_id)


@router.post('/', response_model=OperationCreateSchema)
def create_operation(
        operation_data: OperationCreateSchema,
        service: OperationService = Depends()
):
    return service.create(operation_data)
