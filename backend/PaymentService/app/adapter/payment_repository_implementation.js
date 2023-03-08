import { PaymentRepository } from "../domain/repositories/payment_repository.js";
import { OrderRepositoryGrpc } from "../adapter/order_repository_grpc.js";
import { ProductRepositoryGrpc } from "../adapter/product_repository_grpc.js";
import { json_to_order } from "../parser/order_parser.js";
import { json_to_product } from "../parser/product_parser.js";
import { instance as user_repository } from "./user_repository_implementation.js";

export class PaymentRepositoryImplementation extends PaymentRepository {
    #order_repository
    #product_repository

    constructor() {
        super();
        
        this.#order_repository = new OrderRepositoryGrpc()
        this.#product_repository = new ProductRepositoryGrpc()
    }

    payOrder(payment, callback){
        // 1. Get order
        // 2. Get order product
        // 3. Get user
        // 4. Verify if user is able to pay
        // 5. Verify if theres is enough stock
        // 6. Complete order
        
        // Is a reference to the class PaymentRepository
        const that = this;

        that.#order_repository.get(payment.getOrderId(), function(err, data) {
            if (err) {
                console.log(err);
            } else {
                const order = json_to_order(data);

                that.#product_repository.get(order.getProductId(), function(err, data) {
                    if (err) {
                        console.log(err);
                    } else {
                        const product = json_to_product(data);

                        const user = user_repository.getUser(payment.getUserId());
                        if (user != null){
                            
                            // Verify if user is able to pay
                            if(user.getBalance() >= product.getPrice() * order.getAmount()) {
                                // User is able to pay
                                // Verify if there is enough stock
                                if(product.getStock() - order.getAmount() >= 0){
                                    // There is enough stock
                                    // Complete order and change product
        
                                    that.#order_repository.complete(order.getId(), function(err, data) {
                                        if (err) {
                                            console.log(err);
                                            callback(null, {
                                                "is_successful" : false,
                                                "message" : "There was an error completing the transaction"
                                            });
                                        } else {
                                            callback(null, {
                                                "is_successful" : true,
                                                "message" : "Transaction completed!"
                                            });
                                        }
                                    })
                                } else {
                                    callback(null, {
                                        "is_successful" : false,
                                        "message" : "There is no enough stock!"
                                    });
                                }
                            } else {
                                callback(null, {
                                    "is_successful" : false,
                                    "message" : "User doesn't have enough money"
                                });
                            }
                        }
                    }
                });
            }
        });    
    }
}