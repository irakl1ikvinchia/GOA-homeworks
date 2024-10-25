const request = JSON("https://jsonplaceholder.typicode.com/todos", {
      .then(data => {
        console.log(data); // ბეჭდავს მიღებულ მონაცემებს
      })
      .catch(error => {
        console.error('problem:', error); // გამოაქვს შეცდომა, თუ რაიმე პრობლემა წარმოიშვა
      })
    
  });

  console.log(request);