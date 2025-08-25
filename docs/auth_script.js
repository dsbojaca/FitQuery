// Detectar entorno
const isLocalhost = window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1";

// 🔥 Cambia esta URL por la de tu backend en Render
const BACKEND_URL = isLocalhost
    ? "http://127.0.0.1:8000"
    : "https://fitquery-sn0r.onrender.com";

// Base de autenticación
const AUTH_BASE = `${BACKEND_URL}/auth`;

let accessToken = localStorage.getItem("access_token") || null;

// Utils
const $ = (id) => document.getElementById(id);
const showOutput = (msg, data = null) => {
    const out = $("output");
    if (!out) return;
    out.textContent = data ? `${msg}\n` + JSON.stringify(data, null, 2) : msg;
};

// ---------- REGISTRO ----------
const registerForm = $("registerForm");
if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = $("registerUsername").value.trim();
        const email = $("registerEmail").value.trim();
        const password = $("registerPassword").value;

        try {
            // 1) Registrar
            const res = await fetch(`${AUTH_BASE}/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, email, password }),
            });

            const data = await res.json();

            if (!res.ok) {
                const msg = data?.detail || "Error al registrarse";
                showOutput(`❌ ${msg}`);
                return;
            }

            showOutput("✅ Registro exitoso. Autenticando...");

            // 2) Auto-login tras registro
            const loginRes = await fetch(`${AUTH_BASE}/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            const loginData = await loginRes.json();

            if (!loginRes.ok || !loginData?.access_token) {
                const msg = loginData?.detail || "No se pudo iniciar sesión tras registrarse";
                showOutput(`❌ ${msg}`);
                return;
            }

            accessToken = loginData.access_token;
            localStorage.setItem("access_token", accessToken);

            showOutput("✅ Registrado y autenticado. Redirigiendo a /inicio...");
            window.location.href = "inicio.html"; // frontend redirige a inicio.html
        } catch (err) {
            console.error(err);
            showOutput("❌ Error de red o servidor al registrarse");
        }
    });
}

// ---------- LOGIN ----------
const loginForm = $("loginForm");
if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const username = $("loginUsername").value.trim();
        const password = $("loginPassword").value;

        try {
            const res = await fetch(`${AUTH_BASE}/login`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ username, password }),
            });

            const data = await res.json();

            if (!res.ok || !data?.access_token) {
                const msg = data?.detail || "Usuario o contraseña incorrectos";
                showOutput(`❌ ${msg}`);
                return;
            }

            accessToken = data.access_token;
            localStorage.setItem("access_token", accessToken);

            showOutput("✅ Login exitoso. Cargando /inicio...");

            // Pedir /inicio con token
            const token = localStorage.getItem("access_token");
            try {
                const res = await fetch(`${BACKEND_URL}/inicio`, {
                    headers: { Authorization: `Bearer ${token}` }
                });

                if (!res.ok) {
                    showOutput("❌ No autorizado para /inicio");
                    return;
                }

                // Si estás en GitHub Pages, mejor redirigir a inicio.html
                const html = await res.text();
                document.open();
                document.write(html);
                document.close();
            } catch (err) {
                console.error(err);
                showOutput("❌ Error cargando /inicio");
            }
        } catch (err) {
            console.error(err);
            showOutput("❌ Error de red o servidor al iniciar sesión");
        }
    });
}

// ---------- PERFIL (opcional para pruebas) ----------
const profileBtn = $("getProfile");
if (profileBtn) {
    profileBtn.addEventListener("click", async () => {
        const token = localStorage.getItem("access_token");
        if (!token) {
            showOutput("⚠️ Primero inicia sesión");
            return;
        }
        try {
            const res = await fetch(`${AUTH_BASE}/me`, {
                method: "GET",
                headers: { Authorization: `Bearer ${token}` },
            });
            const data = await res.json();
            if (!res.ok) {
                showOutput(`❌ Error perfil: ${data?.detail || "Desconocido"}`);
                return;
            }
            showOutput("👤 Perfil:", data);
        } catch (err) {
            console.error(err);
            showOutput("❌ Error de red al obtener perfil");
        }
    });
}