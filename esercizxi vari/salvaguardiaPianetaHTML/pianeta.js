function validaRegistrazione(){
    if(document.registrazione.nameField.value==""){
        alert('Inserisci nome');
        return false;
    }
    if(document.registrazione.surnameField.value==""){
        alert('Inserisci cognome');
        return false;
    }
    if(document.registrazione.usernameField.value==""){
        alert('Inserisci username');
        return false;
    }
    if(document.registrazione.emailField.value==""){
        alert('Inserisci email');
        return false;
    }
    if(document.registrazione.passwordField.value==""){
        alert('Inserisci password');
        return false;
    }

    alert("Registrazione effettuata");
    alert("Stai per essere reindirizzato al profilo");
    window.open("profilo.html");
    return true;
}


function validaAccesso(){
    if(document.accesso.userField.value==""){
        alert('Inserisci username');
        return false;
    }
    if(document.accesso.passwordField.value==""){
        alert('Inserisci password');
        return false;
    }

    alert("Stai per essere reindirizzato al profilo");
    window.open("profilo.html");
    return true;
}

function profilo(){
    let nome=document.accesso.userField;

}

function popUpGrazie(){
    alert("grazie del suggerimento!");
}