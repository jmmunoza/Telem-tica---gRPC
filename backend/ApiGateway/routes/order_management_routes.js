const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const order_management_controller = require("../controllers/order_management_controller.js");

router.get("/get/:id", order_management_controller.get);
router.post("/add", json_parser, order_management_controller.add);
router.put("/update", json_parser, order_management_controller.update);
router.delete("/delete", json_parser, order_management_controller.delete)

module.exports = router;