const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const inventory_controller = require("../controllers/inventory_controller.js");


router.get("/get/:id", inventory_controller.get);
router.get("/getall", inventory_controller.getall);
router.post("/add", json_parser, inventory_controller.add);
router.put("/update", json_parser, inventory_controller.update);
router.delete("/delete", json_parser, inventory_controller.delete);

module.exports = router;