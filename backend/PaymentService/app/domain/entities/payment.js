class Payment {
    #order_id
    #amount
    #user_id

    constructor(order_id, user_id, amount){
        this.#order_id      = order_id;
        this.#amount        = amount;
        this.#user_id       = user_id;
    }

    getOrderId() {
        return this.#order_id;
    }

    getAmount() {
        return this.#amount;
    }

    getUserId(){
        return this.#user_id;
    }
}