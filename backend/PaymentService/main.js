import dotenv      from 'dotenv';
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import { PaymentService } from './app/services/payment_service.js';

dotenv.config()

const PAYMENT_SERVICE_PROTO          = process.env.PAYMENT_SERVICE_PROTO;
const ORDER_MANAGEMENT_SERVICE_PROTO = process.env.ORDER_MANAGEMENT_SERVICE_PROTO;
const REMOTE_HOST                    = process.env.REMOTE_HOST;
const LOCAL_HOST                     = process.env.LOCAL_HOST;

function serve() {
    console.info("Consumer service is started...");
    const package_definition = protoLoader.loadSync(
        PAYMENT_SERVICE_PROTO, {
            keepCase: true,
            longs: String,
            enums: String,
            defaults: true,
            oneofs: true
    });
    const proto_descriptor = grpc.loadPackageDefinition(package_definition).PaymentService;
    const payment_service = proto_descriptor.service;
    var server = new grpc.Server();
    server.addService(payment_service, {payOrder: PaymentService.payOrder});
    server.bindAsync(LOCAL_HOST, grpc.ServerCredentials.createInsecure(), () => {
        server.start();
    });
};

function run() {
    console.info("Consumer service is started...");
    const package_definition = protoLoader.loadSync(
        ORDER_MANAGEMENT_SERVICE_PROTO, {
            keepCase: true,
            longs: String,
            enums: String,
            defaults: true,
            oneofs: true
    });

    const order_management_service = grpc.loadPackageDefinition(package_definition).OrderManagementService;
	const client = new order_management_service(REMOTE_HOST, grpc.credentials.createInsecure());

    const order = {
        order_id : 1,
        product_id: 2,
        amount: 4
    };

	client.get(order, (err, data) => {
		console.log(data)
		if (err) {
			console.log(err);
		} else {
			console.log('Response received from remote service:', data); // API response
		}
	});

};

run();