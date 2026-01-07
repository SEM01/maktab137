
const url = "https://dummyjson.com/users";
const root = document.getElementById("app");
const card = (img, desc, name, email,state) => {return `
<div class="card" style="width: 18rem;">
  <img src=${img} class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">${name}</h5>
    <p>${email}</p>
    <p>${state}</p>
    <p>${desc}</p>
    

  </div>
</div>
`};

const getproduct = async () => {
    const res = await fetch(url);
    if (res.ok) {
        const data = await res.json();
        console.log(data.users);
        const mappedproduct = data.users.map( (user) => card(user.image , user.address.address, user.firstName+" "+user.lastName, user.email, user.address.state));   
        root.innerHTML=(mappedproduct.join(""));
    }
};

getproduct();