
//Tela de profissiolnal

$(document).ready(function(){
    // verificar se esse id existe no documento html
    if ($("#show_profissional").length){
        if (document.getElementById('optionsRadios1').checked){
            hide_profissional();
        } else {
            show_profissional();
        }
    }


});

$("#optionsRadios2").click(function(){
    show_profissional()
})

$("#optionsRadios1").click(function(){
    hide_profissional()
})

function show_profissional(){
    const div = document.getElementById('show_profissional')
    div.hidden = false;
    const div_class = document.getElementById('show_class')
    div_class.setAttribute('class', 'col-lg-6')
}

function hide_profissional(){
    const div = document.getElementById('show_profissional')
    div.hidden = true;
    const div_class = document.getElementById('show_class')
    div_class.setAttribute('class', 'col-lg-12')
}


function gotoBottom(){
   var element = document.getElementById("sobre");
   element.scrollTop = element.scrollHeight - element.clientHeight;
}
