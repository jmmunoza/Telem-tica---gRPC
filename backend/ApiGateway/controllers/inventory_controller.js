const grpc        = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");

const INVENTORY_SERVICE_PROTO   = process.env.INVENTORY_SERVICE_PROTO;
const INVENTORY_SERVICE_ADDRESS = process.env.INVENTORY_SERVICE_ADDRESS;


exports.get = (req, res) => {
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

    const id = req.params.id;

	client.get({product_id: id}, (err, data) => {
		console.log(data)
		if (err) {
			console.log(err);
		} else {
            res.send(data);
			console.log('Response received from remote service:', data); // API response
		}
	});
};

exports.getall = (req, res) => {
    res.send({ "a": 1231222222223213 });
};