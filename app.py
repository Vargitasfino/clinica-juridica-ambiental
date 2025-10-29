import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime

# Configuración de página
st.set_page_config(
    page_title="Marco Normativo del Aire - Perú",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra Profesional - VERSIÓN MEJORADA CON MEJOR VISIBILIDAD Y TRANSICIONES
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Smooth scroll global */
    html {
        scroll-behavior: smooth;
    }
    
    /* Variables de color corporativas */
    :root {
        --primary-blue: #0052CC;
        --secondary-blue: #0065FF;
        --accent-teal: #00B8D9;
        --dark-bg: #0A1929;
        --card-bg: #132F4C;
        --text-primary: #E3E8EF;
        --text-secondary: #B2BAC2;
        --success: #00C853;
        --warning: #FFB300;
        --danger: #D32F2F;
    }
    
    /* MEJORA CRÍTICA: Componentes nativos de Streamlit más visibles */
    div[data-testid="stMarkdownContainer"] >
    div[data-testid="stAlert"] {
        background-color: rgba(96, 165, 250, 0.3) !important;
        border: 1px solid rgba(96, 165, 250, 0.5) !important;
        border-left: 4px solid #60A5FA !important;
    }
    
    div[data-testid="stAlert"] p,
    div[data-testid="stAlert"] strong,
    div[data-testid="stAlert"] span {
        color: #FFFFFF !important;
        font-weight: 500 !important;
    }
    
    /* Background principal */
    .stApp {
        background: linear-gradient(135deg, #0A1929 0%, #132F4C 50%, #1A3A52 100%);
        background-attachment: fixed;
    }
    
    .main {
        background: transparent;
        padding-top: 0 !important;
    }
    
    .block-container {
        padding-top: 1rem !important;
    }
    
    header {
        background: transparent !important;
    }
    
    [data-testid="stHeader"] {
        background: transparent !important;
    }
    
    /* Sidebar profesional */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #132F4C 0%, #0A1929 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.12);
    }
    
    [data-testid="stSidebar"] .element-container {
        padding: 0.5rem 1rem;
    }
    
    button[kind="header"],
    button[kind="headerNoPadding"],
    [data-testid="collapsedControl"] {
        background-color: rgba(255, 255, 255, 0.2) !important;
        border-radius: 8px !important;
    }
    
    button[kind="header"] svg,
    button[kind="headerNoPadding"] svg,
    [data-testid="collapsedControl"] svg {
        filter: brightness(0) invert(1) !important;
        -webkit-filter: brightness(0) invert(1) !important;
    }
    
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }
    
    [data-testid="stSidebar"] input {
        background: rgba(255, 255, 255, 0.15) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    [data-testid="stSidebar"] input::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    
    /* Expanders - SOLUCIÓN PARA TEXTOS NEGROS */
    [data-testid="stExpander"] {
        background: rgba(19, 47, 76, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
    }
    
    [data-testid="stExpander"] summary {
        color: #FFFFFF !important;
        font-weight: 600 !important;
        font-size: 1.05rem !important;
    }
    
    [data-testid="stExpander"] p,
    [data-testid="stExpander"] span,
    [data-testid="stExpander"] div {
        color: #FFFFFF !important;
    }
    
    /* Asegurar que el icono del expander sea visible */
    [data-testid="stExpander"] svg {
        color: #FFFFFF !important;
        fill: #FFFFFF !important;
    }
    
    details summary {
        color: #FFFFFF !important;
    }
    
    details[open] {
        border-color: rgba(0, 184, 217, 0.3) !important;
    }
    
    /* Header institucional */
    .institutional-header {
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.95) 0%, rgba(0, 101, 255, 0.9) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem 3rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 20px 60px rgba(0, 82, 204, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
        position: relative;
        overflow: hidden;
    }
    
    .institutional-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.6), transparent);
    }
    
    .institutional-header h1 {
        font-size: 2.5rem;
        font-weight: 800;
        color: white !important;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.02em;
        line-height: 1.2;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .institutional-header .subtitle {
        font-size: 1.1rem;
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 500;
        margin: 0.5rem 0;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .institutional-header .metadata {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.85) !important;
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(255, 255, 255, 0.15);
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .breadcrumb {
        background: rgba(19, 47, 76, 0.8);
        backdrop-filter: blur(10px);
        padding: 0.75rem 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.95) !important;
    }
    
    .breadcrumb a {
        color: #60A5FA !important;
        text-decoration: none;
        transition: color 0.2s;
        font-weight: 600;
    }
    
    .breadcrumb a:hover {
        color: #00B8D9 !important;
    }
    
    .breadcrumb-separator {
        margin: 0 0.5rem;
        color: rgba(255, 255, 255, 0.5);
    }
    
    .corporate-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.85) 0%, rgba(26, 58, 82, 0.75) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), 0 0 0 1px rgba(255, 255, 255, 0.03) inset;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
    }
    
    .corporate-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, var(--primary-blue), var(--accent-teal));
        border-radius: 12px 12px 0 0;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .corporate-card:hover {
        transform: translateY(-4px);
        border-color: rgba(0, 101, 255, 0.3);
        box-shadow: 0 16px 48px rgba(0, 82, 204, 0.25), 0 0 0 1px rgba(255, 255, 255, 0.05) inset;
    }
    
    .corporate-card:hover::before {
        opacity: 1;
    }
    
    .corporate-card h2, .corporate-card h3 {
        color: white !important;
        font-weight: 700;
        margin-top: 0;
        letter-spacing: -0.01em;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    /* Tarjetas de contaminantes - NUEVO DISEÑO */
    .pollutant-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.9) 0%, rgba(26, 58, 82, 0.8) 100%);
        backdrop-filter: blur(15px);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .pollutant-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    
    .pollutant-card h3 {
        margin: 0;
        font-size: 1.3rem;
        font-weight: 700;
    }
    
    .pollutant-card p {
        margin: 0.5rem 0;
        color: rgba(255, 255, 255, 0.95) !important;
        font-size: 0.95rem;
    }
    
    .pollutant-card strong {
        color: #FFFFFF !important;
        font-weight: 600;
    }
    
    /* Tarjetas de proceso de monitoreo - NUEVO DISEÑO */
    .process-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.9) 0%, rgba(26, 58, 82, 0.8) 100%);
        backdrop-filter: blur(15px);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .process-card:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    }
    
    .process-card h3 {
        margin: 0;
        font-size: 1.3rem;
        font-weight: 700;
    }
    
    .process-card p {
        margin: 0.3rem 0;
        color: #FFFFFF !important;
        font-size: 0.95rem;
    }
    
    .corporate-card h2 {
        font-size: 1.75rem;
        margin-bottom: 1rem;
    }
    
    .corporate-card h3 {
        font-size: 1.4rem;
        margin-bottom: 0.75rem;
    }
    
    .corporate-card h4 {
        color: white !important;
        font-weight: 600;
        font-size: 1.2rem;
        margin-top: 1rem;
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    }
    
    .corporate-card p, .corporate-card li {
        color: var(--text-secondary);
        line-height: 1.7;
        font-size: 1rem;
    }
    
    .normative-card {
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.9) 0%, rgba(26, 58, 82, 0.85) 100%);
        backdrop-filter: blur(20px) saturate(180%);
        padding: 2rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid var(--primary-blue);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .normative-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(0, 101, 255, 0.05));
        pointer-events: none;
    }
    
    .normative-card:hover {
        transform: translateX(8px);
        border-left-color: var(--accent-teal);
        box-shadow: 0 16px 48px rgba(0, 82, 204, 0.3);
    }
    
    .normative-card.vigente {
        border-left-color: var(--success);
    }
    
    .normative-card.modificatoria {
        border-left-color: var(--warning);
    }
    
    .normative-card.referencia {
        border-left-color: var(--text-secondary);
    }
    
    .normative-card h3 {
        color: white !important;
        font-weight: 700;
        font-size: 1.35rem;
        margin: 0 0 1rem 0;
        text-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .normative-card p {
        color: rgba(255, 255, 255, 0.95) !important;
        line-height: 1.7;
        margin: 0.75rem 0;
    }
    
    .normative-card strong {
        color: white !important;
        font-weight: 600;
    }
    
    .status-badge {
        display: inline-flex;
        align-items: center;
        padding: 0.4rem 1rem;
        border-radius: 6px;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .status-badge.vigente {
        background: linear-gradient(135deg, var(--success) 0%, #00E676 100%);
        color: white;
    }
    
    .status-badge.modificatoria {
        background: linear-gradient(135deg, var(--warning) 0%, #FFC107 100%);
        color: #000;
    }
    
    .status-badge.referencia {
        background: linear-gradient(135deg, #546E7A 0%, #78909C 100%);
        color: white;
    }
    
    .status-badge.internacional {
        background: linear-gradient(135deg, var(--accent-teal) 0%, #26C6DA 100%);
        color: white;
    }
    
    .status-badge.ntp {
        background: linear-gradient(135deg, #FF6F00 0%, #FF9800 100%);
        color: white;
    }
    .corporate-button {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.875rem 1.75rem;
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
        color: #FFFFFF !important;
        text-decoration: none;
        border-radius: 8px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 12px rgba(0, 82, 204, 0.3);
        margin: 0.5rem 0.5rem 0.5rem 0;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    .corporate-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 82, 204, 0.4);
        background: linear-gradient(135deg, var(--secondary-blue) 0%, var(--accent-teal) 100%);
        color: #FFFFFF !important;
    }
    
    /* Tablas - Selectores ultra específicos para Streamlit */
    div[data-testid="stDataFrame"] {
        background: transparent !important;
    }
    
    div[data-testid="stDataFrame"] > div {
        background: rgba(19, 47, 76, 0.8) !important;
        backdrop-filter: blur(15px);
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid rgba(0, 184, 217, 0.3) !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
    }
    
    div[data-testid="stDataFrame"] table {
        background: transparent !important;
    }
    
    div[data-testid="stDataFrame"] thead th {
        background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.05em !important;
        padding: 1rem !important;
        border: none !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3) !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr {
        background: transparent !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        transition: all 0.2s ease !important;
    }
    
    div[data-testid="stDataFrame"] tbody tr:hover {
        background: rgba(0, 184, 217, 0.15) !important;
    }
    
    div[data-testid="stDataFrame"] tbody td {
        color: #FFFFFF !important;
        padding: 0.875rem 1rem !important;
        border: none !important;
        font-size: 0.9rem !important;
        font-weight: 500 !important;
    }
    
    /* Selectores adicionales por si acaso */
    .dataframe {
        background: rgba(19, 47, 76, 0.8) !important;
        backdrop-filter: blur(15px);
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid rgba(0, 184, 217, 0.3) !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3) !important;
    }
    
    .dataframe thead tr th {
        background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.05em !important;
        padding: 1rem !important;
        border: none !important;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3) !important;
    }
    
    .dataframe tbody tr {
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        transition: all 0.2s ease !important;
    }
    
    .dataframe tbody tr:hover {
        background: rgba(0, 184, 217, 0.15) !important;
    }
    
    .dataframe tbody tr td {
        color: #FFFFFF !important;
        padding: 0.875rem 1rem !important;
        border: none !important;
        font-size: 0.9rem !important;
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.15) 0%, rgba(0, 101, 255, 0.15) 100%);
        backdrop-filter: blur(10px);
        color: var(--text-primary);
        border: 1px solid rgba(0, 101, 255, 0.3);
        border-radius: 8px;
        padding: 0.75rem 1.25rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(0, 82, 204, 0.3) 0%, rgba(0, 101, 255, 0.3) 100%);
        border-color: var(--secondary-blue);
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 82, 204, 0.3);
    }
    
    .stButton > button:active {
        transform: translateY(0);
    }
    
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        padding: 0.5rem;
        border-radius: 10px;
        border: 1px solid rgba(255, 255, 255, 0.06);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: var(--text-secondary);
        border-radius: 6px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: 1px solid transparent;
        transition: all 0.2s;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(0, 101, 255, 0.1);
        color: var(--text-primary);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--primary-blue) 0%, var(--secondary-blue) 100%);
        color: white;
        border-color: rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 12px rgba(0, 82, 204, 0.3);
    }
    
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
        font-weight: 800;
        color: #60A5FA !important;
        letter-spacing: -0.02em;
        text-shadow: 0 2px 8px rgba(96, 165, 250, 0.4);
    }
    
    [data-testid="stMetricLabel"] {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.85rem;
        letter-spacing: 0.05em;
    }
    
    [data-testid="stMetricDelta"] {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    
    .streamlit-expanderHeader {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.06);
        color: var(--text-primary);
        font-weight: 600;
    }
    
    .stSelectbox > div > div,
    .stTextInput > div > div {
        background: rgba(19, 47, 76, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 8px;
        color: var(--text-primary);
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(255, 179, 0, 0.2) 0%, rgba(255, 152, 0, 0.15) 100%);
        border-left: 4px solid var(--warning);
        padding: 1.25rem;
        border-radius: 8px;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
    }
    
    .warning-box p {
        color: rgba(255, 255, 255, 0.95) !important;
        margin: 0;
        line-height: 1.6;
    }
    
    .warning-box strong {
        color: white !important;
    }
    
    .warning-box h4 {
        color: white !important;
        margin-top: 0;
    }
    
    .corporate-footer {
        text-align: center;
        background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(10, 25, 41, 0.98) 100%);
        backdrop-filter: blur(20px);
        padding: 3rem 2rem;
        border-radius: 12px;
        margin-top: 4rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 -4px 24px rgba(0, 0, 0, 0.3);
    }
    
    .corporate-footer h2, .corporate-footer h3, .corporate-footer h4 {
        color: white !important;
        font-weight: 700;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .corporate-footer p {
        color: rgba(255, 255, 255, 0.9) !important;
        margin: 0.5rem 0;
        line-height: 1.6;
    }
    
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(19, 47, 76, 0.3);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue));
        border-radius: 5px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, var(--secondary-blue), var(--accent-teal));
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fade-in {
        animation: fadeInUp 0.6s ease-out;
    }
    
    @media (max-width: 768px) {
        .institutional-header h1 {
            font-size: 1.75rem;
        }
        
        .corporate-card {
            padding: 1.5rem;
        }
        
        .normative-card {
            padding: 1.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Estado de sesión
if 'pagina' not in st.session_state:
    st.session_state.pagina = "Inicio"
if 'busqueda' not in st.session_state:
    st.session_state.busqueda = ""
    # Sidebar profesional
with st.sidebar:
    st.markdown("""
    <h3 style='color: white; font-weight: 700; font-size: 1.2rem; margin-bottom: 0.25rem; margin-top: 0; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        🔍 NAVEGACIÓN RÁPIDA
    </h3>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("🔎 Buscar normativa...", placeholder="Ej: PM2.5, ECA, protocolo...", key="search_input")
    
    if busqueda:
        busqueda_lower = busqueda.lower()
        
        keywords = {
            "ECA": ["eca", "estándar", "estandar", "calidad ambiental", "pm2.5", "pm10", "no2", "so2", "co", "o3", "ozono", "003-2017", "010-2019", "074-2001"],
            "LMP": ["lmp", "límite", "limite", "máximo permisible", "maximo permisible", "emisión", "emision", "termoeléctrica", "termoelectrica", "vehicular", "minería", "mineria", "003-2010", "011-2009", "010-2010"],
            "Protocolo": ["protocolo", "monitoreo", "digesa", "medición", "medicion", "muestreo", "1404-2005", "026-2000", "195-2010"],
            "Lineamiento": ["lineamiento", "inventario", "alerta", "estado de alerta", "181-2016", "009-2003", "1278"],
            "Medidas": ["medida", "control", "tecnología", "tecnologia", "filtro", "precipitador", "scrubber", "fgd", "scr", "nox", "28611"],
            "Normativas": ["internacional", "oms", "who", "epa", "usa", "canadá", "canada", "naaqs", "caaqs", "guía", "guia"]
        }
        
        mejor_match = None
        max_coincidencias = 0
        
        for pagina, palabras in keywords.items():
            coincidencias = sum(1 for palabra in palabras if palabra in busqueda_lower)
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                mejor_match = pagina
        
        if mejor_match and max_coincidencias > 0:
            st.success(f"✓ Encontrado en: **{mejor_match}**")
            if st.button(f"Ir a {mejor_match}", use_container_width=True, type="primary", key="search_go"):
                st.session_state.pagina = mejor_match
                st.rerun()
        else:
            st.warning("⚠️ No se encontraron resultados. Intenta con: ECA, LMP, Protocolo, PM2.5, etc.")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.75rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        📋 SECCIONES
    </h4>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Inicio", use_container_width=True, key="nav_inicio"):
        st.session_state.pagina = "Inicio"
    
    if st.button("📋 Estándares ECA", use_container_width=True, key="nav_eca"):
        st.session_state.pagina = "ECA"
    
    if st.button("🏭 Límites LMP", use_container_width=True, key="nav_lmp"):
        st.session_state.pagina = "LMP"
    
    if st.button("📖 Protocolos", use_container_width=True, key="nav_protocolo"):
        st.session_state.pagina = "Protocolo"
    
    if st.button("📐 Lineamientos", use_container_width=True, key="nav_lineamiento"):
        st.session_state.pagina = "Lineamiento"
    
    if st.button("🛡️ Control de Emisiones", use_container_width=True, key="nav_medidas"):
        st.session_state.pagina = "Medidas"
    
    if st.button("🌍 Normativas Internacionales", use_container_width=True, key="nav_normativas"):
        st.session_state.pagina = "Normativas"
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        📊 ESTADÍSTICAS
    </h4>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Normativas", "18+")
    with col2:
        st.metric("Países", "4")
    
    st.markdown("---")
    
    st.markdown("""
    <h4 style='color: white; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; margin-top: 0.5rem; text-shadow: 0 2px 4px rgba(0,0,0,0.5);'>
        ℹ️ INFORMACIÓN
    </h4>
    """, unsafe_allow_html=True)
    
    st.info("**Última actualización:** Octubre 2024")
    
    with st.expander("📞 Contacto"):
        st.markdown("""
        <p style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
        <strong style='color: white;'>Universidad Nacional de Moquegua</strong><br>
        Facultad de Ingeniería y Arquitectura<br><br>
        
        📧 contacto@unam.edu.pe<br>
        📱 +51 961 854 041
        </p>
        """, unsafe_allow_html=True)

# Header institucional premium
st.markdown(f"""
<div class='institutional-header fade-in'>
    <h1>🌍 Marco Normativo de Calidad del Aire</h1>
    <p class='subtitle'>Sistema Integral de Consulta de Normativas Ambientales</p>
    <div class='metadata'>
        <strong>Universidad Nacional de Moquegua</strong> | 
        Facultad de Ingeniería y Arquitectura | 
        Prof. Dr. José Antonio Valeriano Zapana | 
        <span style='opacity: 0.7;'>{datetime.now().strftime('%d/%m/%Y')}</span>
    </div>
</div>
""", unsafe_allow_html=True)

# Breadcrumb
breadcrumb_map = {
    "Inicio": "🏠 Inicio",
    "ECA": "📋 Estándares ECA",
    "LMP": "🏭 Límites LMP",
    "Protocolo": "📖 Protocolos",
    "Lineamiento": "📐 Lineamientos",
    "Medidas": "🛡️ Control de Emisiones",
    "Normativas": "🌍 Normativas Internacionales"
}

st.markdown(f"""
<div class='breadcrumb fade-in'>
    <a href='#' onclick='return false;'>Inicio</a>
    <span class='breadcrumb-separator'>›</span>
    <span>{breadcrumb_map.get(st.session_state.pagina, st.session_state.pagina)}</span>
</div>
""", unsafe_allow_html=True)

# ===================== PÁGINA INICIO - REORGANIZADA =====================
if st.session_state.pagina == "Inicio":
    
    # ========== 1. RESUMEN EJECUTIVO ==========
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Sistema de Información sobre Calidad del Aire en Perú</h2>
        <p style='font-size: 1.05rem; line-height: 1.8;'>
            Plataforma integral que consolida el <strong>marco normativo peruano</strong> de calidad del aire,
            incluyendo Estándares de Calidad Ambiental (ECA), Límites Máximos Permisibles (LMP), protocolos
            de monitoreo y comparativas con estándares internacionales de la OMS, EPA y Canadá.
        </p>
    </div>
    """, unsafe_allow_html=True)
    

    
    # ========== 3. ACCESO RÁPIDO - CATEGORÍAS DEL SISTEMA ==========
    st.markdown("""
    <div style='text-align: center; margin: 3rem 0 2rem 0;'>
        <h2 style='font-size: 2rem; font-weight: 700; background: linear-gradient(135deg, #00B8D9, #0065FF);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0 0 0.5rem 0;'>
            📂 Explora el Marco Normativo
        </h2>
        <p style='color: #B2BAC2; font-size: 1.05rem; margin: 0;'>
            Accede directamente a cada categoría del sistema regulatorio
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        # ECA
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0, 200, 83, 0.2), rgba(0, 230, 118, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #00C853; text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📋</div>
            <h4 style='color: #00C853; margin: 0.5rem 0;'>ECA</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                Estándares de Calidad Ambiental del Aire
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #00C853;'>3</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Normativas</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver ECA", key="goto_eca_main", use_container_width=True):
            st.session_state.pagina = "ECA"
            st.rerun()
        
        # Lineamientos
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0091EA; text-align: center; margin-bottom: 1rem; margin-top: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📐</div>
            <h4 style='color: #0091EA; margin: 0.5rem 0;'>Lineamientos</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                Guías Técnicas
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #0091EA;'>3</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Lineamientos</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver Lineamientos", key="goto_linea_main", use_container_width=True):
            st.session_state.pagina = "Lineamiento"
            st.rerun()
    
    with col_b:
        # LMP
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(255, 111, 0, 0.2), rgba(255, 152, 0, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #FF6F00; text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🏭</div>
            <h4 style='color: #FF6F00; margin: 0.5rem 0;'>LMP</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                Límites Máximos Permisibles
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #FF6F00;'>4</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Normativas</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver LMP", key="goto_lmp_main", use_container_width=True):
            st.session_state.pagina = "LMP"
            st.rerun()
        
        # Marco Legal
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #D32F2F; text-align: center; margin-bottom: 1rem; margin-top: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>⚖️</div>
            <h4 style='color: #D32F2F; margin: 0.5rem 0;'>Control de Emisiones</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                Tecnologías y Marco Legal
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #D32F2F;'>3</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Leyes</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver Control", key="goto_legal_main", use_container_width=True):
            st.session_state.pagina = "Medidas"
            st.rerun()
    
    with col_c:
        # Protocolos
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #8E24AA; text-align: center; margin-bottom: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>📖</div>
            <h4 style='color: #8E24AA; margin: 0.5rem 0;'>Protocolos</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                Procedimientos de Monitoreo
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #8E24AA;'>4</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Protocolos</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver Protocolos", key="goto_proto_main", use_container_width=True):
            st.session_state.pagina = "Protocolo"
            st.rerun()
        
        # Internacional
        st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 188, 212, 0.1)); 
                    padding: 1.5rem; border-radius: 12px; border-left: 4px solid #00B8D9; text-align: center; margin-bottom: 1rem; margin-top: 1rem;'>
            <div style='font-size: 3rem; margin-bottom: 0.5rem;'>🌍</div>
            <h4 style='color: #00B8D9; margin: 0.5rem 0;'>Internacional</h4>
            <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                OMS, EPA, Canadá
            </p>
            <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <span style='font-size: 1.5rem; font-weight: 700; color: #00B8D9;'>3</span>
                <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Estándares</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📄 Ver Internacional", key="goto_inter_main", use_container_width=True):
            st.session_state.pagina = "Normativas"
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ========== 4. COMPARATIVA PERÚ VS OMS ==========
    st.markdown("""
    <div style='text-align:center;margin:3rem 0 1.5rem 0'>
        <h2 style='font-size:2rem;font-weight:700;background:linear-gradient(135deg,#00B8D9,#0065FF);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0'>
            🔬 Comparativa: Estándares Peruanos vs OMS
        </h2>
        <p style='color:#B2BAC2;margin:0.5rem 0 0 0;font-size:1.05rem'>
            Análisis de brechas en los principales contaminantes atmosféricos
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Datos para la comparativa
    comparativa_data = pd.DataFrame({
        'Contaminante': ['PM2.5\nAnual', 'PM2.5\n24h', 'PM10\nAnual', 'PM10\n24h', 'SO2\n24h', 'NO2\nAnual'],
        'Perú (ECA)': [25, 50, 50, 100, 250, 100],
        'OMS 2021': [5, 15, 15, 45, 40, 10],
        'Diferencia': [5.0, 3.3, 3.3, 2.2, 6.3, 10.0]
    })
    
    fig_comparativa = go.Figure()
    
    # Barras de Perú
    fig_comparativa.add_trace(go.Bar(
        name='Perú (ECA)',
        x=comparativa_data['Contaminante'],
        y=comparativa_data['Perú (ECA)'],
        marker=dict(
            color='#FF6F00',
            line=dict(color='rgba(255, 255, 255, 0.3)', width=2)
        ),
        text=comparativa_data['Perú (ECA)'],
        texttemplate='%{text} μg/m³',
        textposition='outside',
        textfont=dict(size=11, color='#E3E8EF')
    ))
    
    # Barras de OMS
    fig_comparativa.add_trace(go.Bar(
        name='OMS 2021',
        x=comparativa_data['Contaminante'],
        y=comparativa_data['OMS 2021'],
        marker=dict(
            color='#00C853',
            line=dict(color='rgba(255, 255, 255, 0.3)', width=2)
        ),
        text=comparativa_data['OMS 2021'],
        texttemplate='%{text} μg/m³',
        textposition='outside',
        textfont=dict(size=11, color='#E3E8EF')
    ))
    
    # Línea de diferencia (multiplicador)
    fig_comparativa.add_trace(go.Scatter(
        name='Veces más permisivo',
        x=comparativa_data['Contaminante'],
        y=comparativa_data['Diferencia'],
        mode='lines+markers+text',
        line=dict(color='#D32F2F', width=3, dash='dash'),
        marker=dict(size=10, color='#D32F2F', symbol='diamond'),
        text=[f'{x}x' for x in comparativa_data['Diferencia']],
        textposition='top center',
        textfont=dict(size=12, color='#D32F2F', family='Inter'),
        yaxis='y2'
    ))
    
    fig_comparativa.update_layout(
        height=550,
        plot_bgcolor='rgba(10, 25, 41, 0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', family='Inter', size=12),
        xaxis=dict(
            showgrid=False,
            title=dict(text='<b>Contaminante / Período</b>', font=dict(size=13, color='#00B8D9'))
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.08)',
            title=dict(text='<b>Concentración (μg/m³)</b>', font=dict(size=13, color='#00B8D9')),
            range=[0, max(comparativa_data['Perú (ECA)']) * 1.2]
        ),
        yaxis2=dict(
            title=dict(text='<b>Factor de diferencia (veces)</b>', font=dict(size=13, color='#D32F2F')),
            overlaying='y',
            side='right',
            showgrid=False,
            range=[0, max(comparativa_data['Diferencia']) * 1.3]
        ),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            bgcolor='rgba(19, 47, 76, 0.9)',
            bordercolor='rgba(255,255,255,0.3)',
            borderwidth=2,
            font=dict(size=16, color='#FFFFFF', family='Inter, sans-serif')
        ),
        barmode='group',
        bargap=0.15,
        bargroupgap=0.1,
        margin=dict(l=60, r=60, t=60, b=80)
    )
    
    st.plotly_chart(fig_comparativa, use_container_width=True)
    
    # Alerta crítica
    st.markdown("""
    <div style='background:linear-gradient(135deg,rgba(211,47,47,0.2),rgba(211,47,47,0.05));
                padding:1.5rem;border-radius:12px;border-left:4px solid #D32F2F;margin:1.5rem 0'>
        <h4 style='color:#D32F2F;margin:0 0 0.8rem 0;font-size:1.1rem'>⚠️ Análisis Crítico</h4>
        <p style='color:#E3E8EF;margin:0;line-height:1.7;font-size:0.95rem'>
            Los estándares peruanos son <strong style='color:#FFB300'>significativamente más permisivos</strong> que las 
            recomendaciones de la OMS 2021. El PM2.5 anual peruano (25 μg/m³) es <strong style='color:#D32F2F'>5 veces 
            mayor</strong> que el valor OMS (5 μg/m³), mientras que el SO2 es <strong style='color:#D32F2F'>6.3 veces 
            más alto</strong>. Se recomienda una <strong style='color:#00C853'>actualización gradual</strong> de los ECA 
            nacionales para proteger mejor la salud pública.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ========== 5. COMPARATIVA LATINOAMERICANA ==========
    st.markdown("""
    <div style='text-align:center;margin:3rem 0 1.5rem 0'>
        <h2 style='font-size:2rem;font-weight:700;background:linear-gradient(135deg,#8E24AA,#D32F2F);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0'>
            🌎 Perú en el Contexto Latinoamericano
        </h2>
        <p style='color:#B2BAC2;margin:0.5rem 0 0 0;font-size:1.05rem'>
            Comparación de estándares PM2.5 con países de la región
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Datos comparativos de Latinoamérica
    latam_data = pd.DataFrame({
        'País': ['Chile', 'Colombia', 'México', 'Brasil', 'Perú', 'Argentina'],
        'PM2.5 Anual': [20, 25, 12, 20, 25, 15],
        'PM2.5 24h': [50, 50, 45, 60, 50, 65],
        'Año Actualización': [2023, 2021, 2022, 2018, 2017, 2021]
    })
    
    fig_latam = go.Figure()
    
    # Barras de PM2.5 Anual
    colors_anual = ['#00C853' if x <= 15 else '#FFB300' if x <= 20 else '#D32F2F' 
                    for x in latam_data['PM2.5 Anual']]
    
    fig_latam.add_trace(go.Bar(
        name='PM2.5 Anual',
        x=latam_data['País'],
        y=latam_data['PM2.5 Anual'],
        marker=dict(
            color=colors_anual,
            line=dict(color='rgba(255,255,255,0.3)', width=2)
        ),
        text=latam_data['PM2.5 Anual'],
        texttemplate='%{text} μg/m³',
        textposition='outside',
        textfont=dict(size=12, color='#E3E8EF'),
        hovertemplate='<b>%{x}</b><br>PM2.5 Anual: %{y} μg/m³<br>' +
                     'Actualización: %{customdata}<extra></extra>',
        customdata=latam_data['Año Actualización']
    ))
    
    # Línea de referencia OMS
    fig_latam.add_hline(
        y=5, 
        line_dash="dash", 
        line_color="#00C853",
        line_width=2,
        annotation_text="OMS 2021: 5 μg/m³",
        annotation_position="right",
        annotation_font=dict(size=11, color='#00C853')
    )
    
    # Línea de referencia EPA
    fig_latam.add_hline(
        y=9, 
        line_dash="dot", 
        line_color="#0065FF",
        line_width=2,
        annotation_text="EPA USA: 9 μg/m³",
        annotation_position="right",
        annotation_font=dict(size=11, color='#0065FF')
    )
    
    fig_latam.update_layout(
        height=500,
        plot_bgcolor='rgba(10, 25, 41, 0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', family='Inter', size=12),
        xaxis=dict(
            showgrid=False,
            title=dict(text='<b>País</b>', font=dict(size=13, color='#00B8D9'))
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.08)',
            title=dict(text='<b>PM2.5 Anual (μg/m³)</b>', font=dict(size=13, color='#00B8D9')),
            range=[0, 30]
        ),
        showlegend=False,
        margin=dict(l=60, r=150, t=40, b=80)
    )
    
    st.plotly_chart(fig_latam, use_container_width=True)
    
    # Tarjetas de posición
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(0,200,83,0.15),rgba(0,200,83,0.05));
                    padding:1.2rem;border-radius:10px;border:2px solid rgba(0,200,83,0.3);text-align:center'>
            <div style='color:#00C853;font-size:1.8rem;font-weight:800;margin-bottom:0.3rem'>🥇 México</div>
            <div style='color:#E3E8EF;font-size:0.85rem'>12 μg/m³ - Más estricto</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_b:
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(255,179,0,0.15),rgba(255,179,0,0.05));
                    padding:1.2rem;border-radius:10px;border:2px solid rgba(255,179,0,0.3);text-align:center'>
            <div style='color:#FFB300;font-size:1.8rem;font-weight:800;margin-bottom:0.3rem'>4️⃣ Perú</div>
            <div style='color:#E3E8EF;font-size:0.85rem'>25 μg/m³ - Requiere mejora</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_c:
        st.markdown("""
        <div style='background:linear-gradient(135deg,rgba(0,184,217,0.15),rgba(0,184,217,0.05));
                    padding:1.2rem;border-radius:10px;border:2px solid rgba(0,184,217,0.3);text-align:center'>
            <div style='color:#00B8D9;font-size:1.8rem;font-weight:800;margin-bottom:0.3rem'>📊 Brecha</div>
            <div style='color:#E3E8EF;font-size:0.85rem'>5x más permisivo que OMS</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.info("💡 **Contexto regional:** México lidera con el estándar más estricto (12 μg/m³), seguido de Argentina (15 μg/m³). Perú y Colombia comparten el mismo valor (25 μg/m³), situándose entre los más permisivos de la región.")
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # ========== 6. TIMELINE ==========
    st.markdown("""
    <div style='text-align:center;margin:3rem 0 2rem 0'>
        <h2 style='font-size:2.5rem;font-weight:800;background:linear-gradient(135deg,#00B8D9,#0065FF);
                   -webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0 0 0.5rem 0;letter-spacing:-0.02em'>
            📜 Línea de Tiempo de Normativas Ambientales
        </h2>
        <p style='color:#B2BAC2;font-size:1.15rem;margin:0;font-weight:400'>
            Evolución histórica del marco regulatorio de calidad del aire en el Perú
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    timeline_data = [
        {'año': 1996, 'titulo': 'R.M. N° 315-96-EM/VMM', 'categoria': 'LMP', 'descripcion': 'Primeros límites para fundiciones y refinerías mineras'},
        {'año': 2000, 'titulo': 'R.M. N° 026-2000-ITINCI/DM', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de monitoreo industrial'},
        {'año': 2001, 'titulo': 'D.S. N° 074-2001-PCM', 'categoria': 'ECA', 'descripcion': 'Primeros Estándares de Calidad Ambiental para Aire'},
        {'año': 2003, 'titulo': 'D.S. N° 009-2003-SA', 'categoria': 'Lineamiento', 'descripcion': 'Niveles de Estados de Alerta Nacional'},
        {'año': 2005, 'titulo': 'R.D. N° 1404-2005/DIGESA', 'categoria': 'Protocolo', 'descripcion': 'Protocolo de Monitoreo de Calidad del Aire'},
        {'año': 2005, 'titulo': 'Ley N° 28611', 'categoria': 'Marco Legal', 'descripcion': 'Ley General del Ambiente'},
        {'año': 2009, 'titulo': 'D.S. N° 011-2009-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para vehículos automotores'},
        {'año': 2010, 'titulo': 'D.S. N° 003-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para centrales termoeléctricas'},
        {'año': 2010, 'titulo': 'D.S. N° 010-2010-MINAM', 'categoria': 'LMP', 'descripcion': 'Límites para industrias manufactureras'},
        {'año': 2016, 'titulo': 'R.M. N° 181-2016-MINAM', 'categoria': 'Lineamiento', 'descripcion': 'Lineamientos para Inventario de Emisiones'},
        {'año': 2017, 'titulo': 'D.S. N° 003-2017-MINAM', 'categoria': 'ECA', 'descripcion': 'Actualización de Estándares de Calidad Ambiental'},
        {'año': 2018, 'titulo': 'Ley N° 30754', 'categoria': 'Marco Legal', 'descripcion': 'Ley Marco sobre Cambio Climático'},
        {'año': 2019, 'titulo': 'D.S. N° 010-2019-MINAM', 'categoria': 'ECA', 'descripcion': 'Modificatoria de ECA para Aire'}
    ]
    
    df_timeline = pd.DataFrame(timeline_data)
    
    # Crear gráfico moderno y mejorado con mejor diseño
    fig_timeline = go.Figure()
    
    colores_cat = {
        'ECA': '#00C853',
        'LMP': '#FF6F00',
        'Protocolo': '#8E24AA',
        'Lineamiento': '#0091EA',
        'Marco Legal': '#D32F2F'
    }
    
    # Línea base horizontal con gradiente mejorado y más visible
    fig_timeline.add_trace(go.Scatter(
        x=[1995, 2022],
        y=[0, 0],
        mode='lines',
        line=dict(color='rgba(0, 184, 217, 0.7)', width=3),
        showlegend=False,
        hoverinfo='skip'
    ))
    
    # Agregar cada normativa con posicionamiento inteligente para años consecutivos
    categorias_mostradas = set()
    
    for idx, row in df_timeline.iterrows():
        año = row['año']
        
        # Detectar años consecutivos y forzar alternancia
        if idx > 0:
            año_anterior = df_timeline.iloc[idx-1]['año']
            if abs(año - año_anterior) == 1:
                # Si son años consecutivos, forzar lado opuesto al anterior
                y_pos_anterior = 3.5 if (idx-1) % 2 == 0 else -3.5
                y_pos = -y_pos_anterior  # Lado opuesto
            else:
                # Si no son consecutivos, alternar normalmente
                y_pos = 3.5 if idx % 2 == 0 else -3.5
        else:
            y_pos = 3.5
        
        # Sin offset horizontal
        x_offset = 0
        
        color = colores_cat[row['categoria']]
        mostrar_leyenda = row['categoria'] not in categorias_mostradas
        
        if mostrar_leyenda:
            categorias_mostradas.add(row['categoria'])
        
        # Línea conectora más elegante con mejor grosor
        fig_timeline.add_trace(go.Scatter(
            x=[row['año'] + x_offset, row['año'] + x_offset],
            y=[0, y_pos * 0.80],
            mode='lines',
            line=dict(color=color, width=2, dash='dot'),
            showlegend=False,
            hoverinfo='skip',
            opacity=0.75
        ))
        
        # Punto en la base más grande y con sombra
        fig_timeline.add_trace(go.Scatter(
            x=[row['año']],
            y=[0],
            mode='markers',
            marker=dict(
                size=12, 
                color=color, 
                line=dict(color='white', width=2),
                opacity=1
            ),
            showlegend=False,
            hoverinfo='skip'
        ))
        
        # Marcador superior mejorado con más información
        simbolos = {
            'ECA': 'star',
            'LMP': 'diamond',
            'Protocolo': 'circle',
            'Lineamiento': 'square',
            'Marco Legal': 'hexagon'
        }
        
        size_marker = 28 if row['categoria'] == 'LMP' else 24
        
        fig_timeline.add_trace(go.Scatter(
            x=[row['año'] + x_offset],
            y=[y_pos],
            mode='markers+text',
            marker=dict(
                size=size_marker, 
                color=color, 
                symbol=simbolos.get(row['categoria'], 'square'),
                line=dict(color='white', width=2),
                opacity=0.95
            ),
            text=str(row['año']),
            textposition='middle center',
            textfont=dict(color='white', size=9, family='Inter', weight='bold'),
            name=row['categoria'],
            legendgroup=row['categoria'],
            showlegend=mostrar_leyenda,
            hovertemplate=(
                '<b style="font-size:14px">%s</b><br><br>'
                '<b>📋 Descripción:</b> %s<br>'
                '<b>📅 Año:</b> %d<br>'
                '<b>🏷️ Categoría:</b> %s<br>'
                '<extra></extra>'
            ) % (row['titulo'], row['descripcion'], row['año'], row['categoria'])
        ))
    
    # Layout mejorado con mejor espaciado y diseño
    fig_timeline.update_layout(
        height=650,
        showlegend=True,
        plot_bgcolor='rgba(10, 25, 41, 0.3)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', family='Inter', size=12),
        xaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.08)', 
            title=dict(text='<b>Año</b>', font=dict(size=14, color='#00B8D9')),
            dtick=1, 
            range=[1994, 2022],
            tickfont=dict(size=11, color='#E3E8EF')
        ),
        yaxis=dict(
            showgrid=False, 
            showticklabels=False, 
            range=[-4.5, 4.5],
            zeroline=False
        ),
        legend=dict(
            orientation='h', 
            yanchor='bottom', 
            y=-0.20, 
            xanchor='center', 
            x=0.5,
            bgcolor='rgba(19, 47, 76, 0.9)',
            bordercolor='rgba(255, 255, 255, 0.3)',
            borderwidth=2,
            font=dict(size=16, color='#FFFFFF', family='Inter, sans-serif')
        ),
        hovermode='closest',
        margin=dict(l=50, r=50, t=40, b=110),
        hoverlabel=dict(
            bgcolor='rgba(19, 47, 76, 0.95)',
            font_size=12,
            font_family='Inter',
            bordercolor='rgba(0, 184, 217, 0.5)'
        )
    )
    
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    st.success("""
    **✓ Beneficios del Sistema**
    
    **📄 Acceso Directo:** Enlaces actualizados a documentos oficiales
    
    **📊 Visualizaciones:** Gráficos interactivos para análisis comparativo
    
    **✅ Información Validada:** Datos técnicos verificados y referencias completas
    """)

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📋 Estándares de Calidad Ambiental (ECA) para Aire</h2>
        <p style='font-size: 1.05rem; line-height: 1.8;'>
            Los <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong> establecen los niveles de concentración 
            de contaminantes en el aire ambiente que <strong>no deben superarse para proteger la salud de la población</strong>. 
            Son instrumentos de gestión ambiental prioritarios para prevenir y planificar el control de la contaminación del aire.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Normativas ECA
    st.markdown("""
    <div class='normative-card vigente'>
        <div class='status-badge vigente'>✅ VIGENTE PRINCIPAL</div>
        <h3>📋 D.S. N° 003-2017-MINAM</h3>
        <p><strong>Título:</strong> Aprueban Estándares de Calidad Ambiental (ECA) para Aire y establecen Disposiciones Complementarias</p>
        <p><strong>Publicación:</strong> 7 de junio de 2017</p>
        <p><strong>Alcance:</strong> Aplicable a nivel nacional en zonas de aire de exterior consideradas habitables</p>
        <p><strong>Contaminantes regulados:</strong> PM2.5, PM10, SO2, NO2, CO, O3, Pb, BaP, H2S</p>
        <p><strong>Características:</strong></p>
        <ul style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
            <li>Actualiza y reemplaza parcialmente el D.S. N° 074-2001-PCM</li>
            <li>Introduce nuevos estándares más restrictivos para PM2.5</li>
            <li>Establece períodos de transición para el cumplimiento</li>
            <li>Define zona de atención prioritaria (ZAP) y áreas degradadas</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://www.minam.gob.pe/disposiciones/decreto-supremo-n-003-2017-minam/' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 003-2017-MINAM
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card modificatoria'>
        <div class='status-badge modificatoria'>📝 MODIFICATORIA</div>
        <h3>📋 D.S. N° 010-2019-MINAM</h3>
        <p><strong>Título:</strong> Modifica el Decreto Supremo N° 003-2017-MINAM</p>
        <p><strong>Publicación:</strong> 18 de noviembre de 2019</p>
        <p><strong>Modificaciones clave:</strong></p>
        <ul style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
            <li>Ajusta el cronograma de implementación de ECA para PM2.5</li>
            <li>Prorroga plazos de cumplimiento para zonas de atención prioritaria</li>
            <li>Modifica disposiciones complementarias transitorias</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://busquedas.elperuano.pe/normaslegales/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1827836-1/' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 010-2019-MINAM
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card referencia'>
        <div class='status-badge referencia'>📚 REFERENCIA HISTÓRICA</div>
        <h3>📋 D.S. N° 074-2001-PCM</h3>
        <p><strong>Título:</strong> Reglamento de Estándares Nacionales de Calidad Ambiental del Aire</p>
        <p><strong>Publicación:</strong> 24 de junio de 2001</p>
        <p><strong>Estado actual:</strong> Derogado parcialmente por D.S. N° 003-2017-MINAM</p>
        <p><strong>Importancia histórica:</strong> Primera normativa integral de ECA para Aire en el Perú</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_074-2001-pcm.pdf' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 074-2001-PCM
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabla de ECA vigentes con diseño azul profesional
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(10, 25, 41, 0.98) 100%); 
                padding: 2rem; border-radius: 16px; margin: 2rem 0; 
                border: 1px solid rgba(0, 184, 217, 0.3);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);'>
        <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;'>
            <div style='font-size: 2.5rem;'>📊</div>
            <h2 style='color: #FFFFFF; margin: 0; font-size: 1.8rem; font-weight: 900;'>
                Valores de Estándares de Calidad Ambiental (ECA) Vigentes
            </h2>
        </div>
        <p style='color: rgba(255, 255, 255, 0.8); font-size: 1rem; margin: 0.5rem 0 0 0;'>
            Valores según D.S. N° 003-2017-MINAM y modificatorias
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Usar components.html para renderizado garantizado
    import streamlit.components.v1 as components
    
    html_eca = """
    <div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); 
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);'>
        <table style='width: 100%; border-collapse: collapse; 
                      background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(26, 58, 82, 0.9) 100%);'>
            <thead>
                <tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Contaminante</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Período</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Valor</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Unidad</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Método de Análisis</th>
                </tr>
            </thead>
            <tbody>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #3B82F6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>PM2.5</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>24 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>50</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Separación inercial/filtración</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #3B82F6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>PM2.5</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>Anual</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>25</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Separación inercial/filtración</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #8B5CF6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>PM10</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>24 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>100</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Separación inercial/filtración</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #8B5CF6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>PM10</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>Anual</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>50</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Separación inercial/filtración</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #EAB308; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>SO2</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>24 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>250</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Fluorescencia UV</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #EF4444; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>NO2</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>1 hora</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>200</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Quimioluminiscencia</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #EF4444; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>NO2</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>Anual</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>100</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Quimioluminiscencia</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #A855F7; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>CO</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>8 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>10000</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Infrarrojo no dispersivo</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #06B6D4; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>O3</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>8 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>100</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Fotometría UV</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #F59E0B; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Pb</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>Anual</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>0.5</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Espectrometría de masas</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #10B981; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>BaP</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>Anual</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>0.0001</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Cromatografía</td>
                </tr>
                <tr onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #EC4899; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>H2S</td>
                    <td style='color: #FFF; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>24 horas</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>150</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem;'>µg/m³</td>
                    <td style='color: rgba(255,255,255,0.9); padding: 1rem 1.5rem; text-align: center; font-size: 0.9rem;'>Fluorescencia UV</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    
    components.html(html_eca, height=600, scrolling=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Descripción de contaminantes
    st.markdown("""
    <div class='corporate-card'>
        <h3>🔬 Descripción de Contaminantes Regulados</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #FF6F00;'>💨 Material Particulado PM2.5</h3>
            <p><strong>Definición:</strong> Partículas con diámetro aerodinámico ≤ 2.5 micrómetros</p>
            <p><strong>Fuentes:</strong> Combustión de vehículos, industrias, quema de biomasa</p>
            <p><strong>Efectos en salud:</strong> Penetra profundamente en los pulmones, causa enfermedades respiratorias y cardiovasculares</p>
            <p><strong>ECA Perú:</strong> 50 µg/m³ (24h) | 25 µg/m³ (anual)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #00C853;'>💨 Material Particulado PM10</h3>
            <p><strong>Definición:</strong> Partículas con diámetro aerodinámico ≤ 10 micrómetros</p>
            <p><strong>Fuentes:</strong> Polvo de caminos, construcción, minería, industrias</p>
            <p><strong>Efectos en salud:</strong> Irritación respiratoria, agravamiento de asma</p>
            <p><strong>ECA Perú:</strong> 100 µg/m³ (24h) | 50 µg/m³ (anual)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #0091EA;'>☁️ Dióxido de Azufre (SO2)</h3>
            <p><strong>Fuentes:</strong> Fundiciones, refinerías, termoeléctricas a carbón</p>
            <p><strong>Efectos en salud:</strong> Irritación del sistema respiratorio, broncoconstricción</p>
            <p><strong>ECA Perú:</strong> 250 µg/m³ (24h)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #8E24AA;'>⚡ Dióxido de Nitrógeno (NO2)</h3>
            <p><strong>Fuentes:</strong> Vehículos, termoeléctricas, procesos industriales</p>
            <p><strong>Efectos en salud:</strong> Inflamación vías respiratorias, reducción función pulmonar</p>
            <p><strong>ECA Perú:</strong> 200 µg/m³ (1h) | 100 µg/m³ (anual)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #D32F2F;'>🔥 Monóxido de Carbono (CO)</h3>
            <p><strong>Fuentes:</strong> Combustión incompleta en vehículos e industrias</p>
            <p><strong>Efectos en salud:</strong> Reduce transporte de oxígeno en sangre, afecta sistema cardiovascular</p>
            <p><strong>ECA Perú:</strong> 10,000 µg/m³ (8h)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #00B8D9;'>☀️ Ozono (O3)</h3>
            <p><strong>Formación:</strong> Reacción fotoquímica de NOx y VOCs bajo luz solar</p>
            <p><strong>Efectos en salud:</strong> Irritación respiratoria, daño pulmonar, agrava asma</p>
            <p><strong>ECA Perú:</strong> 100 µg/m³ (8h)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #FFB300;'>🧪 Plomo (Pb)</h3>
            <p><strong>Fuentes:</strong> Fundiciones, baterías, combustibles con plomo (histórico)</p>
            <p><strong>Efectos en salud:</strong> Neurotoxicidad, afecta desarrollo cognitivo en niños</p>
            <p><strong>ECA Perú:</strong> 0.5 µg/m³ (anual)</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class='pollutant-card'>
            <h3 style='color: #9C27B0;'>☠️ Benzo(a)pireno (BaP)</h3>
            <p><strong>Fuentes:</strong> Combustión incompleta de materia orgánica</p>
            <p><strong>Efectos en salud:</strong> Cancerígeno, daño al ADN</p>
            <p><strong>ECA Perú:</strong> 0.0001 µg/m³ (anual)</p>
        </div>
        """, unsafe_allow_html=True)

# ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🏭 Límites Máximos Permisibles (LMP) de Emisiones Atmosféricas</h2>
        <p style='font-size: 1.05rem; line-height: 1.8;'>
            Los <strong>Límites Máximos Permisibles (LMP)</strong> son medidas de control que establecen la cantidad máxima 
            de contaminantes que pueden ser emitidos por <strong>fuentes puntuales específicas</strong> (chimeneas, ductos). 
            Son instrumentos de gestión ambiental que regulan directamente las actividades productivas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP Minero-Metalúrgico
    st.markdown("""
    <div class='normative-card vigente'>
        <div class='status-badge vigente'>✅ VIGENTE</div>
        <h3>🏭 R.M. N° 315-96-EM/VMM</h3>
        <p><strong>Título:</strong> Niveles Máximos Permisibles de Emisión de Gases y Partículas para las Actividades Minero-Metalúrgicas</p>
        <p><strong>Publicación:</strong> 19 de julio de 1996</p>
        <p><strong>Alcance:</strong> Fundiciones, refinerías y plantas de procesamiento minero-metalúrgico</p>
        <p><strong>Contaminantes regulados:</strong> PM, SO2, Pb, As</p>
        <p><strong>Nota:</strong> Documento histórico de referencia técnica</p>
    </div>
    """, unsafe_allow_html=True)
    
    # LMP Termoeléctrico
    st.markdown("""
    <div class='normative-card vigente'>
        <div class='status-badge vigente'>✅ VIGENTE</div>
        <h3>⚡ D.S. N° 003-2010-MINAM</h3>
        <p><strong>Título:</strong> Límites Máximos Permisibles para Emisiones de Centrales Termoeléctricas</p>
        <p><strong>Publicación:</strong> 17 de febrero de 2010</p>
        <p><strong>Alcance:</strong> Centrales termoeléctricas con combustibles fósiles (GN, diésel, carbón, residual)</p>
        <p><strong>Contaminantes regulados:</strong> PM, SO2, NOx</p>
        <p><strong>Características:</strong></p>
        <ul style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
            <li>Diferencia límites según tipo de combustible</li>
            <li>Establece cronograma de adecuación para instalaciones existentes</li>
            <li>Define métodos de medición y monitoreo continuo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 003-2010-MINAM
    </a>
    """, unsafe_allow_html=True)
    
    # LMP Vehicular
    st.markdown("""
    <div class='normative-card vigente'>
        <div class='status-badge vigente'>✅ VIGENTE</div>
        <h3>🚗 D.S. N° 011-2009-MINAM</h3>
        <p><strong>Título:</strong> Límites Máximos Permisibles de Emisiones Vehiculares</p>
        <p><strong>Publicación:</strong> 13 de abril de 2009</p>
        <p><strong>Alcance:</strong> Vehículos automotores que circulan por la red vial</p>
        <p><strong>Contaminantes regulados:</strong> CO, HC, NOx, PM</p>
        <p><strong>Categorías:</strong> Vehículos ligeros (gasolina/diésel) y vehículos pesados (diésel)</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 011-2009-MINAM
    </a>
    """, unsafe_allow_html=True)
    
    # LMP Industria Manufacturera
    st.markdown("""
    <div class='normative-card vigente'>
        <div class='status-badge vigente'>✅ VIGENTE</div>
        <h3>🏭 D.S. N° 010-2010-MINAM</h3>
        <p><strong>Título:</strong> Límites Máximos Permisibles para Emisiones de la Industria de Cemento, Papel, Cerveza y Curtiembre</p>
        <p><strong>Publicación:</strong> 24 de agosto de 2010</p>
        <p><strong>Alcance:</strong> Industrias manufactureras específicas</p>
        <p><strong>Sectores regulados:</strong></p>
        <ul style='color: rgba(255,255,255,0.95); line-height: 1.8;'>
            <li><strong>Cemento:</strong> PM, SO2, NOx</li>
            <li><strong>Papel:</strong> PM, TRS (compuestos reducidos de azufre totales)</li>
            <li><strong>Cerveza:</strong> PM, SO2, NOx</li>
            <li><strong>Curtiembre:</strong> PM, H2S</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
       target='_blank' class='corporate-button'>
        📄 Ver D.S. N° 010-2010-MINAM
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tabla comparativa LMP con diseño azul profesional
    st.markdown("""
    <div style='background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(10, 25, 41, 0.98) 100%); 
                padding: 2rem; border-radius: 16px; margin: 2rem 0; 
                border: 1px solid rgba(0, 184, 217, 0.3);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);'>
        <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;'>
            <div style='font-size: 2.5rem;'>📊</div>
            <h2 style='color: #FFFFFF; margin: 0; font-size: 1.8rem; font-weight: 900;'>
                Comparación de LMP por Sector
            </h2>
        </div>
        <p style='color: rgba(255, 255, 255, 0.8); font-size: 1rem; margin: 0.5rem 0 0 0;'>
            Valores referenciales de PM y SO2 según actividad
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Usar components.html para renderizado garantizado
    import streamlit.components.v1 as components
    
    html_lmp = """
    <div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); 
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);'>
        <table style='width: 100%; border-collapse: collapse; 
                      background: linear-gradient(135deg, rgba(19, 47, 76, 0.95) 0%, rgba(26, 58, 82, 0.9) 100%);'>
            <thead>
                <tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Sector</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>PM (mg/Nm³)</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>SO2 (mg/Nm³)</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>NOx (mg/Nm³)</th>
                    <th style='color: #FFF; padding: 1.2rem 1.5rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.95rem; font-weight: 900; border: none;'>Normativa</th>
                </tr>
            </thead>
            <tbody>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #3B82F6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Minero-Metalúrgico</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>100</td>
                    <td style='color: #FF9800; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>800</td>
                    <td style='color: rgba(255,255,255,0.5); padding: 1rem 1.5rem; text-align: center; font-size: 1.05rem; font-weight: 900;'>-</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>R.M. 315-96</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #10B981; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Termoeléctrico (Gas Natural)</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>50</td>
                    <td style='color: #FF9800; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>300</td>
                    <td style='color: #A855F7; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>320</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 003-2010</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #10B981; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Termoeléctrico (Carbón)</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>150</td>
                    <td style='color: #FF9800; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>1600</td>
                    <td style='color: #A855F7; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>1200</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 003-2010</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #F59E0B; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Cemento</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>150</td>
                    <td style='color: #FF9800; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>700</td>
                    <td style='color: #A855F7; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>800</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 010-2010</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #8B5CF6; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Papel</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>120</td>
                    <td style='color: rgba(255,255,255,0.5); padding: 1rem 1.5rem; text-align: center; font-size: 1.05rem; font-weight: 900;'>-</td>
                    <td style='color: rgba(255,255,255,0.5); padding: 1rem 1.5rem; text-align: center; font-size: 1.05rem; font-weight: 900;'>-</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 010-2010</td>
                </tr>
                <tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08);' onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #EF4444; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Cerveza</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>150</td>
                    <td style='color: #FF9800; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>700</td>
                    <td style='color: #A855F7; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>800</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 010-2010</td>
                </tr>
                <tr onmouseover='this.style.background="rgba(0,184,217,0.15)"' onmouseout='this.style.background="transparent"'>
                    <td style='color: #06B6D4; padding: 1rem 1.5rem; font-weight: 700; font-size: 1.05rem; font-weight: 900;'>Curtiembre</td>
                    <td style='color: #FDD835; padding: 1rem 1.5rem; text-align: center; font-size: 1.1rem; font-weight: 900;'>150</td>
                    <td style='color: rgba(255,255,255,0.5); padding: 1rem 1.5rem; text-align: center; font-size: 1.05rem; font-weight: 900;'>-</td>
                    <td style='color: rgba(255,255,255,0.5); padding: 1rem 1.5rem; text-align: center; font-size: 1.05rem; font-weight: 900;'>-</td>
                    <td style='color: #00B8D9; padding: 1rem 1.5rem; text-align: center; font-size: 0.95rem; font-weight: 600;'>D.S. 010-2010</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    
    components.html(html_lmp, height=500, scrolling=True)
    
    st.info("📌 **Nota:** Los valores son referenciales y pueden variar según las condiciones específicas de cada normativa (temperatura, oxígeno de referencia, etc.)")

# Footer
st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<h3 style='color: #00E5FF;'>🌍 Marco Normativo</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-size: 1.05rem; font-weight: 900;'>Sistema integral de consulta de normativas ambientales para la gestión y control de la calidad del aire en el Perú.</p>", unsafe_allow_html=True)
    st.info("📚 Herramienta Educativa & Profesional")

with col2:
    st.markdown("<h3 style='color: #00E5FF;'>🎓 Institución</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-size: 1rem; font-weight: 600;'>Universidad Nacional de Moquegua</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>Facultad de Ingeniería y Arquitectura</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: rgba(255,255,255,0.9); font-size: 0.95rem;'>Escuela Profesional de Ingeniería Ambiental</p>", unsafe_allow_html=True)
    st.success("🏛️ Moquegua, Perú")

with col3:
    st.markdown("<h3 style='color: #00E5FF;'>👨‍🏫 Docente</h3>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-size: 1rem; font-weight: 600;'>Prof. Dr. José Antonio Valeriano Zapana</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-size: 0.95rem;'>📧 <a href='mailto:contacto@unam.edu.pe' style='color: #00FFB8; text-decoration: none;'>contacto@unam.edu.pe</a></p>", unsafe_allow_html=True)
    st.markdown("<p style='color: white; font-size: 0.95rem;'>📱 <span style='color: #00FFB8;'>+51 961 854 041</span></p>", unsafe_allow_html=True)
    st.info("💼 Especialista en Calidad del Aire")

st.divider()

col_a, col_b = st.columns([2, 1])
with col_a:
    st.markdown("<p style='color: white; font-size: 0.95rem;'>© 2024 UNAM - Todos los derechos reservados</p>", unsafe_allow_html=True)
with col_b:
    st.markdown("<div style='text-align:right'><span style='background: linear-gradient(90deg, #00B8D9, #0065FF); padding: 0.6rem 1.2rem; border-radius: 20px; color: white; font-weight: 700; box-shadow: 0 4px 15px rgba(0,184,217,0.5);'>📅 Octubre 2024</span></div>", unsafe_allow_html=True)
