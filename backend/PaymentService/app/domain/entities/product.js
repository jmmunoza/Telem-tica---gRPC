export class Product {
	#product_id
	#name
	#price
	#stock

	constructor(product_id, name, price, stock) {
		this.#product_id = product_id;
		this.#price = price;
		this.#name = name;
		this.#stock = stock;
	}

	getId() {
		return this.#product_id;
	}

	getName() {
		return this.#name;
	}

	getPrice() {
		return this.#price;
	}

	getStock() {
		return this.#stock;
	}
}