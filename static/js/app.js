var date;
$(document).ready(function () {
     $('.timepicker').pickatime({
        default: 'now', // Set default time: 'now', '1:30AM', '16:30'
        fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
        twelvehour: false, // Use AM/PM or 24-hour format
        donetext: 'OK', // text for done-button
        cleartext: 'Clear', // text for clear-button
        canceltext: 'Cancel', // Text for cancel-button
        autoclose: false, // automatic close timepicker
        ampmclickable: true, // make AM PM clickable
        aftershow: function(){} //Function for after opening timepicker
     });

     var d = new Date();
     d.setFullYear( d.getFullYear() - 100 );

     $('.datepicker').pickadate({
        selectMonths: true, // Creates a dropdown to control month
        selectYears: 0, // Creates a dropdown of 15 years to control year,
        today: 'Today',
        clear: 'Clear',
        min: d,
        max: new Date(),
        close: 'Ok',
        format: 'yyyy-mm-dd',
        closeOnSelect: true // Close upon selecting a date,
     });

     $(".addAlumno").click(function () {
         $("#modalTitle").text("Agregar nuevo alumno");
         $("#modalBody").html(
             '<label for="exp">Expediente</label>'+
             '<input id="exp" type="number" class="validate">'+
             '<label for="nom">Nombre</label>'+
             '<input id="nom" type="text" class="validate">'+
             '<label for="car">Carrera</label>'+
             '<input id="car" type="text" class="validate">'
         );
         $("#buttonSendModal").removeClass();
         $("#buttonSendModal").addClass("modal-action waves-effect waves-green btn-flat ");
         $("#buttonSendModal").click(addAlumnos);
         $('#modal1').modal('open');
     });

     $(".settings").click(function () {
         $("#modalTitle").text("Agregar metricas");
         $("#modalBody").html(

            '<div class="row">\n' +
                '<div class="input-field col s6">\n'+
                    '<label for="exam_num">Numero de examenes:</label>\n'+
                    '<input placeholder="" id="exam_num" type="number" min="0" >\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="exam_por">Porcentaje de examen:</label>\n'+
                    '<input placeholder="" id="exam_por" type="number" class="inputAvg" min="0" max="100">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="proy_num">Numero de proyectos:</label>\n'+
                    '<input placeholder="" id="proy_num" type="number" min="0" >\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="proy_por">Porcentaje de proyecto:</label>\n'+
                    '<input placeholder="" id="proy_por" type="number" class="inputAvg" min="0" max="100">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="asis_num">Numero de retardos (para una falta):</label>\n'+
                    '<input placeholder="" id="asis_num" type="number" min="0" >\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="asis_por">Porcentaje de asistencias:</label>\n'+
                    '<input placeholder="" id="asis_por" type="number" class="inputAvg" min="0" max="100">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="part_por">Porcentaje de participaciones:</label>\n'+
                    '<input placeholder="" id="part_por" type="number" class="inputAvg" min="0" max="100">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<label for="tar_por">Porcentaje de tareas:</label>\n'+
                    '<input placeholder="" id="tar_por" type="number" class="inputAvg" min="0" max="100">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                '</div>'+
                '<div class="input-field col s6">\n'+
                    '<input value="0" type="number" class="totalInput" disabled>\n'+
                '</div>'+
            '</div>'
         );
         $("#buttonSendModal").click(addMetricas);
         $('#modal1').modal('open');
     });

     $(".searchAlumnos").click(function () {
         $("#modalTitle").text("Buscar alumnos");
     });

     $(document).ready(function() {
         $('select').material_select();
     });

     $(document).on("change", ".inputAvg", function() {
        var sum = 0;
        $(".inputAvg").each(function(){
            sum += +$(this).val();
        });
        $(".inputAvg").attr({"max":(100 - sum)});
        $(".totalInput").val(sum);
    });

     $('.modal').modal();
     getAlumnos();
});

function getAlumnos(){
   var url = document.URL;
   if(url.indexOf("/") > 0 ) {
       url = url.split("/");
       url = url[4];
   }
   if(url !== undefined) {
       $.ajax({
           method: "POST",
           url: "/getAlumnos/",
           data: {id: url},
           success: function (success) {
               var result = eval(success);
               $("#alumnosTab").html("");
               for (var i = 0; i < result.length; i++) {
                   $("#alumnosTab").append(
                       '<tr>' +
                       '<td>' + result[i]["fields"]["expediente"] + '</td>' +
                       '<td>' + result[i]["fields"]["nombre"] + '</td>' +
                       '<td>' + result[i]["fields"]["carrera"] + '</td>' +
                       '<td>' +
                       '<a style="width: 100%;" class="waves-effect waves-light btn red darken-2 deleteStudent" value="' + result[i]["pk"] + '" onclick="deleteStudent(this)">' +
                       'Eliminar alumno' +
                       '</a>' +
                       '</td>' +
                       '</tr>'
                   )
               }
           }
       });
   }
}

