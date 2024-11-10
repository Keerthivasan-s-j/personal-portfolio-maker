document.addEventListener("DOMContentLoaded", function() {
    document.querySelector(".user-profile-dropdown").onclick = toggleDropDown;
    function toggleDropDown(){
        var parent = document.querySelector(".user-profile-dropdown");
        var dropDownMenu = document.querySelector(".dropdown-menu");
        var dropDownIcon = parent.querySelector("i");
        if (dropDownMenu.style.display === "" || dropDownMenu.style.display === "none"){
            dropDownMenu.style.display = "flex";
            dropDownIcon.classList.replace("fa-chevron-down", "fa-chevron-up");
        }
        else{
            dropDownMenu.style.display = "none";
            dropDownIcon.classList.replace("fa-chevron-up", "fa-chevron-down");
        }
    }
});
