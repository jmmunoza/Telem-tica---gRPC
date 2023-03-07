import { OrderRepository } from "../domain/repositories/order_repository.js";
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

export class OrderRepositoryGrpc extends OrderRepository {
    #client

    constructor() {
        super();

        const ORDER_MANAGEMENT_SERVICE_PROTO   = process.env.ORDER_MANAGEMENT_SERVICE_PROTO;
        const ORDER_MANAGEMENT_SERVICE_ADDRESS = process.env.ORDER_MANAGEMENT_SERVICE_ADDRESS;

        const package_definition = protoLoader.loadSync(
            ORDER_MANAGEMENT_SERVICE_PROTO, {
                keepCase: true,
                longs: String,
                enums: String,
                defaults: true,
                oneofs: true
        });

        const inventory_service = grpc.loadPackageDefinition(package_definition).InventoryService;
        this.#client = new inventory_service(ORDER_MANAGEMENT_SERVICE_ADDRESS, grpc.credentials.createInsecure());
    }

    get(order_id){
        this.#client.get(order, (err, data) => {
            console.log(data)
            if (err) {
                console.log(err);
            } else {
                console.log('Response received from remote service:', data); 
            }
        });
    }
}