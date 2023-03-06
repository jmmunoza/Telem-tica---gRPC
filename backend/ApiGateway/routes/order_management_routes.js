const express = require("express");
const router  = express.Router();

const order_management_controller = require("../controllers/order_management_controller.js");

router.get("/get/:id", order_management_controller.get);
router.post("/add", order_management_controller.add);
router.put("/update", order_management_controller.update);
router.delete("/delete", order_management_controller.delete)

module.exports = router;