function deleteStudent(elem) {
    var id = $(elem).attr("value");
    $.ajax({
        method: "POST",
        url:"/deleteStudent/",
        data: {id:id},
        success:function (success) {
            if ( success ){
                Materialize.toast('Se elimino el alumno', 4000);
                getAlumnos();
            }
        }
    });
}

function selectDay(elem) {
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    date = $(elem).val();
    $.ajax({
        method: "POST",
        url:"/selectAsistencia/",
        data: {dateSel:date, id:url},
        success:function (success) {
            var response = eval(success);
            console.log(response);
            var html = "";
            for ( var i = 0; i < (response.length/2); i++){
                var j = response.length/2;
                console.log(response);
                html += '<tr><td>'+response[i]["fields"]["expediente"]+'</td>'+
                    '<td>'+response[i]["fields"]["nombre"]+'</td>'+
                    '<input type="hidden" value='+response[i+j]["fields"]["idA"]+' id="idAlumno">'+
                    '<td>'+selectList(response[i+j]["fields"]["status"])+'</td></tr>';
            }
            $("#alumnosTabAsistencia").html(html);
        }
    });
}

var cont = 0;

function selectList(type){
    var list = "";
    cont = cont + 1;
    switch (type) {
        case 'A':
            list =
                '<select onchange="updateAt(this)" class="input-field" style="display: block;" id="selType"+cont+">' +
                    '<option value="A">Asistencia</option>'+
                    '<option value="F">Falta</option>'+
                    '<option value="J">Justificar</option>'+
                    '<option value="R">Retardo</option>'+
                '</select>'
            break;
        case 'F':
            list =
                '<select onchange="updateAt(this)" class="input-field" style="display: block;" id="selType"+cont+">' +
                    '<option value="F">Falta</option>'+
                    '<option value="A">Asistencia</option>'+
                    '<option value="J">Justificar</option>'+
                    '<option value="R">Retardo</option>'+
                '</select>'
            break;
        case 'J':
            list =
                '<select onchange="updateAt(this)" class="input-field" style="display: block;" id="selType"+cont+">' +
                    '<option value="J">Justificar</option>'+
                    '<option value="A">Asistencia</option>'+
                    '<option value="F">Falta</option>'+
                    '<option value="R">Retardo</option>'+
                '</select>'
            break;
        case 'R':
            list =
                '<select onchange="updateAt(this)" class="input-field" style="display: block;" id="selType"+cont+">' +
                    '<option value="R">Retardo</option>'+
                    '<option value="J">Justificar</option>'+
                    '<option value="A">Asistencia</option>'+
                    '<option value="F">Falta</option>'+
                '</select>'
            break;
        case ' ':
            list =
                '<select onchange="updateAt(this)" class="input-field" style="display: block;" id="selType"+cont+">' +
                    '<option>Seleccione una opción</option>'+
                    '<option value="R">Retardo</option>'+
                    '<option value="J">Justificar</option>'+
                    '<option value="A">Asistencia</option>'+
                    '<option value="F">Falta</option>'+
                '</select>'
            break;
    }
    return list;
}

function updateAt(selectObject) {
    var x = selectObject.value;
    var url = document.URL;
    var idA = $(selectObject).parent().parent().children("#idAlumno").val();
    url = url.split("/");
    url = url[4];
    $.ajax({
        method: "POST",
        url:"/updateAt/",
        data: {dateSel:date, id:url, status:x, idAlumno:idA},
        success:function (success) {
           if( success ){
               Materialize.toast('Se actualizo la lista', 4000);
           }
        }
    });
}

function setParcial(elem){
    var parcial = $(elem).val();
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    if( parcial > 0 ){
        $.ajax({
            method: "POST",
            url:"/setExamCalif/",
            data: {id:url, parcial:parcial},
            success:function (success) {
                var response = eval(success);
                var html = "";
                var j = response.length/2;
                for ( var i = 0; i < (response.length/2); i++){
                    var idAlumno = response[i+j]['fields']['idAlumno'];
                    var idCalif = response[i+j]['fields']['idCalif'];
                    var calif = response[i+j]['fields']['calif'];
                    html += '<tr><td>'+response[i]["fields"]["expediente"]+'</td>'+
                        '<td>'+response[i]["fields"]["nombre"]+'</td>'+
                        '<td><input type="number" value="'+calif+'" max="100" min="0" onblur="setCalifAlumno('+idAlumno+',this,'+idCalif+')"></td></tr>';
                }
                $("#alumnosTabAsistencia").html(html);
            }
        });
    }
}

