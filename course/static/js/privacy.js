function validateform(x) {

    if(x.oldpsw.value == ""){
        alert("please enter your old password");
        x.oldpsw.focus();
        return false;
    }
    if(x.newpsw.value == ""){
        alert("please enter your new password");
        x.newpsw.focus();
        return false;
    }
    if(x.vpsw.value == ""){
        alert("please confirm your new password");
        x.vpsw.focus();
        return false;
    }
    if(x.newpsw.value != x.vpsw.value){
        alert("passwords are not matching");
        x.vpsw.focus();
        return false;
    }
}