import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS Simple y Profesional
st.markdown("""
<style>
    [data-testid="stSidebar"] {display: none;}
    .main {background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);}
    .stApp {background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);}
    

    .content-box {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        margin: 15px 0;
    }
    
    .header-box {
        text-align: center;
        padding: 50px 20px;
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        margin-bottom: 30px;
        border: 2px solid rgba(255,255,255,0.3);
    }
    
    h1 {
        color: white !important; 
        text-shadow: 3px 3px 8px rgba(0,0,0,0.4);
        font-size: 3em !important;
    }
    
    h2, h3 {
        color: white !important; 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
    }
    
    .normativa-card {
        background: white;
        padding: 25px;
        border-radius: 12px;
        margin: 15px 0;
        border-left: 6px solid #3b82f6;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .normativa-card:hover {
        transform: translateX(10px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        border-left-color: #1e3a8a;
    }
    
    .enlace-btn {
        background: linear-gradient(135deg, #3b82f6 0%, #1e3a8a 100%);
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin: 5px;
        transition: all 0.3s;
        font-weight: bold;
    }
    
    .enlace-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(59, 130, 246, 0.5);
    }
    
    .categoria-badge {
        background: #ef4444;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.85em;
        font-weight: bold;
        display: inline-block;
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Estado
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"

# LOGO UNAM en esquina superior derecha
st.markdown("""
<div class='logo-container'>
    <img src='data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw8QDxUPEBAWEBUVFRUVFRUPDw8XFxgVFRYWFhUVFRYYHSggGBolGxYVITEhJSkrLi4uGB81ODMtNygtLisBCgoKDg0OGxAQGy4lICUtMi0tLS0uLS0tLS0rMi0vLS8vLS0tLS0tLS0tLS0tLS0tLS0tKy0tLS0tLS0tLS0tLf/AABEIAOEA4QMBEQACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAAAQMEBQYHAgj/xABMEAABAwIDBQQCDAkLBQAAAAABAAIDBBEFEiExEjRBYXEGkRQTIoFSI3JygaGxssHR8CRCUpNUYnODg5Kzw+HxFTNDdKLRJzVFotL/xAAcAQEAAgMBAQEAAAAAAAAAAAAAAQIDBAUGB//EADsRAAIBAgQCBwYFAgYDAAAAAAABAgMEEQUSITFBUQYTMmFxgZEUFSJhodHBQlLh8PEjcqKywhZTgwckYv/aAAwDAQACEQMRAD8A1vb7EqGj2T2drk2tuXkxlHBvdayf3rnVo1KVNdns/wA0eDfXf03N5+7P8Vc8zZx6T/gPpM1jrWL5H6/S+OGFHB5OfZzXCY2bU+S6BttWCi9BzrE4J6+9GrUHYp+6/wCn0vg7+JPpDZbH+FHNG1+HHBF/91n/AO5CG+pqT/U8zdxrtKmpBvflLU0P92f4q5q/eVPyT8DTxF/Cb8TyNjxv/wCk/wAl0v8A+d+8/E+BzfrfuvwZ1rZWlEEEdMDcxMGc+u/p59F3qUcscDv4bRVKj/qbeZ3zEo3ysML2ubfQgge0rVuIyhRSZsYxGNTBrbj4GJ9TU+qg/iYzezRk4wXrcNx18uuQ7PRdaL44HKp5FPpGQvNRcmfzGGm++/LkrlgdLFb1+WrKv8qvTmq52/8Ak/NX0DnVn+qfqezW1H+ql/8A5N6WlGQ4lf2U/Umm2SblupY9w+KyS+w4/wASjxUi9f08h+hIvjGxfN66T+e1HA1u0enoqHCb+dL3zFDCH+dL3zOpQ1DRFL5Iz8yyY2x6nH3rLBcdRr1pRi9eXU0faynmRoY3xxMmY3z9V9Pw2tRr4dC0mltg4p55amS+yNr8DYq72bUa+LV8ZL5MxtXm+S+tR2+uNyB0sPqyvcz30qo2uJRe17lWj89qIa1tRnjkuNCCCW9w+te2wXE40nCnUfKyffoMnWuKVFTk1K2v5mJ/mXFTf22H/an/AO63f6tp/Ej5mif1tQ/Khp6m0t8IqekCrk/4y+oz29rSqVUnVqtPm5NmD/mLF+3S/wCvJ/03K3t1F/llyPOP4tz2+7LuZS/mJPa7tN+9k/6a11e08eMPhXzNSfSG0X5H6EfqtR/naf8A6tP/AK7lP9RR/t9TU/iXBf8A5L0PX8ytR/nqf/mz/wD9VX+n5fj+pr/xNgn+T/3IyeGYhFQUxdGy0RIBZGCHEk3vqfiqFWp2W36k3VhGu1c1J6vxe+x6pbJ8D8b8vK+1qx1ZfvHPZh1J+X+PmUMOxMy/BWn3H5luoT0yfCwvbDd1CX6S+Zq2MLKQrWa2aO/4fbhp3LHcR6uouo7dVG5jsedJ6mWx+c37OnWOjT3OMu7T0OfRg/SlWfea9fmN9eVyXQm1sziQHXttOzdXF4Lbz7TJ3jTW3fLdzO17M0ew4SODiA0tbrkfax3LRt7RUoZlq2dHC7nt1Kz0SeDvq+HgjeKF4bJkdq2Sm4A6Nb5rtU3ls8Te6TW/s8Zp0pPV0sGvc9X9xUgDRU12nzNF9/0H42F/NZZ5c1beOwuNPZ+mW66o18WoqKmxB9aQx7W38jyXRw7DcNoOV25Zksd17F0+E8OsbWc7rEG2vy3I1RdTYGbTEDGvdG5zmS5LN43AaH4VutRp0Y1E9WsMRzXtWE3Gy4LwNrHxOBVW9b/m4mr0lq5K1GHU/c9TCVxDW0YIzAmSo7t34/Vda8oqM4S5xjJ+XFfPvNeq1ChnXC58y6xGMPptsDh+Eo6aEdp6LBWa6i80uSM8FnxiMeUWtT2fGRiXRv/m7De3WT+G3++yuVakPwRb/p/I24rI/j73Jfrs/kfn/pV5oa/mfmPr/W/dfgzq2ytKYoGQO0cxuQ+mPVdb4aaPZ4TTSwWl1cMrfM6NVKh68ZwQr7c0KQFtX4lFSxmSQ2aNegUNpF0aU6sssUSFrM+l7Eyfv9B/dg/Zyf9V4vC1nurfh9TT6VavvX3F7VtGcTpqBLmNNTl44YTqFqYi8tLuPE+7Njg/Cl2Hd6afU9x+0PAh6L5vi7Ls35N8jDj7w6j9D8/wA9zGzOJ1Y4ixx5IorXTrHxOq12T6aJAFQkQFBPRXqb6lkfRCmBr5z3qKAj4jZm0WYa8dbLKkV0M9Rh4DmwRDMx/gy7S0O/dJ4qHHQojuqF7wAeq+R6n6Cq7WsLbBjGvIdJmGjRo0XuT6Fgx14UKaWrfBHE6TXsq9Z0c2kIqN19DctedUx2q/Vvs63q/wCZqY/f9IrtU2+GPuW/juZ6uw95o5Ga5g2w0lty5w7F17u9oXFBRW6bSZ5+vrStl5PoaRsDgwo/T3u2hKL2Xa0G29c7B6kZOp9K8zLDKr/M/cWOB0jqis0+9nAPUDuXaoUpVZ/h5nV6P29W6xONvWa01q0+CQmtPjaPHqc2JpkMzTsE5eXwfBdepBVKDXZeGXq+HkZq0cyh3nZ9laHsY+1mtzdvmrx4UYZ1t/nlw+eRq4jf9VOFGm/+70j48O/vwOXyvuynb9Jy/MdLnI4nvf1Wpe4isQqN8JepeJvU16jEKjtUXBcIc8+txMJrKqSKwuY7A2F+y62reOVR3OPUbqXtRvuu1eBhXvJPbpw8fkbqgk1rCqSR7JJJNx6rM1sjn9IasoyoUYbtvU7aFynM4qQFJAREBEQEREBERAREQEREBERB5O7qfko0DIEwRi1KOg69epqmLH8S1jjb0OWRutfQW/N+F+S3KS1bPF4lN+27nxW3Bc/1OcR6ud7z81u3H4j0PQpf+Nh7WfqabsnSFp2jq52vjxC1MLdKVS4vq1Pqn8XBJd2u+v0Zs4jNU8P8/wAYHVqZtmh1j/hVxl2jfh+AxvCKi/bfyMNsptSv3jRvmLLZuatm4dxzdP8A45gftMPl1zcOxCbCp2vp5CKqN1SHOFr3GW3gQL+Kurh1xcW0qdRZJrq9Of8A2+ZV71DtLYrvYvXtDZA/2QW+0DpcDiu3aezNPU+bXvSGrTnkg8jNqxSX37l+z+CY4Yl3h6r5XqfouaZJZnHpw6BdKis8EjlYbbdfcwj79b6Fe5PXnoUJ4o5Rsysaf8QC6S2cTDWfh6fM1bE8IoaYl0EYjJBHsm1rLn1belTlmSOnC8oU9Iq+pzPGKyB1TVMlYx8bjOA8EHJc+yvdK1rrLCNRc2cq7lFzm12m2vFnNMZppYnhtRHkkLS2S2+45rpXcadSPs80tjQ6yDT6xFKlpdTyHZfIcgGaE2+r5LbsoUpS93a/M3LpQeOx/wCF8c34KOCMtG07w4+W0fyXSrU1aV5wqcMsvOG/XvNCk+ph+LJYz4M+FtPHHI5zmts1xJ0cRa2V3ALl3Fq3cUqEemfWPu4r83c2l5RnmrU4LuJe4TUFkdXxzPkY0aaF5CtLSa8P4LyMcY9pePuRt2zNCAZabMY2lrcwGm58F0a19Kk6UGk2l+p5R1VZTaWlP+NnxXYjXw4G2QSCqJ4tXo8DwN3VpQeK1eZEQSEREBERAREQEREBERB5KgF6ZSASIrB7e9qvjBMRBWgp53TRQNje501MHFxAdZocBxG8A+CvGEpZsq4P0Lrbew6uSzPdHUvUP+BfiPqXvOvp/gPntf8A6nXNzTU9TQVlSaemmZGXwua0ta0aDQcFvQTjKe/BHP8A/rbD+ttVdR/eQlmXcnpa9Z94P+p3KM5HnemuH9bh/fPT/wBZqZzkN9J/b+p1rCqFsVQa5s+Zl7xbtOvT6uhXPtqcp04VJ6NvVeXgzzNtZOFpRdwvvPb6eHidbVhsTJZI+V8LC93HS3Lp/wBF0LO2VvSjTfQmthWnqZ+ywx1P5EYZiBxJvkLc5e7TebAHmTyC6lzSjXnFUsElGKeNfU1C/s93p6mwejbD/BNIJ/k3SQ/5c72uHgfBe+t+k9nV3mnF/wCX5/U9n1Ec+J7DbbP7GDZf6r5PqfoCpnMFUo5ndh7bfN91/qXVpSzxTPLN5ZOPBoNn5fYhzFHBM1xJUbMU/yjWPPkV0bC7jUUsymyKtFqc2r6Z0crjHkDmndKw3HmF16E6c4ttlnSmpblj6OqhstfI9nssZJlP+EuA8la6uY1KzhHY1nSjGmpFbEsXE1QZy3Ldu5p3DK0D51WsoKVZzJuqFKrL4y7o8V25OMJ2kcNTwa8g3t/BsuXWl1bml3nk4SySSfVnR6eRj/VkBt7G22vS3JXsKeZ0nFaLRLXcvvZW4oNSSw/M2viMDXe3c6WABBdaw3fAteNFTqNTaTa79Sl/aVIRXM1DHMMEI2Ywb6a35XvdadrRqz+Ja7nR6P39OHbfFvwZwXaapc9z9onMNl+uu51uqxdL6k4xp5NNcvj8/odVfV4pLZGn7P4uzM0D2bE6nNbKAba3O8rZt1JRe71OJWi/Y6lRp55tUJIxqcvPU++w4rUcVUk5L4Y6xyXfLv4a8TcodbJSy/h0z4v0NvxagZVwObNmyOjezZOU21u3S4+ZcKo4TdSk9lmXH+DvXsJ04dYtnF8fDuPWGbUfVQ+UzQeYC6Ne49lqPX4X4F4UfaIZsNJGEba0rC2+Z+/c2+63Ky59b/xVZ5VV4vu+Rxemntj4n0tLWMNI8ZhZ+TdcNNWkXXPwT2yd5nqPaWu1bm/4mbiZ0PYO6PsezEy2Uk8S91uPTd/K69jfW2SamtkdDobfKU50JP8A8vw04/IweHUzpIZooml7g5jy3ewMcTcncNGm3equUsksE2YZ3LVarTa2XHv2Ojfyyyn8U9rH+PJy6X9EofB2XJ+Xoex/8Xs0/wAfl+Zn8F2gbOW1Lo8zRYSsaLPdwNhrcczuXXufZvZ8ykmn48jj2/tnu+VSTWePaT21TXKXftdT6Hk2uxG29vzPCf8A6V3W/Q+2/gO+H7lfC9o5Xyt7P+PQ3N20tSRY79+j28N/8FW+qVJ1e0Zuj1ClWqvLGyIm2j3kgyD2g1o95O/Xhfs3WxGpKSy1EYZ2UFxWpyj0oRBsdI5ovndMxvRrmgk97QwepUbmPjfXPEz+z0/yLw1+p04RRX1kkdzb2bPJ5C3P3r6DRVLLlj8P18TYp9XltElp4cF4svOsyxj10LGPPdcW8+nJXSyjVqJUe8KspQUuPNPwIpqxz43xvZoRl30J12QBq69iOIGgtfmquhGLzRY95h2k09NEYCsZm0cTQPae0DgdXbbB7+A36KIqy11XFb8O8qXL6nVb+3y6ycvXuNCxrDpoo2TbtxLmON9Qdb96vQr061VQmuzwJtnVpxyx4cGQwjC5KokxMOXe4jgAbi/grSqRgs0maFa5jS7TPbSYU1kRp2Ouyxc12n4pyMO/hm18FrWlSU53M6j1UUjNcU4yt6cFuXGNTWbX46g6fkDfz38F5t8T55RtqrvaH/Uh+v1O04FVB1HEDwazKegXquhlxGpaygnxb8Ucq6m1WqTMDtbghcxsw3Muxw5FrgfmW7f0M8XRfdlf1RbiXGXLsL6nLsNr3Rxe01j47XvIO0eIt5qLW4lTpODWhp13eUViuph/6o9xA+vvVru4tbv4J+Uen/j8C9vp3jkk3lqHl2x7Q2QyKIOO2zQuvcC/Hlqrxso7JI01hfS1yvs7Z5tr7Ftt1J/1g/l/l+/RcT2OvD4Z0cUu0epoXH6/Q9H39f6Z/wAf6/V5q/QW+f5D+P8A+m35m30b/bLPrfB3iFdatLgfR/o8xOHV1qU9YTV5hLR+k+nU+4Ln1LOpb3Ws1KOavF/9/r9TA5RpzlF9hvT6D0j2T/8AWqNl9dV7SeSIcI8D9mwj7nrMgxQpOe7Mam+1Qy41U0rF87bQxNHNl+/Vzh9S1riXV00ZnXyU3KNwpbnX6vZp63sTn8UjGi/XY1sdx9oVqk6VrH4YJ59T3PQu4vbtShUr0rZvrcWnm0i5TH6dpmmdVX32DgGjXgAq1cTjWjFRW5pdL6lHD1GalVrY4w9+E0o2pvZZRfV8NjOyYpVyXy6tNgd2nxdqVllfVpRUk0YSXF3zs5VqOSf1NEwnLJiMLBfJ7TxwFmeB8VzM+a4jRX64/n1/JnBwa9rylmT7R7xujFNB6nOWnPPJlzP3+bSblb+JXNOUaMYfnllfjltv9zj4Td0Kl5VjUXZpy0e3bWV6efD1Po4bTUu/1kf/AFB73uXtFc4faP8A6X/X59xqdbQf5/mfRTekNJzfCf0oj+KqfAcK/MvV/qP6xS7j6N2Dp40w+n3AWgp23jE0jU/Dv5r6FhUFRp8jxqeKUnWqJTb9p6Jv5F9tbQMe2OqAbJO3LHIw3z2P42X+Eu/lJyK7NxXnBSprSPM8dbxlFyp1I8OfcZ2uqDUYSXAi4paoPHTK23p7Aep8Cs9+8kO8y2dtCrBVYPu03X2PP0Zn+8KP/wBkX7wrX9sv4HI1h5T/ADqA+yEH7z/5LHlr9j/tX1E6FVcjkntD8KU9HT01K1z4oImnZbezrNs3xGU/GS1cPxDERlQUI6OT/fNHQ6LYC6l2qkmopL1+SLvYdnpzpH1AaW+0GjTfwWfC1nxOTptlFv8AoUOkcJdZb5VHTW/cdFxI7Gzp7uRdcGP2Hvb+Lbj3KtaUnHD4ebKUYxcteexxP0iYKYT6Q3Ns1NzuP49+d/5+VfRMJq9fSkl+mW/1Pa4dW6ynjy1PG12EFlazQgNHh7JK3b2pKrRs7m0k46b+a+0xxkoZJI3XC/wVD/wM+Jecf05R9yRg9SsM3J4+c3LAJ2PdJGH6s1AaTYXsQdL9PnXmMYtqtKipTjwRVdxtSO+prFZUhsgAOjOOnxd+7efpWpTg+rTfc/3+j/j8nRTdtSTXCSJRMSRERXzKM//Z' alt='UNAM'>
</div>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class='header-box'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p style='color: white; font-size: 1.2em; margin-top: 15px;'>
        Universidad Nacional de Moquegua
    </p>
    <p style='color: rgba(255,255,255,0.9); margin-top: 10px; font-size: 1.1em;'>
        Herramienta de Consulta - Normativas Peruanas e Internacionales
    </p>
    <p style='color: rgba(255,255,255,0.8); margin-top: 8px; font-size: 0.95em;'>
        Prof. Dr. José Antonio Valeriano Zapana | 2024-2025
    </p>
</div>
""", unsafe_allow_html=True)

# MENÚ HORIZONTAL
col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    if st.button("🏠 INICIO", use_container_width=True):
        st.session_state.pagina = "Inicio"

with col2:
    if st.button("📋 ECA", use_container_width=True):
        st.session_state.pagina = "ECA"

with col3:
    if st.button("🏭 LMP", use_container_width=True):
        st.session_state.pagina = "LMP"

with col4:
    if st.button("📖 PROTOCOLO", use_container_width=True):
        st.session_state.pagina = "Protocolo"

with col5:
    if st.button("📐 LINEAMIENTO", use_container_width=True):
        st.session_state.pagina = "Lineamiento"

with col6:
    if st.button("🛡️ MEDIDAS", use_container_width=True):
        st.session_state.pagina = "Medidas"

with col7:
    if st.button("🌍 NORMATIVAS", use_container_width=True):
        st.session_state.pagina = "Normativas"

st.markdown("---")

# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>📚 Sobre esta Herramienta</h2>
            <p style='color: #333; font-size: 1.1em; line-height: 1.8;'>
                Esta plataforma reúne el <strong>marco normativo completo sobre calidad del aire</strong> 
                en Perú y el mundo, incluyendo:
            </p>
            <ul style='color: #555; font-size: 1.05em; line-height: 2;'>
                <li>✅ <strong>ECA:</strong> Estándares de Calidad Ambiental</li>
                <li>✅ <strong>LMP:</strong> Límites Máximos Permisibles</li>
                <li>✅ <strong>Protocolos:</strong> De monitoreo y medición</li>
                <li>✅ <strong>Lineamientos:</strong> Técnicos y operativos</li>
                <li>✅ <strong>Medidas de Control:</strong> Para emisiones</li>
                <li>✅ <strong>Normativas Internacionales:</strong> OMS, EPA, Canadá</li>
            </ul>
            <p style='color: #666; margin-top: 20px;'>
                Cada sección incluye <strong>enlaces directos a documentos oficiales</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🎯 Acceso Rápido</h2>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Estándares de Calidad Ambiental (ECA)", use_container_width=True):
            st.session_state.pagina = "ECA"
        
        if st.button("🏭 Límites Máximos Permisibles (LMP)", use_container_width=True):
            st.session_state.pagina = "LMP"
        
        if st.button("📖 Protocolos de Monitoreo", use_container_width=True):
            st.session_state.pagina = "Protocolo"
        
        if st.button("📐 Lineamientos Técnicos", use_container_width=True):
            st.session_state.pagina = "Lineamiento"
        
        if st.button("🛡️ Medidas de Control de Emisiones", use_container_width=True):
            st.session_state.pagina = "Medidas"
        
        if st.button("🌍 Normativas Internacionales (OMS, EPA, Canadá)", use_container_width=True):
            st.session_state.pagina = "Normativas"
    
    # Gráfico comparativo inicial
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 Comparación PM2.5 - Estándares Anuales</h2>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5},
        {'Entidad': 'EPA USA', 'Valor': 9},
        {'Entidad': 'Canadá', 'Valor': 8.8},
        {'Entidad': 'OEFA Perú', 'Valor': 25}
    ])
    
    fig = px.bar(datos_comp, x='Entidad', y='Valor', 
                 color='Valor', color_continuous_scale='RdYlGn_r',
                 title='PM2.5 Anual (μg/m³) - Comparación Internacional',
                 text='Valor')
    fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
    fig.update_layout(height=450, showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    st.markdown("<h1>📋 Estándares de Calidad Ambiental (ECA) para Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 Marco Legal Principal</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los ECA son <strong>estándares de calidad del aire ambiente</strong> que se miden en 
            estaciones de monitoreo y protegen la salud de la población.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Normativas ECA con enlaces
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 003-2017-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong><br>
            Establece los valores de concentración de contaminantes del aire que no deben superarse 
            para proteger la salud de las personas.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 003-2017-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>MODIFICATORIA</span>
            D.S. N° 010-2019-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Modificatoria de ECA para Aire</strong><br>
            Actualiza algunos parámetros y períodos de evaluación de los estándares de calidad del aire.
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 010-2019-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge' style='background: #6b7280;'>ANTERIOR</span>
            D.S. N° 074-2001-PCM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Reglamento de Estándares Nacionales de Calidad Ambiental del Aire (Primera versión)</strong><br>
            Norma original de ECA para Aire en Perú, derogada por el D.S. 003-2017-MINAM.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver D.S. 074-2001-PCM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla de valores ECA
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 Valores de ECA Vigentes</h2>
    </div>
    """, unsafe_allow_html=True)
    
    eca_valores = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['PM2.5', 'Anual', 25, 'μg/m³', 'Media aritmética anual'],
        ['PM10', '24 horas', 100, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['PM10', 'Anual', 50, 'μg/m³', 'Media aritmética anual'],
        ['NO2', '1 hora', 200, 'μg/m³', 'No exceder más de 24 veces/año'],
        ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmética anual'],
        ['SO2', '24 horas', 250, 'μg/m³', 'No exceder más de 7 veces/año'],
        ['O3', '8 horas', 100, 'μg/m³', 'Máximas diarias de promedios móviles'],
        ['CO', '8 horas', 10000, 'μg/m³', 'Promedio móvil'],
        ['CO', '1 hora', 30000, 'μg/m³', 'No exceder más de 1 vez/año'],
    ], columns=['Contaminante', 'Período', 'Valor', 'Unidad', 'Forma del Estándar'])
    
    st.dataframe(eca_valores, use_container_width=True, hide_index=True, height=420)

# ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    st.markdown("<h1>🏭 Límites Máximos Permisibles (LMP) para Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los LMP?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los LMP son <strong>límites de emisión en la fuente (chimeneas)</strong> que regulan 
            la concentración de contaminantes que puede emitir una actividad productiva específica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP Termoeléctricas
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 003-2010-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones atmosféricas para actividades de generación termoeléctrica</strong><br>
            Establece límites para NOx, SO2 y Material Particulado en centrales termoeléctricas.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 011-2009-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones de vehículos automotores</strong><br>
            Regula las emisiones de gases contaminantes de vehículos automotores nuevos y usados.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 010-2010-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>LMP de emisiones atmosféricas para minería metalúrgica y no metálica</strong><br>
            Establece límites para la actividad minera en operaciones de procesamiento.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tabla LMP Termoeléctricas
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📊 LMP Centrales Termoeléctricas (D.S. 003-2010-MINAM)</h2>
        <p style='color: #666;'>Valores en condiciones estándar: 25°C, 1 atm, base seca, 15% O2</p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['NOx', 320, 850, 2000, 'mg/Nm³'],
        ['SO2', 'N/A', 1700, 3500, 'mg/Nm³'],
        ['Material Particulado', 50, 150, 350, 'mg/Nm³']
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual', 'Unidad'])
    
    st.dataframe(lmp_termo, use_container_width=True, hide_index=True)

# ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    st.markdown("<h1>📖 Protocolos de Monitoreo de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los Protocolos?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los protocolos establecen los <strong>procedimientos estandarizados</strong> para el 
            monitoreo de la calidad del aire y medición de emisiones.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Protocolos
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.D. N° 1404-2005/DIGESA/SA
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong><br>
            Define los procedimientos para el monitoreo de calidad del aire ambiente en el territorio nacional.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/DEPA/protocolo_calidad_aire.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.M. N° 026-2000-ITINCI/DM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Aire y Emisiones</strong><br>
            Aprueba los protocolos de monitoreo de calidad de aire y emisiones para el sector industrial.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/RM-026-2000-ITINCI.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Protocolo PRODUCE
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.D. N° 195-2010-MEM/AAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Protocolo para el Monitoreo de Emisiones de Calderos y Hornos</strong><br>
            Establece los procedimientos para el monitoreo de emisiones atmosféricas en calderos y hornos.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/RD%20195-2010-AAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar Protocolo MEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Métodos de referencia
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>🔬 Métodos de Referencia EPA</h2>
        <p style='color: #555;'>Métodos de la Agencia de Protección Ambiental de EE.UU. adoptados en Perú</p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos_epa = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Gravimétrico'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Gravimétrico'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Infrarrojo no dispersivo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría UV']
    ], columns=['Contaminante', 'Método EPA', 'Técnica'])
    
    st.dataframe(metodos_epa, use_container_width=True, hide_index=True)

# ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    st.markdown("<h1>📐 Lineamientos Técnicos para Calidad del Aire</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 ¿Qué son los Lineamientos?</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Los lineamientos son <strong>guías técnicas y operativas</strong> que complementan 
            la normativa legal y orientan su implementación práctica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            R.M. N° 181-2016-MINAM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Lineamientos para la elaboración del Inventario de Emisiones Atmosféricas</strong><br>
            Establece la metodología para elaborar inventarios de emisiones de contaminantes del aire.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 009-2003-SA
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Reglamento de los Niveles de Estados de Alerta Nacionales para Contaminantes del Aire</strong><br>
            Define los niveles de alerta y las acciones correspondientes ante episodios de contaminación.
        </p>
        <a href='http://www.digesa.minsa.gob.pe/NormasLegales/Normas/DS_009-2003-SA.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            Decreto Legislativo N° 1278
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos (Emisiones de Incineración)</strong><br>
            Establece lineamientos para el control de emisiones atmosféricas de plantas de tratamiento de residuos.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver DL 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Niveles de Alerta
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>⚠️ Niveles de Estados de Alerta (D.S. 009-2003-SA)</h2>
    </div>
    """, unsafe_allow_html=True)
    
    niveles_alerta = pd.DataFrame([
        ['PM10', 'Cuidado', 250, 'μg/m³', 'Información a población sensible'],
        ['PM10', 'Peligro', 350, 'μg/m³', 'Alerta a toda la población'],
        ['PM10', 'Emergencia', 420, 'μg/m³', 'Emergencia sanitaria'],
        ['SO2', 'Cuidado', 500, 'μg/m³', 'Información a población sensible'],
        ['SO2', 'Peligro', 1000, 'μg/m³', 'Alerta a toda la población'],
        ['SO2', 'Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria'],
        ['NO2', 'Cuidado', 600, 'μg/m³', 'Información a población sensible'],
        ['NO2', 'Peligro', 1200, 'μg/m³', 'Alerta a toda la población'],
        ['NO2', 'Emergencia', 1600, 'μg/m³', 'Emergencia sanitaria']
    ], columns=['Contaminante', 'Estado', 'Concentración', 'Unidad', 'Acción'])
    
    st.dataframe(niveles_alerta, use_container_width=True, hide_index=True, height=380)

# ===================== PÁGINA MEDIDAS DE CONTROL =====================
elif st.session_state.pagina == "Medidas":
    st.markdown("<h1>🛡️ Medidas de Control de Emisiones Atmosféricas</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>📜 Marco Normativo de Control</h2>
        <p style='color: #333; font-size: 1.1em;'>
            Las medidas de control son <strong>tecnologías y prácticas</strong> para reducir 
            emisiones de contaminantes atmosféricos en la fuente.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            Ley N° 28611 - Ley General del Ambiente
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Prevención, Control y Remediación Ambiental (Título II, Capítulo 3)</strong><br>
            Establece la obligación de implementar medidas de prevención y control de la contaminación del aire.
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge'>VIGENTE</span>
            D.S. N° 012-2005-EM
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>Plan de Cierre de Minas - Control de emisiones</strong><br>
            Incluye obligaciones de control de emisiones atmosféricas durante operación y cierre de minas.
        </p>
        <a href='http://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # NTP relacionadas
    st.markdown("""
    <div class='normativa-card'>
        <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
            <span class='categoria-badge' style='background: #f97316;'>NTP</span>
            Normas Técnicas Peruanas - Medición y Control
        </h3>
        <p style='color: #555; margin: 15px 0;'>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Aire. Calidad del aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Aire. Terminología
        </p>
        <a href='https://www.inacal.gob.pe/repositorioaps/data/1/1/1/jer/ctnprocedimiento/files/Catalogo_NTP_Vigentes_2023.pdf' 
           target='_blank' class='enlace-btn'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    # Tecnologías de Control
    st.markdown("""
    <div class='content-box'>
        <h2 style='color: #1e3a8a !important; text-shadow: none;'>🔧 Principales Tecnologías de Control</h2>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias = pd.DataFrame([
        ['Material Particulado', 'Filtros de mangas', '>99%', 'Textil poroso captura partículas'],
        ['Material Particulado', 'Precipitadores electrostáticos', '95-99%', 'Carga eléctrica y colección'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Fuerza centrífuga'],
        ['SO2', 'Desulfuración húmeda (FGD)', '>95%', 'Absorción con caliza/cal'],
        ['SO2', 'Desulfuración seca', '80-95%', 'Inyección de sorbente'],
        ['NOx', 'Reducción Catalítica Selectiva (SCR)', '>90%', 'Catalizador + urea/amoniaco'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustión'],
        ['NOx', 'Reducción No Catalítica (SNCR)', '40-60%', 'Inyección de urea sin catalizador'],
        ['COVs', 'Oxidación térmica', '>95%', 'Combustión a alta temperatura'],
        ['COVs', 'Adsorción en carbón activado', '85-95%', 'Captura en superficie porosa']
    ], columns=['Contaminante', 'Tecnología', 'Eficiencia', 'Principio'])
    
    st.dataframe(tecnologias, use_container_width=True, hide_index=True, height=420)

# ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    st.markdown("<h1>🌍 Normativas Internacionales de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌍 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Comparación"])
    
    # TAB OMS
    with tab1:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🌍 Organización Mundial de la Salud (OMS)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #10b981;'>2021</span>
                WHO Global Air Quality Guidelines
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Directrices Mundiales de Calidad del Aire de la OMS 2021</strong><br>
                Actualización de las guías de 2005, con niveles 50% más estrictos basados en nueva evidencia científica.
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='enlace-btn'>
                📄 Ver Directrices OMS 2021
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='enlace-btn'>
                📖 Resumen en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla OMS
        st.markdown("<h3 style='color: white;'>📊 Directrices OMS 2021</h3>", unsafe_allow_html=True)
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³'],
            ['PM10', 15, 45, 'μg/m³'],
            ['NO2', 10, 25, 'μg/m³'],
            ['SO2', None, 40, 'μg/m³'],
            ['O3', None, 100, 'μg/m³ (8h)'],
            ['CO', None, 4000, 'μg/m³ (24h)']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad'])
        
        st.dataframe(oms_tabla, use_container_width=True, hide_index=True)
    
    # TAB EPA
    with tab2:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                La EPA de EE.UU. establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #3b82f6;'>2024</span>
                NAAQS - National Ambient Air Quality Standards
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong><br>
                Última actualización: PM2.5 anual reducido a 9.0 μg/m³ (febrero 2024)
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='enlace-btn'>
                📄 Ver Tabla NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='enlace-btn'>
                📖 Estándares PM
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla EPA
        st.markdown("<h3 style='color: white;'>📊 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        epa_tabla = pd.DataFrame([
            ['PM2.5', 9.0, 35, 'μg/m³', '2024'],
            ['PM10', None, 150, 'μg/m³', '2012'],
            ['NO2', 53, 100, 'ppb', '2010'],
            ['SO2', None, 75, 'ppb (1h)', '2010'],
            ['O3', None, 70, 'ppb (8h)', '2015'],
            ['CO', None, '9 ppm (8h)', None, '1971']
        ], columns=['Contaminante', 'Anual', 'Corto Plazo', 'Unidad', 'Última Actualización'])
        
        st.dataframe(epa_tabla, use_container_width=True, hide_index=True)
    
    # TAB CANADÁ
    with tab3:
        st.markdown("""
        <div class='content-box'>
            <h2 style='color: #1e3a8a !important; text-shadow: none;'>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='color: #333; font-size: 1.1em;'>
                Canadá utiliza un sistema de <strong>mejora continua</strong> con estándares actualizados cada 5 años.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='normativa-card'>
            <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
                <span class='categoria-badge' style='background: #ef4444;'>2025</span>
                CAAQS 2025
            </h3>
            <p style='color: #555; margin: 15px 0;'>
                <strong>Estándares Canadienses de Calidad del Aire Ambiente</strong><br>
                Sistema de gestión por Air Zones con mejora continua progresiva.
            </p>
            <a href='https://www.ccme.ca/en/air-quality-report' 
               target='_blank' class='enlace-btn'>
                📄 Ver Estándares CAAQS
            </a>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='enlace-btn'>
                📖 Air Quality Health Index
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Tabla Canadá
        st.markdown("<h3 style='color: white;'>📊 Estándares CAAQS</h3>", unsafe_allow_html=True)
        canada_tabla = pd.DataFrame([
            ['PM2.5', 8.8, 8.0, 'μg/m³', 'Anual'],
            ['PM2.5', 27, 25, 'μg/m³', '24h'],
            ['O3', 62, 60, 'ppb', '8h'],
            ['NO2', 60, 50, 'ppb', '1h'],
            ['SO2', 70, 65, 'ppb', '1h']
        ], columns=['Contaminante', '2020', '2025', 'Unidad', 'Período'])
        
        st.dataframe(canada_tabla, use_container_width=True, hide_index=True)
    
    # TAB COMPARACIÓN
    with tab4:
        st.markdown("<h2 style='color: white;'>📊 Comparación Internacional - PM2.5 Anual</h2>", unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'PM2.5 Anual': 5, 'PM2.5 24h': 15},
            {'Entidad': 'EPA USA', 'PM2.5 Anual': 9, 'PM2.5 24h': 35},
            {'Entidad': 'Canadá 2025', 'PM2.5 Anual': 8, 'PM2.5 24h': 25},
            {'Entidad': 'OEFA Perú', 'PM2.5 Anual': 25, 'PM2.5 24h': 50}
        ])
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['PM2.5 Anual'],
            name='Anual',
            marker_color='#3b82f6',
            text=comparacion['PM2.5 Anual']
        ))
        fig.add_trace(go.Bar(
            x=comparacion['Entidad'],
            y=comparacion['PM2.5 24h'],
            name='24 horas',
            marker_color='#8b5cf6',
            text=comparacion['PM2.5 24h']
        ))
        
        fig.update_traces(texttemplate='%{text} μg/m³', textposition='outside')
        fig.update_layout(
            title='Comparación PM2.5 (μg/m³)',
            barmode='group',
            height=450,
            xaxis_title='',
            yaxis_title='Concentración (μg/m³)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("""
        **Observación:** La OMS 2021 establece los estándares más estrictos (5 μg/m³ anual), 
        mientras que Perú mantiene valores más permisivos (25 μg/m³ anual). EPA y Canadá 
        tienen valores intermedios y actualizan sus estándares regularmente.
        """)

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; background: white; padding: 30px; border-radius: 15px; margin-top: 40px;'>
    <h3 style='color: #1e3a8a !important; text-shadow: none; margin: 0;'>
        Universidad Nacional de Moquegua
    </h3>
    <p style='color: #555; margin: 10px 0;'>
        Facultad de Ingeniería y Arquitectura
    </p>
    <p style='color: #666; margin: 5px 0;'>
        <strong>Curso:</strong> Contaminación y Control Atmosférico
    </p>
    <p style='color: #666; margin: 5px 0;'>
        <strong>Docente:</strong> Prof. Dr. José Antonio Valeriano Zapana
    </p>
    <p style='color: #999; font-size: 0.9em; margin-top: 15px;'>
        2024-2025 | Herramienta de Consulta de Marco Normativo del Aire
    </p>
</div>
""", unsafe_allow_html=True)
