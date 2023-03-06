import { PaymentRepository } from "../domain/repositories/payment_repository.js";

export class PaymentRepositoryImplementation extends PaymentRepository {
    constructor() {
        super();
    }

    payOrder(payment){
        console.log(payment);
    }
}