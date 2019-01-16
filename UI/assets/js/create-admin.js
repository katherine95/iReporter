document.getElementById('createAdmin').addEventListener('click', createAdmin);
function createAdmin(){
    const token = localStorage.getItem("token");
    let message = localStorage.getItem("message");
    let url = new URL(window.location.href);
    let userName = url.searchParams.get("userName");

    fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/auth/users/${userName}`,{
        method:'PATCH',
        headers:{
            Accept:'application/json',
            'Content-type':'application/json',
            'mode':'cors',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Request-Method": "*",
            Authorization: "Bearer " + token
        }
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        if(data.status === 200){
            window.alert("Admin created Successfully")
            window.location.replace('users-list.html')
        // }else if(message === "Token has expired"){
        //     window.alert("Please log in");
        //     window.location.replace('index.html')
        }else{
            console.log(data.msg)
            localStorage.setItem("message",data.msg);
            document.getElementById("alert").style.color = "red";
            document.getElementById("alert").innerHTML = data.message;
        }
    })
}