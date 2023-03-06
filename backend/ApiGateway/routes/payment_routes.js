const express = require("express");
const router  = express.Router();

const body_parser = require('body-parser');
const json_parser = body_parser.json();

const payment_controller = require("../controllers/payment_controller.js");

router.post("/payorder", json_parser, payment_controller.payorder);

module.exports = router;