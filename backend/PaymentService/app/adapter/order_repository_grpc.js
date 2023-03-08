import { OrderRepository } from "../domain/repositories/order_repository.js";
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import dotenv      from 'dotenv';

dotenv.config();

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

        const proto_descriptor = grpc.loadPackageDefinition(package_definition).OrderManagementService;
        this.#client = new proto_descriptor(ORDER_MANAGEMENT_SERVICE_ADDRESS, grpc.credentials.createInsecure());
    }

    
    get(order_id, callback){
        this.#client.get({"order_id": order_id}, (err, data) => {
            callback(err, data);
        });
    }

    complete(order_id, callback){
        this.#client.complete({"order_id": order_id}, (err, data) => {
            callback(err, data);
        });
    }
}