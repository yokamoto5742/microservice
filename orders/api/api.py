import uuid
from datetime import datetime
from http import HTTPStatus
from uuid import UUID

from fastapi import HTTPException
from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import CreateOrderSchema, GetOrderSchema, GetOrdersSchema

ORDERS =[]


@app.get('/orders', response_model=GetOrdersSchema)
def get_orders():
    return {'orders': [ORDERS]}


@app.post('/orders', status_code=status.HTTP_201_CREATED, response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    order = order_details.dict()
    order['id'] = uuid.uuid4()
    order['created'] = datetime.utcnow()
    order['status'] = 'created'
    ORDERS.append(order)
    return order


@app.get('/orders/{order_id}', response_model=GetOrderSchema)
def get_order(order_id: UUID):
    for order in ORDERS:
        if order['id'] == order_id:
            return order
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value, detail=f'Order with ID {order_id} not found')


@app.put('/orders/{order_id}', response_model=GetOrderSchema)
def update_order(order_id: UUID, order_details: CreateOrderSchema):
    for order in ORDERS:
        if order['id'] == order_id:
            order.update(order_details.dict())
            return order
    raise HTTPException(status_code=HTTPStatus.NOT_FOUND.value, detail=f'Order with ID {order_id} not found')


@app.delete('/orders/{order_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
def delete_order(order_id: UUID):
    return Response(status_code=HTTPStatus.NO_CONTENT.value)


@app.post('/orders/{order_id}/cancel')
def cancel_order(order_id: UUID):
    return orders


@app.post('/orders/{order_id}/pay')
def pay_order(order_id: UUID):
    return orders
