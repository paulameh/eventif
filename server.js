const express = require("express");
const app = express();
const { engine } = require("express-handlebars");
     app.engine('handlebars', engine());
     app.set("view engine", "handlebars");
const bodyParser = require('body-parser')

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))

// parse application/json
app.use(bodyParser.json())

const allRoutes = require("./routes/allRoutes");
     app.use(allRoutes);

const query = require("./controller/controller_");

app.listen(3000, 'localhost', () => {
     console.log("Servidor em funcionamento :3 \nPorta: 3000 \nAwaiting requests...");
})



