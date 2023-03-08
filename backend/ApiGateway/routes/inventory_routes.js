const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const inventory_controller = require("../controllers/inventory_controller.js");


router.get("/get/:product_id", inventory_controller.get);
router.get("/getall", inventory_controller.getAll);
router.post("/add", json_parser, inventory_controller.add);
router.delete("/delete", json_parser, inventory_controller.delete);
router.post("/update", json_parser, inventory_controller.update);

module.exports = router;