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
	client.get(req.params, (err, data) => {
		if (err) {
			console.log(err);
			res.json({"error": err});
		} else {
            res.json(data);
		}
	});
};

exports.getAll = (req, res) => {
	var orders_list = []

	let call = client.getAll({});
	call.on('data', function(response) {
		orders_list.push(response);
	});

	call.on('end',function() {
		res.json(orders_list);
	});
};

exports.create = (req, res) => {
    client.create(req.body, (err, data) => {
		if (err) {
			console.log(err);
		} else {
            res.json(data);
		}
	});
}

exports.cancel = (req, res) => {
    client.cancel(req.body, (err, data) => {
		if (err) {
			console.log(err);
		} else {
            res.json(data);
		}
	});
}

exports.complete = (req, res) => {
    client.complete(req.body, (err, data) => {
		if (err) {
			console.log(err);
		} else {
            res.json(data);
		}
	});
}