function setCalifAlumno(id,elem,idCalif) {
    var calif = $(elem).val();
    if( calif > 100 ) {
        $(elem).val(100);
    }
    else if( calif < 0 ){
        $(elem).val(0)
    }else{
        $.ajax({
            method: "POST",
            url: "/setCalifStudent/",
            data: {id: id, calif: calif, idCalif:idCalif},
            success: function (success) {
               Materialize.toast('Se actualizo la lista', 4000);
            }
        });
    }
}

function addMetricas() {
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    var obj ={
        exam_num : $("#exam_num").val(),
        exam_por : $("#exam_por").val(),
        proy_num : $("#proy_num").val(),
        proy_por : $("#proy_por").val(),
        asis_num : $("#asis_num").val(),
        asis_por : $("#asis_por").val(),
        part_por : $("#part_por").val(),
        tar_por  : $("#tar_por").val(),
        id_group : url
    };
    var num = $(".totalInput").val();


    if(num > 100){
        Materialize.toast('Por favor disminuye el porcentaje de las metricas', 4000);
    }else if(num < 100){
        Materialize.toast('Por favor aumenta el porcentaje de las metricas', 4000);
    }else {
        $.ajax({
            method: "POST",
            url: "/addMetricas/",
            data: obj,
            success: function (success) {
                console.log(success);
                if (success) {
                    Materialize.toast('Se editaron las metricas correctamente', 4000);
                    getAlumnos();
                }
            }
        });
    }
}

function addAlumnos() {
    var exp = $("#exp").val();
        var nombre = $("#nom").val();
        var carrera = $("#car").val();
        var url = document.URL;
        url = url.split("/");
        url = url[4];
        $.ajax({
            method: "POST",
            url:"/addAlumnosurl/",
            data: {exp: exp, nombre:nombre, carrera:carrera, id:url},
            success:function (success) {
               if ( success ){
                  Materialize.toast('Se agrego un nuevo alumno', 4000);
                  getAlumnos();
               }
            }
        })
}

function setMetrica(elem){
    var metrica = $(elem).val();
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    if( metrica > 0 ){
        $.ajax({
            method: "POST",
            url:"/setProjectCalif/",
            data: {id:url, metrica:metrica},
            success:function (success) {
                var response = eval(success);
                var html = "";
                var j = response.length/2;

                for ( var i = 0; i < (response.length/2); i++){
                    console.log(response);
                    var idAlumno = response[i+j]['fields']['idAlumno'];
                    var idCalif = response[i+j]['fields']['idCalif'];
                    var calif = response[i+j]['fields']['calif'];
                    html += '<tr><td>'+response[i]["fields"]["expediente"]+'</td>'+
                        '<td>'+response[i]["fields"]["nombre"]+'</td>'+
                        '<td><input type="number" value="'+calif+'" max="100" min="0" onblur="setCalifProject('+idAlumno+',this,'+idCalif+')"></td></tr>';
                }
                $("#alumnosTabAsistencia").html(html);
            }
        });
    }
}

function setCalifProject(id,elem,idCalif) {
    var calif = $(elem).val();
    if( calif > 100 ) {
        $(elem).val(100);
    }
    else if( calif < 0 ){
        $(elem).val(0)
    }else{
        $.ajax({
            method: "POST",
            url: "/setCalifStudentProject/",
            data: {id: id, calif: calif, idCalif:idCalif},
            success: function (success) {
               Materialize.toast('Se actualizo la lista', 4000);
            }
        });
    }
}

function setTabla() {
    var type = $("#setParcialSelect").val();
    var date = $("#fechaSel").val();
    var url = document.URL;
    url = url.split("/");
    url = url[4];

    if(type != "" && date != ""){
        $.ajax({
            method: "POST",
            url: "/worksList/",
            data: {id: url, type: type, date:date},
            success: function (success) {
                var response = eval(success);
                var html = "";
                for (var i = 0; i < (response.length / 2); i++) {
                    var j = response.length / 2;
                    var idAlumno = response[i + j]['fields']['idAlumno'];
                    var idWork = response[i + j]['fields']['idWork'];
                    var calif = response[i + j]['fields']['calif'];
                    html += '<tr><td>' + response[i]["fields"]["expediente"] + '</td>' +
                        '<td>' + response[i]["fields"]["nombre"] + '</td>' +
                        '<td>' +
                            '<select onchange="setWork(this,'+idWork+','+idAlumno+')" class="input-field" style="display: block;">' +
                                getStatus(calif,type)+
                            '</select>' +
                        '</td></tr>';
                }
                $("#alumnosTabAsistencia").html(html);

            }
        });
    }
}

