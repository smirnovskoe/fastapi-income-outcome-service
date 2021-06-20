from typing import List, Optional

from fastapi import APIRouter, Depends, Response, status

from ..schemas.operations import OperationSchema, OperationKind, OperationCreateSchema, OperationUpdateSchema
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


@router.put('/{operation_id}', response_model=OperationSchema)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdateSchema,
        service: OperationService = Depends()
):
    return service.update(
        operation_id,
        operation_data
    )


@router.delete('/{operation_id}')
def update_operation(
        operation_id: int,
        service: OperationService = Depends()
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
