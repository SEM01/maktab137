const url = "https://dummyjson.com/users";
fetch(url)
    .then((response) => {
        if (response.ok) {
            return response.json();
        }
    })
    .then((resjson) => {
        console.log(resjson);
    })

