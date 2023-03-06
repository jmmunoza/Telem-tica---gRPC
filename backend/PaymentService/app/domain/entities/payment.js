class Payment {
    #order_id
    #amount
    #customer_name

    constructor(order_id, amount, customer_name){
        this.#order_id      = order_id;
        this.#amount        = amount;
        this.#customer_name = customer_name;
    }

    getOrderId() {
        return this.#order_id;
    }

    getAmount() {
        return this.#amount;
    }

    getCustomerName(){
        return this.#customer_name;
    }
}