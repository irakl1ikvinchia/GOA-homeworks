function varr() {
    var x = 10; 
    if (true) {
        var x = 20; // იგივე x, შეიცვლის მნიშვნელობას
        console.log(x); // 20
    }
    console.log(x); // 20
};

function lett() {
    let x = 10; 
    if (true) {
        let x = 20; // ახალი x, ბლოკის შიგნით
        console.log(x); 
    }
    console.log(x);
};

function constt() {
    const x = 10; // ლოკალური
    if (true) {
        const y = 20; // ახალი y, ბლოკის შიგნით
        console.log(y); 
    }
};