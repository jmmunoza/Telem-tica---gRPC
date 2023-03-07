import dotenv      from 'dotenv';
import grpc        from '@grpc/grpc-js';
import protoLoader from '@grpc/proto-loader';
import { PaymentService } from './app/services/payment_service.js';

dotenv.config()

const PAYMENT_SERVICE_PROTO            = process.env.PAYMENT_SERVICE_PROTO;
const PAYMENT_SERVICE_ADDRESS          = process.env.PAYMENT_SERVICE_ADDRESS;

function serve() {
    console.info("Payment service is started...");
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
    server.bindAsync(PAYMENT_SERVICE_ADDRESS, grpc.ServerCredentials.createInsecure(), () => {
        server.start();
    });
};


serve();