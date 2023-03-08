import { ProductRepository } from "../domain/repositories/product_repository.js";
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import dotenv      from 'dotenv';

dotenv.config();

export class ProductRepositoryGrpc extends ProductRepository {
    #client

    constructor() {
        super();
        
        const INVENTORY_SERVICE_PROTO   = process.env.INVENTORY_SERVICE_PROTO;
        const INVENTORY_SERVICE_ADDRESS = process.env.INVENTORY_SERVICE_ADDRESS;

        const package_definition = protoLoader.loadSync(
            INVENTORY_SERVICE_PROTO, {
                keepCase: true,
                longs: String,
                enums: String,
                defaults: true,
                oneofs: true
        });

        const proto_descriptor = grpc.loadPackageDefinition(package_definition).InventoryService;
        this.#client = new proto_descriptor(INVENTORY_SERVICE_ADDRESS, grpc.credentials.createInsecure());
    }

    get(product_id, callback){
        this.#client.get({"product_id": product_id}, (err, data) => {
            callback(err, data);
        });
    }
}