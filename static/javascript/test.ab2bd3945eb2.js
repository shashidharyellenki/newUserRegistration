const FirstName = document.querySelector('.FirstName');
const LastName = document.querySelector('.LastName');
const Email = document.querySelector('.Email');
const Username = document.querySelector('.Username');
const Password = document.querySelector('.Password');
const Confrim_Password = document.querySelector('.Confrim_Password');
const Birthday_date = document.querySelector('.Birthday_date');
const phone = document.querySelector('.phone');
const Register = document.getElementById('Register')
const validateEmail =/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
let components = [FirstName, LastName, Email, Username, Password, Confrim_Password, Birthday_date, phone];
//adding eventlistners to all the components
// testing




Register.disabled = true;
components.forEach(component=>{
   component.addEventListener('input',()=>{
       let id_span = component.parentElement.children[2];
       if(component.value === "" ){
           id_span.innerHTML="feild can't be empty";
          component.id="fail"

        }else{
            id_span.textContent="";
            component.id="success"
        }
        if((FirstName.value !=""   && LastName.value !="" ) && (Email.value !=""  && Username.value  !="") &&( Password.value   !="" && Confrim_Password.value !="" )   && (Birthday_date.value  !=""  && phone.value  !="" ) ){
            Register.disabled=false
        } 
        
        if(component == Password){
            if(Password.value.length >= 8){
                id_span.innerHTML="strength: good";
                id_span.classList.add('green');
                id_span.classList.remove('blue');
            }else if (Password.value.length == 5){
                id_span.innerHTML="strength: Moderate";
                id_span.classList.add('blue');
            }

           
        }
    })
})
//using date class
const date = new Date();
//extracing year from complete date to check age
const year = date.getFullYear(); //2022
// const userYear = Birthday_date.value.split("-")[0]

//validating input fields

Register.addEventListener('click',(e)=>{
   e.preventDefault();

    //validating passwords
    if(Password.value !== Confrim_Password.value){
        Register.disabled=true;
          Password.id="fail"
          Confrim_Password.id="fail"
          let span_id = Password.parentElement.children[2];
          span_id.innerHTML="Passwords doesn't match"

    }else{
        Password.id="success"
        Confrim_Password.id="success"
    }
    //validating email
    if(!validateEmail.test(Email.value)){
        Register.disabled=true;
        // alert("Invalid Email")
        Email.id="fail"
        let span = Email.parentElement.children[2];
        span.innerHTML="Invaild Email"
    }else{
        Email.id="success"
    }
    //validating phone number
    const userYear = parseInt(Birthday_date.value.split("-")[0])
    if(phone.value.length != 10){
        Register.disabled=true;
        phone.id="fail"
        let span = phone.parentElement.children[2];
        span.innerHTML='Invalid Phone Number'
        console.log(userYear)
    }else{
        phone.id="success"
    }
    //validating date
   
    if((year-userYear)<13){
        console.log(userYear)
        Register.disabled=true;
        Birthday_date.id="fail"
        let span = Birthday_date.parentElement.children[2];
        span.innerHTML="Minimum age required for this course is 13"
    }
    //noticing user
    if((Password.value === Confrim_Password.value) && (validateEmail.test(Email.value)) && (phone.value.length === 10) && ((year-userYear)>=13)){
        FirstName.id="success";
        LastName.id="success";
        Username.id="success";
        Birthday_date.id="success";
        alert("Hey form submitted sucessfully!!");
        Register.disabled=false;
        

    }
    
})












