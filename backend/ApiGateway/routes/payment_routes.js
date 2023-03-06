const express = require("express");
const router  = express.Router();

const bodyParser = require('body-parser');
const jsonParser = bodyParser.json();

const payment_controller = require("../controllers/payment_controller.js");

router.post("/payorder", jsonParser, payment_controller.payorder);

module.exports = router;