class User {
	#product_id
	#amount
	#order_id

	constructor(order_id, product_id, amount) {
		this.#product_id = product_id;
		this.#order_id = order_id;
		this.#amount = amount;
	}

	getId() {
		return this.#order_id;
	}

	getProductId() {
		return this.#product_id;
	}

	getAmount() {
		return this.#amount;
	}
}