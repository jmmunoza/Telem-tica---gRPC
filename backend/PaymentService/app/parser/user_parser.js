export function user_to_json(user) {
    console.log(user);
    console.log(user.getId());

    return {
        "user_id" : user.getId(),
        "name" : user.getName(),
        "balance" : user.getBalance()
    }
}