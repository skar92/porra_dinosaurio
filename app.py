import streamlit as st
import streamlit.components.v1 as components

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="La Web de JUAN", layout="centered")
st.title("🧩 La Web de JUAN")

# --- LÓGICA DE ESTADO ---
if 'score_final' not in st.session_state: st.session_state.score_final = 0
if 'juego_terminado' not in st.session_state: st.session_state.juego_terminado = False

# --- CÓDIGO DEL JUEGO (TODO AQUÍ) ---
html_code = """
<canvas id="runnerCanvas" width="600" height="200" style="background:#111; border-radius:8px; width:100%;"></canvas>
<script>
    const canvas = document.getElementById('runnerCanvas');
    const ctx = canvas.getContext('2d');
    let score = 0, gameOver = false, gameStarted = false, gameSpeed = 6;
    let obstacles = [];
    
    const img = new Image();
    // Ruta relativa a la carpeta static en la raíz
    img.src = 'static/ChatGPT Image 18 jun 2026, 14_36_28.png';
    
    const juan = { x: 60, y: 135, w: 50, h: 50, vy: 0, gravity: 0.8, jumpForce: -13, isGrounded: true };

    function triggerJump() {
        if (!gameStarted) { gameStarted = true; return; }
        if (juan.isGrounded) { juan.vy = juan.jumpForce; juan.isGrounded = false; }
    }

    window.addEventListener('keydown', (e) => { if(e.code==='Space') triggerJump(); });
    canvas.addEventListener('click', triggerJump);

    function loop() {
        if (gameStarted && !gameOver) {
            juan.vy += juan.gravity; juan.y += juan.vy;
            if (juan.y >= 135) { juan.y = 135; juan.vy = 0; juan.isGrounded = true; }
            
            if (Math.random() < 0.03) obstacles.push({x: 600, y: 160, w: 20, h: 40});
            
            obstacles.forEach((o, i) => {
                o.x -= gameSpeed;
                gameSpeed += 0.002;
                if (o.x < juan.x + juan.w && o.x + o.w > juan.x && juan.y + juan.h > 160) {
                    gameOver = true;
                }
                if (o.x < -20) { obstacles.splice(i, 1); score++; }
            });
        }
        
        ctx.clearRect(0,0,600,200);
        try { ctx.drawImage(img, juan.x, juan.y, juan.w, juan.h); } 
        catch(e) { ctx.fillStyle = 'green'; ctx.fillRect(juan.x, juan.y, juan.w, juan.h); }
        
        ctx.fillStyle = 'red';
        obstacles.forEach(o => ctx.fillRect(o.x, o.y, o.w, o.h));
        
        ctx.fillStyle = 'white';
        ctx.font = '16px Arial';
        ctx.fillText('SCORE: ' + score, 10, 20);
        ctx.fillText('KANE: 2 GOLES', 470, 20);
        
        if (!gameStarted) ctx.fillText('CLIC O ESPACIO PARA EMPEZAR', 180, 100);
        if (gameOver) ctx.fillText('GAME OVER - RECARGA PARA REINTENTAR', 150, 100);
        requestAnimationFrame(loop);
    }
    loop();
</script>
"""

# --- ESTRUCTURA ---
tab1, tab2 = st.tabs(["🧩 Sopa de Letras", "🕹️ Runner de Juan"])

with tab1:
    st.header("Sopa de Letras")
    st.write("Tu sopa de letras aquí.")

with tab2:
    st.subheader("🕹️ ¡Competición: El Runner de JUAN!")
    components.html(html_code, height=250)
