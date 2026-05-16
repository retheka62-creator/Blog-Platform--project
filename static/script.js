function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")) {
        localStorage.setItem("theme", "dark");
    } else {
        localStorage.setItem("theme", "light");
    }
}

window.onload = function() {
    if(localStorage.getItem("theme") === "dark") {
        document.body.classList.add("dark-mode");
    }
}

function showCustomCategory() {
    const category = document.getElementById("categorySelect").value;
    const customInput = document.getElementById("customCategory");

    if(category === "Other") {
        customInput.style.display = "block";
        customInput.required = true;
    } else {
        customInput.style.display = "none";
        customInput.required = false;
    }
}