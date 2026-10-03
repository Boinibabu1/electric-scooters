console.log("VoltRide website loaded");

const buttons = document.querySelectorAll(".card button");

buttons.forEach(function(button) {

    button.addEventListener("click", function() {

        alert("Thank you for your interest in VoltRide!");

    });

});
