import { ProductRepository } from "../domain/repositories/product_repository.js";
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';

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

        const inventory_service = grpc.loadPackageDefinition(package_definition).InventoryService;
        this.#client = new inventory_service(INVENTORY_SERVICE_ADDRESS, grpc.credentials.createInsecure());
    }

    get(product_id){
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