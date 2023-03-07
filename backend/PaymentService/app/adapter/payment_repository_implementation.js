import { PaymentRepository } from "../domain/repositories/payment_repository.js";

export class PaymentRepositoryImplementation extends PaymentRepository {
    constructor() {
        super();
    }

    payOrder(payment){
        console.log(payment);
        // 1. Get order
        // 2. Get order product
        // 3. Get user
        // 4. Verify if user is able to pay
        // 5. Verify if theres is enough stock
        // 6. Complete order
        
        // Falta implementar los metodos de update en inventory 
        // Falta conectar paymentservice con inventory
        // Falta implementar el get order
        // Falta implementar el productrepository grpc, order repository grpc, los repositories.

    }
}