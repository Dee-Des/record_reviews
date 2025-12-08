const editButtons = document.getElementsByClassName("btn-edit");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    // Get value from the button attribute
    let ratingValue = e.target.getAttribute("data-review_rating");  
    // Get body text only (not rating)
    let reviewContent = document
      .getElementById(`review${reviewId}`)
      .querySelector(".review-body").innerText;
    // Get the correct form inputs
    let reviewRatingInput = document.getElementById('id_rating'); // select
    let reviewTextInput = document.getElementById('id_body'); //textarea
    // Prepopulate fields
    reviewRatingInput.value = ratingValue;   // selects the matching option
    reviewTextInput.value = reviewContent;   // fills in the body text
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}


/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific review.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}