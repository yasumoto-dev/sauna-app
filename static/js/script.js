function openDeleteModal(reviewId){
    const modal = document.getElementById("deleteModal");
    const form = document.getElementById("deleteForm");

    form.action = `/review/${reviewId}/delete`;
    modal.style.display = "flex";
}

function closeDeleteModal(){
    const modal = document.getElementById("deleteModal");
    modal.style.display = "none";
}