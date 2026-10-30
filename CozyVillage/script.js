function handleRegister() {
    const mainCard = document.getElementById('main-card');
    const registerCard = document.getElementById('register-card');

    if (mainCard && registerCard) {
        mainCard.classList.add('hidden');
        registerCard.classList.remove('hidden');
    }
}

// Para el botón "Back", por si el jugador quiere regresar al menú principal
function showMainView() {
    const mainCard = document.getElementById('main-card');
    const registerCard = document.getElementById('register-card');

    if (mainCard && registerCard) {
        registerCard.classList.add('hidden');
        mainCard.classList.remove('hidden');
    }
}

// Función que procesa y valida el registro del usuario
function processRegister(event) {
    // 1. Evitamos que la página se recargue por defecto
    event.preventDefault();

    // 2. Capturamos los valores de los inputs y del elemento de error
    const usernameInput = document.getElementById('reg-username').value.trim();
    const passwordInput = document.getElementById('reg-password').value;
    const confirmInput = document.getElementById('reg-confirm').value;
    const errorElement = document.getElementById('register-error');

    // Limpiamos cualquier error anterior en pantalla
    errorElement.textContent = "";

    // 3. Validación: Verificar que el nombre de usuario no esté vacío
    if (usernameInput === "") {
        errorElement.textContent = "Error: Username cannot be empty.";
        return;
    }

    // 4. Validación: Verificar que las contraseñas coincidan
    if (passwordInput !== confirmInput) {
        errorElement.textContent = "Error: Passwords do not match.";
        return;
    }

    // 5. Validación: Verificar si el usuario ya existe en el almacenamiento local
    let registeredUsers = JSON.parse(localStorage.getItem('cozyUsers')) || [];
    
    const userExists = registeredUsers.some(user => user.username === usernameInput);
    if (userExists) {
        errorElement.textContent = "Error: Username is already taken.";
        return;
    }

    // 6. Si todo pasa las validaciones, guardamos el nuevo usuario
    registeredUsers.push({ username: usernameInput, password: passwordInput });
    localStorage.setItem('cozyUsers', JSON.stringify(registeredUsers));

    console.log("¡Registro exitoso para el usuario:", usernameInput);
    alert("Account created successfully!");
    
    // Limpiamos el formulario y regresamos a la tarjeta principal
    document.getElementById('register-form').reset();
    showMainView();
}