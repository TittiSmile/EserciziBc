function foo(){
    arr=[1,31,5,39,8];
    let val = "";
    for(let i of arr){ // questo è il for of, simile al for potenziato in java... basta che si ha a che fare con un iterabile
        val+="\nvalore: " +i;
    }
    alert(val);
}

function foo2(){
    i = 0;
    let val2 = "";   //il nome è lo stesso di sopra ma let ha delle regole di scope tali che valgono solo dove è dichiarato
    while(i<10){
        val2+="\nnumero: " +i; //in JS si concatena in maniera strana... cioè si fa così, ta-dan
        i++;
    }
    alert(val2);
}