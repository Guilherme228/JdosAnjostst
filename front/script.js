async function login() {
  const email = document.getElementById('email').value;
  const senha = document.getElementById('senha').value;

  if (email === '' || senha === '') {
    alert('Preencha todos os campos!');
    return;
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, senha })
    });

    const data = await response.json();

    if (response.ok) {
      localStorage.setItem('token', data.token);
      localStorage.setItem('email', data.email);
      alert('Login realizado com sucesso!');
    } else {
      alert('Email ou senha incorretos!');
    }

  } catch (error) {
    alert('Erro ao conectar com o servidor. Verifique se o backend está rodando.');
  }
}