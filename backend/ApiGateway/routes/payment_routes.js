const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const payment_controller = require("../controllers/payment_controller.js");

router.post("/payorder", json_parser, payment_controller.payOrder);
router.post("/addmoney", json_parser, payment_controller.addMoney);
router.post("/createuser", json_parser, payment_controller.createUser);

module.exports = router;