const DataTypes = require("sequelize");
const {sequelize} = require("../config/db");

const empregado = sequelize.define("empregados",
      {
          id: {
               type: DataTypes.INTEGER,
               autoIncrement: true,
               allowNull: false,
               primaryKey: true
          },
          nome: {
               type: DataTypes.STRING(100),
               allowNull: false
          },
          salario: {
               type: DataTypes.DECIMAL(8,2),
               allowNull: false
          },
          departamento: {
               type: DataTypes.INTEGER,
               allowNull: false
          }
     }, 
     {
          tableName: "empregados",
          timestamps: false
     }
)

module.exports = {empregado};