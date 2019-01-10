document.getElementById('signup').addEventListener('submit', signup);
function signup(e){
    e.preventDefault();
    let firstname = document.getElementById('firstname').value;
    let lastname = document.getElementById('lastname').value;
    let othernames = document.getElementById('othernames').value;
    let phonenumber = document.getElementById('phonenumber').value;
    let email = document.getElementById('email').value;
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/signup', {
        method:'POST',
        headers:{
            'Accept':'application/json',
            'Content-type':'application/json',
            'mode':'cors'
        },
        body:JSON.stringify(
            {
                firstname:firstname,
                lastname:lastname,
                othernames:othernames, 
                phonenumber:phonenumber, 
                email:email, 
                username:username, 
                password:password
            })
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.status === 201){
            console.log(data)
            console.log(data.data[0]["token"])
            window.location.replace('index.html');
        }else{
            console.log(data)
            document.getElementById("alert").style.color = "red";
            document.getElementById("alert").innerHTML = data.message;
        }
    })
}
