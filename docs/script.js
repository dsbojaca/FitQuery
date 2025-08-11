const API_BASE_URL = "https://fitquery-sn0r.onrender.com";

document.getElementById("searchForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const nombre = document.getElementById("nombre").value;
    const grupo = document.getElementById("grupo_muscular").value;
    const dificultad = document.getElementById("dificultad").value;

    const params = new URLSearchParams();
    if (nombre) params.append("nombre", nombre);
    if (grupo) params.append("grupo_muscular", grupo);
    if (dificultad) params.append("dificultad", dificultad);

    try {
        console.log("Enviando petición a:", `${API_BASE_URL}/ejercicios?${params.toString()}`);

        const response = await fetch(`${API_BASE_URL}/ejercicios?${params.toString()}`);

        if (!response.ok) {
            console.error("Error en la respuesta del backend:", response.status, response.statusText);
            alert("Error al obtener los ejercicios. Intenta de nuevo.");
            return;
        }

        const data = await response.json();
        console.log("Datos recibidos:", data);

        const resultsDiv = document.getElementById("results");
        resultsDiv.innerHTML = "";

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
        console.error("Error en la llamada fetch:", error);
        alert("Error al conectar con el servidor. Revisa la consola para más detalles.");
    }
});