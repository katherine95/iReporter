describe('Testing the functionality, this is the checklist', ()=>{
  let e = event;
    it('should create a new user', () => {
    })
    it('should log in a user', ()=>{
      let token = "";
      // let button = document.getElementById('redflags');
      login(e);
      event = {
        type: 'submit',
        stopPropagation: function () {},
        preventDefault: function () {}
        };
      token = localStorage.getItem(token);
      // button.addEventListener('submit', function(e){
        // let table = document.getElementById("redflags");
        // let comment = new_row.insertCell(1);

        // e.preventDefault();
        expect(token).toBe(token);
      });
    })
    it('should create a new record', ()=>{
      //...
  })