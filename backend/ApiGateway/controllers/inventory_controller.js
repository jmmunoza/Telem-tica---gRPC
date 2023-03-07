const grpc        = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const INVENTORY_SERVICE_PROTO   = process.env.INVENTORY_SERVICE_PROTO;
const INVENTORY_SERVICE_ADDRESS = process.env.INVENTORY_SERVICE_ADDRESS;

// Setting up the gRPC client
const package_definition = protoLoader.loadSync(
    INVENTORY_SERVICE_PROTO, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
});

const inventory_service = grpc.loadPackageDefinition(package_definition).InventoryService;
const client = new inventory_service(INVENTORY_SERVICE_ADDRESS, grpc.credentials.createInsecure());

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
	var products_list = []

	let call = client.getAll({});
	call.on('data', function(response) {
		products_list.push(response);
	});

	call.on('end',function() {
		res.json(products_list);
	});
};

exports.add = (req, res) => {
    client.add(req.body, (err, data) => {
		if (err) {
			console.log(err);
			res.json({"error": err});
		} else {
            res.json(data);
		}
	});
}

exports.delete = (req, res) => {
    client.delete(req.body, (err, data) => {
		if (err) {
			console.log(err);
			res.json({"error": err});
		} else {
            res.json(data);
		}
	});
}