const grpc        = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const ORDER_MANAGEMENT_SERVICE_PROTO   = process.env.ORDER_MANAGEMENT_SERVICE_PROTO;
const ORDER_MANAGEMENT_SERVICE_ADDRESS = process.env.ORDER_MANAGEMENT_SERVICE_ADDRESS;

// Setting up the gRPC client
const package_definition = protoLoader.loadSync(
	ORDER_MANAGEMENT_SERVICE_PROTO, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
});

const order_management_service = grpc.loadPackageDefinition(package_definition).OrderManagementService;
const client = new order_management_service(ORDER_MANAGEMENT_SERVICE_ADDRESS, grpc.credentials.createInsecure());

exports.get = (req, res) => {
    const id = req.params.id;
	res.json({"233" : id});
};

exports.add = (req, res) => {
    res.json({"sexual" : "ssss"});
}

exports.update = (req, res) => {
    res.json({"sexual" : "ss33333ss"});
}

exports.delete = (req, res) => {
    res.json({"sexual" : "12ssss"});
}