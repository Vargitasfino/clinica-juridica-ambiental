import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
```

Y termina con el footer. Son aproximadamente **1000+ líneas de código**.

5. Baja hasta el final de la página y haz click en el botón verde **"Commit new file"**

---

### **PASO 2: Crear el archivo `requirements.txt`**

Una vez que hayas creado `app.py`, repite el proceso:

1. Click en **"Add file"** → **"Create new file"**
2. Nombre del archivo:
```
requirements.txt
```
3. En el editor pega esto:
```
streamlit==1.28.0
pandas==2.1.1
plotly==5.17.0
