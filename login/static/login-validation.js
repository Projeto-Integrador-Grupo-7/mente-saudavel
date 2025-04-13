document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const emailInput = document.getElementById("txt_email");
    const passwordInput = document.getElementById("txt_senha");

    form.addEventListener("submit", (event) => {
        let isValid = true;

        // Verifica se o campo de e-mail está preenchido
        if (emailInput.value.trim() === "") {
            alert("O campo de e-mail é obrigatório.");
            isValid = false;
        }

        // Verifica se o campo de senha está preenchido
        if (passwordInput.value.trim() === "") {
            alert("O campo de senha é obrigatório.");
            isValid = false;
        }        


        // Validação do e-mail
        if (!validateEmail(emailInput.value)) {
            alert("Por favor, insira um e-mail válido.");
            isValid = false;
        }

        // Impede o envio do formulário se houver erros
        if (!isValid) {
            event.preventDefault();
        }
    });

    function validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
});