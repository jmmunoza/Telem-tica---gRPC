export class UserRepository {
    constructor() {
        // It's to force the dev to include the methods
        // Trying to simulate a Interface

        if(!this.createUser) {
            throw new Error("createUser() method is missing");
        }

        if(!this.addMoney) {
            throw new Error("addMoney() method is missing");
        }
    }
}