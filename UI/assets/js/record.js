window.onload = function(){
    getRecord();

    function getRecord(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
        let url = new URL(window.location.href);
        let recordId = url.searchParams.get("recordId");
        let role = localStorage.getItem("role");
    
        fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`,{
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
            if (data.status === 200 && role == 'true'){
                let incidentType = document.getElementById("type");
                let comment = document.getElementById("comment");
                let location = document.getElementById("location");
                let createdOn = document.getElementById("createdOn");
                let image = document.getElementById("image");
                let status = document.getElementById("status");
                let editRecord = document.getElementById("edit");

                incidentType.innerHTML = data.data.incidentType;
                comment.innerHTML = data.data.comment;
                location.innerHTML = data.data.location;
                createdOn.innerHTML = data.data.createdOn;
                image.innerHTML = data.data.image[0];
                status.innerHTML = data.data.status;
                editRecord.innerHTML =  "<a href='update-record-status.html?recordId="+ data.data.id +"'>Edit</a>";
            }else if(data.status === 200){
                let incidentType = document.getElementById("type");
                let comment = document.getElementById("comment");
                let location = document.getElementById("location");
                let createdOn = document.getElementById("createdOn");
                let image = document.getElementById("image");
                let status = document.getElementById("status");
                let editRecord = document.getElementById("edit");

                incidentType.innerHTML = data.data.incidentType;
                comment.innerHTML = data.data.comment;
                location.innerHTML = data.data.location;
                createdOn.innerHTML = data.data.createdOn;
                image.innerHTML = data.data.image[0];
                status.innerHTML = data.data.status;
                editRecord.innerHTML =  "<a href='update-record.html?recordId="+ data.data.id +"'>Edit</a>";
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
document.getElementById('delete').addEventListener('click', deleteRecord);
function deleteRecord(){
    const token = localStorage.getItem("token");
    let message = localStorage.getItem("message");
    let url = new URL(window.location.href);
    let recordId = url.searchParams.get("recordId");
        
    fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`,{
        method:'DELETE',
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
            console.log(data.message);
                    if (data.status === 200){
                        window.alert('Deleted successfully');
                        window.location.replace('user-account.html');
                    }else if(data.status === 404){
                        window.alert("Record with that ID does not exist.");
                        window.location.replace('user-account.html');
                    }else if(data.message){
                        document.getElementById("alert").style.color = "red";
                        document.getElementById("alert").innerHTML = data.message;}
                })
            }
