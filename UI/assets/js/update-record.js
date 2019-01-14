window.onload = function(){
    getRecord();

    function getRecord(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
        let url = new URL(window.location.href);
        let recordId = url.searchParams.get("recordId");
        const user_id = localStorage.getItem("user_id");
        let createdBy = localStorage.getItem("createdBy");

        let comment = document.getElementById('comment');
        let location = document.getElementById('location');
        
        fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`,{
            headers:{
                Accept:'application/json',
                'Content-type':'application/json',
                'mode':'cors',
                Authorization: "Bearer " + token
            }
            })
            .then((response) => response.json())
            .then((data) => {
                console.log(data.data["location"])
                if(data.status === 200){
                    comment.value = data.data["comment"];
                    location.value= data.data["location"];

                }})
    }
}
document.getElementById('updateIncident').addEventListener('submit', updateIncident);
function updateIncident(e){
    e.preventDefault();
    const token = localStorage.getItem("token");
    let message = localStorage.getItem("message");
    let url = new URL(window.location.href);
    let recordId = url.searchParams.get("recordId");
    let comment = document.getElementById('comment').value;
    let location = document.getElementById('location').value;

    fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/user/incidents/${recordId}`, {
        method:'PATCH',
        headers:{
            Accept:'application/json',
            'Content-type':'application/json',
            Authorization: "Bearer " + token
        },
        body:JSON.stringify(
            {
                comment:comment, 
                location:location
            })
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.status === 200){
            window.location.replace('user-account.html')
        }else if(message === "Token has expired"){
            window.alert("Please log in");
            window.location.replace('index.html')
        }else{
            console.log(data.msg)
            localStorage.setItem("message",data.msg);
            document.getElementById("alert").style.color = "red";
            document.getElementById("alert").innerHTML = data.message;
        }
    })
}
