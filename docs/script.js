const API_BASE_URL = "https://fitquery-sn0r.onrender.com";

// Cargar opciones de autocompletado al iniciar
document.addEventListener("DOMContentLoaded", async () => {
    await cargarOpciones("nombre", "lista_nombres");
    await cargarOpciones("grupo_muscular", "lista_grupos");
    await cargarOpciones("dificultad", "lista_dificultades");
});

// Función para llenar un <datalist> con opciones únicas desde el backend
async function cargarOpciones(campo, datalistId) {
    try {
        const response = await fetch(`${API_BASE_URL}/ejercicios`);
        const data = await response.json();
        const opciones = [...new Set(data.map(ex => ex[campo]))];

        const datalist = document.getElementById(datalistId);
        datalist.innerHTML = opciones
            .map(valor => `<option value="${valor}">`)
            .join("");
    } catch (error) {
        console.error(`Error cargando opciones para ${campo}:`, error);
    }
}

document.getElementById("searchForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const grupo = document.getElementById("grupo_muscular").value;
    const dificultad = document.getElementById("dificultad").value;

    const params = new URLSearchParams();
    if (nombre) params.append("nombre", nombre);
    if (grupo) params.append("grupo_muscular", grupo);
    if (dificultad) params.append("dificultad", dificultad);

    const resultsDiv = document.getElementById("results");
    const loadingMessage = document.getElementById("loadingMessage");

    // Mostrar mensaje de carga
    loadingMessage.style.display = "block";
    resultsDiv.innerHTML = "";

    try {
        console.log("Enviando petición a:", `${API_BASE_URL}/ejercicios?${params.toString()}`);

        const response = await fetch(`${API_BASE_URL}/ejercicios?${params.toString()}`);

        // Ocultar mensaje de carga
        loadingMessage.style.display = "none";

        if (!response.ok) {
            console.error("Error en la respuesta del backend:", response.status, response.statusText);
            resultsDiv.innerHTML = "<p style='color:red;'>⚠️ Error al obtener los ejercicios.</p>";
            return;
        }

        const data = await response.json();
        console.log("Datos recibidos:", data);

        if (data.length === 0) {
            resultsDiv.innerHTML = "<p>No se encontraron ejercicios.</p>";
            return;
        }

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
    } catch (error) {
        loadingMessage.style.display = "none";
        console.error("Error en la llamada fetch:", error);
        resultsDiv.innerHTML = "<p style='color:red;'>⚠️ Error al conectar con el servidor.</p>";
    }
});