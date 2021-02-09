
//JAVASCRIPT A EJECUTARSE UNA VEZ CARGADA LA PAGINA:
window.onload = function(event){
    event.preventDefault();
    document.getElementById("botonPago").onclick = validaDatosPersonales;
    document.getElementById("MostrarE").onclick = mostrarE;
    document.getElementById("MostrarI").onclick = mostrarI;
    document.getElementById("MostrarF").onclick = mostrarF;
    //document.getElementById("botonConfirmar").onclick = validaDatosPago;


}

function mostrarE(){
	document.getElementById("español").style.display = "block";
	document.getElementById("ingles").style.display = "none";
	document.getElementById("frances").style.display = "none";
}
function mostrarI(){
	document.getElementById("español").style.display = "none";
	document.getElementById("ingles").style.display = "block";
	document.getElementById("frances").style.display = "none";
}
function mostrarF(){
	document.getElementById("español").style.display = "none";
	document.getElementById("ingles").style.display = "none";
	document.getElementById("frances").style.display = "block";
}

//tamaño de letra
// Defino un tamaño de letra inicial de 16px
function tamañoLetra() {
	size = $(".mitexto" ).css("font-size");
	size = parseInt(size, 10);
	$( ".tamaño-actual" ).text(size);
  }

  // Obtengo el tamaño de letra inicial de 16px
  tamañoLetra();

  // Función para disminuir el tamaño del texto (fuente)
  $(".disminuir").on("click", function() {
	if ((size - 2) >= 13) {
	  $(".mitexto").css("font-size", "-=2");
	  $(".tamaño-actual").text(size -= 1);
	}
  });

  // Función para aumentar el tamaño del texto (fuente)
  $(".aumentar").on("click", function() {
	if ((size + 2) <= 47) {
	  $(".mitexto").css("font-size", "+=2");
	  $(".tamaño-actual").text(size += 1);
	}
  });

  // Función para restablecer el tamaño del texto (fuente) al tamaño inicial
  $(".restablecer").on("click", function() {
	$(".mitexto").css("font-size", "initial");
	size = $(".mitexto" ).css("font-size");
	size = parseInt(size, 10);
	$( ".tamaño-actual" ).text(size);
  });



//function cambiart(){
  //  document.getElementById("con").style.fontSize=15;
//}
function validaDatosPersonales() {

    var todoBien = true;

    console.log("8")
     //Nombre:
        var vNombre = document.getElementById("nombre").value;
        if( vNombre == null || vNombre.length == 0 || /^\s+$/.test(vNombre) || !isNaN(vNombre)) {
            todoBien=false;
            document.getElementById("nombre").className = "textMal";
            //alert('[ERROR] El campo debe estar completo y solo debe tener letras');
        }
        else{
            document.getElementById("nombre").className = "textBien";
            
        }

            //Apellido:
			var vApellido = document.getElementById("apellido").value;
			if( vApellido == null || vApellido.length == 0 || /^\s+$/.test(vApellido) || !isNaN(vApellido)) {
				todoBien=false;
                document.getElementById("apellido").className = "textMal";
                //alert('[ERROR] El campo debe estar completo y solo debe tener letras');
			}
			else{
				document.getElementById("apellido").className = "textBien";
			}

	//titular
	
	var vTitular = document.getElementById("titular").value;
	if( vTitular == null || vTitular.length == 0 || /^\s+$/.test(vTitular) || !isNaN(vTitular)) {
		todoBien=false;
		document.getElementById("titular").className = "textMal";
		//alert('[ERROR] El campo debe estar completo y solo debe tener letras');
	}
	else{
		document.getElementById("titular").className = "textBien";
	}

	//Direccion
			var vDireccion = document.getElementById("direccion").value;
			if( vDireccion == null || vDireccion.length == 0 || /^\s+$/.test(vDireccion) || !isNaN(vDireccion)) {
				todoBien=false;
                document.getElementById("direccion").className = "textMal";
                //alert('[ERROR] Se debe iniciar con letras ');
			}
			else{
				document.getElementById("direccion").className = "textBien";
			}

    //email:
			var vEmail1 = document.getElementById("email1").value;
			var vEmail2 = document.getElementById("email2").value;

			//email 1
			if( !(/^\w+([-.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(vEmail1)) ) {
				todoBien=false;
                document.getElementById("email1").className = "textMal";
                //alert('[ERROR] El campo debe tener un @ y un punto');
			}
			else{
				document.getElementById("email1").className = "textBien";
			}

	//email 2
			if( !(/^\w+([-.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/.test(vEmail2)) ) {
				todoBien=false;
                document.getElementById("email2").className = "textMal";
              //  alert('[ERROR] El campo debe tener un @ y un punto');
			}
			else{
				document.getElementById("email2").className = "textBien";
			}

			//Comparacion email 1 y 2
			if (vEmail1 != vEmail2){
				todoBien=false;
                document.getElementById("email2").className = "textMal";
               // alert('[ERROR] Los correos deben ser iguales');
			}


	//Telefono:
			var vMovil = document.getElementById("movil").value;
			if( !(/^\d{9}$/.test(vMovil))  ) {
				todoBien=false;
                document.getElementById("movil").className = "textMal";
                //alert('[ERROR] El campo debe tener solo numeros');
			}
			else{
				document.getElementById("movil").className = "textBien";
			}


    //Localidad:
			var vLocalidad = document.getElementById("localidad").value;
			if( vLocalidad == null || vLocalidad.length == 0 || /^\s+$/.test(vLocalidad) || !isNaN(vLocalidad)) {
				todoBien=false;
                document.getElementById("localidad").className = "textMal";
                //alert('[ERROR] El campo debe tener solo letras');
			}
			else{
				document.getElementById("localidad").className = "textBien";
			}

	//Tarjeta:
	var vTarjeta = document.getElementById("tarjeta").value;
	if( !(/^\d{16}$/.test(vTarjeta))  ) {
		todoBien=false;
		document.getElementById("tarjeta").className = "textMal";
		//alert('[ERROR] El campo debe tener solo numeros');
	}
	else{
		document.getElementById("tarjeta").className = "textBien";
	}

	//Caducidad:
	var vCaducidad = document.getElementById("start").value;
	if( vCaducidad == null || vCaducidad.length == 0 || !isNaN(vCaducida)) {
		todoBien=false;
		document.getElementById("start").className = "textMal";
		//alert('[ERROR] El campo debe tener solo letras');
	}
	else{
		document.getElementById("start").className = "textBien";
	}
	//ccv:
	//Telefono:
	var vCcv = document.getElementById("ccv").value;
	if( !(/^\d{3}$/.test(vCcv))  ) {
		todoBien=false;
		document.getElementById("ccv").className = "textMal";
		//alert('[ERROR] El campo debe tener solo numeros');
	}
	else{
		document.getElementById("ccv").className = "textBien";
	}

return (false);

}

var idioma = "hispano";

function ponerIdioma(cual)	{
	document.getElementById(idioma).style.display = "none";
	idioma = cual;
	document.getElementById(idioma).style.display = "block";
}
//function capturar(e){
  //  e=e || window.event;
    //console.log(e);
//}
//FUNCION DE VALIDAR DATOS PAGO y ENVIAR DATOS
/*
	function validaDatosPagoYEnviaCarro(elEvento) {
		alert("Gracias por su compra, en 24 horas recivira su pedido\nAhora sera redirigido a la pagina de inicio.");
		window.location.reload()
	}*/