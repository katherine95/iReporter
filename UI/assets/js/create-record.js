document.getElementById('createIncident').addEventListener('submit', createIncident);
function createIncident(e){
    e.preventDefault();
    const token = localStorage.getItem("token");
    let message = localStorage.getItem("message");
    let comment = document.getElementById('comment').value;
    let location = document.getElementById('location').value;
    let incidentType = document.getElementById('incidentType').value;
    let image = document.getElementById('custom-text').innerHTML;

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/incidents', {
        method:'POST',
        headers:{
            Accept:'application/json',
            'Content-type':'application/json',
            'mode':'cors',
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Request-Method": "*",
            Authorization: "Bearer " + token
        },
        body:JSON.stringify(
            {
                comment:comment, 
                location:location,
                incidentType:incidentType,
                image:[image]
            })
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        if(data.status === 201){
            console.log(data)
            localStorage.setItem("message",data.msg);
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
const realFileBtn = document.getElementById("real-file");
const customBtn = document.getElementById("custom-button");
const customTxt = document.getElementById("custom-text");

window.addEventListener('load', function() {
    customBtn.addEventListener("click", function() {
        realFileBtn.click();
    });
    document.querySelector('input[type="file"]').addEventListener('change', function() {
        if (realFileBtn.value) {
            var img = document.querySelector('img');  // $('img')[0]
            img.src = URL.createObjectURL(this.files[0]); // set src to file url
            customTxt.innerHTML = img.src;
        }
    });
  });