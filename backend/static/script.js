const imageInput = document.getElementById("imageInput");
const originalImg = document.getElementById("originalImg");
const resultImg = document.getElementById("resultImg");
const statusText = document.getElementById("statusText");

/* Show original image instantly */
imageInput.addEventListener("change", () => {
  const file = imageInput.files[0];
  if (!file) return;

  originalImg.src = URL.createObjectURL(file);
  resultImg.src = "";
});

/* Call backend dehaze API */
function dehazeImage() {
  const file = imageInput.files[0];
  if (!file) {
    alert("Please select an image first!");
    return;
  }

  statusText.classList.remove("hidden");
  statusText.innerText = "Processing image...";

  const formData = new FormData();
  formData.append("image", file);

  fetch("/dehaze", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
      statusText.classList.add("hidden");
      if (data.image) {
        resultImg.src = "data:image/png;base64," + data.image;
      } else {
        alert("Processing failed");
      }
    })
    .catch(err => {
      statusText.innerText = "Server error!";
      console.error(err);
    });
}
