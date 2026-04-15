async function registrar() {
    const usuario = document.getElementById('usuario').value;
    const email = document.getElementById('email').value;
    const senha = document.getElementById('senha').value;
    const confirmar = document.getElementById('confirmar').value;

    if (!usuario || !email || !senha || !confirmar) {
        alert('Preencha todos os campos');
        return;
    }

    if (senha !== confirmar) {
        alert('As senhas não coincidem');
        return;
    }

    try {
        const response = await fetch('http://localhost:3000/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ usuario, email, senha })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Conta criada com sucesso!');
            window.location.href = 'index.html';
        } else {
            alert(data.error);
        }

    } catch {
        alert('Erro ao conectar ao servidor');
    }
}

    document.getElementById('registrarBtn').addEventListener('click', registrar);