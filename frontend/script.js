
const API_URL = "https://processo-seletivo-rede-alpha-fitness.onrender.com/dados";

async function carregarDados() {
    try {
        const res = await fetch(API_URL);
        const novosDados = await res.json();

        dadosGlobais = novosDados;

        const pesquisaInput = document.getElementById("pesquisa").value.toLowerCase();

        if (pesquisaInput) {
            filtrarTabela();
        } else {
            renderTabela(dadosGlobais); 
        }

    } catch (err) {
        console.error("Erro ao buscar dados:", err);
    }
}

//renderiza a tabela, recebendo dados e pesquisa
function renderTabela(dados, pesquisa = "") {
    const cabecalho = document.getElementById("cabecalho");
    cabecalho.innerHTML = "";
    if (dados.length > 0) {
        cabecalho.innerHTML = `<tr>${Object.keys(dados[0]).map(c => `<th>${c}</th>`).join("")}</tr>`;
    }

    const corpo = document.getElementById("corpo");
    corpo.innerHTML = "";
    const fragment = document.createDocumentFragment();

    dados.forEach(linha => {
        const tr = document.createElement("tr");
        Object.values(linha).forEach(val => {
            const td = document.createElement("td");
            let texto = val.toString();
            if (pesquisa && texto.toLowerCase().includes(pesquisa)) {
                const regex = new RegExp(pesquisa, "gi");
                td.innerHTML = texto.replace(regex, match => `<mark>${match}</mark>`);
            } else {
                td.textContent = texto;
            }
            tr.appendChild(td);
        });
        fragment.appendChild(tr);
    });

    corpo.appendChild(fragment);
}

function filtrarTabela() {
    const input = document.getElementById("pesquisa").value.toLowerCase();
    const linhas = document.getElementById("corpo").getElementsByTagName("tr");

    for (let i = 0; i < linhas.length; i++) {
        const tds = linhas[i].getElementsByTagName("td");
        let encontrado = false;

        for (let j = 0; j < tds.length; j++) {
            if (tds[j].textContent.toLowerCase().includes(input)) {
                encontrado = true;
                break;
            }
        }

        linhas[i].style.display = encontrado ? "" : "none";
    }
}

carregarDados();

setInterval(carregarDados, 5000);
