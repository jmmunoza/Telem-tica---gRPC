import { UserRepository } from "../domain/repositories/user_repository.js";
import { User } from "../domain/entities/user.js"
import { v4 as uuidv4 } from 'uuid';

class UserRepositoryImplementation extends UserRepository {
    #users

    constructor() {
        super();
        this.#users = []
    }

    createUser(name) {
        const user_id = uuidv4();
        const new_user = new User(user_id, name, 0.0);
        this.#users.push(new_user);

        return new_user;
    }

    addMoney(user_id, amount) {
        var is_sucessful = false;

        if (amount >= 0) {
            this.#users.forEach(function (user) {
                if (user.getId() == user_id) {
                    user.addMoney(amount);
                    console.log(user.getBalance());
                    is_sucessful = true;
                }
            });
        }

        return is_sucessful;
    }

    getUser(user_id) {
        var user_to_find = null;

        this.#users.forEach(function (user) {
            if (user.getId() == user_id) {
                user_to_find = user;
            }
        });

        return user_to_find;
    }
}

export const instance = new UserRepositoryImplementation();