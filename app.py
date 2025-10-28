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
# ===================== PÁGINA INICIO =====================
if st.session_state.pagina == "Inicio":
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Normativas Nacionales", value="12", delta="Vigentes")
    
    with col2:
        st.metric(label="Estándares Internacionales", value="6", delta="OMS, EPA, Canadá")
    
    with col3:
        st.metric(label="Contaminantes Regulados", value="8", delta="Criterio")
    
    with col4:
        st.metric(label="Protocolos Activos", value="5", delta="Monitoreo")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>📚 Evolución del Marco Normativo Peruano</h2>
            <p style='font-size: 1.05rem; margin-bottom: 2rem;'>
                Recorrido histórico de las principales normativas de calidad del aire en Perú
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
        
        
        # ========== TIMELINE HORIZONTAL SIMPLE (SIN JAVASCRIPT) ==========
        
        st.markdown("""
        <div style='text-align:center;margin:1rem 0;padding:1rem;background:rgba(0,184,217,0.1);border-radius:10px;border:1px solid rgba(0,184,217,0.3)'>
            <p style='color:#00B8D9;font-size:1rem;margin:0;font-weight:600'>
                👉 Arrastra horizontalmente para ver toda la línea de tiempo 👈
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        timeline_html = """<style>
.tl-wrapper{width:100%;padding:1rem 0;margin:2rem 0}
.tl-scroll{width:100%;overflow-x:auto;overflow-y:hidden;padding:4rem 2rem 3rem 2rem;background:linear-gradient(135deg,rgba(10,25,41,0.4),rgba(19,47,76,0.3));border-radius:20px;scroll-behavior:smooth;-webkit-overflow-scrolling:touch}
.tl-scroll::-webkit-scrollbar{height:12px}
.tl-scroll::-webkit-scrollbar-track{background:rgba(19,47,76,0.5);border-radius:10px}
.tl-scroll::-webkit-scrollbar-thumb{background:linear-gradient(90deg,#0052CC,#00B8D9);border-radius:10px;border:2px solid rgba(19,47,76,0.5)}
.tl-scroll::-webkit-scrollbar-thumb:hover{background:linear-gradient(90deg,#0065FF,#00E5FF)}
.tl-container{display:inline-flex;flex-direction:row;gap:0;position:relative;min-width:max-content}
.tl-track{position:absolute;top:50%;left:0;right:0;height:4px;background:linear-gradient(90deg,transparent 2%,#00B8D9 50%,transparent 98%);transform:translateY(-50%);z-index:1;box-shadow:0 0 10px rgba(0,184,217,0.4)}
.tl-item{display:inline-flex;flex-direction:column;align-items:center;padding:0 1.5rem;z-index:2;min-width:260px}
.tl-card{width:230px;background:rgba(19,47,76,0.9);backdrop-filter:blur(15px);border-radius:16px;padding:1.5rem;margin-bottom:2.5rem;border:1px solid rgba(255,255,255,0.1);box-shadow:0 10px 30px rgba(0,0,0,0.4);transition:all 0.4s cubic-bezier(0.4,0,0.2,1);cursor:pointer;position:relative}
.tl-card:hover{transform:translateY(-12px);box-shadow:0 20px 50px rgba(0,82,204,0.6);border-color:rgba(0,184,217,0.5)}
.tl-icon{position:absolute;top:-14px;right:14px;width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;border:1px solid rgba(255,255,255,0.15);transition:all 0.3s}
.tl-card:hover .tl-icon{transform:scale(1.15) rotate(5deg)}
.tl-year{font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,#00B8D9,#0065FF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin:0 0 0.6rem 0;line-height:1}
.tl-badge{display:inline-block;padding:0.4rem 1rem;border-radius:18px;font-size:0.68rem;font-weight:700;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:0.9rem;border:1px solid}
.tl-title{color:#FFF;font-size:0.92rem;font-weight:600;margin:0 0 0.7rem 0;line-height:1.4}
.tl-desc{color:#B2BAC2;font-size:0.82rem;line-height:1.6;margin:0}
.tl-connector{width:2px;height:2.5rem;opacity:0.4;margin-bottom:0.5rem}
.tl-dot{width:22px;height:22px;border-radius:50%;border:4px solid rgba(10,25,41,1);transition:all 0.3s;box-shadow:0 0 0 0 transparent}
.tl-item:hover .tl-dot{transform:scale(1.4);box-shadow:0 0 20px currentColor}
</style>
<div class='tl-wrapper'>
<div class='tl-scroll'>
<div class='tl-track'></div>
<div class='tl-container'>"""
        
        cats = {
            'ECA': {'icon': '⭐', 'color': '#00C853'},
            'LMP': {'icon': '🏭', 'color': '#FF6F00'},
            'Protocolo': {'icon': '📋', 'color': '#8E24AA'},
            'Lineamiento': {'icon': '📐', 'color': '#0091EA'},
            'Marco Legal': {'icon': '⚖️', 'color': '#D32F2F'}
        }
        
        for idx, row in df_timeline.iterrows():
            c = cats[row['categoria']]
            timeline_html += f"""
<div class='tl-item'>
<div class='tl-card'>
<div class='tl-icon' style='background:{c["color"]}15;color:{c["color"]}'>{c["icon"]}</div>
<div class='tl-year'>{row['año']}</div>
<span class='tl-badge' style='color:{c["color"]};border-color:{c["color"]};background:{c["color"]}12'>{row['categoria']}</span>
<h4 class='tl-title'>{row['titulo']}</h4>
<p class='tl-desc'>{row['descripcion']}</p>
</div>
<div class='tl-connector' style='background:linear-gradient(180deg,{c["color"]},transparent)'></div>
<div class='tl-dot' style='background:{c["color"]};box-shadow:0 0 15px {c["color"]}90'></div>
</div>"""
        
        timeline_html += """
</div></div></div>"""
        
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align:center;margin-top:1.5rem'>
            <p style='color:#B2BAC2;font-size:0.9rem'>
                💻 En computadora: Click y arrastra | 📱 En móvil: Desliza con el dedo
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # ========== FIN TIMELINE ==========
        
        
        st.markdown("""
        <div class='corporate-card' style='margin-top: 2rem;'>
            <h3 style='text-align: center; margin-bottom: 1.5rem;'>📂 Categorías del Sistema Normativo</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h3 style='color: #00B8D9;'>📂 Explora por Categoría</h3>
            <p style='color: var(--text-secondary);'>Haz click en cualquier categoría para ver su contenido completo</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            # Card ECA - Clickeable
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
            if st.button("📄 Ver ECA", key="goto_eca", use_container_width=True):
                st.session_state.pagina = "ECA"
                st.rerun()
            
            # Card Protocolos - Clickeable
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(142, 36, 170, 0.2), rgba(156, 39, 176, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #8E24AA; text-align: center; margin-bottom: 1rem; margin-top: 1rem;'>
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
            if st.button("📄 Ver Protocolos", key="goto_proto", use_container_width=True):
                st.session_state.pagina = "Protocolo"
                st.rerun()
        
        with col_b:
            # Card LMP - Clickeable
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
            if st.button("📄 Ver LMP", key="goto_lmp", use_container_width=True):
                st.session_state.pagina = "LMP"
                st.rerun()
            
            # Card Marco Legal - Clickeable
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(211, 47, 47, 0.2), rgba(229, 57, 53, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #D32F2F; text-align: center; margin-bottom: 1rem; margin-top: 1rem;'>
                <div style='font-size: 3rem; margin-bottom: 0.5rem;'>⚖️</div>
                <h4 style='color: #D32F2F; margin: 0.5rem 0;'>Marco Legal</h4>
                <p style='color: var(--text-secondary); font-size: 0.9rem; margin: 0;'>
                    Leyes y Decretos Base
                </p>
                <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                    <span style='font-size: 1.5rem; font-weight: 700; color: #D32F2F;'>3</span>
                    <p style='font-size: 0.8rem; color: var(--text-secondary); margin: 0.25rem 0 0 0;'>Leyes</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("📄 Ver Marco Legal", key="goto_legal", use_container_width=True):
                st.session_state.pagina = "Medidas"
                st.rerun()
        
        with col_c:
            # Card Lineamientos - Clickeable
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 145, 234, 0.2), rgba(3, 169, 244, 0.1)); 
                        padding: 1.5rem; border-radius: 12px; border-left: 4px solid #0091EA; text-align: center; margin-bottom: 1rem;'>
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
            if st.button("📄 Ver Lineamientos", key="goto_linea", use_container_width=True):
                st.session_state.pagina = "Lineamiento"
                st.rerun()
            
            # Card Internacional - Clickeable
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
            if st.button("📄 Ver Internacional", key="goto_inter", use_container_width=True):
                st.session_state.pagina = "Normativas"
                st.rerun()
        
        
        st.success("""
        **✓ Beneficios del Sistema**
        
        **📄 Acceso Directo:** Enlaces actualizados a documentos oficiales
        
        **📊 Visualizaciones:** Gráficos interactivos para análisis comparativo
        
        **✅ Información Validada:** Datos técnicos verificados y referencias completas
        """)
    
    with col2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>⚡ Acceso Directo</h2>
            <p style='color: rgba(255,255,255,0.95); margin-bottom: 1.5rem;'>
                Navegue rápidamente a las secciones principales
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📋 Estándares ECA", use_container_width=True, type="primary", key="quick_eca"):
            st.session_state.pagina = "ECA"
            st.rerun()
        
        if st.button("🏭 Límites LMP", use_container_width=True, key="quick_lmp"):
            st.session_state.pagina = "LMP"
            st.rerun()
        
        if st.button("📖 Protocolos", use_container_width=True, key="quick_protocolo"):
            st.session_state.pagina = "Protocolo"
            st.rerun()
        
        if st.button("📐 Lineamientos", use_container_width=True, key="quick_lineamiento"):
            st.session_state.pagina = "Lineamiento"
            st.rerun()
        
        if st.button("🛡️ Control Emisiones", use_container_width=True, key="quick_medidas"):
            st.session_state.pagina = "Medidas"
            st.rerun()
        
        if st.button("🌍 Normativas Mundial", use_container_width=True, key="quick_normativas"):
            st.session_state.pagina = "Normativas"
            st.rerun()
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.info("**Sugerencia:** Utilice el buscador del menú lateral para encontrar normativas específicas.")
        st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Análisis Comparativo: PM2.5 Anual</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Comparación de estándares internacionales vs. normativa peruana vigente
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    datos_comp = pd.DataFrame([
        {'Entidad': 'OMS 2021', 'Valor': 5, 'Tipo': 'Internacional'},
        {'Entidad': 'EPA USA 2024', 'Valor': 9, 'Tipo': 'Internacional'},
        {'Entidad': 'Canadá 2025', 'Valor': 8, 'Tipo': 'Internacional'},
        {'Entidad': 'OEFA Perú', 'Valor': 25, 'Tipo': 'Nacional'}
    ])
    
    fig = go.Figure()
    
    internacional = datos_comp[datos_comp['Tipo'] == 'Internacional']
    nacional = datos_comp[datos_comp['Tipo'] == 'Nacional']
    
    fig.add_trace(go.Bar(
        name='Internacional',
        x=internacional['Entidad'],
        y=internacional['Valor'],
        marker_color='#00B8D9',
        text=internacional['Valor'],
        texttemplate='%{text} μg/m³',
        textposition='outside'
    ))
    
    fig.add_trace(go.Bar(
        name='Nacional',
        x=nacional['Entidad'],
        y=nacional['Valor'],
        marker_color='#FFB300',
        text=nacional['Valor'],
        texttemplate='%{text} μg/m³',
        textposition='outside'
    ))
    
    fig.update_layout(
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title=''),
        yaxis=dict(
            showgrid=True, 
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentración (μg/m³)',
            range=[0, 30]
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(19, 47, 76, 0.8)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1
        ),
        margin=dict(t=40, b=60, l=60, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.warning("**⚠️ Análisis:** El estándar peruano de PM2.5 anual (25 μg/m³) es 5 veces más permisivo que la recomendación de la OMS (5 μg/m³) y 2.8 veces más alto que el estándar de EPA USA (9 μg/m³). Se recomienda evaluar una actualización gradual de los ECA nacionales para mejor protección de la salud pública.")

# ===================== PÁGINA ECA =====================
elif st.session_state.pagina == "ECA":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📋 Estándares de Calidad Ambiental (ECA)</h2>
        <p style='font-size: 1.05rem;'>
            Los ECA establecen los <strong>niveles de concentración de contaminantes en el aire ambiente</strong> 
            que no deben superarse para proteger la salud de la población. Se miden en estaciones de monitoreo 
            de calidad del aire y son de cumplimiento obligatorio en todo el territorio nacional.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Diferencia clave:** ECA se mide en aire ambiente (lo que respiramos), mientras que LMP se mide en la fuente de emisión (chimeneas, ductos).")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 003-2017-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Estándares de Calidad Ambiental (ECA) para Aire</strong>
        </p>
        <p>
            Norma principal que establece los valores de concentración máxima de contaminantes del aire 
            que no deben superarse para proteger la salud humana y el ambiente. Incluye PM2.5, PM10, SO2, 
            NO2, O3, CO, Pb, H2S y BaP. Establece períodos de cumplimiento y métodos de referencia.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 07 de junio de 2017 | 
            <strong>Vigencia:</strong> Desde junio 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/06/DS-003-2017-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 003-2017-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card modificatoria fade-in'>
        <span class='status-badge modificatoria'>● MODIFICATORIA</span>
        <h3>D.S. N° 010-2019-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Modificatoria del D.S. N° 003-2017-MINAM</strong>
        </p>
        <p>
            Actualiza parámetros y períodos de evaluación de los ECA para aire. Modifica las formas de 
            cumplimiento de algunos estándares adaptándose a nueva evidencia científica sobre efectos en 
            la salud pública y capacidades de monitoreo nacional.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 12 de julio de 2019 | 
            <strong>Vigencia:</strong> Desde julio 2019
        </p>
        <a href='https://busquedas.elperuano.pe/download/url/decreto-supremo-que-modifica-el-decreto-supremo-n-003-2017-decreto-supremo-n-010-2019-minam-1792823-1' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 010-2019-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card referencia fade-in'>
        <span class='status-badge referencia'>● REFERENCIA HISTÓRICA</span>
        <h3>D.S. N° 074-2001-PCM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Estándares Nacionales de Calidad Ambiental del Aire (Derogado)</strong>
        </p>
        <p>
            Primera norma que estableció los ECA para aire en Perú. Estuvo vigente durante 16 años hasta 
            su reemplazo por el D.S. 003-2017-MINAM. Importante para contexto histórico y análisis de la 
            evolución normativa nacional en materia de calidad del aire.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 24 de junio de 2001 | 
            <strong>Derogación:</strong> Junio 2017
        </p>
        <a href='https://sinia.minam.gob.pe/normas/reglamento-estandares-nacionales-calidad-ambiental-aire' 
           target='_blank' class='corporate-button'>
            📄 Ver D.S. 074-2001-PCM (Histórico)
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Valores de ECA Vigentes (D.S. 003-2017-MINAM)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1.5rem;'>
            Concentraciones máximas permitidas en aire ambiente para protección de salud pública
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eca_valores = pd.DataFrame([
        ['PM2.5', '24 horas', 50, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM2.5', 'Anual', 25, 'μg/m³', 'Media aritmética anual'],
        ['PM10', '24 horas', 100, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM10', 'Anual', 50, 'μg/m³', 'Media aritmética anual'],
        ['NO2', '1 hora', 200, 'μg/m³', 'No exceder más de 24 veces al año'],
        ['NO2', 'Anual', 100, 'μg/m³', 'Media aritmética anual'],
        ['SO2', '24 horas', 250, 'μg/m³', 'No exceder más de 7 veces al año'],
        ['O3', '8 horas', 100, 'μg/m³', 'Máximas diarias de promedios móviles'],
        ['CO', '8 horas', 10000, 'μg/m³', 'Promedio móvil'],
        ['CO', '1 hora', 30000, 'μg/m³', 'No exceder más de 1 vez al año'],
        ['Pb', 'Mensual', 1.5, 'μg/m³', 'Media aritmética mensual'],
        ['Pb', 'Anual', 0.5, 'μg/m³', 'Media aritmética anual'],
        ['H2S', '24 horas', 150, 'μg/m³', 'Media aritmética'],
        ['BaP', 'Anual', 0.0012, 'μg/m³', 'Media aritmética anual']
    ], columns=['Contaminante', 'Período', 'Valor', 'Unidad', 'Forma del Estándar'])
    
    # Tabla HTML personalizada para ECA
    tabla_eca_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Período</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Valor</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Forma del Estándar</th>
</tr>
</thead>
<tbody>"""
    
    # Generar filas dinámicamente
    filas = [
        ['PM2.5', '24 horas', '50', 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM2.5', 'Anual', '25', 'μg/m³', 'Media aritmética anual'],
        ['PM10', '24 horas', '100', 'μg/m³', 'No exceder más de 7 veces al año'],
        ['PM10', 'Anual', '50', 'μg/m³', 'Media aritmética anual'],
        ['NO2', '1 hora', '200', 'μg/m³', 'No exceder más de 24 veces al año'],
        ['NO2', 'Anual', '100', 'μg/m³', 'Media aritmética anual'],
        ['SO2', '24 horas', '250', 'μg/m³', 'No exceder más de 7 veces al año'],
        ['O3', '8 horas', '100', 'μg/m³', 'Máximas diarias de promedios móviles'],
        ['CO', '8 horas', '10000', 'μg/m³', 'Promedio móvil'],
        ['CO', '1 hora', '30000', 'μg/m³', 'No exceder más de 1 vez al año'],
        ['Pb', 'Mensual', '1.5', 'μg/m³', 'Media aritmética mensual'],
        ['Pb', 'Anual', '0.5', 'μg/m³', 'Media aritmética anual'],
        ['H2S', '24 horas', '150', 'μg/m³', 'Media aritmética'],
        ['BaP', 'Anual', '0.0012', 'μg/m³', 'Media aritmética anual']
    ]
    
    for i, fila in enumerate(filas):
        border = '' if i == len(filas) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
        tabla_eca_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[4]}</td>
</tr>"""
    
    tabla_eca_html += """</tbody>
</table>
</div>"""
    
    st.markdown(tabla_eca_html, unsafe_allow_html=True)
    
    with st.expander("Ver información adicional sobre contaminantes criterio", expanded=False):
        st.markdown("""
        <div style='margin-bottom: 2rem;'>
            <h2 style='text-align: center; color: #00B8D9; margin-bottom: 2rem;'>🔬 Contaminantes Criterio Regulados</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(0, 184, 217, 0.15), rgba(139, 92, 246, 0.05)); 
                         border-left: 4px solid #8B5CF6;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>💨</div>
                    <div>
                        <h3 style='color: #8B5CF6; margin: 0;'>Material Particulado</h3>
                        <p style='color: #00B8D9; margin: 0; font-size: 0.9rem;'>PM2.5 y PM10</p>
                    </div>
                </div>
                <div style='line-height: 1.6;'>
                    <p style='color: #FFFFFF; margin: 0.5rem 0;'><strong style='color: #FFFFFF;'>Descripción:</strong> Partículas sólidas o líquidas suspendidas en el aire</p>
                    <p style='color: #FFFFFF; margin: 0.5rem 0;'><strong style='color: #FFFFFF;'>Características:</strong><br>
                    • PM2.5: diámetro ≤ 2.5 μm (penetran profundamente en pulmones)<br>
                    • PM10: diámetro ≤ 10 μm (afectan vías respiratorias superiores)</p>
                    <p style='color: #FFFFFF; margin: 0.5rem 0;'><strong style='color: #FFFFFF;'>Fuentes:</strong> Combustión, polvo, actividades industriales, quema de biomasa</p>
                    <p style='color: #FFFFFF; background: rgba(139, 92, 246, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem; color: #FFFFFF;'>
                        <strong style='color: #FFFFFF;'>⚠️ Impacto en salud:</strong> Enfermedades respiratorias, cardiovasculares, mortalidad prematura
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(239, 68, 68, 0.15), rgba(239, 68, 68, 0.05)); 
                         border-left: 4px solid #EF4444;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>🚗</div>
                    <div>
                        <h3 style='color: #EF4444; margin: 0;'>Dióxido de Nitrógeno</h3>
                        <p style='color: #F87171; margin: 0; font-size: 0.9rem;'>NO₂</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Gas irritante de color marrón rojizo</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Combustión vehicular e industrial, centrales eléctricas</p>
                    <p style='color: #FFFFFF; background: rgba(239, 68, 68, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Irritación respiratoria, reducción función pulmonar, agrava asma
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(234, 179, 8, 0.15), rgba(234, 179, 8, 0.05)); 
                         border-left: 4px solid #EAB308;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>🏭</div>
                    <div>
                        <h3 style='color: #EAB308; margin: 0;'>Dióxido de Azufre</h3>
                        <p style='color: #FBBF24; margin: 0; font-size: 0.9rem;'>SO₂</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Gas incoloro con olor penetrante</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Combustión de combustibles fósiles con azufre, fundiciones</p>
                    <p style='color: #FFFFFF; background: rgba(234, 179, 8, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Irritación respiratoria, enfermedades cardiovasculares, lluvia ácida
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(6, 182, 212, 0.15), rgba(6, 182, 212, 0.05)); 
                         border-left: 4px solid #06B6D4;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>☀️</div>
                    <div>
                        <h3 style='color: #06B6D4; margin: 0;'>Ozono Troposférico</h3>
                        <p style='color: #22D3EE; margin: 0; font-size: 0.9rem;'>O₃</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Contaminante secundario (no se emite directamente)</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Formación:</strong> Reacción fotoquímica de NOx y COVs bajo luz solar</p>
                    <p style='color: #FFFFFF; background: rgba(6, 182, 212, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Daño pulmonar, reducción función respiratoria, agrava enfermedades
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(168, 85, 247, 0.05)); 
                         border-left: 4px solid #A855F7;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>🔥</div>
                    <div>
                        <h3 style='color: #A855F7; margin: 0;'>Monóxido de Carbono</h3>
                        <p style='color: #C084FC; margin: 0; font-size: 0.9rem;'>CO</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Gas incoloro e inodoro (altamente peligroso)</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Combustión incompleta de vehículos, calefacción, industrias</p>
                    <p style='color: #FFFFFF; background: rgba(168, 85, 247, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Reduce capacidad de transporte de oxígeno en sangre, fatal en altas concentraciones
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(244, 63, 94, 0.15), rgba(244, 63, 94, 0.05)); 
                         border-left: 4px solid #F43F5E;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>⚠️</div>
                    <div>
                        <h3 style='color: #F43F5E; margin: 0;'>Plomo</h3>
                        <p style='color: #FB7185; margin: 0; font-size: 0.9rem;'>Pb</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Metal pesado tóxico persistente</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Históricamente gasolina con plomo, baterías, industrias mineras y metalúrgicas</p>
                    <p style='color: #FFFFFF; background: rgba(244, 63, 94, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Neurotoxicidad, afecta desarrollo infantil, daño renal y cardiovascular
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(34, 197, 94, 0.15), rgba(34, 197, 94, 0.05)); 
                         border-left: 4px solid #22C55E;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>🧪</div>
                    <div>
                        <h3 style='color: #22C55E; margin: 0;'>Sulfuro de Hidrógeno</h3>
                        <p style='color: #4ADE80; margin: 0; font-size: 0.9rem;'>H₂S</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Gas con olor característico a huevo podrido</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Actividades petroleras, refinerías, descomposición de materia orgánica</p>
                    <p style='color: #FFFFFF; background: rgba(34, 197, 94, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> Irritación ocular y respiratoria, tóxico en altas concentraciones
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='pollutant-card' style='background: linear-gradient(135deg, rgba(249, 115, 22, 0.15), rgba(249, 115, 22, 0.05)); 
                         border-left: 4px solid #F97316;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='font-size: 3rem;'>☢️</div>
                    <div>
                        <h3 style='color: #F97316; margin: 0;'>Benzo(a)pireno</h3>
                        <p style='color: #FB923C; margin: 0; font-size: 0.9rem;'>BaP</p>
                    </div>
                </div>
                <div style='line-height: 1.6; color: #FFFFFF;'>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Descripción:</strong> Hidrocarburo aromático policíclico (HAP)</p>
                    <p style="color: #FFFFFF; margin: 0.5rem 0;"><strong style="color: #FFFFFF;">Fuentes:</strong> Combustión incompleta de materia orgánica, humo de tabaco, asado de carnes</p>
                    <p style='color: #FFFFFF; background: rgba(249, 115, 22, 0.2); padding: 0.75rem; border-radius: 8px; margin-top: 0.5rem;'>
                        <strong style="color: #FFFFFF;">⚠️ Impacto en salud:</strong> <span style='color: #FFA500;'>Cancerígeno confirmado</span>, mutagénico, teratogénico
                    </p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        # ===================== PÁGINA LMP =====================
elif st.session_state.pagina == "LMP":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🏭 Límites Máximos Permisibles (LMP)</h2>
        <p style='font-size: 1.05rem;'>
            Los LMP son <strong>valores de concentración máxima de contaminantes</strong> que pueden 
            ser emitidos al ambiente desde una fuente puntual de emisión (chimeneas, ductos). Son 
            específicos por sector productivo y tipo de actividad, estableciendo obligaciones para 
            el cumplimiento ambiental de las empresas.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Diferencia clave:** Los LMP se aplican a la fuente emisora y son medidos en el punto de descarga, mientras que los ECA se miden en el aire ambiente que respira la población.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 003-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones Atmosféricas para Centrales Termoeléctricas</strong>
        </p>
        <p>
            Establece límites de emisión de NOx, SO2 y Material Particulado para plantas de generación 
            termoeléctrica. Los límites varían según el tipo de combustible utilizado (gas natural, diesel, 
            residual). Mediciones en condiciones normalizadas: 25°C, 1 atm, base seca, 15% O2.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 17 de enero de 2010 | 
            <strong>Sector:</strong> Energía
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_003-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 003-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 011-2009-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Vehículos Automotores</strong>
        </p>
        <p>
            Regula las emisiones de gases contaminantes de vehículos automotores que circulan por la red 
            vial. Incluye límites para CO, HC, NOx y Material Particulado según categoría vehicular 
            (ligeros, pesados) y tipo de combustible. Establece procedimientos de verificación técnica vehicular.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 13 de marzo de 2009 | 
            <strong>Sector:</strong> Transporte
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_011-2009-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 011-2009-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 010-2010-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>LMP de Emisiones para Industrias de Cemento, Papel, Cerveza y Curtiembre</strong>
        </p>
        <p>
            Establece límites de emisión atmosférica para industrias de cemento, papel, cerveza y curtiembre. 
            Regula emisiones de Material Particulado, SO2, NOx y otros contaminantes específicos según el 
            proceso industrial. Define métodos de muestreo y análisis, así como plazos de cumplimiento.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 17 de agosto de 2010 | 
            <strong>Sector:</strong> Industria Manufacturera
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2013/09/ds_010-2010-minam.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 010-2010-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 315-96-EM/VMM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Niveles Máximos Permisibles para Fundiciones y Refinerías</strong>
        </p>
        <p>
            Establece los niveles máximos permisibles de emisiones de gases y partículas para las actividades 
            minero-metalúrgicas de fundición y refinación. Regula emisiones de SO2, Material Particulado, 
            plomo, arsénico y otros metales pesados específicos de procesos metalúrgicos.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 19 de julio de 1996 | 
            <strong>Sector:</strong> Minería y Metalurgia
        </p>
        <a href='https://sinia.minam.gob.pe/normas/niveles-maximos-permisibles-elementos-compuestos-presentes-emisiones' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 315-96-EM/VMM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 LMP para Centrales Termoeléctricas por Tipo de Combustible</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            D.S. 003-2010-MINAM | Condiciones: 25°C, 1 atm, base seca, 15% O2
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    lmp_termo = pd.DataFrame([
        ['Óxidos de Nitrógeno (NOx)', 320, 850, 2000, 'mg/Nm³'],
        ['Dióxido de Azufre (SO2)', 0, 1700, 3500, 'mg/Nm³'],
        ['Material Particulado (MP)', 50, 150, 350, 'mg/Nm³']
    ], columns=['Contaminante', 'Gas Natural', 'Diesel', 'Residual', 'Unidad'])
    
    # Tabla HTML personalizada para LMP Termoeléctricas
    tabla_lmp_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none; min-width: 250px;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Gas Natural</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Diesel</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Residual</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
</tr>
</thead>
<tbody>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>Óxidos de Nitrógeno (NOx)</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>320</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>850</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>2000</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>mg/Nm³</td>
</tr>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>Dióxido de Azufre (SO2)</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>0</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>1700</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>3500</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>mg/Nm³</td>
</tr>
<tr style='transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>Material Particulado (MP)</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>50</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>150</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>350</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>mg/Nm³</td>
</tr>
</tbody>
</table>
</div>"""
    
    st.markdown(tabla_lmp_html, unsafe_allow_html=True)
    
    fig_lmp = go.Figure()
    
    contaminantes = lmp_termo['Contaminante'].tolist()
    
    fig_lmp.add_trace(go.Bar(
        name='Gas Natural',
        x=contaminantes,
        y=lmp_termo['Gas Natural'],
        marker_color='#00C853',
        text=lmp_termo['Gas Natural'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.add_trace(go.Bar(
        name='Diesel',
        x=contaminantes,
        y=lmp_termo['Diesel'],
        marker_color='#FFB300',
        text=lmp_termo['Diesel'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.add_trace(go.Bar(
        name='Residual',
        x=contaminantes,
        y=lmp_termo['Residual'],
        marker_color='#D32F2F',
        text=lmp_termo['Residual'],
        texttemplate='%{text}',
        textposition='outside'
    ))
    
    fig_lmp.update_layout(
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=13, family='Inter'),
        xaxis=dict(showgrid=False, title=''),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Concentración (mg/Nm³)',
            type='log'
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(19, 47, 76, 0.8)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1
        )
    )
    
    st.plotly_chart(fig_lmp, use_container_width=True)
    
    st.info("**Nota técnica:** Los límites son más estrictos para combustibles más limpios. El gas natural tiene los LMP más bajos debido a su menor contenido de azufre y mejor eficiencia de combustión, mientras que el residual (combustóleo) tiene los límites más permisivos debido a su mayor contenido de impurezas.")
    # ===================== PÁGINA PROTOCOLO =====================
elif st.session_state.pagina == "Protocolo":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📖 Protocolos de Monitoreo y Medición</h2>
        <p style='font-size: 1.05rem;'>
            Los protocolos establecen <strong>procedimientos técnicos estandarizados</strong> para el 
            monitoreo de calidad del aire y la medición de emisiones atmosféricas. Garantizan que las 
            mediciones sean comparables, confiables y válidas a nivel nacional, cumpliendo con estándares 
            internacionales de calidad analítica.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Importancia:** Los protocolos aseguran la trazabilidad, precisión y validez legal de las mediciones ambientales realizadas por laboratorios acreditados y empresas consultoras.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.D. N° 1404-2005/DIGESA/SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad del Aire y Gestión de Datos</strong>
        </p>
        <p>
            Define los procedimientos técnicos para el monitoreo de calidad del aire ambiente en todo el 
            territorio nacional. Incluye métodos de muestreo, ubicación de estaciones, calibración de 
            equipos, análisis de laboratorio, aseguramiento y control de calidad, y gestión de datos. 
            Aplicable a redes de monitoreo públicas y privadas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 11 de noviembre de 2005 | 
            <strong>Entidad:</strong> DIGESA-MINSA
        </p>
        <a href='https://sinia.minam.gob.pe/documentos/protocolo-monitoreo-calidad-aire-gestion-datos' 
           target='_blank' class='corporate-button'>
            📄 Descargar Protocolo DIGESA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 026-2000-ITINCI/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Aire y Emisiones - Sector Industrial</strong>
        </p>
        <p>
            Aprueba protocolos específicos de monitoreo de calidad de aire y emisiones atmosféricas para 
            actividades industriales manufactureras. Establece metodologías de muestreo isocinético, análisis 
            de gases, y determinación de caudales en fuentes fijas industriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 28 de febrero de 2000 | 
            <strong>Sector:</strong> Industria - PRODUCE
        </p>
        <a href='https://sinia.minam.gob.pe/normas/protocolo-monitoreo-calidad-aire-emisiones-para-actividades' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 026-2000-ITINCI/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.D. N° 195-2010-MEM/AAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calderos y Hornos Industriales</strong>
        </p>
        <p>
            Establece procedimientos estandarizados para el monitoreo de emisiones atmosféricas en calderos 
            y hornos industriales de diversos sectores. Incluye métodos isocinéticos para material particulado, 
            análisis instrumental de gases (SO2, NOx, CO), y determinación de parámetros de proceso.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 12 de agosto de 2010 | 
            <strong>Sector:</strong> Energía y Minas
        </p>
        <a href='https://sinia.minam.gob.pe/normas/aprueban-lineamientos-emision-opiniones-tecnicas-protocolos' 
           target='_blank' class='corporate-button'>
            📄 Ver Legislación MINEM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 247-2009-MEM/DM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Protocolo de Monitoreo de Calidad de Agua y Aire - Minería</strong>
        </p>
        <p>
            Protocolo específico para actividades minero-metalúrgicas que establece procedimientos de monitoreo 
            de calidad de aire en zonas de influencia minera. Define ubicación de estaciones, frecuencias de 
            muestreo, parámetros a evaluar y procedimientos de reporte ante autoridades sectoriales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 14 de mayo de 2009 | 
            <strong>Sector:</strong> Minería
        </p>
        <a href='https://sinia.minam.gob.pe/normas/protocolo-monitoreo-calidad-agua-aire-subsector-mineria' 
           target='_blank' class='corporate-button'>
            📄 Ver R.M. 247-2009-MEM/DM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🔬 Métodos de Referencia EPA Adoptados en Perú</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Métodos estandarizados de la Agencia de Protección Ambiental de EE.UU. (EPA) 
            reconocidos en normativa peruana para asegurar calidad analítica
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    metodos = pd.DataFrame([
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Muestreo gravimétrico con separador inercial', 'Alto volumen (Hi-Vol)'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Muestreo gravimétrico con separador inercial', 'Bajo volumen (Low-Vol)'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV pulsada', 'Analizador continuo'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia', 'Analizador continuo'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Espectrometría infrarroja no dispersiva (NDIR)', 'Analizador continuo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría de absorción UV', 'Analizador continuo'],
        ['Pb', 'EPA Method 40 CFR Part 50, Appendix G', 'Espectrometría de absorción atómica', 'Filtros PM10'],
        ['H2S', 'EPA Method 11', 'Tren de muestreo con solución absorbente', 'Método manual']
    ], columns=['Contaminante', 'Método EPA', 'Técnica Analítica', 'Tipo de Equipo'])
    
    # Generar tabla HTML para Métodos EPA
    filas_metodos = [
        ['PM10', 'EPA Method 40 CFR Part 50, Appendix J', 'Muestreo gravimétrico con separador inercial', 'Alto volumen (Hi-Vol)'],
        ['PM2.5', 'EPA Method 40 CFR Part 50, Appendix L', 'Muestreo gravimétrico con separador inercial', 'Bajo volumen (Low-Vol)'],
        ['SO2', 'EPA Method 40 CFR Part 50, Appendix A-1', 'Fluorescencia UV pulsada', 'Analizador continuo'],
        ['NO2', 'EPA Method 40 CFR Part 50, Appendix F', 'Quimioluminiscencia', 'Analizador continuo'],
        ['CO', 'EPA Method 40 CFR Part 50, Appendix C', 'Espectrometría infrarroja no dispersiva (NDIR)', 'Analizador continuo'],
        ['O3', 'EPA Method 40 CFR Part 50, Appendix D', 'Fotometría de absorción UV', 'Analizador continuo'],
        ['Pb', 'EPA Method 40 CFR Part 50, Appendix G', 'Espectrometría de absorción atómica', 'Filtros PM10'],
        ['H2S', 'EPA Method 11', 'Tren de muestreo con solución absorbente', 'Método manual']
    ]
    
    tabla_metodos_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Método EPA</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Técnica Analítica</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Tipo de Equipo</th>
</tr>
</thead>
<tbody>"""
    
    for i, fila in enumerate(filas_metodos):
        border = '' if i == len(filas_metodos) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
        tabla_metodos_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
</tr>"""
    
    tabla_metodos_html += """</tbody>
</table>
</div>"""
    
    st.markdown(tabla_metodos_html, unsafe_allow_html=True)
    
    with st.expander("Ver flujo de proceso de monitoreo de calidad del aire", expanded=False):
        st.markdown("""
        <div style='margin-bottom: 2rem;'>
            <h2 style='text-align: center; color: #00B8D9; margin-bottom: 1rem;'>🔄 Proceso Completo de Monitoreo de Calidad del Aire</h2>
            <p style='text-align: center; color: #FFFFFF; font-size: 1.05rem;'>Flujo sistemático desde la planificación hasta el reporte</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(59, 130, 246, 0.2), rgba(59, 130, 246, 0.05)); 
                         border-left: 4px solid #3B82F6;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(59, 130, 246, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>📋</div>
                    <div>
                        <h3 style='color: #60A5FA; margin: 0; font-size: 1.4rem;'>1. Planificación</h3>
                        <p style='color: #93C5FD; margin: 0; font-size: 0.85rem;'>Fase inicial de diseño</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Definición de objetivos del monitoreo</p>
                    <p style='margin: 0.3rem 0;'>✓ Selección de ubicación de estaciones (macro y microescala)</p>
                    <p style='margin: 0.3rem 0;'>✓ Determinación de parámetros y frecuencias</p>
                    <p style='margin: 0.3rem 0;'>✓ Elaboración de Plan de Monitoreo</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(16, 185, 129, 0.05)); 
                         border-left: 4px solid #10B981;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(16, 185, 129, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>⚙️</div>
                    <div>
                        <h3 style='color: #34D399; margin: 0; font-size: 1.4rem;'>2. Implementación</h3>
                        <p style='color: #6EE7B7; margin: 0; font-size: 0.85rem;'>Instalación y puesta en marcha</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Instalación y configuración de equipos</p>
                    <p style='margin: 0.3rem 0;'>✓ Calibración inicial con gases certificados</p>
                    <p style='margin: 0.3rem 0;'>✓ Verificación de condiciones ambientales</p>
                    <p style='margin: 0.3rem 0;'>✓ Inicio de operación según protocolo</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(245, 158, 11, 0.2), rgba(245, 158, 11, 0.05)); 
                         border-left: 4px solid #F59E0B;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(245, 158, 11, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>🔧</div>
                    <div>
                        <h3 style='color: #FBBF24; margin: 0; font-size: 1.4rem;'>3. Operación y Mantenimiento</h3>
                        <p style='color: #FCD34D; margin: 0; font-size: 0.85rem;'>Funcionamiento continuo</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Calibraciones periódicas (diarias, semanales, mensuales)</p>
                    <p style='margin: 0.3rem 0;'>✓ Mantenimiento preventivo de equipos</p>
                    <p style='margin: 0.3rem 0;'>✓ Verificación de flujos y condiciones operativas</p>
                    <p style='margin: 0.3rem 0;'>✓ Registro de eventos y anomalías</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(168, 85, 247, 0.2), rgba(168, 85, 247, 0.05)); 
                         border-left: 4px solid #A855F7;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(168, 85, 247, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>✅</div>
                    <div>
                        <h3 style='color: #C084FC; margin: 0; font-size: 1.4rem;'>4. Aseguramiento de Calidad</h3>
                        <p style='color: #D8B4FE; margin: 0; font-size: 0.85rem;'>Control de calidad de datos</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Auditorías internas y externas</p>
                    <p style='margin: 0.3rem 0;'>✓ Análisis de blancos y duplicados</p>
                    <p style='margin: 0.3rem 0;'>✓ Control de precisión y exactitud</p>
                    <p style='margin: 0.3rem 0;'>✓ Validación de datos</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(236, 72, 153, 0.2), rgba(236, 72, 153, 0.05)); 
                         border-left: 4px solid #EC4899;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(236, 72, 153, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>🔬</div>
                    <div>
                        <h3 style='color: #F472B6; margin: 0; font-size: 1.4rem;'>5. Análisis de Laboratorio</h3>
                        <p style='color: #F9A8D4; margin: 0; font-size: 0.85rem;'>Análisis químico y físico</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Análisis gravimétrico (PM)</p>
                    <p style='margin: 0.3rem 0;'>✓ Análisis químico (metales, iones)</p>
                    <p style='margin: 0.3rem 0;'>✓ Control de calidad analítico</p>
                    <p style='margin: 0.3rem 0;'>✓ Certificados de análisis</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(20, 184, 166, 0.2), rgba(20, 184, 166, 0.05)); 
                         border-left: 4px solid #14B8A6;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(20, 184, 166, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>💾</div>
                    <div>
                        <h3 style='color: #2DD4BF; margin: 0; font-size: 1.4rem;'>6. Gestión de Datos</h3>
                        <p style='color: #5EEAD4; margin: 0; font-size: 0.85rem;'>Procesamiento y validación</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Transferencia y almacenamiento de datos</p>
                    <p style='margin: 0.3rem 0;'>✓ Validación estadística</p>
                    <p style='margin: 0.3rem 0;'>✓ Cálculo de promedios según ECA</p>
                    <p style='margin: 0.3rem 0;'>✓ Identificación de excedencias</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='process-card' style='background: linear-gradient(135deg, rgba(239, 68, 68, 0.2), rgba(239, 68, 68, 0.05)); 
                         border-left: 4px solid #EF4444;'>
                <div style='display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;'>
                    <div style='background: rgba(239, 68, 68, 0.3); border-radius: 50%; width: 60px; height: 60px; 
                                display: flex; align-items: center; justify-content: center; font-size: 2rem;'>📊</div>
                    <div>
                        <h3 style='color: #F87171; margin: 0; font-size: 1.4rem;'>7. Reporte</h3>
                        <p style='color: #FCA5A5; margin: 0; font-size: 0.85rem;'>Comunicación de resultados</p>
                    </div>
                </div>
                <div style='color: #FFFFFF; line-height: 1.8; padding-left: 1rem;'>
                    <p style='margin: 0.3rem 0;'>✓ Informes técnicos periódicos</p>
                    <p style='margin: 0.3rem 0;'>✓ Reportes a autoridades competentes</p>
                    <p style='margin: 0.3rem 0;'>✓ Publicación de resultados (cuando aplique)</p>
                    <p style='margin: 0.3rem 0;'>✓ Acciones correctivas si hay excedencias</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div style='background: linear-gradient(135deg, rgba(0, 184, 217, 0.2), rgba(0, 184, 217, 0.05)); 
                         border: 2px dashed #00B8D9; border-radius: 12px; padding: 1.5rem; margin-top: 1rem; text-align: center;'>
                <h4 style='color: #00B8D9; margin: 0 0 0.5rem 0;'>♻️ Proceso Cíclico Continuo</h4>
                <p style='color: #FFFFFF; margin: 0; font-size: 0.9rem;'>
                    El monitoreo de calidad del aire es un proceso continuo que se repite periódicamente,
                    con mejoras constantes basadas en los resultados obtenidos y lecciones aprendidas.
                </p>
            </div>
            """, unsafe_allow_html=True)
        # ===================== PÁGINA LINEAMIENTO =====================
elif st.session_state.pagina == "Lineamiento":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📐 Lineamientos y Guías Técnicas</h2>
        <p style='font-size: 1.05rem;'>
            Los lineamientos son <strong>instrumentos técnico-normativos complementarios</strong> que 
            proporcionan guías operativas para la implementación de normativas ambientales. Establecen 
            metodologías, procedimientos y criterios técnicos específicos para la gestión de calidad del aire.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Función:** Los lineamientos facilitan la aplicación práctica de la normativa legal, proporcionando herramientas técnicas para su cumplimiento efectivo por parte de autoridades, empresas y consultores.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>R.M. N° 181-2016-MINAM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Lineamientos para la Elaboración del Inventario de Emisiones Atmosféricas</strong>
        </p>
        <p>
            Establece la metodología estandarizada para elaborar inventarios de emisiones de contaminantes 
            atmosféricos a nivel nacional, regional y local. Incluye factores de emisión, procedimientos de 
            cálculo, categorización de fuentes, y formatos de reporte. Aplicable a autoridades ambientales 
            y titulares de actividades productivas.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 13 de julio de 2016 | 
            <strong>Ámbito:</strong> Nacional
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2016/07/RM-N%C2%B0-181-2016-MINAM.pdf' 
           target='_blank' class='corporate-button'>
            📄 Descargar R.M. 181-2016-MINAM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 009-2003-SA</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Niveles de Estados de Alerta Nacionales para Contaminantes del Aire</strong>
        </p>
        <p>
            Define los niveles de alerta ambiental (Cuidado, Peligro y Emergencia) ante episodios críticos 
            de contaminación del aire. Establece umbrales de concentración que activan protocolos de emergencia, 
            acciones obligatorias para autoridades y población, y mecanismos de comunicación pública del riesgo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 25 de junio de 2003 | 
            <strong>Entidad:</strong> MINSA
        </p>
        <a href='https://sinia.minam.gob.pe/normas/reglamento-niveles-estados-alerta-nacionales-contaminantes-del-aire' 
           target='_blank' class='corporate-button'>
            📄 Descargar D.S. 009-2003-SA
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>Decreto Legislativo N° 1278</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Ley de Gestión Integral de Residuos Sólidos</strong>
        </p>
        <p>
            Establece lineamientos para el control de emisiones atmosféricas de instalaciones de tratamiento, 
            valorización e incineración de residuos sólidos. Define obligaciones de monitoreo continuo de 
            emisiones (CEMS), límites operativos y procedimientos de reporte ante autoridades sanitarias y ambientales.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 23 de diciembre de 2016 | 
            <strong>Vigencia:</strong> Desde diciembre 2017
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Decreto-Legislativo-N%C2%B0-1278.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Decreto Legislativo 1278
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>⚠️ Niveles de Estados de Alerta Nacional (D.S. 009-2003-SA)</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Umbrales de concentración que activan protocolos de emergencia ambiental
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    niveles_data = [
        ['PM10', '🟡 Cuidado', '250', '350', 'μg/m³', 'Información a grupos sensibles'],
        ['PM10', '🟠 Peligro', '350', '420', 'μg/m³', 'Alerta general a población'],
        ['PM10', '🔴 Emergencia', '> 420', '---', 'μg/m³', 'Emergencia sanitaria regional'],
        ['SO2', '🟡 Cuidado', '500', '1000', 'μg/m³', 'Advertencia a grupos sensibles'],
        ['SO2', '🟠 Peligro', '1000', '1600', 'μg/m³', 'Restricción actividades al aire libre'],
        ['SO2', '🔴 Emergencia', '> 1600', '---', 'μg/m³', 'Suspensión actividades productivas'],
        ['NO2', '🟡 Cuidado', '600', '1200', 'μg/m³', 'Alerta a grupos de riesgo'],
        ['NO2', '🟠 Peligro', '1200', '1600', 'μg/m³', 'Reducción tráfico vehicular'],
        ['NO2', '🔴 Emergencia', '> 1600', '---', 'μg/m³', 'Cierre de vías principales'],
        ['CO', '🟡 Cuidado', '15000', '30000', 'μg/m³', 'Información preventiva'],
        ['CO', '🟠 Peligro', '30000', '40000', 'μg/m³', 'Restricción circulación vehicular'],
        ['CO', '🔴 Emergencia', '> 40000', '---', 'μg/m³', 'Estado de emergencia sanitaria']
    ]
    
    tabla_niveles_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Nivel de Alerta</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Límite Inferior</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Límite Superior</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Acción Requerida</th>
</tr>
</thead>
<tbody>"""
    
    for i, fila in enumerate(niveles_data):
        border = '' if i == len(niveles_data) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
        tabla_niveles_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none; font-size: 1rem;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[4]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[5]}</td>
</tr>"""
    
    tabla_niveles_html += """</tbody>
</table>
</div>"""
    
    st.markdown(tabla_niveles_html, unsafe_allow_html=True)
    
    st.warning("**⚠️ Protocolo de activación:** Las autoridades ambientales y de salud deben activar los niveles de alerta cuando se registren o pronostiquen concentraciones en los rangos establecidos. Las medidas incluyen difusión masiva de información, restricción de actividades, y en casos de emergencia, la declaratoria de estado de emergencia ambiental.")
    # ===================== PÁGINA MEDIDAS =====================
elif st.session_state.pagina == "Medidas":
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🛡️ Medidas y Tecnologías de Control de Emisiones</h2>
        <p style='font-size: 1.05rem;'>
            Las tecnologías de control son <strong>sistemas y equipos diseñados para reducir las emisiones</strong> 
            de contaminantes atmosféricos desde fuentes puntuales. Su implementación es obligatoria para cumplir 
            con los LMP establecidos y representan la mejor tecnología disponible económicamente viable (BATEA).
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("**Marco legal:** La Ley General del Ambiente (Ley 28611) establece la obligación de implementar medidas de prevención y control de la contaminación del aire, priorizando tecnologías limpias y sistemas de reducción de emisiones.")
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>Ley N° 28611 - Ley General del Ambiente</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Título II, Capítulo 3: De la Calidad Ambiental</strong>
        </p>
        <p>
            Establece la obligación legal de implementar medidas de prevención, control y remediación de la 
            contaminación del aire. Define responsabilidades de titulares de actividades productivas para 
            adoptar tecnologías limpias, sistemas de tratamiento de emisiones y programas de monitoreo continuo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 15 de octubre de 2005 | 
            <strong>Ámbito:</strong> Marco general ambiental
        </p>
        <a href='https://www.minam.gob.pe/wp-content/uploads/2017/04/Ley-N%C2%B0-28611.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver Ley 28611
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card vigente fade-in'>
        <span class='status-badge vigente'>● VIGENTE</span>
        <h3>D.S. N° 012-2005-EM</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Reglamento de Plan de Cierre de Minas - Control de Emisiones</strong>
        </p>
        <p>
            Incluye obligaciones específicas de implementación y mantenimiento de sistemas de control de 
            emisiones atmosféricas durante las fases de operación, cierre progresivo y cierre final de 
            operaciones mineras. Define responsabilidades técnicas y financieras para asegurar el cumplimiento 
            a largo plazo.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Publicación:</strong> 05 de agosto de 2005 | 
            <strong>Sector:</strong> Minería
        </p>
        <a href='https://www.minem.gob.pe/minem/archivos/file/Mineria/LEGISLACION/2005/agosto/DS012-2005.pdf' 
           target='_blank' class='corporate-button'>
            📄 Ver D.S. 012-2005-EM
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='normative-card ntp fade-in'>
        <span class='status-badge ntp'>● NORMAS TÉCNICAS</span>
        <h3>Normas Técnicas Peruanas (NTP) - INACAL</h3>
        <p style='font-size: 1.05rem; margin: 1rem 0;'>
            <strong>Gestión Ambiental del Aire - Metodologías y Terminología</strong>
        </p>
        <p>
            <strong>NTP 900.058:2019</strong> - Gestión Ambiental. Calidad del Aire. Métodos de muestreo<br>
            <strong>NTP 900.030:2003</strong> - Gestión Ambiental. Calidad del Aire. Terminología<br>
            <strong>NTP-ISO 9169:2014</strong> - Calidad del aire. Determinación de características de funcionamiento<br><br>
            Normas técnicas que establecen procedimientos estandarizados para evaluación de eficiencia de 
            sistemas de control, métodos de medición de emisiones, y terminología técnica normalizada.
        </p>
        <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
            <strong>Entidad emisora:</strong> Instituto Nacional de Calidad (INACAL)
        </p>
        <a href='https://www.inacal.gob.pe/cid/categoria/normas-tecnicas-peruanas' 
           target='_blank' class='corporate-button'>
            📄 Ver Catálogo NTP INACAL
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>🔧 Tecnologías de Control de Emisiones por Contaminante</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Principales sistemas utilizados en la industria peruana para cumplimiento de LMP
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    tecnologias_data = [
        ['Material Particulado', 'Filtros de mangas (Baghouse)', '>99%', 'Captación por filtración textil', 'Media-Alta', 'Alto', 'Industria general'],
        ['Material Particulado', 'Precipitadores electrostáticos (ESP)', '95-99%', 'Carga eléctrica y colección', 'Alta', 'Medio', 'Termoeléctricas, cemento'],
        ['Material Particulado', 'Ciclones', '70-90%', 'Separación por fuerza centrífuga', 'Baja', 'Bajo', 'Pre-tratamiento'],
        ['Material Particulado', 'Lavadores húmedos (Scrubbers)', '85-95%', 'Absorción líquido-gas', 'Media', 'Medio', 'Industria química'],
        ['SO2', 'Desulfuración húmeda (FGD)', '>95%', 'Absorción con caliza/cal + agua', 'Muy Alta', 'Alto', 'Termoeléctricas, fundiciones'],
        ['SO2', 'Desulfuración seca (SDA)', '80-95%', 'Inyección de sorbente seco', 'Alta', 'Medio-Alto', 'Industria general'],
        ['SO2', 'Scrubber de doble álcali', '90-98%', 'Absorción NaOH regenerativo', 'Alta', 'Alto', 'Metalurgia'],
        ['NOx', 'Reducción Catalítica Selectiva (SCR)', '>90%', 'Reducción con NH3/urea + catalizador', 'Muy Alta', 'Muy Alto', 'Termoeléctricas, cemento'],
        ['NOx', 'Reducción No Catalítica (SNCR)', '40-60%', 'Inyección térmica de urea', 'Media', 'Medio', 'Calderos, hornos'],
        ['NOx', 'Quemadores Low-NOx', '30-50%', 'Control de combustión (T y O2)', 'Media', 'Bajo-Medio', 'Calderos industriales'],
        ['NOx', 'Recirculación de gases (FGR)', '20-40%', 'Reducción T de llama', 'Baja-Media', 'Bajo', 'Calderos pequeños'],
        ['COVs', 'Oxidación térmica', '>95%', 'Combustión 700-850°C', 'Alta', 'Alto', 'Química, pinturas'],
        ['COVs', 'Oxidación catalítica', '>90%', 'Combustión catalítica 350-450°C', 'Alta', 'Medio-Alto', 'Imprentas, recubrimientos'],
        ['COVs', 'Adsorción carbón activado', '85-95%', 'Captura en microporos', 'Media', 'Medio', 'Baja concentración'],
        ['COVs', 'Condensación criogénica', '80-90%', 'Enfriamiento bajo punto rocío', 'Alta', 'Alto', 'Recuperación solventes'],
        ['CO', 'Oxidación catalítica', '>98%', 'Conversión CO a CO2', 'Media-Alta', 'Medio', 'Escape vehicular, hornos']
    ]
    
    tabla_tecnologias_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Tecnología</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Eficiencia</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Principio de Operación</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Complejidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Costo</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Aplicación Principal</th>
</tr>
</thead>
<tbody>"""
    
    for i, fila in enumerate(tecnologias_data):
        border = '' if i == len(tecnologias_data) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
        tabla_tecnologias_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[4]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[5]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[6]}</td>
</tr>"""
    
    tabla_tecnologias_html += """</tbody>
</table>
</div>"""
    
    tabla_tecnologias_html += """
            </tbody>
        </table>
    </div>
    """
    
    st.markdown(tabla_tecnologias_html, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='corporate-card fade-in'>
        <h2>📊 Comparación de Eficiencias de Remoción</h2>
        <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
            Eficiencia típica de principales tecnologías de control
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    eficiencias_data = pd.DataFrame([
        {'Tecnología': 'Filtros mangas', 'Eficiencia': 99.5, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'ESP', 'Eficiencia': 97, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'Ciclones', 'Eficiencia': 80, 'Tipo': 'Material Particulado'},
        {'Tecnología': 'FGD Húmedo', 'Eficiencia': 97, 'Tipo': 'SO2'},
        {'Tecnología': 'SDA Seco', 'Eficiencia': 87.5, 'Tipo': 'SO2'},
        {'Tecnología': 'SCR', 'Eficiencia': 92, 'Tipo': 'NOx'},
        {'Tecnología': 'SNCR', 'Eficiencia': 50, 'Tipo': 'NOx'},
        {'Tecnología': 'Low-NOx', 'Eficiencia': 40, 'Tipo': 'NOx'},
        {'Tecnología': 'Oxidación térmica', 'Eficiencia': 97, 'Tipo': 'COVs'},
        {'Tecnología': 'Carbón activado', 'Eficiencia': 90, 'Tipo': 'COVs'}
    ])
    
    fig2 = px.bar(
        eficiencias_data,
        x='Tecnología',
        y='Eficiencia',
        color='Tipo',
        color_discrete_map={
            'Material Particulado': '#00B8D9',
            'SO2': '#FFB300',
            'NOx': '#00C853',
            'COVs': '#D32F2F'
        },
        text='Eficiencia'
    )
    
    fig2.update_traces(
        texttemplate='%{text}%',
        textposition='outside',
        marker=dict(line=dict(color='rgba(255,255,255,0.2)', width=1))
    )
    
    fig2.update_layout(
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#E3E8EF', size=12, family='Inter'),
        xaxis=dict(showgrid=False, title='', tickangle=-45),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(255,255,255,0.06)',
            title='Eficiencia de Remoción (%)',
            range=[0, 105]
        ),
        legend=dict(
            title='Tipo de Contaminante',
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor='rgba(19, 47, 76, 0.8)',
            bordercolor='rgba(255,255,255,0.1)',
            borderwidth=1
        )
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    # ===================== PÁGINA NORMATIVAS INTERNACIONALES =====================
elif st.session_state.pagina == "Normativas":
    
    st.markdown("<h1 style='text-align: center; margin-bottom: 2rem; color: #FFFFFF;'>🌍 Estándares Internacionales de Calidad del Aire</h1>", unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🏥 OMS", "🇺🇸 EPA USA", "🇨🇦 Canadá", "📊 Análisis Comparativo"])
    
    with tab1:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🏥 Organización Mundial de la Salud (OMS)</h2>
            <p style='font-size: 1.05rem;'>
                La OMS establece las <strong>directrices globales más estrictas</strong> para proteger 
                la salud pública de la contaminación del aire basándose en la mejor evidencia científica disponible.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("**✓ Referencia mundial:** Las guías OMS son la mejor evidencia científica disponible sobre efectos de la contaminación del aire en la salud.")
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● GUÍAS 2021</span>
            <h3>WHO Global Air Quality Guidelines 2021</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Directrices Mundiales de Calidad del Aire</strong>
            </p>
            <p>
                Primera actualización mayor desde 2005. Reduce niveles recomendados en 50% para PM2.5 basándose en 
                más de 500 estudios científicos que demuestran efectos adversos en salud incluso a concentraciones 
                muy bajas. Establece guías para PM2.5, PM10, O3, NO2, SO2 y CO, con metas intermedias para 
                implementación gradual en países en desarrollo.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Publicación:</strong> 22 de septiembre de 2021 | 
                <strong>Impacto:</strong> Referencia mundial
            </p>
            <a href='https://www.who.int/publications/i/item/9789240034228' 
               target='_blank' class='corporate-button'>
                📄 Ver Directrices OMS 2021 (Inglés)
            </a>
            <a href='https://www.who.int/es/news-room/feature-stories/detail/what-are-the-who-air-quality-guidelines' 
               target='_blank' class='corporate-button'>
                📄 Resumen Ejecutivo en Español
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        oms_tabla = pd.DataFrame([
            ['PM2.5', 5, 15, 'μg/m³', 'Media anual / 24h'],
            ['PM10', 15, 45, 'μg/m³', 'Media anual / 24h'],
            ['NO2', 10, 25, 'μg/m³', 'Media anual / 24h'],
            ['SO2', None, 40, 'μg/m³', '24 horas'],
            ['O3', None, 100, 'μg/m³', 'Pico estacional (8h)'],
            ['CO', None, 4, 'mg/m³', '24 horas']
        ], columns=['Contaminante', 'Anual', '24 horas', 'Unidad', 'Período'])
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📋 Valores Guía OMS 2021</h3>", unsafe_allow_html=True)
        
        # Tabla HTML personalizada
        tabla_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Anual</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>24 horas</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Período</th>
</tr>
</thead>
<tbody>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>PM2.5</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>5</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>15</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>μg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>Media anual / 24h</td>
</tr>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>PM10</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>15</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>45</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>μg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>Media anual / 24h</td>
</tr>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>NO2</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>10</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>25</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>μg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>Media anual / 24h</td>
</tr>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>SO2</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>-</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>40</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>μg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>24 horas</td>
</tr>
<tr style='border-bottom: 1px solid rgba(255, 255, 255, 0.08); transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>O3</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>-</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>100</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>μg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>Pico estacional (8h)</td>
</tr>
<tr style='transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>CO</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>-</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>4</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>mg/m³</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>24 horas</td>
</tr>
</tbody>
</table>
</div>"""
        st.markdown(tabla_html, unsafe_allow_html=True)
        
        st.info("**Metas Intermedias:** La OMS establece 4 niveles intermedios (IT-1 a IT-4) para países que no pueden alcanzar inmediatamente las guías finales, permitiendo mejora progresiva.")
    
    with tab2:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🇺🇸 Environmental Protection Agency (EPA)</h2>
            <p style='font-size: 1.05rem;'>
                La EPA de Estados Unidos establece los <strong>National Ambient Air Quality Standards (NAAQS)</strong>, 
                estándares vinculantes de cumplimiento obligatorio que se revisan cada 5 años basándose en la mejor 
                ciencia disponible.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("**✓ Sistema dual:** La EPA establece estándares primarios (protección de salud) y secundarios (protección de bienestar público: vegetación, visibilidad, edificios).")
        
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● NAAQS 2024</span>
            <h3>National Ambient Air Quality Standards</h3>
            <p style='font-size: 1.05rem; margin: 1rem 0;'>
                <strong>Estándares Nacionales de Calidad del Aire Ambiente</strong>
            </p>
            <p>
                Última actualización: PM2.5 anual reducido de 12 a 9.0 μg/m³ (febrero 2024), el cambio más 
                significativo desde 2012. Los NAAQS son legalmente vinculantes y su cumplimiento es monitoreado 
                en todo el territorio estadounidense. Estados que no cumplen deben implementar State Implementation 
                Plans (SIPs) con medidas correctivas.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Base legal:</strong> Clean Air Act (1970, enmendado 1990) | 
                <strong>Revisión:</strong> Cada 5 años
            </p>
            <a href='https://www.epa.gov/criteria-air-pollutants/naaqs-table' 
               target='_blank' class='corporate-button'>
                📄 Ver Tabla Completa NAAQS
            </a>
            <a href='https://www.epa.gov/pm-pollution/national-ambient-air-quality-standards-naaqs-pm' 
               target='_blank' class='corporate-button'>
                📄 Estándares PM Detallados
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📋 Estándares EPA (NAAQS)</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: var(--text-secondary); margin-bottom: 1rem;'>(P) = Primario (salud) | (S) = Secundario (bienestar)</p>", unsafe_allow_html=True)
        
        # Tabla HTML profesional EPA
        epa_data = [
            ['PM2.5', '9.0 (P)', '35 (P)', 'μg/m³', '2024', 'Anual / 24h'],
            ['PM2.5', '15.0 (S)', '35 (S)', 'μg/m³', '2012', 'Anual / 24h (secundario)'],
            ['PM10', 'None', '150 (P,S)', 'μg/m³', '2012', '24 horas'],
            ['NO2', '53 (P,S)', '100 (P)', 'ppb', '2010', 'Anual / 1h'],
            ['SO2', 'None', '75 (P)', 'ppb', '2010', '1 hora (percentil 99)'],
            ['O3', 'None', '70 (P,S)', 'ppb', '2015', '8h (4to máximo anual)'],
            ['CO', 'None', '9 ppm (P)', 'ppm', '1971', '8 horas'],
            ['CO', 'None', '35 ppm (P)', 'ppm', '1971', '1 hora'],
            ['Pb', '0.15 (P,S)', 'None', 'μg/m³', '2008', 'Promedio móvil 3 meses']
        ]
        
        tabla_epa_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Anual</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Corto Plazo</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Última Actualización</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Forma del Estándar</th>
</tr>
</thead>
<tbody>"""
        
        for i, fila in enumerate(epa_data):
            border = '' if i == len(epa_data) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
            tabla_epa_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[4]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[5]}</td>
</tr>"""
        
        tabla_epa_html += """</tbody>
</table>
</div>"""
        
        st.markdown(tabla_epa_html, unsafe_allow_html=True)
        st.warning("**⚠️ Designaciones de no cumplimiento:** Áreas que exceden NAAQS son designadas como 'nonattainment' y deben desarrollar planes de mejora con cronograma específico.")
    
    with tab3:
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h2>🇨🇦 Canadian Ambient Air Quality Standards (CAAQS)</h2>
            <p style='font-size: 1.05rem;'>
                Canadá utiliza un <strong>sistema de mejora continua</strong> con estándares que se actualizan 
                progresivamente cada 5 años. La gestión se realiza por Air Zones con sistema de clasificación 
                por colores que determina las acciones requeridas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("**✓ Enfoque innovador:** Sistema de 'Management Levels' (Verde, Amarillo, Naranja, Rojo) que vincula automáticamente el nivel de calidad del aire con acciones obligatorias.")
        
        # Card 1: Marco Legal
        st.markdown("""
        <div class='normative-card vigente fade-in'>
            <span class='status-badge vigente'>● VIGENTE</span>
            <h3>Canadian Environmental Protection Act (CEPA 1999)</h3>
            <p><strong>Base Legal del Sistema CAAQS</strong></p>
            <p style='color: var(--text-secondary); line-height: 1.8;'>
                Ley federal que establece el marco para la protección ambiental en Canadá. Los CAAQS son 
                desarrollados bajo esta autoridad por el Canadian Council of Ministers of the Environment (CCME), 
                un organismo intergubernamental que coordina acciones federales y provinciales.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Promulgación:</strong> 1999 | 
                <strong>Organismo:</strong> CCME | 
                <strong>Alcance:</strong> Federal y Provincial
            </p>
            <a href='https://laws-lois.justice.gc.ca/eng/acts/c-15.31/' 
               target='_blank' class='corporate-button'>
                📄 Ver Texto Legal CEPA
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Card 2: Estándares Vigentes 2020
        st.markdown("""
        <div class='normative-card vigente fade-in'>
            <span class='status-badge vigente'>● VIGENTE 2020</span>
            <h3>CAAQS - Estándares Actuales en Vigor</h3>
            <p><strong>Canadian Ambient Air Quality Standards 2020</strong></p>
            <p style='color: var(--text-secondary); line-height: 1.8;'>
                Estándares basados en percentiles altos (98-99) de mediciones anuales para proteger salud 
                pública y medio ambiente. Se aplica sistema de Air Quality Management System (AQMS) con 
                clasificación por colores que determina acciones obligatorias según nivel de cumplimiento.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Vigencia:</strong> 2020-2025 | 
                <strong>Contaminantes:</strong> PM2.5, O3, NO2, SO2 | 
                <strong>Metodología:</strong> Percentiles 98-99
            </p>
            <a href='https://ccme.ca/en/air-quality-report' 
               target='_blank' class='corporate-button'>
                📊 Ver Reporte CCME
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Card 3: Metas 2025
        st.markdown("""
        <div class='normative-card modificado fade-in'>
            <span class='status-badge modificado'>● META 2025</span>
            <h3>Objetivos Intermedios - Fase de Transición</h3>
            <p><strong>Metas de Mejora Progresiva a Corto Plazo</strong></p>
            <p style='color: var(--text-secondary); line-height: 1.8;'>
                Objetivos intermedios establecidos para lograr reducción gradual de contaminantes. 
                Sistema de revisión quinquenal asegura actualización basada en evidencia científica 
                más reciente. Provincias deben desarrollar planes de mejora si exceden estos niveles.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Plazo:</strong> 2025 | 
                <strong>Revisión:</strong> Cada 5 años | 
                <strong>Reducciones esperadas:</strong> 5-10% vs 2020
            </p>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-pollution/monitoring-networks-data.html' 
               target='_blank' class='corporate-button'>
                📈 Ver Monitoreo de Progreso
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Card 4: Objetivos 2030
        st.markdown("""
        <div class='normative-card internacional fade-in'>
            <span class='status-badge internacional'>● OBJETIVO 2030</span>
            <h3>Visión a Largo Plazo - Alineación con Estándares Internacionales</h3>
            <p><strong>Objetivos de Mejora Continua hacia Niveles OMS</strong></p>
            <p style='color: var(--text-secondary); line-height: 1.8;'>
                Compromiso de alineación progresiva con Guías de Calidad del Aire de la OMS. 
                Representa reducción significativa de contaminación atmosférica para 2030. 
                Enfoque en protección de poblaciones vulnerables y ecosistemas sensibles.
            </p>
            <p style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255,255,255,0.1);'>
                <strong>Plazo:</strong> 2030 | 
                <strong>Ambición:</strong> Alineación con OMS | 
                <strong>Reducciones esperadas:</strong> 25-35% vs 2020
            </p>
            <a href='https://www.canada.ca/en/environment-climate-change/services/air-quality-health-index.html' 
               target='_blank' class='corporate-button'>
                🌡️ Ver Índice de Calidad del Aire
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        
        
        st.markdown("<h3 style='text-align: center; color: #00B8D9; margin-top: 2rem;'>📊 Evolución de Estándares CAAQS</h3>", unsafe_allow_html=True)
        
        # Tabla HTML profesional Canadá
        canada_data = [
            ['PM2.5', '8.8', '8', '6', 'μg/m³', 'Anual (percentil 98 de promedios diarios)'],
            ['PM2.5', '27', '25', '20', 'μg/m³', '24h (percentil 98)'],
            ['O3', '62', '60', '56', 'ppb', '8h (4to valor máximo anual)'],
            ['NO2', '60', '50', '42', 'ppb', '1h (percentil 98 anual)'],
            ['SO2', '70', '65', '50', 'ppb', '1h (percentil 99 anual)']
        ]
        
        tabla_canada_html = """<div style='overflow-x: auto; border-radius: 12px; border: 1px solid rgba(0, 184, 217, 0.3); box-shadow: 0 4px 16px rgba(0, 0, 0, 0.3); margin: 1rem 0;'>
<table style='width: 100%; border-collapse: collapse; background: rgba(19, 47, 76, 0.8);'>
<thead>
<tr style='background: linear-gradient(135deg, #0052CC 0%, #00B8D9 100%);'>
<th style='color: #FFFFFF; padding: 1rem; text-align: left; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Contaminante</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Estándar 2020</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Meta 2025</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Objetivo 2030</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Unidad</th>
<th style='color: #FFFFFF; padding: 1rem; text-align: center; font-weight: 700; text-transform: uppercase; font-size: 0.85rem; border: none;'>Forma del Estándar</th>
</tr>
</thead>
<tbody>"""
        
        for i, fila in enumerate(canada_data):
            border = '' if i == len(canada_data) - 1 else 'border-bottom: 1px solid rgba(255, 255, 255, 0.08);'
            tabla_canada_html += f"""<tr style='{border} transition: background 0.2s;' onmouseover='this.style.background="rgba(0, 184, 217, 0.15)"' onmouseout='this.style.background="transparent"'>
<td style='color: #00B8D9; padding: 0.875rem 1rem; font-weight: 700; border: none;'>{fila[0]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[1]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[2]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[3]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[4]}</td>
<td style='color: #FFFFFF; padding: 0.875rem 1rem; text-align: center; border: none;'>{fila[5]}</td>
</tr>"""
        
        tabla_canada_html += """</tbody>
</table>
</div>"""
        
        st.markdown(tabla_canada_html, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("<h2 style='text-align: center; margin-bottom: 2rem; color: #FFFFFF;'>📊 Análisis Comparativo Internacional</h2>", unsafe_allow_html=True)
        
        st.markdown("""
        <div class='corporate-card fade-in'>
            <h3>🔬 Comparación PM2.5 - Estándar Más Crítico para Salud</h3>
            <p style='color: var(--text-secondary); margin-bottom: 1rem;'>
                Valores anuales y de 24 horas según cada jurisdicción
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        comparacion = pd.DataFrame([
            {'Entidad': 'OMS 2021', 'Anual': 5, '24h': 15},
            {'Entidad': 'EPA USA 2024', 'Anual': 9, '24h': 35},
            {'Entidad': 'Canadá 2025', 'Anual': 8, '24h': 25},
            {'Entidad': 'OEFA Perú', 'Anual': 25, '24h': 50}
        ])
        
        fig3 = go.Figure()
        
        fig3.add_trace(go.Bar(
            name='Anual',
            x=comparacion['Entidad'],
            y=comparacion['Anual'],
            marker=dict(
                color=['#00C853', '#0065FF', '#8b5cf6', '#FFB300'],
                line=dict(color='rgba(255,255,255,0.2)', width=1)
            ),
            text=comparacion['Anual'],
            texttemplate='%{text} μg/m³',
            textposition='outside'
        ))
        
        fig3.add_trace(go.Bar(
            name='24 horas',
            x=comparacion['Entidad'],
            y=comparacion['24h'],
            marker=dict(
                color=['#66BB6A', '#42A5F5', '#BA68C8', '#FFA726'],
                line=dict(color='rgba(255,255,255,0.2)', width=1)
            ),
            text=comparacion['24h'],
            texttemplate='%{text} μg/m³',
            textposition='outside'
        ))
        
        fig3.update_layout(
            barmode='group',
            height=550,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#E3E8EF', size=13, family='Inter'),
            xaxis=dict(showgrid=False, title=''),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.06)',
                title='Concentración (μg/m³)',
                range=[0, 60]
            ),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1,
                bgcolor='rgba(19, 47, 76, 0.8)',
                bordercolor='rgba(255,255,255,0.1)',
                borderwidth=1
            )
        )
        
        st.plotly_chart(fig3, use_container_width=True)
        
        st.warning("**⚠️ Análisis:** El estándar peruano de PM2.5 anual (25 μg/m³) es 5 veces más permisivo que la OMS (5 μg/m³) y 2.8 veces más alto que EPA USA (9 μg/m	³). Se recomienda actualización gradual de los ECA nacionales.")
