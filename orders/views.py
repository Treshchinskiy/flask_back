from flask_restx import Resource, Namespace,fields
from ..models.orders import Order
from http import HTTPStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models.users import User

order_namespace = Namespace('orders',description="Namespace for orders")

order_model = order_namespace.model(
    'Order',{
        'id': fields.Integer(),
        'size':fields.String(
            required=True,
            enum=['SMALL','MEDIUM','LARGE']
        ),
        'order_status':fields.String(
            required=True,
            enum=['pending','in_transit','delivered']
        )
    }
)


@order_namespace.route('/orders')
class OrderGetCreate(Resource):
    @order_namespace.marshal_with(order_model)
    @order_namespace.expect(order_model)
    def get(self):
        """
            Get all orders
        """
        orders=Order.query.all()

        return orders, HTTPStatus.OK

    @order_namespace.expect(order_model)
    @order_model.marshal_with(order_model)
    @jwt_required()
    def post(self):
        """
            Create a new order
        """
        data=order_namespace.payload

        new_order = Order(
            size=data['size'],
            quantity=data['quantity'],
            flavour=data['flavour']
        )

        username = get_jwt_identity()
        current_user = User.query.filter_by(username=username).first()
        new_order.user = current_user
        new_order.save()
    

        return data, HTTPStatus.CREATED



@order_namespace.route('/order/<int:order_id>')
class GetUpdateDelete(Resource):
    def get(self,order_id):
        '''
            Retrieve an order by id
        '''

    def put(self,order_id):
        '''
            Update an order by id
        '''

    def delete(self,order_id):
       '''
            Delete an order by id
        '''

    
@order_namespace.route('/users/<int:user_id>/order/<int:order_id>')
class GetSpecificOrderByUser(Resource):
    def get(self,user_id,order_id):
        """
            Get a specific order by user
        """
        pass


@order_namespace.route('/users/<int:user_id>/orders')
class UserOrders(Resource):
    def get(self,user_id):
        """
            Get all orders for a specific user
        """
        pass



@order_namespace.route('/order/status/<int:order_id>')
class UpdateOrderStatus(Resource):
    def patch(self,order_id):
        """
            Update an order's status
        """
        pass

    
