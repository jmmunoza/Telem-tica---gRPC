export class PaymentRepository {
    constructor() {
        // It's to force the dev to include the methods
        // Trying to simulate a Interface

        if(!this.payOrder) {
            throw new Error("payOrder() method is missing");
        }
    }
}