import { Payment } from '../domain/entities/payment.js'

export function json_to_payment(json) {
    return new Payment(
        json['order_id'],
        json['user_id'],
        json['amount']
    )
}