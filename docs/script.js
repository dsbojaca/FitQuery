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

    const response = await fetch(`${API_BASE_URL}/ejercicios?${params.toString()}`);
    const data = await response.json();

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
});