function getStatus(calif,type){
    var optionsTarea = ['<option value="E">Entrego</option>', '<option value="N">No entrego</option>'];
    var optionsPart = ['<option value="P">Participo</option>', '<option value="NP">No participo</option>'];

    if(type == 'T'){
        var options = optionsTarea;
    }else{
        var options = optionsPart;
    }
    var cleanHTML = "";
    for (var i = 0; i < options.length; i++){
        if (options[i].indexOf(calif) >= 0 && calif != ' ') {
            cleanHTML += '<option value="' + calif + '" selected>' + getTypeName(calif) + '</option>';
        } else {
            cleanHTML += options[i];
        }
    }
    if (calif == ' '){
        cleanHTML += '<option selected>Seleccione una opción</option>';
    }

    return cleanHTML;
}

function getTypeName(type) {
    switch (type){
        case 'E':
            return "Entregado";
            break;
        case 'P':
            return "Participo";
            break;
        case 'N':
            return "No entrego";
            break;
        case 'NP':
            return "No participo";
            break;
    }
}

function setWork(elem,idwork,idalumno) {
    var obj = {
        status : $(elem).val(),
        idWork : idwork,
        idalumno: idalumno,
    };

    $.ajax({
        method: "POST",
        url: "/worksSet/",
        data: obj,
        success:function (success) {
            console.log(success);
            if ( success ){
                Materialize.toast('Se actualizo correctamente', 4000);
            }
        }
    })
}

function setCalif(id,num){
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    console.log(url);
    $.ajax({
        method:"POST",
        url:"/getCalifStudent/",
        async: !1,
        data:{id:id, idgroup:url},
        success:function (success) {
            $("#calif"+num).text(calif(success));
        }
    })
}

function openModalCalif(id){
    var url = document.URL;
    url = url.split("/");
    url = url[4];
    console.log(url);
    $.ajax({
        method:"POST",
        url:"/getCalifStudent/",
        async: !1,
        data:{id:id, idgroup:url},
        success:function (success) {
            $("#modal1").modal("open");
            $("#modalTitle").text("Información del alumno");
            var examTotal = ""

            for ( var i = 0; i < success["Examen"].length; i++ ){
               examTotal += success["Examen"][i]["calif"] + ", ";
            }

            var proy = ""

            for ( var i = 0; i < success["Proyecto"].length; i++ ){
               proy += success["Proyecto"][i]["calif"] + ", ";
            }

            $("#modalBody").html(
                "<table>" +
                 "<tr>" +
                    '<td>Examenes: '+(examTotal.replace(/,$/, ""))+'</td>'+
                    '<td>Proyectos: '+(proy.replace(/,$/, ""))+'</td>'+
                    '<td>Asistencia: '+success["Asistencia"]+'</td>'+
                    '<td>Participaciones: '+success["Participacion"]+'</td>'+
                    '<td>Tareas: '+success["Tareas"]+'</td>'+
                "</tr>"+
                    '<td>Total de asistencia: '+$("#totalAtt").val()+'</td>'+
                    '<td>Total de trabajos: '+$("#totalhomework").val()+'</td>'+
                    '<td>Total de Participaciones:  '+$("#totalProjects").val()+'</td>'+
                    '<td>Total de proyectos: '+$("#totalProy").val()+'</td>'+
                    '<td>Total de Examenes:  '+$("#totalExam").val()+'</td>'
                );
        }
    })
}

function calif(array) {
    var calif = 0;
    var totalExam = $("#totalExam").val();
    console.log(array);

    if(totalExam != 0){
        var examAvg = $("#examAvg").val();
        var examV = 0;

        for ( var i = 0; i < array["Examen"].length; i++ ){
            examV = examV + array["Examen"][i]["calif"];
        }

        examV = examV/ totalExam;
        calif += (examV*examAvg)/100;
    }

    var totalProy = $("#totalProy").val();

    if(totalProy != 0){
        var proyAvg = $("#proyAvg").val();
        var proyV = 0;

        for ( var i = 0; i < array["Proyecto"].length; i++ ){
            proyV = proyV + parseFloat(array["Proyecto"][i]["calif"]);
        }

        proyV = proyV/ totalProy;
        proyV = ((proyV*proyAvg)/100);
        calif = proyV+calif;
    }

    var totalAtt = $("#totalAttendence").val();

    if( totalAtt > 0 ){
        var att = array["Asistencia"];
        var attTotal = $("#totalAttendence").val();

        att = att*$("#attAvg").val();
        att = att/attTotal;

        calif += att;
    }

    var totalHome = $("#totalhomework").val();
    if(totalHome > 0){
        var homeWork = array["Tareas"];
        var homeWorkAvg = parseFloat($("#tareaAvg").val());

        homeWork = homeWork*homeWorkAvg;

        homeWork = homeWork/totalHome;

        calif += homeWork;
    }

    var totalPart = $("#totalProjects").val();

    if(totalHome > 0){
        var part = array["Participacion"];
        var partAvg = parseFloat($("#partAvg").val());

        part = part*partAvg;

        part = part/totalPart;

        calif += part;
    }

    console.log(calif);

    return calif;
}