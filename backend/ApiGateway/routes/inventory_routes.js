const express = require("express");
const router  = express.Router();

const inventory_controller = require("../controllers/inventory_controller.js");

router.get("/get/:id", inventory_controller.get);
router.get("/getall", inventory_controller.getall)

module.exports = router;