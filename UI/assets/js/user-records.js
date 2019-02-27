
/* eslint-disable no-undef */
/* eslint-disable func-names */
/* eslint-disable no-use-before-define */
// import { login } from './index';

window.onload = function () {
  getRecords();

  function getRecords() {
    const token = localStorage.getItem('token');
    const message = localStorage.getItem('message');
    const user_id = localStorage.getItem('user_id');
    const role = localStorage.getItem('role');
    const username = localStorage.getItem('username');
    document.getElementById('username').innerHTML = username;
    console.log(username);

    fetch('https://floating-reaches-50695.herokuapp.com/api/v2/incidents', {
      headers: {
        Accept: 'application/json',
        'Content-type': 'application/json',
        mode: 'cors',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': '*',
        Authorization: `Bearer ${token}`,
      },
    })
      .then(response => response.json())
      .then((data) => {
        if (data.status === 200 && role == 'true') {
          const table = document.getElementById('redflags');
          const records = data.data;
          document.getElementById('incidents').innerHTML = records.length;
          document.getElementById('redflag').innerHTML = records.filter(redflag => redflag.incidentType === 'Redflag').length;
          document.getElementById('intervention').innerHTML = records.filter(intervention => intervention.insertCell === 'Intervention').length;
          console.log(records);
          records.map((record) => {
            const new_row = table.insertRow();

            const id = new_row.insertCell(0);
            const comment = new_row.insertCell(1);
            const createdOn = new_row.insertCell(2);
            const incidentType = new_row.insertCell(3);
            const location = new_row.insertCell(4);
            const status = new_row.insertCell(5);
            const viewRecord = new_row.insertCell(6);

            id.innerHTML = records.indexOf(record) + 1;
            comment.innerHTML = record.comment;
            createdOn.innerHTML = record.createdOn;
            incidentType.innerHTML = record.incidentType;
            location.innerHTML = record.location;
            status.innerHTML = record.status;
            viewRecord.innerHTML = `<a href='record.html?recordId=${record.id}'>View</a>`;
          });
        } else if (data.status === 200) {
          const table = document.getElementById('redflags');
          const allRecords = data.data;
          const userRecords = allRecords.filter(userRecord => userRecord.createdBy == user_id);
          const records = userRecords;
          document.getElementById('incidents').innerHTML = records.length;
          document.getElementById('resolved').innerHTML = records.filter(resolved => resolved.status === 'resolved').length;
          document.getElementById('inDraft').innerHTML = records.filter(resolved => resolved.status === 'inDraft').length;
          document.getElementById('rejected').innerHTML = records.filter(resolved => resolved.status === 'rejected').length;
          console.log(records);
          records.map((record) => {
            console.log(record.image[0]);
            const new_row = table.insertRow();

            const id = new_row.insertCell(0);
            const comment = new_row.insertCell(1);
            const createdOn = new_row.insertCell(2);
            const incidentType = new_row.insertCell(3);
            const location = new_row.insertCell(4);
            const status = new_row.insertCell(5);
            const viewRecord = new_row.insertCell(6);

            id.innerHTML = records.indexOf(record) + 1;
            comment.innerHTML = record.comment;
            createdOn.innerHTML = record.createdOn;
            incidentType.innerHTML = record.incidentType;
            location.innerHTML = record.location;
            status.innerHTML = record.status;
            viewRecord.innerHTML = `<a href='record.html?recordId=${record.id}'>View</a>`;
          });
          setTimeout(() => {
            window.location.replace('index.html');
          }, 300000);
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
setTimeout(() => {
  window.location.replace('index.html');
}, 250000);
