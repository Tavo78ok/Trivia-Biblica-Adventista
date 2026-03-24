# ✝️ Trivia Bíblica Adventista

<p align="center">
  <img src="https://img.shields.io/badge/versión-2.0-gold?style=for-the-badge" alt="Versión"/>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/GTK-4.0-green?style=for-the-badge" alt="GTK4"/>
  <img src="https://img.shields.io/badge/Libadwaita-1.0-purple?style=for-the-badge" alt="Libadwaita"/>
  <img src="https://img.shields.io/badge/plataforma-Linux-orange?style=for-the-badge&logo=linux" alt="Linux"/>
</p>

<p align="center">
  <i>Juego educativo de trivia bíblica para toda la familia · Adventista del Séptimo Día</i>
</p>

<p align="center">
  <b>"Tu palabra es lámpara a mis pies y lumbrera a mi camino." — Salmo 119:105</b>
</p>

---

## 📖 Descripción

**Trivia Bíblica Adventista** es un juego educativo y familiar desarrollado en Python 3 con interfaz gráfica moderna usando GTK4 y Libadwaita. Diseñado para niños y adultos de la comunidad Adventista del Séptimo Día, cubre toda la Biblia desde Génesis hasta Apocalipsis.

---

## ✨ Características

- 📜 **219+ preguntas** de toda la Biblia
- 🎲 **100% aleatorio** — preguntas y opciones se mezclan en cada partida
- ❓ **Dos tipos de preguntas** — Opción múltiple y Verdadero/Falso
- 📚 **4 categorías:**
  - 📜 Antiguo Testamento
  - ✝️ Nuevo Testamento
  - ⭐ Doctrina Adventista
  - 📖 General
- 🎯 **3 niveles de dificultad** — Fácil, Medio, Difícil
- 🔥 **Sistema de racha** — puntos extra por respuestas consecutivas correctas
- ⭐ **Puntuación** — 10, 20 o 30 puntos según dificultad
- 📌 **Referencia bíblica** visible en cada pregunta
- 🏆 **Pantalla de resultados** con estadísticas detalladas
- 🌙 **Tema claro/oscuro** automático según el sistema
- 🖥️ Interfaz moderna con **GTK4 + Libadwaita**

---

## 🖼️ Capturas de pantalla

> *Menú principal, pantalla de juego y resultados*

| Inicio | Jugando | Resultados |
|--------|---------|------------|
| *(Menú de configuración)* | *(Pregunta con opciones)* | *(Estadísticas finales)* |

---

## 📦 Instalación

### Opción 1 — Paquete `.deb` (recomendado) ⭐

La forma más fácil. Descarga el archivo `.deb` desde [Releases](../../releases) e instala con un solo comando:

```bash
sudo apt install ./trivia-biblica_2.0_all.deb
```

Esto instala automáticamente todas las dependencias. Al finalizar, el juego aparece en el menú de aplicaciones como **"Trivia Bíblica Adventista"**.

Para desinstalar:
```bash
sudo apt remove trivia-biblica
```

---

### Opción 2 — Desde el código fuente

**1. Instalar dependencias:**

```bash
sudo apt install python3 python3-gi python3-gi-cairo \
    gir1.2-gtk-4.0 gir1.2-adw-1 libadwaita-1-0
```

**2. Clonar el repositorio:**

```bash
git clone https://github.com/TU_USUARIO/trivia-biblica.git
cd trivia-biblica
```

**3. Ejecutar:**

```bash
python3 trivia_biblica.py
```

---

## 🐧 Sistemas compatibles

| Distribución | Versión mínima | Estado |
|---|---|---|
| Ubuntu | 22.04 LTS+ | ✅ Probado |
| Linux Mint | 21+ | ✅ Probado |
| Debian | 12 (Bookworm)+ | ✅ Compatible |
| Fedora | 38+ | ✅ Compatible |
| Arch Linux | Actual | ✅ Compatible |

> El paquete `.deb` funciona en cualquier distribución basada en **Debian/Ubuntu**.

---

## 🛠️ Tecnologías

| Tecnología | Uso |
|---|---|
| **Python 3** | Lenguaje principal |
| **GTK 4** | Framework de interfaz gráfica |
| **Libadwaita** | Diseño moderno GNOME / integración con el sistema |
| **PyGObject** | Binding Python para GTK |

---

## 📁 Estructura del proyecto

```
trivia-biblica/
├── trivia_biblica.py          # Código fuente principal
├── trivia-biblica_2.0_all.deb # Paquete instalable
├── build_appimage.sh          # Script para generar AppImage
└── README.md                  # Este archivo
```

---

## ➕ Agregar preguntas

Para contribuir nuevas preguntas, editá el array `PREGUNTAS` en `trivia_biblica.py` siguiendo este formato:

**Pregunta de opción múltiple:**
```python
{
    "pregunta": "¿Tu pregunta aquí?",
    "tipo": "multiple",
    "categoria": "Antiguo Testamento",  # o "Nuevo Testamento", "Doctrina Adventista", "General"
    "dificultad": "fácil",              # o "medio" o "difícil"
    "opciones": ["Respuesta correcta", "Opción 2", "Opción 3", "Opción 4"],
    "respuesta": 0,                     # índice de la opción correcta (0, 1, 2 o 3)
    "referencia": "Génesis 1:1"
}
```

**Pregunta de Verdadero/Falso:**
```python
{
    "pregunta": "Afirmación verdadera o falsa.",
    "tipo": "verdadero_falso",
    "categoria": "Nuevo Testamento",
    "dificultad": "medio",
    "respuesta": True,   # o False
    "referencia": "Juan 3:16"
}
```

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Podés ayudar:

- 📝 Agregando más preguntas bíblicas
- 🌍 Traduciendo a otros idiomas
- 🐛 Reportando errores en [Issues](../../issues)
- 💡 Sugiriendo mejoras

---

## 📄 Licencia

Este proyecto es software libre distribuido para uso educativo en la comunidad cristiana adventista.

---

## 🙏 Créditos

Desarrollado con ❤️ para la **Iglesia Adventista del Séptimo Día**.

*"Y conoceréis la verdad, y la verdad os hará libres." — Juan 8:32*
