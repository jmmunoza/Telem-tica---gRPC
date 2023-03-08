import { Product } from '../domain/entities/product.js'

export function json_to_product(json) {
    return new Product(
        json['product_id'],
        json['name'],
        json['stock'],
        json['price']
    )
}