window.onload = function(){
    getRecords();

    function getRecords(){
        const token = localStorage.getItem("token");
        let message = localStorage.getItem("message");
        let user_id = localStorage.getItem("user_id");
        console.log(user_id);
    
        fetch('https://floating-reaches-50695.herokuapp.com/api/v2/incidents',{
        headers:{
            Accept:'application/json',
            'Content-type':'application/json',
            'mode':'cors',
            Authorization: "Bearer " + token
        }
        })
        .then((response) => response.json())
        .then((data) => {
            console.log(data.data[0]["createdBy"])
            if(data.status === 200){
                let table = document.getElementById("redflags");
                let allRecords = data.data;
                let userRecords = allRecords.filter(userRecord => {
                    return userRecord.createdBy == user_id;
                })
                let records = userRecords;
                console.log(records)
                records.map((record) => {
                    let new_row = table.insertRow();
                    // console.log(record.id);
                    
                    let id = new_row.insertCell(0)
                    let comment = new_row.insertCell(1);
                    let createdOn = new_row.insertCell(2);
                    let incidentType = new_row.insertCell(3);
                    let location = new_row.insertCell(4);
                    let status = new_row.insertCell(5);
                    let edit = new_row.insertCell(6);
                    let del = new_row.insertCell(7);
                    let viewRecord= new_row.insertCell(8);

                    id.innerHTML = records.indexOf(record) + 1;
                    comment.innerHTML = record.comment;
                    createdOn.innerHTML = record.createdOn;
                    incidentType.innerHTML =record.incidentType;
                    location.innerHTML =record.location;                  
                    status.innerHTML = record.status;
                    edit.innerHTML = "<a href='update-record.html?recordId="+ record.id +"'>Edit</a>";
                    del.innerHTML = "<a href=\"record.html\">Delete</a>";
                    viewRecord.innerHTML = "<a href='record.html?recordId="+ record.id +"'>View</a>";
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

