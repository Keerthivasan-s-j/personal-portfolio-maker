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

    // Confermation for delete operation
    document.querySelectorAll(".del_form").forEach(form => {
        form.addEventListener("submit", function(event){
            user_conf = confirm("Are you sure you want to delete this?");
            if (!user_conf){
                event.preventDefault();
            }
        });
    });
});
