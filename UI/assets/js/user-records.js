window.onload = function () {
  getRecords();

  function getRecords() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const user_id = localStorage.getItem('user_id');
    const role = localStorage.getItem('role');
    console.log(user_id);
    console.log(role);

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/incidents', {
      headers: {
        Accept: 'application/json',
        'Content-type': 'application/json',
        mode: 'cors',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': '*',
        Authorization: `Bearer ${  token}`,
      },
    })
      .then(response => response.json())
      .then((data) => {
        if (data.status === 200 && role == 'true') {
          const table = document.getElementById('redflags');
          const records = data.data;
          console.log(records);
          records.map((record) => {
            const new_row = table.insertRow();

            const id = new_row.insertCell(0);
            const comment = new_row.insertCell(1);
            const createdOn = new_row.insertCell(2);
            const incidentType = new_row.insertCell(3);
            const location = new_row.insertCell(4);
            const image = new_row.insertCell(5);
            const status = new_row.insertCell(6);
            const viewRecord = new_row.insertCell(7);

            id.innerHTML = records.indexOf(record) + 1;
            comment.innerHTML = record.comment;
            createdOn.innerHTML = record.createdOn;
            incidentType.innerHTML = record.incidentType;
            location.innerHTML = record.location;
            image.innerHTML = record.image[0];
            status.innerHTML = record.status;
            viewRecord.innerHTML = `<a href='record.html?recordId=${record.id}'>View</a>`;
          });
        } else if (data.status === 200) {
          const table = document.getElementById('redflags');
          const allRecords = data.data;
          const userRecords = allRecords.filter(userRecord => userRecord.createdBy == user_id);
          const records = userRecords;
          console.log(records);
          records.map((record) => {
            console.log(record.image[0]);
            const new_row = table.insertRow();

            const id = new_row.insertCell(0);
            const comment = new_row.insertCell(1);
            const createdOn = new_row.insertCell(2);
            const incidentType = new_row.insertCell(3);
            const location = new_row.insertCell(4);
            const image = new_row.insertCell(5);
            const status = new_row.insertCell(6);
            const viewRecord = new_row.insertCell(7);

            id.innerHTML = records.indexOf(record) + 1;
            comment.innerHTML = record.comment;
            createdOn.innerHTML = record.createdOn;
            incidentType.innerHTML = record.incidentType;
            location.innerHTML = record.location;
            image.innerHTML = record.image[0];
            status.innerHTML = record.status;
            viewRecord.innerHTML = `<a href='record.html?recordId=${record.id}'>View</a>`;
          });
        } else if (message === 'Token has expired') {
          window.alert('Please log in');
          window.location.replace('index.html');
        } else {
          window.alert('Please log in');
          window.location.replace('index.html');
        }
      });
  }
};
