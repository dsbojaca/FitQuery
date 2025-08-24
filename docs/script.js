// Detectar entorno y definir la URL base del backend
const API_BASE_URL =
    location.hostname === "127.0.0.1" || location.hostname === "localhost"
        ? "http://127.0.0.1:8000" // backend local
        : "https://fitquery-sn0r.onrender.com"; // backend en Render

console.log("Backend usado:", API_BASE_URL);

// ✅ 1. Verificar si hay token antes de cargar la página
const token = localStorage.getItem("access_token");
if (!token) {
    // Si no hay token, redirige a la página de login
    window.location.href = "auth.html";
}

// ✅ 2. Proteger las peticiones con el token
document.getElementById("searchForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    // Mostrar overlay
    document.getElementById("loadingOverlay").style.display = "flex";

    const nombre = document.getElementById("nombre").value.trim();
    const grupo = document.getElementById("grupo_muscular").value.trim();
    const dificultad = document.getElementById("dificultad").value.trim();

    const params = new URLSearchParams();
    if (nombre) params.append("nombre", nombre);
    if (grupo) params.append("grupo_muscular", grupo);
    if (dificultad) params.append("dificultad", dificultad);

    try {
        const response = await fetch(`${API_BASE_URL}/ejercicios?${params.toString()}`, {
            headers: {
                "Authorization": `Bearer ${token}` // 🔑 Token en headers
            }
        });

        if (response.status === 401) {
            alert("Sesión expirada. Inicia sesión nuevamente.");
            localStorage.removeItem("access_token");
            window.location.href = "auth.html";
            return;
        }

        if (!response.ok) {
            alert("Error al obtener los ejercicios. Intenta de nuevo.");
            return;
        }

        const data = await response.json();
        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No se encontraron ejercicios.</p>";
        } else {
            data.forEach(ex => {
                const div = document.createElement("div");
                div.classList.add("exercise");
                div.innerHTML = `
                    <h3>${ex.nombre}</h3>
                    <p><strong>Grupo muscular:</strong> ${ex.grupo_muscular}</p>
                    <p><strong>Dificultad:</strong> ${ex.dificultad}</p>
                    <p><strong>Instrucciones:</strong> ${ex.instrucciones}</p>
                `;
                resultsDiv.appendChild(div);
            });
        }

    } catch (error) {
        console.error("Error:", error);
        alert("Error al conectar con el servidor.");
    } finally {
        // Ocultar overlay después de 2 segundos
        setTimeout(() => {
            document.getElementById("loadingOverlay").style.display = "none";
        }, 2000);
    }
});