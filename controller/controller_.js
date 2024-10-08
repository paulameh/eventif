// const mysql = require("mysql2/promise");
// const dotenv = require("dotenv");
//      dotenv.config();
     // const pool = mysql.createPool({
     //      host: process.env.DB_HOST,
     //      user: process.env.DB_USER,
     //      password: process.env.DB_PASSWORD,
     //      database: process.env.DB_NAME
     // });
require("../config/db");
const {empregado} = require("../models/empregados");
const { Op } = require("sequelize");



     // pool.query("select * from empregados").then((result) => {
     //      console.log(result);
     // })

     function organiza(result){ // Cria o salario líquido e associa valor com departamento
          result.forEach((unit) => {
               INSS = unit.salario * .11;
               IRPF = 0;
               if (unit.salario > 1903.98)
                    IRPF += (2826.65 - 1903.98) * .075;
                    if(unit.salario > 2826.65)
                         IRPF += (3751.06 - 2826.65) * .15;
                         if(unit.salario > 3751.06)
                              IRPF +=  + (4664.68 - 3751.06) * .225;
                              if(unit.salario > 4664.68)
                                   IRPF += (unit.salario - 4664.68) * .275;

               unit.salarioLiq = (unit.salario - INSS - IRPF).toFixed(2);

               switch (unit.departamento){
                    case 1:
                         unit.departamento = "Administrativo";
                    break;
                    case 2:
                         unit.departamento = "Designer";
                    break;
                    case 3:
                         unit.departamento = "Contábil";
                    break;
                    case 4:
                         unit.departamento = "Fábrica";
                    break;
               }
          })
          return result;
     }

     async function getEmpregados(){
          // let result = await pool.query("select * from empregados");
          // console.log(result);
          let result = await empregado.findAll();
          result = JSON.stringify(result)
           result = JSON.parse(result)
           console.log(result);

           result = organiza(result);

          // console.log("\n\n------ Resultados na função get", result);
          return result

     }

// getEmpregados();

     async function getEmpregadosBySalario(order) {
          let result = await empregado.findAll();
          result = JSON.stringify(result)
           result = JSON.parse(result)
           result.forEach((unit) => {
               unit.salario = parseFloat(unit.salario);
           })
          result.sort((a, b) => a.salario - b.salario);
          if (order == "decrescente")
               result.reverse();
          organiza(result) 
          return result       
     }

     async function getEmpregadosByDepartamentos() {
          let result = [];
          for (let i = 1; i < 5; i++){
               let search = await empregado.findAll({
                    where: {departamento: i}
               });
               // console.log("\n-----search: \n", search);
               search = JSON.stringify(search);
               search = JSON.parse(search);
               result = result.concat(search);
          }
          result = organiza(result);         
          // console.log("\n------Pegando por departamentos", result);  
          return result       
     }

     async function getEmpregadosByNome(nome) {
          let result = await empregado.findAll({
               where: {nome: { [Op.like]: `%${nome}%` }}
          });
          result = JSON.stringify(result);
          result = JSON.parse(result);
          // console.log("\n\n------ resultados da pesquisa", result);   
          return result
     }

     async function getEmpregado(id){
          // let result = await pool.query(`select * from empregados where id = ${id}`); funciona mas segurança duvidosa
          // let result = await pool.query(`select * from empregados where id = ?`, id);
          // return result[0] //{ id: x, nome: 'x', salario: x, departamento: x }
          let result = await empregado.findAll({
               where: {id: id}
          });
          // console.log(result[0].dataValues);
          return result[0].dataValues
     }

// getEmpregado(1);

     async function insertEmpregado(nome, salario, departamento) {
          // let result = await pool.query(`
          //      insert into empregados (nome, salario, departamento)
          //      values (?, ?, ?)`, [nome, salario, departamento]
          // );
          //    console.log(getEmpregado(result[0].insertId)); // result[0].insertId -> id

          let result = await empregado.create({nome: nome, salario: salario, departamento: departamento});
          console.log(result);
     }

// insertEmpregado("Biana", "2450", 2);

     async function deleteEmpregado(id) {
          console.log(await getEmpregado(id));
          // let result = await pool.query(`
          //      delete from empregados where id = ?`, id
          // );
          let result = await empregado.destroy({
               where: {id: id}
          });
          console.log("Exclusão realizada");
          // console.log("All result", JSON.stringify(result)) Ver isso aqui
     }

// deleteEmpregado(7)

     async function updateEmpregado(id, nome, salario, departamento) {
          // console.log("Antes: ");
          // console.log(await getEmpregado(id));     
          // let result = pool.query(`
          //      update empregados set nome = ?, salario = ?, departamento = ? where id = ?    
          // `, [nome, salario, departamento, id]);
          // console.log("\nAgora: ");
          // console.log(await getEmpregado(id));  
          
          let result = await empregado.update(
               {
                    nome: nome, 
                    salario: salario, 
                    departamento: departamento
               },
               {
                    where: {id: id}
               }
          );
     }

// updateEmpregado(8, "Dj", 4500.12, 3);

module.exports = {getEmpregado, getEmpregados, getEmpregadosBySalario, getEmpregadosByDepartamentos, getEmpregadosByNome, insertEmpregado, deleteEmpregado, updateEmpregado};