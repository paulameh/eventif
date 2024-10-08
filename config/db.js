const dotenv = require("dotenv");
     dotenv.config();

const {Sequelize} = require("sequelize");
const sequelize = new Sequelize(process.env.DB_NAME, process.env.DB_USER, "", {
     dialect: "mysql",
     host: process.env.DB_HOST,
     logging: false
});

module.exports = {sequelize};

const {empregado} = require("../models/empregados");

(async () => {
     try {
          await sequelize.authenticate();
          await sequelize.sync();
          console.log('\n--- Connection/Sync to empresa has been established successfully --- \n\n');
          
        } catch (error) {
          console.error('--- Unable to connect to the database:', error);
        }
})();