import { PaymentRepositoryImplementation } from "../adapter/payment_repository_implementation.js";
import { UserRepositoryImplementation } from "../adapter/user_repository_implementation.js";

export class PaymentService {
    #payment_repository
    #user_repository

    constructor() {
        this.#payment_repository = new PaymentRepositoryImplementation();
        this.#user_repository = new UserRepositoryImplementation();
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