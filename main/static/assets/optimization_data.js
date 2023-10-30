const app = new Vue({
  el: '#app',
  delimiters : ['${','}'],
  data: {
    all_data : [],
    quiz : null,
    project_selected: false,
    current_project: null,
    current_objective: null,
    current_category: null,
    current_subcat:null,
    project: 'Seleccione a la Izquierda',
    report : [],
    objec_category : [],
    questions: [],
    view_quiz : false,
    view_graph : false,
    view_objectives : false,
    view_obj_cat : false,
    view_subcateg : false,
    vew_questions : false,
    show_button: false,
    report:[],
  },methods:{
    setProject(name){
      console.log('Seleccionamos el proyecto como activo');
      this.project_selected = true;
      this.project=name;
      this.view_quiz = true;
      this.view_graph = false;
      this.current_project = 0;
      this.view_obj_cat = false;
      this.view_subcateg = false;
      this.vew_questions = false;
      let x = 0;
      this.all_data.forEach(el=>{
            if( el.project === name ){
              this.current_project = x;
              console.log(`marcamos como activo ${el.project}`);
            }
            x += 1;
        });
    },
    listObjCat(itm){
      console.log('Listamoa las categotias');
      this.objec_category =  [];
      this.view_obj_cat = true;
      this.view_subcateg = false;
      this.vew_questions = false;
      this.current_objective = itm.id_objetive;
    },
    listSubcateg(itm){
      this.view_subcateg = true;
      this.vew_questions = false;
      this.current_category = itm.id_objective_category
    },
    listQuestions(itm){
      this.current_subcat = itm.id_subcategory;
      this.questions = [];
      this.vew_questions = true;
    },
    addResult(item){
      this.all_data[this.current_project].quiz.questions.forEach(element=>{
        // Desmarco  de todas las opciones de la subcategoria
        if(item.id_subcategory === element.id_subcategory){
          element.selected = 0;
        }
        if (item.id_question === element.id_question){
          element.selected = 1;
        }
      });
      // Verificamos la subcategoria
      this.all_data[this.current_project].quiz.subcategory.forEach(element=>{
          if(item.id_subcategory == element.id_subcategory)
          {
            element.complete = 1;
          }
      });

      //verificamos todas las objectives_categories
      this.all_data[this.current_project].quiz.objectives_categories.forEach(element=>{
        let selected = 1;
        this.all_data[this.current_project].quiz.subcategory.forEach(elem=>{
            if (element.id_objective_category === elem.objective_category_id){
              if( elem.complete === 0 ){
                selected = 0;
              } 
            }
        });
        element.complete = selected;
      });
      
      let show_button = false;
      // Verificar objectives
      this.all_data[this.current_project].quiz.objectives.forEach(element => {
         let selected = 1;
         this.all_data[this.current_project].quiz.objectives_categories.forEach(elem=>{
           if (element.id_objetive === elem.id_objetive){
             if(elem.complete === 0){
               selected = 0;
             }
           }
         });
         element.complete = selected;
         if(element.complete === 0){
           show_button = false;
         }
      });
      this.show_button = show_button;
    },
    showGraph(){
      this.view_quiz = false;
      this.view_graph = true;
    },
    showQuiz(){
      this.view_quiz = true;
      this.view_graph = false;
    },
    generateGraph(objective){
      let labels_chart = [];
      let scores = [];
      let title =  'Totales';
      // generamos la data para los totales
      if (objective === 0) {
        title = 'Resumen General';
        data = this.exportCSV(true);
        data.shift();
        this.all_data[this.current_project].quiz.objectives.forEach(objective=>{
          labels_chart.push(objective.name);
          
          let score = 0.0;
          data.forEach(item=>{
            if(item[1] === objective.name){
              score +=  item[3];
            }
          });
          scores.push(score);
        });
        
      }else{
        title =  objective.name;
     // Bar chart
     this.all_data[this.current_project].quiz.objectives_categories.forEach(elem=>{
       if(objective.id_objetive === elem.id_objetive){
         labels_chart.push(elem.name);
         let objetive_score = 0.0;
         let subcategory = [];
         // Extramos todas las subcategorias
         this.all_data[this.current_project].quiz.subcategory.forEach(el=>{
            if(elem.id_objective_category === el.objective_category_id ){
              subcategory.push(el);
            }
         });
         //sumamos los puntos de las preguntas de la cateogris
         subcategory.forEach(elem=>{
           this.all_data[this.current_project].quiz.questions.forEach(elm => {
            if(elem.id_subcategory === elm.id_subcategory && elm.selected == 1){
              objetive_score += elm.score;
            }
           });
         });
         scores.push(objetive_score);
       }
     });
      }
    const my_chart = new Chart(document.getElementById("bar-chart"), {
    type: 'bar',
    data: {
      labels: labels_chart,
      datasets: [
        {
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9", "#43aafe"],
          data: scores,
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: title,
      }
    }
  });
    },
    exportCSV(return_data = false){
      let csv_lines = [['proyecto','objetivo','categorias','score']];
      this.all_data[this.current_project].quiz.objectives.forEach(objct => {
        this.all_data[this.current_project].quiz.objectives_categories.forEach(objetive_cat=> {
          if(objct.id_objetive == objetive_cat.id_objetive){
            let cat_score = 0.0
            this.all_data[this.current_project].quiz.subcategory.forEach(subcat => {
              if(objetive_cat.id_objective_category === subcat.objective_category_id){
                 this.all_data[this.current_project].quiz.questions.forEach(question=>{
                  if(question.id_subcategory === subcat.id_subcategory){
                    if (question.selected){
                      cat_score += question.score;
                    }
                  }
                });
              }
            });
            csv_lines.push([ this.project, objct.name, objetive_cat.name, cat_score ]);
          }
        });
      })
      if (return_data === true){
        return csv_lines;
      }
      let csv = csv_lines.map(function(d){
        return d.join(',');
      }).join('\n');

      var pom = document.createElement('a');
      pom.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv));
      pom.setAttribute('download', 'report.csv');
      pom.click();
    },
    exportAllCSV(){
      let csv_lines = [['proyecto','objetivo','categorias','score']];
      let x = 0;
      this.all_data.forEach(item=>{
          csv_lines = csv_lines.concat(this.csvObjetive(item.project, x));
          x++;
      });
      let csv = csv_lines.map(function(d){
        return d.join(',');
      }).join('\n');

      var pom = document.createElement('a');
      pom.setAttribute('href', 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv));
      pom.setAttribute('download', 'report.csv');
      pom.click();
    },
    csvObjetive(project, idx){
      let csv_lines = [];
      this.all_data[idx].quiz.objectives.forEach(objct => {
        this.all_data[idx].quiz.objectives_categories.forEach(objetive_cat=> {
          if(objct.id_objetive == objetive_cat.id_objetive){
            let cat_score = 0.0
            this.all_data[idx].quiz.subcategory.forEach(subcat => {
              if(objetive_cat.id_objective_category === subcat.objective_category_id){
                 this.all_data[idx].quiz.questions.forEach(question=>{
                  if(question.id_subcategory === subcat.id_subcategory){
                    if (question.selected){
                      cat_score += question.score;
                    }
                  }
                });
              }
            });
            csv_lines.push([ project, objct.name, objetive_cat.name, cat_score ]);
          }
        });
      })
      return csv_lines;
    },
    newProgram(){
      localStorage.setItem("program", window.location.href);
      window.location.href = '/program/create/';
    },
    saveOptimization(){
      let index = 0;
      let data = null;
      this.all_data.forEach(el=>{
        if (this.project === el.project){
          data = this.all_data[index];
          console.log(`Encontramos la data a guardar es ${data.project}`);
        }
        index+=1;
      });
      console.dir(data);
      this.$http.post('http://localhost:8000/program/update/', data).then(
            resp=>{
              return window.location.reload(true);
            },
            err=>{
              alert('Ocurrio un error al intentar guardar la informacion');
              console.dir(err);
              return false;
            }
          );
        return true;
    }
  },
 mounted: function(){
    projects.forEach(proj => {
      console.log(`Consulta de la quiz del proyecto ${proj}`);
      this.$http.get('http://localhost:8000/questions-projects/' + proj + '/').then(
        response => {
          console.log(`Respuesta de quiz proyecto ${proj}`);
          console.dir(JSON.parse(response.body));
          this.view_objectives = true;
          this.all_data.push(JSON.parse(response.body));
        }, err => {
          alert('Error al consultar quiz');
          console.dir(err);
        }
      )
    });
  }
})