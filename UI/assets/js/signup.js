document.getElementById('signup').addEventListener('click', signup);
function signup(e){
    e.preventDefault();
    let email = document.getElementById('email').value;
    let username = document.getElementById('username').value;
    let password = document.getElementById('password').value;

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/signup',{
        method:'POST',
        headers:{
            'Accept':'application/json',
            'Content-type':'application/json',
            'mode':'cors'
        },
        body:JSON.stringify({email:email, username:username, passsword:password})
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}
