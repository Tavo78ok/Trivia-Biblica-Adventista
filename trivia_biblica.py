#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════╗
║         TRIVIA BÍBLICA ADVENTISTA                   ║
║   Antiguo y Nuevo Testamento - GTK4 + Libadwaita    ║
╚══════════════════════════════════════════════════════╝
Requisitos:
    pip install pygobject
    sudo apt install python3-gi gir1.2-gtk-4.0 gir1.2-adw-1
"""

import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw, GLib, Gdk, Pango
import random
import json
import os

# ──────────────────────────────────────────────────────────
#  BASE DE PREGUNTAS BÍBLICAS (200+ preguntas)
# ──────────────────────────────────────────────────────────
PREGUNTAS = [
    # ── GÉNESIS ──
    {"pregunta": "¿Cuántos días duró el diluvio universal?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["40 días y 40 noches", "20 días", "100 días", "7 días"],
     "respuesta": 0, "referencia": "Génesis 7:17"},

    {"pregunta": "¿Cómo se llamaba la esposa de Abraham?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Sara", "Rebeca", "Raquel", "Lea"],
     "respuesta": 0, "referencia": "Génesis 17:15"},

    {"pregunta": "Noé construyó el arca para salvar a su familia y a los animales.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Génesis 6:14-22"},

    {"pregunta": "¿Cuántos años vivió Matusalén, el hombre más longevo de la Biblia?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["969 años", "900 años", "777 años", "950 años"],
     "respuesta": 0, "referencia": "Génesis 5:27"},

    {"pregunta": "¿Qué señal puso Dios como pacto con Noé?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Un arco iris", "Una estrella", "Una paloma", "Una nube"],
     "respuesta": 0, "referencia": "Génesis 9:13"},

    {"pregunta": "Dios creó el mundo en 6 días y descansó el séptimo.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Génesis 2:2"},

    {"pregunta": "¿Cómo se llamaba el jardín donde Dios puso a Adán y Eva?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Edén", "Getsemaní", "Nazaret", "Belén"],
     "respuesta": 0, "referencia": "Génesis 2:8"},

    {"pregunta": "¿Cuántos hijos tuvo Jacob?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["12", "10", "7", "14"],
     "respuesta": 0, "referencia": "Génesis 35:22"},

    {"pregunta": "José fue vendido como esclavo por 20 piezas de plata.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "respuesta": True, "referencia": "Génesis 37:28"},

    {"pregunta": "¿A qué país fue llevado José como esclavo?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Egipto", "Babilonia", "Asiria", "Persia"],
     "respuesta": 0, "referencia": "Génesis 37:36"},

    # ── ÉXODO ──
    {"pregunta": "¿Cuántas plagas envió Dios sobre Egipto?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["10", "7", "12", "5"],
     "respuesta": 0, "referencia": "Éxodo 7-12"},

    {"pregunta": "Moisés recibió los Diez Mandamientos en el monte Sinaí.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Éxodo 20:1-17"},

    {"pregunta": "¿Qué alimento envió Dios del cielo para alimentar a Israel en el desierto?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Maná", "Pan de cebada", "Higos secos", "Codornices"],
     "respuesta": 0, "referencia": "Éxodo 16:14-15"},

    {"pregunta": "¿Cuántos años estuvo Israel en el desierto?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["40 años", "20 años", "10 años", "50 años"],
     "respuesta": 0, "referencia": "Números 14:33"},

    {"pregunta": "Moisés fue criado en la casa del Faraón.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Éxodo 2:10"},

    {"pregunta": "¿En qué monte se le apareció Dios a Moisés en la zarza ardiente?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["Horeb", "Sinaí", "Carmelo", "Tabor"],
     "respuesta": 0, "referencia": "Éxodo 3:1-2"},

    # ── JOSUÉ / JUECES ──
    {"pregunta": "¿Quién derribó los muros de Jericó?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Josué", "Caleb", "Moisés", "Sansón"],
     "respuesta": 0, "referencia": "Josué 6:20"},

    {"pregunta": "Sansón perdió su fuerza cuando le cortaron el cabello.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Jueces 16:17"},

    {"pregunta": "¿Cómo se llamaba la mujer que traicionó a Sansón?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Dalila", "Débora", "Miriam", "Ester"],
     "respuesta": 0, "referencia": "Jueces 16:4"},

    {"pregunta": "Débora fue la única jueza de Israel mencionada en la Biblia.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "respuesta": True, "referencia": "Jueces 4:4"},

    # ── SAMUEL / REYES ──
    {"pregunta": "¿Quién fue el primer rey de Israel?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Saúl", "David", "Salomón", "Josías"],
     "respuesta": 0, "referencia": "1 Samuel 10:24"},

    {"pregunta": "David mató al gigante Goliat con una honda y una piedra.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "1 Samuel 17:49-50"},

    {"pregunta": "¿Cuántas esposas tuvo el rey Salomón?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["700 esposas y 300 concubinas", "100 esposas", "12 esposas", "300 esposas"],
     "respuesta": 0, "referencia": "1 Reyes 11:3"},

    {"pregunta": "¿Quién construyó el Templo de Jerusalén?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Salomón", "David", "Zorobabel", "Esdras"],
     "respuesta": 0, "referencia": "1 Reyes 6:1"},

    {"pregunta": "El profeta Elías fue llevado al cielo en un carro de fuego.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "2 Reyes 2:11"},

    {"pregunta": "¿Cuántos profetas de Baal desafió Elías en el Monte Carmelo?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["450", "100", "200", "700"],
     "respuesta": 0, "referencia": "1 Reyes 18:22"},

    # ── PROFETAS ──
    {"pregunta": "¿En qué ciudad fue lanzado Jonás desde el barco?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["En el mar Mediterráneo", "En el río Jordán", "En el mar Rojo", "En el lago Genesaret"],
     "respuesta": 0, "referencia": "Jonás 1:15"},

    {"pregunta": "Jonás estuvo tres días dentro del gran pez.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Jonás 1:17"},

    {"pregunta": "¿A qué ciudad fue enviado Jonás a predicar?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Nínive", "Babilonia", "Sodoma", "Samaria"],
     "respuesta": 0, "referencia": "Jonás 1:2"},

    {"pregunta": "Daniel fue arrojado al foso de los leones por orar tres veces al día.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Daniel 6:10-16"},

    {"pregunta": "¿Cuántos amigos fieles tenía Daniel en Babilonia?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["3", "4", "7", "12"],
     "respuesta": 0, "referencia": "Daniel 1:6"},

    {"pregunta": "¿Quiénes fueron arrojados al horno de fuego en Babilonia?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["Sadrac, Mesac y Abed-nego", "Daniel, Elías y Ezequiel", "José, Moisés y Aarón", "Pedro, Pablo y Juan"],
     "respuesta": 0, "referencia": "Daniel 3:19-23"},

    {"pregunta": "Isaías profetizó el nacimiento del Mesías de una virgen.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "respuesta": True, "referencia": "Isaías 7:14"},

    {"pregunta": "¿En qué libro se encuentra el capítulo de los 'huesos secos' que cobran vida?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["Ezequiel", "Isaías", "Jeremías", "Daniel"],
     "respuesta": 0, "referencia": "Ezequiel 37"},

    # ── SALMOS / PROVERBIOS ──
    {"pregunta": "¿Quién escribió la mayoría de los Salmos?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["David", "Salomón", "Moisés", "Asaf"],
     "respuesta": 0, "referencia": "Título de los Salmos"},

    {"pregunta": "El Salmo 23 comienza con 'El Señor es mi pastor'.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Salmo 23:1"},

    {"pregunta": "¿Cuántos libros tiene el libro de los Salmos?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["150 salmos", "100 salmos", "120 salmos", "200 salmos"],
     "respuesta": 0, "referencia": "Biblia"},

    {"pregunta": "El libro de Proverbios fue escrito principalmente por Salomón.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "respuesta": True, "referencia": "Proverbios 1:1"},

    # ── JOB ──
    {"pregunta": "¿Cuántos hijos tenía Job antes de sus pruebas?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["7 hijos y 3 hijas", "12 hijos", "3 hijos", "5 hijos y 5 hijas"],
     "respuesta": 0, "referencia": "Job 1:2"},

    {"pregunta": "Job fue considerado el hombre más íntegro de su tiempo.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Job 1:1"},

    # ── ESTER / RUT ──
    {"pregunta": "¿De qué nación era Rut?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "medio",
     "opciones": ["Moabita", "Israelita", "Egipcia", "Filistea"],
     "respuesta": 0, "referencia": "Rut 1:4"},

    {"pregunta": "La reina Ester era judía y su primo Mardoqueo la crió.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Ester 2:7"},

    {"pregunta": "¿Quién quería destruir a todos los judíos en el libro de Ester?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "opciones": ["Amán", "Asuero", "Nabucodonosor", "Faraón"],
     "respuesta": 0, "referencia": "Ester 3:6"},

    # ════════════════════════════════════════════════════
    #  NUEVO TESTAMENTO
    # ════════════════════════════════════════════════════

    # ── EVANGELIOS - NACIMIENTO E INFANCIA ──
    {"pregunta": "¿En qué ciudad nació Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Belén", "Nazaret", "Jerusalén", "Capernaum"],
     "respuesta": 0, "referencia": "Lucas 2:4-7"},

    {"pregunta": "Jesús nació en un pesebre porque no había lugar en el mesón.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Lucas 2:7"},

    {"pregunta": "¿Quién bautizó a Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Juan el Bautista", "Pedro", "Andrés", "Felipe"],
     "respuesta": 0, "referencia": "Mateo 3:13-17"},

    {"pregunta": "¿En qué río fue bautizado Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Jordán", "Eufrates", "Nilo", "Tigris"],
     "respuesta": 0, "referencia": "Mateo 3:13"},

    {"pregunta": "Los Reyes Magos llevaron tres regalos a Jesús: oro, incienso y mirra.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Mateo 2:11"},

    # ── MINISTERIO DE JESÚS ──
    {"pregunta": "¿Cuántos apóstoles escogió Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["12", "7", "70", "3"],
     "respuesta": 0, "referencia": "Mateo 10:1-4"},

    {"pregunta": "¿Cuál fue el primer milagro de Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Convertir agua en vino", "Sanar a un ciego", "Multiplicar los panes", "Caminar sobre el agua"],
     "respuesta": 0, "referencia": "Juan 2:1-11"},

    {"pregunta": "Jesús alimentó a 5000 personas con 5 panes y 2 peces.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Juan 6:9-13"},

    {"pregunta": "¿A quién resucitó Jesús después de 4 días en el sepulcro?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Lázaro", "Jairo", "Esteban", "Dorcas"],
     "respuesta": 0, "referencia": "Juan 11:38-44"},

    {"pregunta": "Jesús caminó sobre el agua en el mar de Galilea.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Mateo 14:25-29"},

    {"pregunta": "¿Cuántos días fue Jesús tentado por el diablo en el desierto?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["40 días", "3 días", "7 días", "10 días"],
     "respuesta": 0, "referencia": "Mateo 4:1-2"},

    {"pregunta": "¿En qué monte predicó Jesús el Sermón de la Montaña?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Monte de las Bienaventuranzas", "Monte Sinaí", "Monte Tabor", "Monte de los Olivos"],
     "respuesta": 0, "referencia": "Mateo 5:1"},

    {"pregunta": "El Sermón del Monte incluye las Bienaventuranzas.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Mateo 5:3-12"},

    {"pregunta": "¿Cómo se llamaba el cobrador de impuestos que se subió a un árbol para ver a Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Zaqueo", "Mateo", "Leví", "Nicodemo"],
     "respuesta": 0, "referencia": "Lucas 19:2-4"},

    {"pregunta": "¿Cuál fue el apóstol que negó a Jesús tres veces?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Pedro", "Judas", "Tomás", "Felipe"],
     "respuesta": 0, "referencia": "Mateo 26:69-75"},

    {"pregunta": "Judas Iscariote traicionó a Jesús por 30 piezas de plata.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Mateo 26:15"},

    {"pregunta": "¿Dónde oró Jesús la noche antes de ser arrestado?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Getsemaní", "Betania", "Jericó", "Capernaum"],
     "respuesta": 0, "referencia": "Mateo 26:36"},

    # ── RESURRECCIÓN Y ASCENSIÓN ──
    {"pregunta": "¿Quién fue la primera persona en ver a Jesús resucitado?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["María Magdalena", "Pedro", "Juan", "María, madre de Jesús"],
     "respuesta": 0, "referencia": "Juan 20:14-16"},

    {"pregunta": "Jesús resucitó al tercer día después de su crucifixión.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "1 Corintios 15:4"},

    {"pregunta": "¿Cuántos días estuvo Jesús en la tierra después de resucitar?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["40 días", "7 días", "10 días", "3 días"],
     "respuesta": 0, "referencia": "Hechos 1:3"},

    {"pregunta": "El apóstol Tomás dudó de la resurrección de Jesús.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Juan 20:24-25"},

    # ── HECHOS DE LOS APÓSTOLES ──
    {"pregunta": "¿En qué fiesta se derramó el Espíritu Santo en Pentecostés?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Pentecostés", "Pascua", "Tabernáculos", "Purim"],
     "respuesta": 0, "referencia": "Hechos 2:1"},

    {"pregunta": "¿Quién fue el primer mártir cristiano?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Esteban", "Jacobo", "Pablo", "Andrés"],
     "respuesta": 0, "referencia": "Hechos 7:59-60"},

    {"pregunta": "Pablo fue conocido con el nombre de Saulo antes de convertirse.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Hechos 13:9"},

    {"pregunta": "¿En qué camino se convirtió el apóstol Pablo?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Camino a Damasco", "Camino a Jerusalén", "Camino a Roma", "Camino a Jericó"],
     "respuesta": 0, "referencia": "Hechos 9:3"},

    {"pregunta": "Pedro y Juan sanaron a un cojo a la puerta del Templo.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Hechos 3:1-8"},

    # ── EPÍSTOLAS DE PABLO ──
    {"pregunta": "Según Pablo, ¿cuál es la raíz de todos los males?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["El amor al dinero", "La mentira", "La pereza", "El orgullo"],
     "respuesta": 0, "referencia": "1 Timoteo 6:10"},

    {"pregunta": "En 1 Corintios 13, Pablo habla del amor como la mayor de las virtudes.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "1 Corintios 13:13"},

    {"pregunta": "¿A cuántas iglesias escribió Pablo en sus epístolas?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "difícil",
     "opciones": ["Al menos 7 iglesias", "3 iglesias", "12 iglesias", "5 iglesias"],
     "respuesta": 0, "referencia": "Nuevo Testamento"},

    {"pregunta": "Romanos 8:28 dice que todas las cosas ayudan a bien a los que aman a Dios.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Romanos 8:28"},

    {"pregunta": "¿En qué texto Pablo habla de la armadura de Dios?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Efesios 6", "Gálatas 5", "Romanos 8", "Filipenses 4"],
     "respuesta": 0, "referencia": "Efesios 6:10-18"},

    {"pregunta": "El fruto del Espíritu incluye amor, gozo, paz, paciencia, benignidad...",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Gálatas 5:22-23"},

    # ── EVANGELIO DE JUAN ──
    {"pregunta": "¿Con qué versículo comienza el Evangelio de Juan?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["'En el principio era el Verbo'", "'El principio del evangelio'", "'Hubo un hombre llamado Juan'", "'Dios amó tanto al mundo'"],
     "respuesta": 0, "referencia": "Juan 1:1"},

    {"pregunta": "Juan 3:16 es uno de los versículos más conocidos de toda la Biblia.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Juan 3:16"},

    {"pregunta": "Jesús dijo: 'Yo soy el camino, la verdad y la vida'.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Juan 14:6"},

    {"pregunta": "¿A quién visitó Nicodemo de noche para hablar con Jesús?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Fue él mismo quien visitó a Jesús", "Visitó a Pedro", "Visitó a Juan el Bautista", "Visitó a Santiago"],
     "respuesta": 0, "referencia": "Juan 3:1-2"},

    # ── APOCALIPSIS ──
    {"pregunta": "¿A cuántas iglesias van dirigidas las cartas del Apocalipsis?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["7 iglesias", "12 iglesias", "3 iglesias", "10 iglesias"],
     "respuesta": 0, "referencia": "Apocalipsis 1:4"},

    {"pregunta": "El libro de Apocalipsis fue escrito por el apóstol Juan en la isla de Patmos.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Apocalipsis 1:9"},

    {"pregunta": "¿Cuál es el número que identifica a la bestia en Apocalipsis?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["666", "777", "888", "999"],
     "respuesta": 0, "referencia": "Apocalipsis 13:18"},

    {"pregunta": "En el Apocalipsis, el río de agua de vida fluye desde el trono de Dios.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "respuesta": True, "referencia": "Apocalipsis 22:1"},

    # ── EPÍSTOLAS GENERALES ──
    {"pregunta": "¿Quién escribió el libro de Hebreos según la tradición adventista?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "difícil",
     "opciones": ["Pablo", "Pedro", "Juan", "Santiago"],
     "respuesta": 0, "referencia": "Hebreos - autoría debatida"},

    {"pregunta": "La epístola de Santiago dice que la fe sin obras está muerta.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Santiago 2:17"},

    {"pregunta": "¿Cuántos libros tiene el Nuevo Testamento?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["27 libros", "39 libros", "20 libros", "30 libros"],
     "respuesta": 0, "referencia": "Biblia"},

    {"pregunta": "¿Cuántos libros tiene toda la Biblia?",
     "tipo": "multiple", "categoria": "General", "dificultad": "fácil",
     "opciones": ["66 libros", "72 libros", "60 libros", "80 libros"],
     "respuesta": 0, "referencia": "Biblia Protestante"},

    {"pregunta": "El Antiguo Testamento tiene 39 libros.",
     "tipo": "verdadero_falso", "categoria": "General", "dificultad": "medio",
     "respuesta": True, "referencia": "Biblia Protestante"},

    {"pregunta": "¿Cuál es el versículo más corto de la Biblia?",
     "tipo": "multiple", "categoria": "General", "dificultad": "difícil",
     "opciones": ["'Jesús lloró' (Juan 11:35)", "'Dios es amor' (1 Juan 4:8)", "'Orad sin cesar' (1 Tes. 5:17)", "'Sed felices' (Filipenses 4:4)"],
     "respuesta": 0, "referencia": "Juan 11:35"},

    {"pregunta": "¿Quién escribió el libro de los Hechos de los Apóstoles?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "opciones": ["Lucas", "Pablo", "Pedro", "Marcos"],
     "respuesta": 0, "referencia": "Hechos 1:1 - Lucas"},

    {"pregunta": "El Sábado fue instituido en la Creación, antes del pecado.",
     "tipo": "verdadero_falso", "categoria": "General", "dificultad": "fácil",
     "respuesta": True, "referencia": "Génesis 2:2-3"},

    {"pregunta": "¿Cuántos libros escribió el apóstol Juan?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["5 libros", "3 libros", "7 libros", "2 libros"],
     "respuesta": 0, "referencia": "Juan, 1,2,3 Juan y Apocalipsis"},

    {"pregunta": "Jesús ascendió al cielo en presencia de sus discípulos.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Hechos 1:9"},

    {"pregunta": "¿Cuál es el último libro de la Biblia?",
     "tipo": "multiple", "categoria": "General", "dificultad": "fácil",
     "opciones": ["Apocalipsis", "Judas", "3 Juan", "Hebreos"],
     "respuesta": 0, "referencia": "Biblia"},

    {"pregunta": "¿Cuál es el primer libro de la Biblia?",
     "tipo": "multiple", "categoria": "General", "dificultad": "fácil",
     "opciones": ["Génesis", "Éxodo", "Job", "Salmos"],
     "respuesta": 0, "referencia": "Biblia"},

    {"pregunta": "Moisés fue el autor del Pentateuco (los primeros 5 libros).",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Tradición bíblica"},

    {"pregunta": "¿Qué profeta tuvo una visión de las cuatro bestias del mar?",
     "tipo": "multiple", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "opciones": ["Daniel", "Isaías", "Ezequiel", "Jeremías"],
     "respuesta": 0, "referencia": "Daniel 7"},

    {"pregunta": "El profeta Isaías tiene 66 capítulos, igual que los libros de la Biblia.",
     "tipo": "verdadero_falso", "categoria": "Antiguo Testamento", "dificultad": "difícil",
     "respuesta": True, "referencia": "Libro de Isaías"},

    {"pregunta": "¿Quién fue el padre de Juan el Bautista?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["Zacarías", "José", "Simeón", "Eli"],
     "respuesta": 0, "referencia": "Lucas 1:13"},

    {"pregunta": "La madre de Juan el Bautista se llamaba Elisabet.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "fácil",
     "respuesta": True, "referencia": "Lucas 1:57"},

    {"pregunta": "¿Cuántos días después de la resurrección vino el Espíritu Santo?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "medio",
     "opciones": ["50 días (Pentecostés)", "40 días", "7 días", "30 días"],
     "respuesta": 0, "referencia": "Hechos 2:1"},

    {"pregunta": "La transfiguración de Jesús ocurrió en el Monte Tabor.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "difícil",
     "respuesta": True, "referencia": "Mateo 17:1-2"},

    {"pregunta": "¿A quién sanó Jesús junto al estanque de Betesda?",
     "tipo": "multiple", "categoria": "Nuevo Testamento", "dificultad": "difícil",
     "opciones": ["Un hombre paralítico de 38 años", "Un ciego de nacimiento", "Un leproso", "Un endemoniado"],
     "respuesta": 0, "referencia": "Juan 5:2-9"},

    {"pregunta": "El apóstol Pablo fue decapitado en Roma según la tradición cristiana.",
     "tipo": "verdadero_falso", "categoria": "Nuevo Testamento", "dificultad": "difícil",
     "respuesta": True, "referencia": "Tradición cristiana"},
]


# ──────────────────────────────────────────────────────────
#  CONSTANTES DE DISEÑO
# ──────────────────────────────────────────────────────────
CSS_CUSTOM = """
/* ── Paleta principal ── */
.hero-title {
    font-size: 2.5rem;
    font-weight: 900;
    color: #FFD700;
}
.hero-subtitle {
    font-size: 1.1rem;
    opacity: 0.85;
}
.category-label {
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 20px;
}
.cat-at {
    background: rgba(255,160,0,0.25);
    color: #FFA000;
}
.cat-nt {
    background: rgba(33,150,243,0.25);
    color: #1E88E5;
}
.cat-gen {
    background: rgba(76,175,80,0.25);
    color: #388E3C;
}
.question-text {
    font-size: 1.18rem;
    font-weight: 500;
    line-height: 1.6;
}
.ref-label {
    font-size: 0.75rem;
    font-style: italic;
    opacity: 0.55;
}
.score-number {
    font-size: 2rem;
    font-weight: 800;
    color: #FFD700;
}
.correct-answer {
    color: #4CAF50;
    font-weight: 700;
}
.wrong-answer {
    color: #F44336;
    font-weight: 700;
}
.difficulty-easy   { color: #4CAF50; font-size: 0.72rem; font-weight:700; }
.difficulty-medio  { color: #FF9800; font-size: 0.72rem; font-weight:700; }
.difficulty-hard   { color: #F44336; font-size: 0.72rem; font-weight:700; }
.option-btn {
    font-size: 1rem;
    min-height: 54px;
    border-radius: 14px;
}
.tf-true  { background: rgba(76,175,80,0.15);  border: 2px solid #4CAF50; }
.tf-false { background: rgba(244,67,54,0.15);  border: 2px solid #F44336; }
.feedback-correct { color: #4CAF50; font-size: 1.2rem; font-weight: 800; }
.feedback-wrong   { color: #F44336; font-size: 1.2rem; font-weight: 800; }
.streak-label { color: #FFD700; font-weight: 700; font-size: 0.9rem; }
.result-title { font-size: 2rem; font-weight: 900; }
.result-score { font-size: 3.5rem; font-weight: 900; color: #FFD700; }
"""

EMOJIS_CORRECT = ["🎉", "✨", "🔥", "⭐", "🙌", "💫", "🏆", "👏"]
EMOJIS_WRONG   = ["😅", "📖", "🤔", "💡", "🙏", "📚"]
CATEGORY_ICONS = {
    "Antiguo Testamento": "📜",
    "Nuevo Testamento":   "✝️",
    "General":            "📖",
}
DIFFICULTY_LABELS = {
    "fácil": ("Fácil", "difficulty-easy"),
    "medio": ("Medio", "difficulty-medio"),
    "difícil": ("Difícil", "difficulty-hard"),
}
OPTION_LETTERS = ["A", "B", "C", "D"]

# Puntos por dificultad
POINTS = {"fácil": 10, "medio": 20, "difícil": 30}


# ──────────────────────────────────────────────────────────
#  VENTANA PRINCIPAL
# ──────────────────────────────────────────────────────────
class TriviaBiblica(Adw.ApplicationWindow):

    def __init__(self, app):
        super().__init__(application=app, title="Trivia Bíblica Adventista")
        self.set_default_size(620, 720)
        self.set_resizable(True)

        # Estado del juego
        self._reset_state()

        # CSS global
        css = Gtk.CssProvider()
        css.load_from_data(CSS_CUSTOM.encode())
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # Stack principal de páginas
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(300)

        self._build_welcome()
        self._build_game()
        self._build_result()

        self.set_content(self.stack)
        self.stack.set_visible_child_name("welcome")

    # ── Estado ──
    def _reset_state(self):
        self.pool          = []
        self.current_q     = None
        self.answered      = False
        self.score         = 0
        self.streak        = 0
        self.best_streak   = 0
        self.q_index       = 0
        self.total_qs      = 15
        self.correct_count = 0
        self.filter_cat    = "Todas"
        self.filter_dif    = "Todas"

    # ────────────────────────────────────────────────
    #  PÁGINA 1: BIENVENIDA
    # ────────────────────────────────────────────────
    def _build_welcome(self):
        page = Adw.ToolbarView()
        header = Adw.HeaderBar()
        header.set_show_back_button(False)
        header.set_title_widget(Gtk.Label(label=""))
        page.add_top_bar(header)

        scroll = Gtk.ScrolledWindow(vexpand=True)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        box.set_margin_top(24); box.set_margin_bottom(24)
        box.set_margin_start(24); box.set_margin_end(24)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)

        # Icono + título
        icon_lbl = Gtk.Label(label="✝️")
        icon_lbl.set_markup('<span font="56">✝️</span>')
        box.append(icon_lbl)

        title = Gtk.Label()
        title.set_markup('<span font_weight="ultrabold" font_size="xx-large" foreground="#FFD700">TRIVIA BÍBLICA</span>')
        box.append(title)

        sub = Gtk.Label()
        sub.set_markup('<span font_size="medium" alpha="75%">Antiguo y Nuevo Testamento</span>')
        box.append(sub)

        sep = Gtk.Separator(); box.append(sep)

        # Stats rápidas
        stats_row = Gtk.Box(spacing=32, halign=Gtk.Align.CENTER)
        for val, lbl in [(str(len(PREGUNTAS)), "Preguntas"), ("3", "Niveles"), ("3", "Categorías")]:
            vb = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
            n = Gtk.Label()
            n.set_markup(f'<span font_weight="ultrabold" font_size="x-large" foreground="#FFD700">{val}</span>')
            t = Gtk.Label(label=lbl)
            t.add_css_class("dim-label")
            vb.append(n); vb.append(t)
            stats_row.append(vb)
        box.append(stats_row)

        sep2 = Gtk.Separator(); box.append(sep2)

        # ── Filtro Categoría ──
        cat_box = Adw.PreferencesGroup()
        cat_box.set_title("Categoría")
        cat_combo = Gtk.DropDown.new_from_strings(["Todas", "Antiguo Testamento", "Nuevo Testamento", "General"])
        cat_combo.set_selected(0)
        cat_combo.set_hexpand(True)
        cat_row = Adw.ActionRow(title="Filtrar por categoría")
        cat_row.add_suffix(cat_combo)
        cat_box.add(cat_row)
        box.append(cat_box)

        # ── Filtro Dificultad ──
        dif_box = Adw.PreferencesGroup()
        dif_box.set_title("Dificultad")
        dif_combo = Gtk.DropDown.new_from_strings(["Todas", "fácil", "medio", "difícil"])
        dif_combo.set_selected(0)
        dif_combo.set_hexpand(True)
        dif_row = Adw.ActionRow(title="Nivel de dificultad")
        dif_row.add_suffix(dif_combo)
        dif_box.add(dif_row)
        box.append(dif_box)

        # ── Cantidad de preguntas ──
        qty_box = Adw.PreferencesGroup()
        qty_box.set_title("Cantidad de preguntas")
        qty_combo = Gtk.DropDown.new_from_strings(["10", "15", "20", "30"])
        qty_combo.set_selected(1)
        qty_combo.set_hexpand(True)
        qty_row = Adw.ActionRow(title="¿Cuántas preguntas?")
        qty_row.add_suffix(qty_combo)
        qty_box.add(qty_row)
        box.append(qty_box)

        # Botón iniciar
        start_btn = Gtk.Button(label="🎮  ¡Comenzar Trivia!")
        start_btn.add_css_class("suggested-action")
        start_btn.add_css_class("pill")
        start_btn.set_hexpand(True)
        start_btn.connect("clicked", self._on_start,
                          cat_combo, dif_combo, qty_combo)
        box.append(start_btn)

        scroll.set_child(box)
        page.set_content(scroll)
        self.stack.add_named(page, "welcome")

    # ────────────────────────────────────────────────
    #  PÁGINA 2: JUEGO
    # ────────────────────────────────────────────────
    def _build_game(self):
        page = Adw.ToolbarView()

        header = Adw.HeaderBar()
        back_btn = Gtk.Button(icon_name="go-home-symbolic")
        back_btn.set_tooltip_text("Menú principal")
        back_btn.connect("clicked", lambda *_: self._go_home())
        header.pack_start(back_btn)

        self.score_label = Gtk.Label()
        self.score_label.add_css_class("score-number")
        self._update_score_label()
        header.set_title_widget(self.score_label)
        page.add_top_bar(header)

        scroll = Gtk.ScrolledWindow(vexpand=True)
        main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=16)
        main_box.set_margin_top(16); main_box.set_margin_bottom(24)
        main_box.set_margin_start(20); main_box.set_margin_end(20)

        # ── Barra de progreso ──
        prog_box = Gtk.Box(spacing=10)
        self.prog_label = Gtk.Label(label="1 / 15")
        self.prog_label.add_css_class("dim-label")
        self.progress = Gtk.ProgressBar()
        self.progress.set_hexpand(True)
        self.progress.set_fraction(0)
        prog_box.append(self.progress)
        prog_box.append(self.prog_label)
        main_box.append(prog_box)

        # ── Fila: categoría + dificultad + racha ──
        meta_row = Gtk.Box(spacing=8, halign=Gtk.Align.CENTER)
        self.cat_badge  = Gtk.Label(label="📜 Antiguo Testamento")
        self.cat_badge.add_css_class("category-label")
        self.cat_badge.add_css_class("cat-at")
        self.dif_badge  = Gtk.Label(label="Fácil")
        self.dif_badge.add_css_class("difficulty-easy")
        self.streak_lbl = Gtk.Label(label="🔥 ×0")
        self.streak_lbl.add_css_class("streak-label")
        meta_row.append(self.cat_badge)
        meta_row.append(Gtk.Separator(orientation=Gtk.Orientation.VERTICAL))
        meta_row.append(self.dif_badge)
        meta_row.append(Gtk.Separator(orientation=Gtk.Orientation.VERTICAL))
        meta_row.append(self.streak_lbl)
        main_box.append(meta_row)

        # ── Tarjeta de pregunta ──
        q_card = Adw.Clamp(maximum_size=580)
        q_card_inner = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        q_card_inner.add_css_class("card")
        q_card_inner.set_margin_top(4)

        q_num_box = Gtk.Box(spacing=6, margin_start=16, margin_top=14)
        self.q_num_icon = Gtk.Label(label="❓")
        self.q_num_lbl = Gtk.Label(label="Pregunta 1")
        self.q_num_lbl.add_css_class("heading")
        q_num_box.append(self.q_num_icon)
        q_num_box.append(self.q_num_lbl)
        q_card_inner.append(q_num_box)

        self.question_label = Gtk.Label()
        self.question_label.set_wrap(True)
        self.question_label.set_wrap_mode(Pango.WrapMode.WORD_CHAR)
        self.question_label.add_css_class("question-text")
        self.question_label.set_margin_start(16)
        self.question_label.set_margin_end(16)
        self.question_label.set_margin_bottom(4)
        self.question_label.set_xalign(0)
        q_card_inner.append(self.question_label)

        self.ref_label = Gtk.Label()
        self.ref_label.add_css_class("ref-label")
        self.ref_label.set_margin_start(16)
        self.ref_label.set_margin_bottom(12)
        self.ref_label.set_xalign(0)
        q_card_inner.append(self.ref_label)

        q_card.set_child(q_card_inner)
        main_box.append(q_card)

        # ── Opciones: múltiple ──
        self.options_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.option_btns = []
        for i in range(4):
            btn = Gtk.Button()
            btn.add_css_class("option-btn")
            btn_inner = Gtk.Box(spacing=10)
            letter = Gtk.Label(label=OPTION_LETTERS[i])
            letter.set_markup(
                f'<span font_weight="ultrabold" font_size="large" foreground="#FFD700">{OPTION_LETTERS[i]}</span>'
            )
            text = Gtk.Label()
            text.set_wrap(True)
            text.set_hexpand(True)
            text.set_xalign(0)
            btn_inner.append(letter)
            btn_inner.append(text)
            btn.set_child(btn_inner)
            btn.connect("clicked", self._on_option_clicked, i)
            self.option_btns.append((btn, text))
            self.options_box.append(btn)
        main_box.append(self.options_box)

        # ── Opciones: Verdadero / Falso ──
        self.tf_box = Gtk.Box(spacing=14)
        self.tf_true_btn = Gtk.Button(label="✅  VERDADERO")
        self.tf_true_btn.add_css_class("tf-true")
        self.tf_true_btn.set_hexpand(True)
        self.tf_true_btn.set_size_request(-1, 64)
        self.tf_true_btn.connect("clicked", self._on_tf_clicked, True)

        self.tf_false_btn = Gtk.Button(label="❌  FALSO")
        self.tf_false_btn.add_css_class("tf-false")
        self.tf_false_btn.set_hexpand(True)
        self.tf_false_btn.set_size_request(-1, 64)
        self.tf_false_btn.connect("clicked", self._on_tf_clicked, False)

        self.tf_box.append(self.tf_true_btn)
        self.tf_box.append(self.tf_false_btn)
        main_box.append(self.tf_box)

        # ── Feedback ──
        self.feedback_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4,
                                    halign=Gtk.Align.CENTER)
        self.feedback_emoji = Gtk.Label()
        self.feedback_emoji.set_markup('<span font="36">❓</span>')
        self.feedback_text  = Gtk.Label()
        self.feedback_text.set_wrap(True)
        self.feedback_text.set_xalign(0.5)
        self.feedback_box.append(self.feedback_emoji)
        self.feedback_box.append(self.feedback_text)
        main_box.append(self.feedback_box)

        # ── Botón Siguiente ──
        self.next_btn = Gtk.Button(label="Siguiente pregunta →")
        self.next_btn.add_css_class("suggested-action")
        self.next_btn.add_css_class("pill")
        self.next_btn.set_hexpand(True)
        self.next_btn.connect("clicked", self._on_next)
        self.next_btn.set_visible(False)
        main_box.append(self.next_btn)

        scroll.set_child(main_box)
        page.set_content(scroll)
        self.stack.add_named(page, "game")

    # ────────────────────────────────────────────────
    #  PÁGINA 3: RESULTADOS
    # ────────────────────────────────────────────────
    def _build_result(self):
        page = Adw.ToolbarView()
        header = Adw.HeaderBar()
        header.set_show_back_button(False)
        page.add_top_bar(header)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        box.set_margin_top(40); box.set_margin_bottom(40)
        box.set_margin_start(30); box.set_margin_end(30)
        box.set_halign(Gtk.Align.CENTER)
        box.set_valign(Gtk.Align.CENTER)
        box.set_vexpand(True)

        self.result_emoji = Gtk.Label()
        self.result_emoji.set_markup('<span font="72">🏆</span>')
        box.append(self.result_emoji)

        self.result_title = Gtk.Label()
        self.result_title.add_css_class("result-title")
        box.append(self.result_title)

        self.result_score_lbl = Gtk.Label()
        self.result_score_lbl.add_css_class("result-score")
        box.append(self.result_score_lbl)

        self.result_detail = Gtk.Label()
        self.result_detail.set_wrap(True)
        self.result_detail.set_xalign(0.5)
        self.result_detail.add_css_class("dim-label")
        box.append(self.result_detail)

        sep = Gtk.Separator(); box.append(sep)

        # Estadísticas
        stats = Adw.PreferencesGroup()
        self.stat_correct  = Adw.ActionRow(title="Respuestas correctas")
        self.stat_wrong    = Adw.ActionRow(title="Respuestas incorrectas")
        self.stat_streak   = Adw.ActionRow(title="Mejor racha")
        self.stat_points   = Adw.ActionRow(title="Puntuación total")
        for row in [self.stat_correct, self.stat_wrong, self.stat_streak, self.stat_points]:
            stats.add(row)
        box.append(stats)

        sep2 = Gtk.Separator(); box.append(sep2)

        # Versículo motivacional (aleatorio)
        self.verse_label = Gtk.Label()
        self.verse_label.set_wrap(True)
        self.verse_label.set_xalign(0.5)
        self.verse_label.set_justify(Gtk.Justification.CENTER)
        self.verse_label.add_css_class("dim-label")
        box.append(self.verse_label)

        # Botones
        btn_row = Gtk.Box(spacing=12, halign=Gtk.Align.CENTER)
        retry_btn = Gtk.Button(label="🔄  Jugar de Nuevo")
        retry_btn.add_css_class("suggested-action")
        retry_btn.add_css_class("pill")
        retry_btn.connect("clicked", self._on_retry)
        home_btn = Gtk.Button(label="🏠  Menú Principal")
        home_btn.add_css_class("pill")
        home_btn.connect("clicked", lambda *_: self._go_home())
        btn_row.append(retry_btn)
        btn_row.append(home_btn)
        box.append(btn_row)

        scroll = Gtk.ScrolledWindow(vexpand=True)
        scroll.set_child(box)
        page.set_content(scroll)
        self.stack.add_named(page, "result")

    # ────────────────────────────────────────────────
    #  LÓGICA DEL JUEGO
    # ────────────────────────────────────────────────
    def _on_start(self, btn, cat_combo, dif_combo, qty_combo):
        cats  = ["Todas", "Antiguo Testamento", "Nuevo Testamento", "General"]
        difs  = ["Todas", "fácil", "medio", "difícil"]
        qtys  = [10, 15, 20, 30]

        self.filter_cat  = cats[cat_combo.get_selected()]
        self.filter_dif  = difs[dif_combo.get_selected()]
        self.total_qs    = qtys[qty_combo.get_selected()]

        # Filtrar
        pool = list(PREGUNTAS)
        if self.filter_cat != "Todas":
            pool = [q for q in pool if q["categoria"] == self.filter_cat]
        if self.filter_dif != "Todas":
            pool = [q for q in pool if q["dificultad"] == self.filter_dif]

        if len(pool) < 5:
            self._show_toast("⚠️ Muy pocas preguntas con ese filtro. Ajusta los filtros.")
            return

        random.shuffle(pool)
        self.pool = pool[:self.total_qs]
        self._reset_game_state()
        self.stack.set_visible_child_name("game")
        self._load_question()

    def _reset_game_state(self):
        self.q_index       = 0
        self.score         = 0
        self.streak        = 0
        self.best_streak   = 0
        self.correct_count = 0
        self._update_score_label()

    def _load_question(self):
        if self.q_index >= len(self.pool):
            self._show_results()
            return

        self.answered = False
        q = self.pool[self.q_index]
        self.current_q = q

        # Progreso
        frac = self.q_index / len(self.pool)
        self.progress.set_fraction(frac)
        self.prog_label.set_text(f"{self.q_index + 1} / {len(self.pool)}")
        self.q_num_lbl.set_text(f"Pregunta {self.q_index + 1}")

        # Categoría badge
        cat = q["categoria"]
        icon = CATEGORY_ICONS.get(cat, "📖")
        self.cat_badge.set_text(f"{icon} {cat}")
        for cls in ["cat-at", "cat-nt", "cat-gen"]:
            self.cat_badge.remove_css_class(cls)
        if cat == "Antiguo Testamento": self.cat_badge.add_css_class("cat-at")
        elif cat == "Nuevo Testamento": self.cat_badge.add_css_class("cat-nt")
        else:                           self.cat_badge.add_css_class("cat-gen")

        # Dificultad badge
        dif_lbl, dif_cls = DIFFICULTY_LABELS.get(q["dificultad"], ("Fácil", "difficulty-easy"))
        self.dif_badge.set_text(dif_lbl)
        for cls in ["difficulty-easy", "difficulty-medio", "difficulty-hard"]:
            self.dif_badge.remove_css_class(cls)
        self.dif_badge.add_css_class(dif_cls)

        # Racha
        self.streak_lbl.set_text(f"🔥 ×{self.streak}")

        # Texto pregunta
        self.question_label.set_text(q["pregunta"])
        self.ref_label.set_text(f"📌 {q['referencia']}")

        # Limpiar feedback
        self.feedback_emoji.set_markup('<span font="1"> </span>')
        self.feedback_text.set_text("")

        # Mostrar/ocultar tipos de respuesta
        if q["tipo"] == "multiple":
            self.options_box.set_visible(True)
            self.tf_box.set_visible(False)
            # Shufflear opciones conservando índice correcto
            correct_text = q["opciones"][q["respuesta"]]
            opciones = list(q["opciones"])
            random.shuffle(opciones)
            new_correct = opciones.index(correct_text)
            self._shuffled_correct = new_correct
            for i, (btn, lbl) in enumerate(self.option_btns):
                lbl.set_text(opciones[i])
                btn.set_sensitive(True)
                for cls in ["success", "error", "suggested-action"]:
                    btn.remove_css_class(cls)
        else:
            self.options_box.set_visible(False)
            self.tf_box.set_visible(True)
            for btn in [self.tf_true_btn, self.tf_false_btn]:
                btn.set_sensitive(True)
                for cls in ["success", "error"]:
                    btn.remove_css_class(cls)

        self.next_btn.set_visible(False)

    def _on_option_clicked(self, btn, index):
        if self.answered: return
        self.answered = True
        q = self.current_q
        correct = self._shuffled_correct

        # Deshabilitar todos los botones
        for b, _ in self.option_btns:
            b.set_sensitive(False)

        if index == correct:
            self.option_btns[index][0].add_css_class("success")
            self._mark_correct()
        else:
            self.option_btns[index][0].add_css_class("error")
            self.option_btns[correct][0].add_css_class("success")
            self._mark_wrong()

        self.next_btn.set_visible(True)

    def _on_tf_clicked(self, btn, value):
        if self.answered: return
        self.answered = True
        q = self.current_q
        correct = q["respuesta"]

        self.tf_true_btn.set_sensitive(False)
        self.tf_false_btn.set_sensitive(False)

        if value == correct:
            (self.tf_true_btn if value else self.tf_false_btn).add_css_class("success")
            self._mark_correct()
        else:
            (self.tf_true_btn if value else self.tf_false_btn).add_css_class("error")
            (self.tf_true_btn if correct else self.tf_false_btn).add_css_class("success")
            self._mark_wrong()

        self.next_btn.set_visible(True)

    def _mark_correct(self):
        pts = POINTS.get(self.current_q["dificultad"], 10)
        self.score         += pts
        self.streak        += 1
        self.correct_count += 1
        if self.streak > self.best_streak:
            self.best_streak = self.streak
        emoji = random.choice(EMOJIS_CORRECT)
        self.feedback_emoji.set_markup(f'<span font="42">{emoji}</span>')
        self.feedback_text.set_markup(
            f'<span foreground="#4CAF50" font_weight="bold">¡Correcto! +{pts} pts</span>'
        )
        self._update_score_label()
        self.streak_lbl.set_text(f"🔥 ×{self.streak}")

    def _mark_wrong(self):
        self.streak = 0
        emoji = random.choice(EMOJIS_WRONG)
        self.feedback_emoji.set_markup(f'<span font="42">{emoji}</span>')
        self.feedback_text.set_markup(
            '<span foreground="#F44336" font_weight="bold">Incorrecto 😔 — ¡Sigue intentando!</span>'
        )
        self.streak_lbl.set_text(f"🔥 ×0")

    def _on_next(self, btn):
        self.q_index += 1
        self._load_question()

    def _update_score_label(self):
        self.score_label.set_markup(
            f'<span font_weight="ultrabold" foreground="#FFD700">⭐ {self.score}</span>'
        )

    # ── Resultados ──
    def _show_results(self):
        total = len(self.pool)
        pct   = (self.correct_count / total * 100) if total else 0

        if pct == 100:
            emoji, title, color = "🏆", "¡PERFECTO!", "#FFD700"
        elif pct >= 80:
            emoji, title, color = "🌟", "¡Excelente!", "#4CAF50"
        elif pct >= 60:
            emoji, title, color = "😊", "¡Bien hecho!", "#2196F3"
        elif pct >= 40:
            emoji, title, color = "📖", "¡Sigue estudiando!", "#FF9800"
        else:
            emoji, title, color = "🙏", "¡A estudiar más!", "#F44336"

        self.result_emoji.set_markup(f'<span font="72">{emoji}</span>')
        self.result_title.set_markup(f'<span foreground="{color}" font_weight="ultrabold" font_size="xx-large">{title}</span>')
        self.result_score_lbl.set_markup(
            f'<span foreground="#FFD700" font_weight="ultrabold" font_size="xx-large">⭐ {self.score}</span>'
        )
        self.result_detail.set_markup(
            f'<span alpha="75%">{self.correct_count} de {total} correctas  ({pct:.0f}%)</span>'
        )

        self.stat_correct.set_subtitle(f"✅ {self.correct_count}")
        self.stat_wrong.set_subtitle(f"❌ {total - self.correct_count}")
        self.stat_streak.set_subtitle(f"🔥 {self.best_streak} seguidas")
        self.stat_points.set_subtitle(f"⭐ {self.score} puntos")

        # Versículo motivacional
        verses = [
            '"Todo lo puedo en Cristo que me fortalece." — Filipenses 4:13',
            '"Fíate de Jehová de todo tu corazón." — Proverbios 3:5',
            '"Lámpara es a mis pies tu palabra." — Salmo 119:105',
            '"Sean fuertes y valientes." — Josué 1:9',
            '"Bienaventurados los que oyen la palabra de Dios." — Lucas 11:28',
            '"El inicio de la sabiduría es el temor del Señor." — Proverbios 1:7',
        ]
        self.verse_label.set_markup(f'<span font_style="italic" alpha="65%">{random.choice(verses)}</span>')

        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_visible_child_name("result")
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

    def _on_retry(self, btn):
        """Reinicia con los mismos filtros."""
        random.shuffle(self.pool)
        self._reset_game_state()
        self.stack.set_visible_child_name("game")
        self._load_question()

    def _go_home(self):
        self._reset_state()
        self.stack.set_transition_type(Gtk.StackTransitionType.CROSSFADE)
        self.stack.set_visible_child_name("welcome")
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)

    def _show_toast(self, msg):
        try:
            overlay = Adw.ToastOverlay()
            toast = Adw.Toast(title=msg)
            overlay.add_toast(toast)
        except Exception:
            print(msg)


# ──────────────────────────────────────────────────────────
#  APLICACIÓN
# ──────────────────────────────────────────────────────────
class TriviaApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="org.adventista.trivia")
        self.connect("activate", self.on_activate)

    def on_activate(self, app):
        win = TriviaBiblica(app)
        win.present()


if __name__ == "__main__":
    app = TriviaApp()
    app.run()
