function toggleDrop(dropid, iconId, dropQid) {
    let dropdown = document.getElementById(dropid);
    let icon = document.getElementById(iconId);
    let dropQ = document.getElementById(dropQid);

    if (dropdown.style.display === "block") {
        dropdown.style.display = "none";
        dropdown.style.opacity = 0;
        icon.classList.remove("rotated");
        dropQ.classList.remove("noneborder");
        dropdown.classList.add("noneborder")
    } else {
        dropdown.style.display = "block";
        dropQ.classList.add("noneborder");
        icon.classList.add("rotated");
        dropdown.classList.remove("noneborder")
        setTimeout(function () {
            dropdown.style.opacity = 1;
        }, 100);
    }
}
