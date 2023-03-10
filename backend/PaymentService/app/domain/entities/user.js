export class User {
    #user_id
    #name
    #balance

    constructor(user_id, name, balance){
        this.#user_id       = user_id;
        this.#name          = name;
        this.#balance       = balance;
    }

    getId() {
        return this.#user_id;
    }

    getName() {
        return this.#name;
    }

    getBalance(){
        return this.#balance;
    }

    addMoney(amount){
        this.#balance += amount;
    }
}