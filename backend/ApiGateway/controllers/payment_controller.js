const grpc        = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const PAYMENT_SERVICE_PROTO   = process.env.PAYMENT_SERVICE_PROTO;
const PAYMENT_SERVICE_ADDRESS = process.env.PAYMENT_SERVICE_ADDRESS;

// Setting up the gRPC client
const package_definition = protoLoader.loadSync(
          PAYMENT_SERVICE_PROTO, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
});

const payment_service = grpc.loadPackageDefinition(package_definition).PaymentService;
const client = new payment_service(PAYMENT_SERVICE_ADDRESS, grpc.credentials.createInsecure());

exports.payorder = (req, res) => {
    client.payOrder(req.body, (err, data) => {
		if (err) {
			console.log(err);
		} else {
            res.json(data);
		}
	});
};