const express = require("express");
const router  = express.Router();

const inventory_controller = require("../controllers/inventory_controller.js");


router.get("/get/:id", inventory_controller.get);
router.get("/getall", inventory_controller.getall);
router.post("/add", inventory_controller.add);
router.put("/update", inventory_controller.update);
router.delete("/delete", inventory_controller.delete);

module.exports = router;