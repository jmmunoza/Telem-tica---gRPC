import { PaymentRepositoryImplementation } from "../adapter/payment_repository_implementation.js";

export class PaymentService {
    #payment_repository

    constructor() {
        this.#payment_repository = new PaymentRepositoryImplementation();
    }

    payOrder(call, callback) {
        console.log(call);
    }

    addMoney(call, callback) {
        console.log(call);
    }

    createUser(call, callback) {
        console.log(call);
    }
}