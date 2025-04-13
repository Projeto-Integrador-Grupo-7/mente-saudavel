document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("txtPassword");
    const confirmPasswordInput = document.getElementById("txtTestPassword");
    const submitButton = document.querySelector("button[type='submit']");
    const feedback = document.getElementById("password-feedback");
    const passwordCard = document.getElementById("password-card");
    const emailInput = document.getElementById("txtEmail");
    const emailFeedback = document.getElementById("email-feedback");
    const dataNascimentoInput = document.getElementById("dtpDataNascimento");

    const requiredFields = [
        "txtNome",
        "txtEmail",
        "txtPassword",
        "txtTestPassword",
        "dtpDataNascimento",
    ];

    if (!passwordInput || !confirmPasswordInput || !submitButton || !feedback || !passwordCard) return;

    // Configurações iniciais
    dataNascimentoInput.max = new Date().toISOString().split("T")[0];

    // Adiciona eventos
    addEventListeners();

    function addEventListeners() {
        passwordInput.addEventListener("focus", () => toggleDisplay(passwordCard, true));
        passwordInput.addEventListener("blur", () => setTimeout(() => toggleDisplay(passwordCard, false), 200));
        passwordInput.addEventListener("input", validateForm);
        confirmPasswordInput.addEventListener("input", validateForm);
        dataNascimentoInput.addEventListener("change", validateForm);

        requiredFields.forEach(id => {
            const field = document.getElementById(id);
            if (field) field.addEventListener("input", validateForm);
        });
    }

    function validateForm(event) {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
    
        const rules = {
            length: password.length >= 8,
            uppercase: /[A-Z]/.test(password),
            lowercase: /[a-z]/.test(password),
            number: /\d/.test(password),
            symbol: /[^A-Za-z0-9]/.test(password),
        };
    
        // Atualiza as regras de senha apenas se o evento for no campo de senha ou confirmação
        if (event.target === passwordInput || event.target === confirmPasswordInput) {
            Object.entries(rules).forEach(([id, isValid]) => toggleRule(id, isValid));
    
            const senhaValida = Object.values(rules).every(Boolean);
            const senhasIguais = password === confirmPassword;
    
            toggleFeedback(
                feedback,
                null,
                senhaValida && senhasIguais,
                senhaValida ? "As senhas não coincidem." : "A senha deve atender todos os requisitos."
            );
        }
    
        const allFilled = requiredFields.every(id => {
            const field = document.getElementById(id);
            return field && field.value.trim() !== "";
        });
        const emailValido = /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(emailInput.value);
    
        toggleFeedback(
            emailFeedback,
            emailInput,
            emailValido || emailInput.value.trim() === "",
            "Email deve conter '@' e um domínio válido."
        );
    
        const senhaValida = Object.values(rules).every(Boolean);
        const senhasIguais = password === confirmPassword;
    
        submitButton.disabled = !(senhaValida && senhasIguais && allFilled && emailValido);
    }

    function toggleRule(id, isValid) {
        const element = document.getElementById(id);
        if (element) {
            element.classList.toggle("valid", isValid);
            element.classList.toggle("invalid", !isValid);
        }
    }

    function toggleFeedback(element, input, isValid, message) {
        if (!isValid) {
            element.textContent = message;
            toggleDisplay(element, true);
            if (input) input.classList.add("input-invalid");
        } else {
            toggleDisplay(element, false);
            if (input) input.classList.remove("input-invalid");
        }
    }

    function toggleDisplay(element, show) {
        element.style.display = show ? "block" : "none";
    }
});