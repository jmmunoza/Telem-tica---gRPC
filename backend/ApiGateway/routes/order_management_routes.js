const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const order_management_controller = require("../controllers/order_management_controller.js");

router.get("/get/:id", order_management_controller.get);
router.post("/create", json_parser, order_management_controller.create);
router.post("/cancel", json_parser, order_management_controller.cancel);
router.post("/complete", json_parser, order_management_controller.complete);

module.exports = router;