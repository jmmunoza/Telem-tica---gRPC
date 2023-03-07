import { UserRepository } from "../domain/repositories/user_repository.js";

export class UserRepositoryImplementation extends UserRepository {
    constructor() {
        super();
    }

    createUser(name){
        console.log(name);
    }

    addMoney(user_id, amount){
        console.log(user_id);
        console.log(amount);
    }
}