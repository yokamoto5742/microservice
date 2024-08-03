from datetime import datetime
from enum import Enum
from typing import List, Any
from uuid import UUID

from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing_extensions import Annotated


class Size(Enum):
    small = 'small'
    medium = 'medium'
    big = 'big'


class StatusEnum(Enum):
    created = 'created'
    paid = 'paid'
    progress = 'progress'
    cancelled = 'cancelled'
    dispatched = 'dispatched'
    delivered = 'delivered'


class OrderItemSchema(BaseModel):
    product: str
    size: Size
    quantity: Annotated[int, Field(ge=1, strict=True)] = 1

    model_config = ConfigDict(extra='forbid', strict=True)

    @field_validator('quantity')
    @classmethod
    def quantity_non_nullable(cls, value: Any) -> Any:
        assert value is not None, 'quantity may not be None'
        return value


class CreateOrderSchema(BaseModel):
    order: Annotated[List[OrderItemSchema], Field(min_length=1)]

    model_config = ConfigDict(extra='forbid', strict=True)


class GetOrderSchema(BaseModel):
    id: UUID
    status: StatusEnum
    created: datetime

    model_config = ConfigDict(extra='forbid', strict=True)


class GetOrdersSchema(BaseModel):
    orders: List[GetOrderSchema]

    model_config = ConfigDict(extra='forbid', strict=True)
