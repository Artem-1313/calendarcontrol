document.addEventListener("DOMContentLoaded",function(){



var input_file=document.getElementById('id_tlg_scan');
var div_error=document.getElementById('error')

var btn_submit=document.querySelector('[type=submit]');
input_file.addEventListener("change",function(e){
var file_ext=input_file.value.split(/(\\|\/)/g).pop().split('.').pop()

if (file_ext != 'pdf' || file_ext !='PDF'){
div_error.innerHTML="Можливо загрузити файл лише у форматі PDF."
btn_submit.disabled=true
}
if (file_ext=='pdf' || file_ext=='PDF'){

div_error.innerHTML=""
btn_submit.disabled=false
}
})

})