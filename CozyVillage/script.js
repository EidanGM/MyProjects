function showGameView(username) {
    // Ocultamos todas las tarjetas de autenticación
    document.getElementById('main-card').classList.add('hidden');
    document.getElementById('register-card').classList.add('hidden');
    document.getElementById('login-card').classList.add('hidden');

    // Mostramos la vista del juego
    document.getElementById('game-view').classList.remove('hidden');

    console.log("Welcome", username);
}

function handleLogin() {
    console.log("Tu mensaje aquí");
    document.getElementById('main-card').classList.add('hidden');
    document.getElementById('register-card').classList.add('hidden');
    document.getElementById('login-card').classList.remove('hidden');
}

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

function processLogin(event) {
    event.preventDefault();

    const usernameInput = document.getElementById('login-username').value.trim();
    const passwordInput = document.getElementById('login-password').value;
    const errorElement = document.getElementById('login-error');

    errorElement.textContent = "";

    // 1. Cargar lista de usuarios desde localStorage
    let registeredUsers = JSON.parse(localStorage.getItem('cozyUsers')) || [];

    // 2. Buscar si el usuario existe y coincide la contraseña
    const userFound = registeredUsers.find(
        user => user.username === usernameInput && user.password === passwordInput
    );

    if (!userFound) {
        errorElement.textContent = "Error: Invalid username or password.";
        return;
    }

    // 3. Limpiar formulario
    document.getElementById('login-form').reset();

    // 4. Entrar al juego usando la función reutilizable
    showGameView(userFound.username);
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

    // Guardamos el usuario
    registeredUsers.push({ username: usernameInput, password: passwordInput });
    localStorage.setItem('cozyUsers', JSON.stringify(registeredUsers));

    // Limpiamos los campos del formulario
    document.getElementById('register-form').reset();
    
    // Llamamos a la función compartida
    showGameView(usernameInput);
}

function handleGuest() {
    showGameView("Guest");
}