export class ProductRepository {
	constructor() {
		// It's to force the dev to include the methods
		// Trying to simulate a Interface

		if (!this.get) {
			throw new Error("get() method is missing");
		}
	}
}