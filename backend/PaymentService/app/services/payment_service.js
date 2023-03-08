import { PaymentRepositoryImplementation } from "../adapter/payment_repository_implementation.js";
import { instance as user_repository } from "../adapter/user_repository_implementation.js";
import { json_to_payment } from "../parser/payment_parser.js";
import { user_to_json } from "../parser/user_parser.js";

const payment_repository = new PaymentRepositoryImplementation();


export const PaymentService = function() {
    
}

PaymentService.payOrder = function(call, callback) {
    console.log("payorder " + call.request);
    const payment = json_to_payment(call.request);
    payment_repository.payOrder(payment, callback);
}

PaymentService.addMoney = function(call, callback) {
    console.log("addmoney " + call.request);
    const user_id = call.request["user_id"];
    const amount  = call.request["amount"];
    const is_sucessful = user_repository.addMoney(user_id, amount);
    if(is_sucessful){
        callback(null, {
            "is_sucessful" : true,
            "message" : "Money added successfully"
        })
    } else {
        callback(null, {
            "is_sucessful" : false,
            "message" : "There was an error"
        })
    }
}

PaymentService.createUser = function(call, callback) {
    console.log("createuser " + call.request);
    const name = call.request["name"];
    const user = user_repository.createUser(name);
    const user_json = user_to_json(user);
    callback(null, user_json);
}

PaymentService.getUser = function(call, callback) {
    console.log("getuser " + call.request);
    const user_id = call.request["user_id"];
    const user = user_repository.getUser(user_id);
    const user_json = user_to_json(user);
    callback(null, user_json);
}
