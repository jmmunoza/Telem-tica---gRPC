import { Order } from '../domain/entities/order.js'

export function json_to_order(json) {
    return new Order(
        json['order_id'],
        json['product_id'],
        json['amount']
    )
}