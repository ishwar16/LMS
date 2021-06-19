function error(str){
    var htmlError = '<div class="Montserrat alert alert-danger alert-dismissible fade show text-left" role="alert"><strong>ERROR! </strong><span id="alert-text">$ERROR$</span><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>';
    htmlError = htmlError.replace('$ERROR$',str);
    document.getElementsByTagName('ERROR')[0].innerHTML += htmlError;
}

function validateSignup(){
    var email = document.forms["SignUp"]["EmailId"].value;
    var pass = document.forms["SignUp"]["Password"].value;
    var cpass = document.forms["SignUp"]["CPassword"].value;
    var emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    var passRegex = /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/;
    // console.log(email+" | "+(!email.match(emailRegex))+"\n"+pass+" | "+(!pass.match(passRegex))+"\n"+cpass+" | "+(pass != cpass));
    if(!email.match(emailRegex) ){
      error("Email is Wrong");
      return false;
    }
    else if(!pass.match(passRegex)){
        error("Password should have Atleast 1 Symbol, 1 Number, 1 Uppercase and 1 Lowercase Character and length of 8.");
      return false;
    }
    else if(pass != cpass){
        error("Password does not match");
        return false;
    }
    return true;
  }