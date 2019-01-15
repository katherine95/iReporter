window.onload = function(){
    getUsers();

    function getUsers(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
    
        fetch('https://floating-reaches-50695.herokuapp.com/api/v2/auth/signup',{
        headers:{
            Accept:'application/json',
            'Content-type':'application/json',
            'mode':'cors',
            Authorization: "Bearer " + token
        }
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data.data)
            if(data.status === 200){
                let table = document.getElementById("users");
                let users = data.data;
                users.map((user) => {
                    let new_row = table.insertRow();
                    
                    let id = new_row.insertCell(0);
                    let email = new_row.insertCell(1);
                    let firstname = new_row.insertCell(2);
                    let lastname = new_row.insertCell(3);
                    let othernames = new_row.insertCell(4);
                    let phonenumber = new_row.insertCell(5);
                    let createdOn = new_row.insertCell(6);
                    let username = new_row.insertCell(7);
                    let isAdmin = new_row.insertCell(8);
                    let viewUser = new_row.insertCell(9);

                    id.innerHTML = users.indexOf(user) + 1;
                    email.innerHTML = user.email;
                    firstname.innerHTML = user.firstname;
                    lastname.innerHTML =user.lastname;
                    othernames.innerHTML =user.othernames;                 
                    phonenumber.innerHTML = user.phonenumber;
                    createdOn.innerHTML = user.createdOn;
                    username.innerHTML = user.username;
                    isAdmin.innerHTML = user.isAdmin;
                    viewUser.innerHTML = "<a href='create-admin.html?userName="+ user.username +"' id='makeAdmin'>Make Admin</a>";
                });
            }else if(message === "Token has expired"){
                window.alert("Please log in");
                window.location.replace('index.html')
            }else{
                document.getElementById("alert").style.color = "red";
                document.getElementById("alert").innerHTML = data.message;
            }
        })
    }
}

