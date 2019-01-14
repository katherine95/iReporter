window.onload = function(){
    getRecord();

    function getRecord(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
        let url = new URL(window.location.href);
        let recordId = url.searchParams.get("recordId");
        let comment = document.getElementById('comment').value;
        let location = document.getElementById('location').value;
    
        fetch(`https://floating-reaches-50695.herokuapp.com/api/v2/incidents/${recordId}`,{
            method:'PATCH',
            headers:{
                Accept:'application/json',
                'Content-type':'application/json',
                'mode':'cors',
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
            console.log(data);
            if (data.status === 200){
                window.location.replace('record.html');  
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