window.onload = function(){
    getRecord();

    function getRecord(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
        let url = new URL(window.location.href);
        let recordId = url.searchParams.get("recordId");
    
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
            if (data.status === 200){
                let incidentType = document.getElementById("type");
                let comment = document.getElementById("comment");
                let location = document.getElementById("location");
                let createdOn = document.getElementById("createdOn");
                let status = document.getElementById("status");

                incidentType.innerHTML = data.data.incidentType;
                comment.innerHTML = data.data.comment;
                location.innerHTML = data.data.location;
                createdOn.innerHTML = data.data.createdOn;
                status.innerHTML = data.data.status;  
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

