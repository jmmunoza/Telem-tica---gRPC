const dotenv  = require("dotenv");
const express = require('express')
const app = express()

dotenv.config();

const inventory_routes = require("./routes/inventory_routes.js");

app.use("/inventory", inventory_routes);
app.listen(3000)