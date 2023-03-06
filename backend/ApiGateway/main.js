const express = require('express')
const app = express()

const dotenv      = require("dotenv");
dotenv.config();

const inventory_routes        = require("./routes/inventory_routes.js");
const order_management_routes = require("./routes/order_management_routes.js");
const payment_routes          = require('./routes/payment_routes.js');

app.use("/inventory", inventory_routes);
app.use("/orders",    order_management_routes);
app.use("/payment",   payment_routes);
app.listen(3000);