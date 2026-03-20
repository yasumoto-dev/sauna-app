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

document.addEventListener("DOMContentLoaded", function(){
    const form = document.getElementById("reviewForm");
    const submitButton = document.getElementById("submitButton");

    if(!form) return;

    form.addEventListener("submit", function(event){
        if (form.dataset.submitted == "true") {
            event.preventDefault();
            return;
        }

        form.dataset.submitted = "true"

        if (submitButton) {
            submitButton.disabled = true;
            submitButton.textContent = "送信中…";
        }
    });
});