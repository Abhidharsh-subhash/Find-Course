function valid(x) {
    var name = /^[A-Za-z ]+$/;
	var phone = /^[0-9]+$/;
	var mailformat = /^[a-zA-Z0-9._]+$/;

    if (x.username.value == "") {
        alert('Please enter your username');
        x.username.focus();
        return false;
    }
    else if (!x.username.value.match(name)) {
        alert('Your username contain invalid characters');
        x.username.focus();
        return false;
    }
    if (x.address.value == "") {
        alert('Please enter your address');
        x.address.focus();
        return false;
    }
    if (x.phoneno.value == '') {
        alert('Please enter your mobile number');
        x.phoneno.focus();
        return false;
    }
    else if (!x.phoneno.value.match(phone)) {
        alert('Your mobile number contains invalid characters');
        x.phoneno.focus();
        return false;
    }
    else if (x.phoneno.value.length != 10) {
        alert('Invalid mobile number');
        x.phoneno.focus();
        return false;
    }
    else {
        var a = x.phoneno.value.split("");
        if (a[0] != 9 && a[0] != 8 && a[0] != 7 && a[0] != 6) {
            alert('Invalid mobile number');
            x.phoneno.focus();
            return false;
        }
    }
    if (x.photo.value == '') {
        alert('Please upload your photo');
        x.photo.focus();
        return false;
    }
    if (x.qualification.value == '') {
        alert('Please enter your last qualification');
        x.qualification.focus();
        return false;
    }
    if(x.password.value == ""){
        alert("please enter your new password");
        x.password.focus();
        return false;
    }
}