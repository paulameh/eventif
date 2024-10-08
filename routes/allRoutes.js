const express = require("express");
const router = express.Router();
const controller = require("../controller/controller_");

router.get("/", (req, res) => {
     console.log("\n--Request for index made");
     // res.sendFile("./views/index.html", {root: __dirname}); se html
     // O segundo argumento é necessário já que se trata de caminho absoluto e não relativo.
     controller.getEmpregados().then((results) => {
          // console.log("\n\n------- Resultados dentro do routes: ", results)
          res.render("index", {data: results}); 
     });
});

router.get('/registro', (req, res) => {
     res.render("registro");
     console.log("\n--Request for registro made");
});

router.post('/registro', async (req, res) => {
     await controller.insertEmpregado(req.body.nome, req.body.salario, req.body.departamento);
     res.redirect("/");  
});

router.get('/formulario', (req, res) => {
     res.render("registro");
});

router.get('/editar/:id', (req, res) => {
     const id = req.params.id;
     const empregado = controller.getEmpregado(id).then((result) => {
          console.log("\n\n----Empregado: \n", result);
          res.render("editar", {empregado: result});
     });
})

router.post('/editar', (req, res) => {
     const empregado = controller.updateEmpregado(req.body.id, req.body.nome, req.body.salario, req.body.departamento);
     res.redirect("/");
})

router.get('/deletar/:id', (req, res) => {
     controller.deleteEmpregado(req.params.id);
     res.redirect("/");
});

router.post('/pesquisar', (req, res) => {
     controller.getEmpregadosByNome(req.body.pesquisa).then((result) => {
          res.render("index", {data: result});
     })
})

router.get('/salariosOrdem/:ordem', (req, res) => {
     if (req.params.ordem == "crescente")
          controller.getEmpregadosBySalario('').then((result) => {
               res.render("index", {data: result});
          })
     else if (req.params.ordem == "decrescente")
          controller.getEmpregadosBySalario('decrescente').then((result) => {
               res.render("index", {data: result});
          })
});

router.get('/agruparDepartamentos', (req, res) => {
     controller.getEmpregadosByDepartamentos().then((result) => {
          res.render('index', {data: result})
     })
})

//Deve estar abaixo de todos, senão interrompe as verificações
router.use((req, res) =>{
     // res.status(404).sendFile("./Views/404.html", {root: __dirname});
     res.render("404");
});

module.exports = router;