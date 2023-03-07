import { UserRepository } from "../domain/repositories/user_repository.js";
import { User } from "../domain/entities/user.js"
import { v4 as uuidv4 } from 'uuid';

export class UserRepositoryImplementation extends UserRepository {
    #users

    constructor() {
        super();
        this.#users = []
    }

    createUser(name){
        const user_id  = uuidv4();
        const new_user = new User(user_id, name, 0.0);
        this.#users.push(new_user);
        
        return true;
    }

    addMoney(user_id, amount){
        if(amount >= 0) {
            this.#users.forEach(function (user) {
                if(user.getId() == user_id){
                    user.addMoney(amount);
                    return true;
                }
            });
        }

        return false;
    }
}