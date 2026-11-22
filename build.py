# -*- coding: utf-8 -*-
"""
EFÍMERA CÓRDOBA · v6 (bilingüe ES/EN · convocatoria de empresas 2027 · logo con barras · premio · agenda profesional)
Los DATOS (fechas, lugares, nombres, horarios, fotos) proceden de
efimera.jevamedia.com/es/. Textos propios, en español y en inglés.
Salida: español en la raíz, inglés en /en/.
Uso:  python build.py
"""
import json, time
from html import escape
from pathlib import Path

OUT = Path(__file__).parent
VER = str(int(time.time()))
A = "https://efimera.jevamedia.com/assets/"
IG = "https://www.instagram.com/efimera_fest/"
MAIL = "efimera@fundacionartdecor.org"
C = {"arcilla": "#C98C6C", "arcilla_osc": "#8E5138", "arena": "#D8C4A2", "arena_osc": "#B49A74", "crema": "#F4EDE2", "cal": "#EADFCC", "tinta": "#141210"}


def txt(c):
    """Texto legible sobre cada color de la paleta."""
    return "#fff" if c in (C["tinta"], C["arcilla_osc"]) else C["tinta"]


def local(path):
    return ("../" if LANG == "en" else "") + path

LANG = "es"


def t(es, en):
    return en if LANG == "en" else es


def T(x):
    """Devuelve la versión del idioma actual de una tupla (es, en)."""
    return (x[1] if LANG == "en" else x[0]) if isinstance(x, tuple) else x


def img(p):
    return A + p


def note():
    return t("Versión 6: el envío todavía no está conectado a ningún servidor.", "Version 6: this form is not connected to a server yet.")


# ---------------------------------------------------------------------------
# Rutas: mismo contenido, nombre de archivo por idioma
# ---------------------------------------------------------------------------
SL = {"index": ("index", "index"), "festival": ("festival", "festival"), "obras": ("obras", "works"), "lab": ("lab", "lab"),
      "recorrido": ("recorrido", "route"), "archivo": ("archivo", "archive"), "2027": ("2027", "2027"), "contacto": ("contacto", "contact"),
      "patrocinio": ("convocatoria-empresas", "brand-open-call"), "aviso-legal": ("aviso-legal", "legal-notice"), "privacidad": ("privacidad", "privacy"), "cookies": ("cookies", "cookies")}


def fname(key, lang=None):
    lang = lang or LANG
    return SL.get(key, (key, key))[lang == "en"] + ".html"


def u(key, anchor=""):
    return fname(key) + (f"#{anchor}" if anchor else "")


def other(key):
    return ("en/" + fname(key, "en")) if LANG == "es" else ("../" + fname(key, "es"))


# ---------------------------------------------------------------------------
# DATOS (sin cambios respecto al sitio actual) + textos nuevos
# ---------------------------------------------------------------------------
OBRAS = [
    dict(n="01", slug="bajo-la-fresca", title="Bajo la fresca", title_en="In the Cool Shade", color=C["arena"],
         place="Patio de la Asociación de Amigos de los Patios Cordobeses", addr="C/ San Basilio, 44",
         coords=[37.87595, -4.7856], authors=("Elifsu Genç, Özgün Ege Bilgiç y Sara Serés Béjar", "Elifsu Genç, Özgün Ege Bilgiç and Sara Serés Béjar"), private=True,
         hours=[("Todos los días", "Every day"), ("11:00–14:00 y 18:00–22:00", "11:00–14:00 and 18:00–22:00")],
         tag=("Dentro del patio, el clima es otro.", "Inside the patio, the climate changes."),
         text=[("Un patio cordobés es un ecosistema: las macetas y quien las riega, las vecinas que salen al fresco cuando cae la tarde, los pájaros, los insectos y una conversación que dura siglos.",
                "A Cordoban patio is an ecosystem: the flowerpots and whoever waters them, the neighbours who step out into the cool as evening falls, the birds, the insects and a conversation that has lasted for centuries."),
               ("La obra lo hace visible con color, aroma y materia viva. Agua, sombra y cuidado convertidos en un microclima que se nota en la piel antes que en los ojos.",
                "The work makes it visible through colour, scent and living matter. Water, shade and care turned into a microclimate you feel on your skin before you see it.")],
         card="fotos/2026/01/01-1-1024.42bf866a.webp",
         photos=[("fotos/2026/01/01-1-1536.dbd233fc.webp", "Toldos blancos con piezas de colores colgando sobre el patio de San Basilio, entre buganvillas y macetas", "White awnings with colourful pieces hanging over the San Basilio patio, among bougainvillea and flowerpots"),
                 ("fotos/2026/01/01-2-1024.a4cd8f91.webp", "Vista desde abajo del toldo con piezas de colores, con buganvillas fucsias en primer plano", "View from below the awning with colourful pieces, fuchsia bougainvillea in the foreground"),
                 ("fotos/2026/01/01-4-1024.e2be5b62.webp", "Detalle de las tiras de colores y los pequeños objetos que cuelgan del toldo", "Detail of the coloured strips and small objects hanging from the awning"),
                 ("fotos/2026/01/01-3-1024.ab5f6f89.webp", "El toldo de Bajo la fresca cubre el patio, con las fachadas encaladas y las flores al fondo", "The Bajo la fresca awning covers the patio, with whitewashed façades and flowers behind"),
                 ("fotos/2026/01/01-5-1024.8a1486e5.webp", "Toldo y cielo azul vistos desde el centro del patio, entre plantas trepadoras", "Awning and blue sky seen from the centre of the patio, among climbing plants")]),
    dict(n="02", slug="lo-que-permanece", title="Lo que permanece", title_en="What Remains", color=C["arcilla"],
         place="Capilla Mudéjar de San Bartolomé", addr="Plaza del Cardenal Salazar, s/n",
         coords=[37.87872, -4.78063], authors=("Belinda Moya Martínez, Sonja Mariana Peña Lobo y Máximo Sagel Sánchez", "Belinda Moya Martínez, Sonja Mariana Peña Lobo and Máximo Sagel Sánchez"), private=False,
         hours=[("Hasta el 14/09 · martes a domingo, 10:00–13:00", "Until 14 Sept · Tuesday to Sunday, 10:00–13:00"),
                ("Desde el 15/09 · lunes a sábado, 10:30–13:30 y 15:30–18:30", "From 15 Sept · Monday to Saturday, 10:30–13:30 and 15:30–18:30"),
                ("Desde el 15/09 · domingo, 10:30–13:30", "From 15 Sept · Sunday, 10:30–13:30")],
         tag=("Cada pieza existe dos veces: como cuerpo y como sombra.", "Each piece exists twice: as a body and as a shadow."),
         text=[("Todo parte de una sola forma, el círculo, llevada a la torsión y a la tensión hasta convertirse en estructuras que flotan en el aire de la capilla.",
                "Everything starts from a single shape, the circle, twisted and tensioned until it becomes structures floating in the air of the chapel."),
               ("A lo largo del día, la luz desplaza las sombras y dibuja en los muros una constelación que nunca se repite. En un espacio ligado a lo funerario, la obra habla de lo que se va y de lo que, de algún modo, se queda.",
                "Throughout the day, the light shifts the shadows and draws on the walls a constellation that never repeats. In a space linked to funerary rites, the work speaks of what leaves and of what, somehow, stays.")],
         card="fotos/2026/02/02-1-1024.9b380cac.webp",
         photos=[("fotos/2026/02/02-1-1536.5b2990dc.webp", "Círculos de malla suspendidos entre las arquerías encaladas del patio, con una palmera al fondo", "Mesh circles suspended between the whitewashed arcades of the patio, with a palm tree behind"),
                 ("fotos/2026/02/02-2-1536.175cd189.webp", "Estructuras circulares flotando sobre el patio mudéjar, vistas desde abajo contra el cielo", "Circular structures floating over the Mudéjar patio, seen from below against the sky"),
                 ("fotos/2026/02/02-3-1536.1c684dda.webp", "Detalle de un círculo de malla tensado, retorcido sobre sí mismo junto a la cornisa almenada", "Detail of a tensioned mesh circle twisted on itself next to the crenellated cornice"),
                 ("fotos/2026/02/02-4-1536.af639dec.webp", "Varias piezas circulares suspendidas proyectan su sombra sobre los muros blancos", "Several suspended circular pieces cast their shadows on the white walls"),
                 ("fotos/2026/02/02-5-1536.b5cf0567.webp", "Un gran aro de malla suspendido frente a la fachada encalada con almenas", "A large mesh ring suspended in front of the crenellated whitewashed façade")]),
    dict(n="03", slug="sagrado-florecer", title="Sagrado florecer", title_en="Sacred Blossoming", color=C["arena_osc"],
         place="Patio del Museo de Bellas Artes y Museo Julio Romero de Torres", addr="Plaza del Potro, 1",
         coords=[37.88068, -4.7737], authors=("Sofia Candeo in Art Syamhope, Azra Kaya y Carlo Marco Eurialo De Paoli", "Sofia Candeo in Art Syamhope, Azra Kaya and Carlo Marco Eurialo De Paoli"), private=False,
         hours=[("Martes a domingo", "Tuesday to Sunday"), ("09:00–15:00", "09:00–15:00")],
         tag=("Mira hacia arriba. Después, hacia dentro.", "Look up. Then look within."),
         text=[("Una lluvia de pétalos cae sobre el patio, pero no al azar: sigue la geometría sagrada que ordena muros, celosías y arcos de toda Córdoba.",
                "A rain of petals falls over the patio, but not at random: it follows the sacred geometry that orders the walls, lattices and arches of all of Córdoba."),
               ("El material parece frágil y resiste: florecer como forma de resiliencia. La pieza se completa con una experiencia interactiva sobre las matemáticas sagradas de la ciudad.",
                "The material looks fragile, yet it endures: blossoming as a form of resilience. The piece is completed by an interactive experience on the city's sacred mathematics.")],
         card="fotos/2026/03/03-1-1024.86bcf93f.webp",
         photos=[("fotos/2026/03/03-1-1536.0e4744e4.webp", "Pétalos dorados y plateados suspendidos sobre el patio del Museo de Bellas Artes", "Gold and silver petals suspended over the patio of the Museo de Bellas Artes"),
                 ("fotos/2026/03/03-2-1536.0d440f08.webp", "Lluvia de pétalos metálicos sobre la fuente central del patio, con su suelo de empedrado", "A rain of metallic petals over the central fountain of the cobbled patio"),
                 ("fotos/2026/03/03-5-1536.b1cba9cb.webp", "Gran pétalo dorado en primer plano, recortado contra el cielo y las copas de los árboles", "A large golden petal in the foreground, against the sky and the treetops"),
                 ("fotos/2026/03/03-3-1536.3a3ea069.webp", "Pétalos dorados colgados de una red sobre el patio, con visitantes bajo los naranjos", "Golden petals hanging from a net over the patio, with visitors under the orange trees"),
                 ("fotos/2026/03/03-4-1536.c689a763.webp", "Pétalos plateados y dorados atados a una estructura de cuerdas entre la vegetación", "Silver and gold petals tied to a rope structure among the greenery")]),
    dict(n="04", slug="esperar-a-la-luz", title="Esperar a la luz", title_en="Waiting for the Light", color=C["tinta"],
         place="Patio de las Tazas", addr="Plaza de las Tazas, 11",
         coords=[37.88905, -4.7744], authors=("Zhenxiang Zhao (Axel) y Laura Sánchez Avilés", "Zhenxiang Zhao (Axel) and Laura Sánchez Avilés"), private=True,
         hours=[("Lunes a sábado", "Monday to Saturday"), ("10:00–13:30", "10:00–13:30")],
         tag=("Solo existe una vez, en este momento.", "It only exists once, in this moment."),
         text=[("Komorebi es la palabra japonesa para la luz que se cuela entre las hojas. No se puede fabricar: solo se puede esperar.",
                "Komorebi is the Japanese word for the light that filters through leaves. It cannot be manufactured: it can only be waited for."),
               ("Unos módulos de para-arquitectura se colocan en el patio-jardín para recibirla, y las plantas pasan de decorado a arquitectura blanda y viva. La obra nace de quienes cuidan el lugar —Juan, el jardinero; Cristina, la dueña; Baris, el guitarrista— y conversa con Tao Yuanming y Antonio Machado.",
                "Para-architectural modules are placed in the garden patio to receive it, and the plants shift from backdrop to soft, living architecture. The work grows out of the people who look after the place —Juan, the gardener; Cristina, the owner; Baris, the guitarist— and converses with Tao Yuanming and Antonio Machado.")],
         card=None, photos=[]),
    dict(n="05", slug="leyendas", title="Leyendas", title_en="Legends", color=C["arcilla_osc"],
         place="Casa Palacio de los Angulo", addr="C/ San Pablo, 31",
         coords=[37.8857, -4.7756], authors=("Ángela Moyano, con la asistencia de Max Seguel", "Ángela Moyano, assisted by Max Seguel"), private=True,
         hours=[("Todos los días", "Every day"), ("13:30–15:30", "13:30–15:30")],
         tag=("La leyenda vuelve a nadar.", "The legend swims again."),
         text=[("Cuentan que un pez se tragó el escudo de los Angulo. El patio del palacio se convierte en una pecera gigante donde un pez de metal, red y plástico vuelve a engullirlo.",
                "Legend has it that a fish swallowed the Angulo coat of arms. The palace patio becomes a giant fish tank where a fish of metal, net and plastic swallows it once again."),
               ("Un cuento antiguo con una pregunta de hoy: qué queda en el mar cuando lo llenamos de lo que tiramos, y qué especies dejan de nadar en él.",
                "An old tale with a question for today: what is left in the sea when we fill it with what we throw away, and which species stop swimming in it.")],
         card="fotos/2026/05/05-1-1024.5eda734a.webp",
         photos=[("fotos/2026/05/05-4-1536.8da9d81c.webp", "Vista general del patio-jardín con las piezas blancas flotando entre palmeras y plantas", "General view of the garden patio with white pieces floating among palm trees and plants"),
                 ("fotos/2026/05/05-1-1536.6c0e8477.webp", "Figuras blancas de tela y red, con forma de medusa, flotan entre las palmeras del patio", "White jellyfish-like figures of fabric and net float among the palm trees"),
                 ("fotos/2026/05/05-3-1536.9738474d.webp", "Una medusa de tela blanca con largos filamentos y una burbuja transparente sobre el jardín", "A white fabric jellyfish with long filaments and a transparent bubble over the garden"),
                 ("fotos/2026/05/05-2-1536.df09ba9c.webp", "Burbujas transparentes y velos blancos suspendidos entre palmeras, como dentro de una pecera", "Transparent bubbles and white veils suspended among palm trees, as if inside a fish tank"),
                 ("fotos/2026/05/05-5-1536.a11e0360.webp", "Velos blancos y burbujas entre palmeras y rocas en el jardín del palacio", "White veils and bubbles among palm trees and rocks in the palace garden")]),
]

CAMPANA = [
    ("campana/teaser-800.7b4c5ed8.webp", "Collage: patio con palmera, malla azul y burbujas bajo un círculo fucsia", "Collage: patio with a palm tree, blue mesh and bubbles under a fuchsia circle"),
    ("campana/becas-800.0b743a12.webp", "Collage: un cámara filma una estructura de cortinas de colores frente a una torre cordobesa", "Collage: a camera operator films a structure of coloured curtains in front of a Cordoban tower"),
    ("campana/pergola-800.a94389ea.webp", "Collage: pérgola con flores colgada entre burbujas, círculos amarillos y fucsias", "Collage: a flowering pergola hanging among bubbles and yellow and fuchsia circles"),
    ("campana/taller-800.9971c5de.webp", "Collage: cortina de agua junto a una muralla y un campanario, con un cámara agachado", "Collage: a water curtain beside a city wall and a bell tower, with a crouching camera operator"),
    ("campana/collage-arco-800.ac0a124e.webp", "Collage en blanco y negro con franjas de color: un arco de piedra y paseantes por una calle de Córdoba", "Black-and-white collage with colour bands: a stone arch and passers-by in a Córdoba street"),
    ("campana/efimera-800.5f0f0d39.webp", "Collage: torre cordobesa, burbujas y una pérgola con buganvillas sobre fondo azul y fucsia", "Collage: Cordoban tower, bubbles and a bougainvillea pergola on a blue and fuchsia background"),
    ("campana/collage-torre-800.4d49f367.webp", "Collage en blanco y negro con círculos naranjas y amarillos: palmera, campanario y casas encaladas", "Black-and-white collage with orange and yellow circles: palm tree, bell tower and whitewashed houses"),
]

PRENSA = [
    ("23.10.2026", "Dos estudiantes de Publicidad y Marketing Digital de Loyola reciben una mención de honor en el Festival Efímera Córdoba", "Universidad Loyola",
     "https://www.uloyola.es/blog/grados/dos-estudiantes-de-publicidad-y-marketing-digital-de-loyola-reciben-una-mencion-de-honor-en-el-festival-efimera-cordoba"),
    ("22.09.2026", "El Patio de las Tazas acogerá este jueves la apertura del festival Efímera Córdoba 2026 con música y gastronomía", "Diario Córdoba · Araceli R. Arjona",
     "https://www.diariocordoba.com/cultura/2026/09/22/patio-tazas-acogera-jueves-apertura-134564401.html"),
    ("01.09.2026", "Arte efímero para denunciar desde Córdoba el cambio climático", "El Día de Córdoba · Ángela Alba",
     "https://www.eldiadecordoba.es/cordoba/festival-efimera-cordoba-cambio-climatico_0_2007837952.html"),
    ("01.09.2026", "Un recorrido por las instalaciones del Festival Efímera Córdoba 2026, en fotos", "El Día de Córdoba · Fotos: Luis Navarro",
     "https://www.eldiadecordoba.es/cordoba/recorrido-instalaciones-festival-efimera-cordoba-2026-fotos_3_2007838810.html"),
    ("26.08.2026", "Efímera Córdoba inicia su segunda fase de intervenciones en la ciudad", "Cordópolis · Redacción Cordópolis",
     "https://cordopolis.eldiario.es/cultura/efimera-cordoba-inicia-segunda-fase-intervenciones-ciudad_1_13468684.html"),
    ("26.08.2026", "El cuidado frente al cambio climático será el hilo conductor de las intervenciones artísticas de Efímera Córdoba 2026", "Diario Córdoba · Araceli R. Arjona", None),
]

COLABORAN = [("Fundación Kutxabank", "fundacionkutxabank"), ("Keyter Group", "keyter_hvac"), ("Restaurante Amaltea", "restauranteamaltea"),
             ("Universidad de Córdoba", "universidaddecordoba"), ("Universidad Loyola", "loyolaand"),
             ("C3A · Centro de Creación Contemporánea de Andalucía", "c3a_andalucia"), ("Filmoteca de Andalucía", "filmotecadeandalucia"),
             ("Museo de Bellas Artes de Córdoba", "museo_bellasartes_co"), ("Palacio de Viana", "palaciodeviana"),
             ("Asociación Amigos de los Patios Cordobeses", "amigospatioscordobeses"), ("Teulo", "teulo_cpdplatform")]

PONENTES = [("Nina Chaltiel", ("Cofundadora de MUDD Architects · comisaria", "Co-founder of MUDD Architects · curator")),
            ("Fernando Vacas", ("Músico y productor (Eureka), presidente de la Fundación Artdecor · comisario", "Musician and producer (Eureka), president of Fundación Artdecor · curator")),
            ("James Kingman", ("Associate Director, AKT II", "Associate Director, AKT II")),
            ("Curro Crespo", ("Arquitecto, socio fundador de Amasce · Premio Félix Hernández 2022", "Architect, founding partner of Amasce · Félix Hernández Award 2022")),
            ("Rosa Lara Jiménez", ("Arquitecta, Gerencia Municipal de Urbanismo", "Architect, Córdoba City Planning Office")),
            ("Pedro Caro González", ("Arquitecto, Gerencia Municipal de Urbanismo", "Architect, Córdoba City Planning Office")),
            ("Hugo Lasarte", ("Hugo RedRose · Creative Director & Visual Artist", "Hugo RedRose · Creative Director & Visual Artist")),
            ("Raquel Pascual", ("Economista y chef, Restaurante Amaltea", "Economist and chef, Restaurante Amaltea")),
            ("Pedro García del Barrio", ("Arquitecto y urbanista, presidente de la Fundación Arquitectura Contemporánea", "Architect and urban planner, president of Fundación Arquitectura Contemporánea")),
            ("Lola Baena", ("Museóloga y especialista en patrimonio", "Museologist and heritage specialist")),
            ("Carlos García", ("Head Manager, Keyter Group", "Head Manager, Keyter Group")),
            ("Luis Celorio", ("Artista multidisciplinar", "Multidisciplinary artist")),
            ("Janelle Wynyard", ("Fundadora de Teulo", "Founder of Teulo")),
            ("Hira Wynyard", ("Head of Creative & Customer Success, Teulo", "Head of Creative & Customer Success, Teulo")),
            ("José A. Gutiérrez", ("Director y guionista de cine documental", "Documentary film director and screenwriter"))]

TRAYECTO = [(("Jue 24.09", "Thu 24.09"), "21:30", ("Acústico íntimo de Baris Yavuz", "Intimate acoustic set by Baris Yavuz"), ("Patio de las Tazas · con aperitivo de Amaltea y confirmación previa", "Patio de las Tazas · with an Amaltea aperitif, booking required"), None),
            (("Vie 25.09", "Fri 25.09"), "19:00", ("Entrega de premios de Nuevas Miradas", "Nuevas Miradas award ceremony"), ("Filmoteca de Andalucía, C/ Medina y Corella, 5", "Filmoteca de Andalucía, C/ Medina y Corella, 5"), None),
            (("Sáb 26.09", "Sat 26.09"), "13:00", ("«Lo efímero», poesía de Juan Antonio Bernier", "“Lo efímero”, poetry by Juan Antonio Bernier"), ("Patio de Amigos de los Patios", "Patio de Amigos de los Patios"), ("Suspendido", "Cancelled")),
            (("Sáb 26.09", "Sat 26.09"), "21:30", ("Música experimental de Athene Noctu4", "Experimental music by Athene Noctu4"), ("Capilla Mudéjar de San Bartolomé", "Capilla Mudéjar de San Bartolomé"), None),
            (("Sáb 26.09", "Sat 26.09"), "22:00", ("Fiesta de clausura", "Closing party"), ("Automático, C/ Alfaros, 4", "Automático, C/ Alfaros, 4"), None),
            (("Dom 27.09", "Sun 27.09"), "12:00", ("«8», danza de Irene Lázaro", "“8”, dance by Irene Lázaro"), ("Patio del Museo de Bellas Artes", "Patio of the Museo de Bellas Artes"), None),
            (("Dom 27.09", "Sun 27.09"), "13:00", ("Matu Mati, «Alto Vuelo», y vermú", "Matu Mati, “Alto Vuelo”, and vermouth"), ("Palacio de los Angulo", "Palacio de los Angulo"), None)]

FAQ = [(("¿Qué es EFÍMERA CÓRDOBA?", "What is EFÍMERA CÓRDOBA?"),
        ("Un festival internacional que instala arquitectura temporal, creación contemporánea y actividades abiertas en patios, capillas y palacios del casco histórico de Córdoba, Patrimonio Mundial de la UNESCO.",
         "An international festival that installs temporary architecture, contemporary creation and open activities in the patios, chapels and palaces of Córdoba's historic centre, a UNESCO World Heritage Site.")),
       (("¿Cuándo fue la primera edición?", "When was the first edition?"),
        ("En 2026: becas del 1 al 15 de julio, Efímera Lab del 20 al 30 de agosto en el C3A, obras abiertas del 1 al 30 de septiembre y cierre —Último Trayecto— del 24 al 27 de septiembre.",
         "In 2026: grants from 1 to 15 July, Efímera Lab from 20 to 30 August at the C3A, works open from 1 to 30 September and the closing week —Último Trayecto— from 24 to 27 September.")),
       (("¿Había que pagar?", "Did it cost anything?"),
        ("No. Todas las obras eran de entrada libre, cada una con el horario de su espacio, y las actividades de cierre también, hasta completar aforo.",
         "No. Every work was free to enter, each with its venue's opening hours, and so were the closing activities, until full capacity.")),
       (("¿Quién está detrás?", "Who is behind it?"),
        ("La Fundación Artdecor y MUDD Architects, con la Architectural Association School of Architecture de Londres. Comisariado de Nina Chaltiel y Fernando Vacas.",
         "Fundación Artdecor and MUDD Architects, with the Architectural Association School of Architecture in London. Curated by Nina Chaltiel and Fernando Vacas.")),
       (("¿Habrá 2027?", "Will there be a 2027 edition?"),
        ("Sí. Efímera Lab, con estudiantes de la AA School, del 20 al 31 de agosto, e instalaciones abiertas al público durante todo septiembre de 2027. Las convocatorias se anunciarán aquí, en el boletín y en @efimera_fest.",
         "Yes. Efímera Lab, with AA School students, from 20 to 31 August, and installations open to the public throughout September 2027. Open calls will be announced here, in the newsletter and on @efimera_fest.")),
       (("¿Cómo puedo participar o colaborar?", "How can I take part or partner with you?"),
        ("Como participante, con las convocatorias de cada edición: becas, ayudas a la producción, el Efímera Lab y el concurso audiovisual. Como empresa, presentando candidatura a la convocatoria de empresas 2027.",
         "As a participant, through each edition's open calls: grants, production support, the Efímera Lab and the film competition. As a company, by applying to the 2027 brand open call."))]


def NAV():
    return [("festival", "Festival"), ("obras", t("Obras", "Works")), ("lab", "Lab"), ("recorrido", t("Recorrido", "Route")),
            ("archivo", t("Archivo", "Archive")), ("2027", "2027")]


# ---------------------------------------------------------------------------
# Piezas comunes
# ---------------------------------------------------------------------------
def mark(cls=""):
    """Logo: EFÍMERA CÓRDOBA en Unbounded; las tildes de la Í y la Ó son barras horizontales."""
    k = ("mark " + cls).strip()
    return (f'<span class="{k}" role="img" aria-label="EFÍMERA CÓRDOBA">'
            '<span aria-hidden="true">EF<span class="acc">I</span>MERA</span> <span aria-hidden="true">C<span class="acc">O</span>RDOBA</span></span>')


MARK = mark()
MARK_LINE = mark("line")


def btn(label, href, cls="", ext=False, arrow="→"):
    tg = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="btn {cls}" href="{href}"{tg}>{label} <span class="arr" aria-hidden="true">{arrow}</span></a>'


def marquee(items, big=False, reps=4):
    one = "".join(f"<span>{a}</span><span><i>{b}</i></span>" for a, b in items)
    return f'<div class="marquee{" marquee--big" if big else ""}" aria-hidden="true"><div class="marquee__track">{one * reps}</div></div>'


def hero(crumb, h1, lead="", size="d-xl", extra=""):
    eb = f'<a href="{u("index")}">{t("Inicio", "Home")}</a> <span aria-hidden="true">/</span> <span>{crumb}</span>'
    return f'''<section class="block page-hero"><div class="wrap">
  <div class="eyebrow label">{eb}</div>
  <h1 class="d {size} rv">{h1}</h1>
  {f'<p class="lead rv">{lead}</p>' if lead else ""}
  {extra}
</div></section>'''


def hp():
    return '<div class="hp" aria-hidden="true"><label>Web <input type="text" tabindex="-1" autocomplete="off"></label></div>'


def privacy_check():
    return f'<label class="check"><input type="checkbox" required> <span>{t("He leído la", "I have read the")} <a href="{u("privacidad")}">{t("política de privacidad", "privacy policy")}</a>.</span></label>'


def news_form(ok, cls=""):
    return f'''<form class="{cls}" data-form data-ok="{escape(ok)} ({note()})" novalidate>
  <div class="inline-sub"><label class="vh" for="nl-{cls or 'x'}">{t("Tu email", "Your email")}</label><input id="nl-{cls or 'x'}" type="email" required placeholder="{t("Tu email", "Your email")}"><button type="submit">{t("Avísame", "Notify me")}</button></div>
  {hp()}
  <p class="form-msg mt-s" role="status"></p>
</form>'''


def partners():
    names = "".join(f'<a href="https://www.instagram.com/{n_}/" target="_blank" rel="noopener">{n}</a>' for n, n_ in COLABORAN)
    return f'''<section class="partners" aria-label="{t("Quién lo hace posible", "Who makes it possible")}"><div class="wrap grid">
  <div><span class="label">{t("Organizan, con la AA School", "Organised by, with the AA School")}</span><div class="logos">
    <a href="https://www.fundacionartdecor.org" target="_blank" rel="noopener"><img src="{img('img/logos/artdecor.ae34de74.png')}" alt="Fundación Artdecor"></a>
    <a href="https://www.muddarchitects.com/" target="_blank" rel="noopener"><img src="{img('img/logos/mudd.6f8b5b97.png')}" alt="MUDD Architects"></a>
    <a class="aa-logo" href="https://www.aaschool.ac.uk" target="_blank" rel="noopener"><img src="{local('assets/logos/aa.svg')}" alt=""><span>Architectural Association<br>School of Architecture</span></a></div></div>
  <div><span class="label">{t("Socios 2027", "2027 partners")}</span><br><a class="aa" href="https://www.shimaseiki.com" target="_blank" rel="noopener">Shima Seiki<small>{t("Partner técnico · tejido 3D", "Technical partner · 3D knitting")}</small></a><br><a class="aa" href="https://www.dezeen.com" target="_blank" rel="noopener">Dezeen<small>{t("Socio de prensa", "Media partner")}</small></a><br><a class="aa" href="https://www.juntadeandalucia.es/cultura/c3a/" target="_blank" rel="noopener">C3A<small>{t("Colaborador y espacio de intervención", "Partner and installation venue")}</small></a></div>
  <div><span class="label">{t("Colaboran", "Supported by")}</span><div class="names">{names}</div></div>
</div></section>'''


def lang_switch(key):
    es = '<span aria-current="true">ES</span>' if LANG == "es" else f'<a href="{other(key)}" hreflang="es" lang="es">ES</a>'
    en = '<span aria-current="true">EN</span>' if LANG == "en" else f'<a href="{other(key)}" hreflang="en" lang="en">EN</a>'
    return f'<span class="lang" aria-label="{t("Idioma", "Language")}">{es}{en}</span>'


def footer(key):
    links = "".join(f'<a href="{u(k)}">{l}</a>' for k, l in NAV()) + f'<a href="{u("patrocinio")}">{t("Convocatoria 2027", "Open call 2027")}</a><a href="{u("contacto")}">{t("Contacto", "Contact")}</a>'
    return f'''<footer class="footer"><div class="wrap">
  <div class="top">
    <div><a href="{u("index")}" aria-label="{t("Inicio", "Home")}">{MARK}</a><p class="when">{t("1.ª edición: septiembre de 2026.<br>2.ª edición: septiembre de 2027.", "1st edition: September 2026.<br>2nd edition: September 2027.")}</p><p>{lang_switch(key)}</p></div>
    <div><h4>{t("Explora", "Explore")}</h4><nav class="links" aria-label="{t("Pie", "Footer")}">{links}</nav></div>
    <div><h4>{t("Escríbenos", "Write to us")}</h4>
      <address><a href="mailto:{MAIL}">{MAIL}</a><br><a href="{IG}" target="_blank" rel="noopener">@efimera_fest</a></address>
      <address><strong>Fundación Artdecor</strong><br>C/ Juramento, 1 · 14002 Córdoba</address>
      <address><strong>MUDD Architects</strong><br>Gallery Building, Carrer de l'Escar, 26 · 08039 Barcelona</address></div>
    <div class="news"><h3>{t("Avísame cuando llegue 2027", "Tell me when 2027 arrives")}</h3><p>{t("Un correo cuando haya fechas y convocatorias. Nada más.", "One email when dates and open calls are out. Nothing else.")}</p>{news_form(t("¡Hecho! Te escribiremos cuando haya noticias.", "Done! We'll write when there's news."), "f")}</div>
  </div>
  <div class="giant" aria-hidden="true">{MARK_LINE}</div>
  <div class="bottom"><span>© 2026 Fundación Artdecor · CIF G16673691</span>
    <nav aria-label="Legal"><a href="{u("aviso-legal")}">{t("Aviso legal", "Legal notice")}</a><a href="{u("privacidad")}">{t("Privacidad", "Privacy")}</a><a href="{u("cookies")}">Cookies</a><button type="button" data-cookies-open>{t("Configurar cookies", "Cookie settings")}</button></nav></div>
</div></footer>'''


def shell_end():
    return f'''<div class="lightbox" role="dialog" aria-modal="true" aria-label="{t("Imágenes", "Images")}">
  <span class="lb-count"></span><figure><img alt=""><figcaption></figcaption></figure>
  <button class="round-btn lb-close" aria-label="{t("Cerrar", "Close")}">✕</button><button class="round-btn lb-prev" aria-label="{t("Anterior", "Previous")}">←</button><button class="round-btn lb-next" aria-label="{t("Siguiente", "Next")}">→</button>
</div>
<div class="cookies" role="dialog" aria-label="Cookies">
  <p>{t("Usamos cookies técnicas para que la web funcione y, solo si nos dejas, cookies de analítica para entender cómo se usa. Puedes cambiarlo cuando quieras.", "We use technical cookies to make the site work and, only if you allow it, analytics cookies to understand how it is used. You can change this at any time.")} <a href="{u("cookies")}">{t("Más información", "More information")}</a></p>
  <div class="cfg">
    <label><input type="checkbox" checked disabled> <span><strong>{t("Necesarias.", "Necessary.")}</strong> {t("Recuerdan tu elección. Siempre activas.", "They remember your choice. Always on.")}</span></label>
    <label><input type="checkbox" data-ck-an> <span><strong>{t("Analítica.", "Analytics.")}</strong> {t("Google Analytics 4, de forma agregada.", "Google Analytics 4, aggregated.")}</span></label>
    <label><input type="checkbox" data-ck-pub> <span><strong>{t("Publicidad.", "Advertising.")}</strong> {t("Ahora mismo no usamos ninguna.", "We don't use any right now.")}</span></label>
    <div class="btn-row mt-s"><button class="btn btn--light" data-ck-save>{t("Guardar", "Save")}</button></div>
  </div>
  <div class="btn-row"><button class="btn btn--light" data-ck-all>{t("Aceptar", "Accept")}</button><button class="btn btn--light" data-ck-none>{t("Rechazar", "Reject")}</button><button class="btn btn--light" data-ck-cfg>{t("Configurar", "Settings")}</button></div>
</div>'''


def no_widows(html):
    """Evita que la última palabra de un título quede sola en su línea (une las dos últimas con un espacio fijo)."""
    import re

    def fix(m):
        inner = m.group(2)
        words = re.sub(r"<[^>]+>", " ", inner).replace("&nbsp;", " ").split()
        if len(words) < 3 or len(words[-2]) + len(words[-1]) > 16:
            return m.group(0)
        depth = 0
        inside = []
        for ch in inner:
            if ch == "<": depth += 1
            inside.append(depth > 0)
            if ch == ">": depth -= 1
        for i in range(len(inner) - 1, -1, -1):
            if inner[i] == " " and not inside[i]:
                tail = re.sub(r"<[^>]+>", "", inner[i + 1:])
                if 0 < len(tail) <= 14:
                    return m.group(1) + inner[:i] + "&nbsp;" + inner[i + 1:] + m.group(3)
                break
        return m.group(0)
    return re.sub(r"(<h[123][^>]*>)(.*?)(</h[123]>)", fix, html, flags=re.S)



def page(key, title, desc, navkey, body, bloque=None, bloque_txt="#fff", head="", foot="", show_partners=False):
    style = f' style="--bloque:{bloque};--bloque-txt:{bloque_txt}"' if bloque else ""
    full = t("EFÍMERA CÓRDOBA · Festival internacional de arquitectura efímera", "EFÍMERA CÓRDOBA · International festival of ephemeral architecture") if key == "index" else f"{title} · EFÍMERA CÓRDOBA"
    P = "../" if LANG == "en" else ""
    nav = "".join(f'<a href="{u(k)}"{" aria-current=page" if k == navkey else ""}>{l}</a>' for k, l in NAV())
    cta = f'<a class="cta" href="{u("patrocinio")}"{" aria-current=page" if navkey == "patrocinio" else ""}>{t("Convocatoria 2027", "Open call 2027")}</a>'
    es_url, en_url = fname(key, "es"), "en/" + fname(key, "en")
    html = f'''<!DOCTYPE html>
<html lang="{LANG}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full)}</title>
<meta name="description" content="{escape(desc)}">
<meta property="og:title" content="{escape(full)}"><meta property="og:description" content="{escape(desc)}"><meta property="og:locale" content="{t("es_ES", "en_GB")}">
<link rel="alternate" hreflang="es" href="{P}{es_url}"><link rel="alternate" hreflang="en" href="{P}{en_url}"><link rel="alternate" hreflang="x-default" href="{P}{es_url}">
<meta name="theme-color" content="{bloque or C['arcilla']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@300;400;500;700&family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{P}assets/styles.css?v={VER}">
{head}
</head>
<body{style}>
<a class="skip" href="#contenido">{t("Ir al contenido", "Skip to content")}</a>
<div class="topbar"><div class="wrap"><span class="hide-s">{t("2.ª edición · septiembre 2027 · Córdoba", "2nd edition · September 2027 · Córdoba")}</span><span style="display:flex;gap:22px;align-items:center"><a class="hide-s" href="{u("patrocinio")}">{t("Convocatoria de empresas: hasta el 28 feb →", "Brand open call: until 28 Feb →")}</a><a href="{u("contacto")}">{t("Contacto", "Contact")}</a>{lang_switch(key)}</span></div></div>
<header class="header"><div class="wrap">
  <a href="{u("index")}" aria-label="EFÍMERA CÓRDOBA · {t("inicio", "home")}">{MARK}</a>
  <nav class="nav" aria-label="{t("Principal", "Main")}">{nav}{cta}</nav>
  <button class="menu-btn" data-menu-open aria-label="{t("Abrir menú", "Open menu")}">{t("Menú", "Menu")}</button>
</div></header>
<div class="mobile-nav" aria-label="{t("Menú", "Menu")}"><div class="top">{MARK}<button class="menu-btn" style="display:inline-flex" data-menu-close>{t("Cerrar", "Close")}</button></div>
  <nav><a href="{u("index")}">{t("Inicio", "Home")}</a>{nav.replace(" aria-current=page", "")}{cta.replace(" aria-current=page", "")}<a href="{u("contacto")}">{t("Contacto", "Contact")}</a></nav>
  {lang_switch(key)}
  <div class="foot"><a href="mailto:{MAIL}">{MAIL}</a><a href="{IG}" target="_blank" rel="noopener">@efimera_fest</a></div></div>
<main id="contenido">
{body}
</main>
{partners() if show_partners else ""}
{footer(key)}
{shell_end()}
{foot}
<script src="{P}assets/main.js?v={VER}"></script>
</body>
</html>'''
    d = OUT / ("en" if LANG == "en" else "")
    d.mkdir(exist_ok=True)
    (d / fname(key)).write_text(no_widows(html), encoding="utf-8")
    print("✓", ("en/" if LANG == "en" else "") + fname(key))


def work_row(o):
    th = f'<img src="{img(o["card"])}" alt="" loading="lazy">' if o["card"] else f'<div class="tile" style="background:{o["color"]};color:{txt(o["color"])}"><b>{o["n"]}</b></div>'
    sub = f' <span class="vh">({o["title_en"]})</span>' if LANG == "en" else ""
    return f'''<a class="work rv" href="{u(o["slug"])}"><span class="n">{o["n"]}</span><h3 lang="es">{o["title"]}{sub}</h3><p>{o["place"]}</p><div class="th">{th}</div></a>'''


def arch_card(href, image, title, sub, tile=None):
    media = f'<img src="{img(image)}" alt="" loading="lazy">' if image else f'<div class="tile"><span class="label">{tile[0]}</span><b>{tile[1]}</b><span class="label">{tile[2]}</span></div>'
    return f'<a class="card" href="{href}"><div class="img">{media}</div><div class="meta"><div><strong>{title}</strong><small>{sub}</small></div><span class="go" aria-hidden="true">→</span></div></a>'


def rail(title, cards, right=""):
    return f'''<div data-rail>
  <div class="head rv"><h2 class="d d-l">{title}</h2><div class="btn-row">{right}<button class="round-btn" data-prev aria-label="{t("Anterior", "Previous")}">←</button><button class="round-btn" data-next aria-label="{t("Siguiente", "Next")}">→</button></div></div>
  <div class="rail rv">{cards}</div><div class="rail-progress"><span></span></div>
</div>'''


def prensa_row(d, ti, s, url):
    ln = f' <span class="lang-note">· {t("", "in Spanish")}</span>' if LANG == "en" else ""
    inner = f'<span class="date">{d}</span><div><h3 lang="es">{ti}</h3><span class="src">{s}{ln}</span></div>'
    return (f'<a class="rv" href="{url}" target="_blank" rel="noopener">{inner}<span aria-hidden="true">↗</span><span class="vh">({t("se abre en otra pestaña", "opens in a new tab")})</span></a>'
            if url else f'<div class="rv">{inner}<span></span></div>')


# ---------------------------------------------------------------------------
# INICIO
# ---------------------------------------------------------------------------
def home():
    col = OBRAS

    def fig(o, ph, cls=""):
        return f'<a class="{cls} rv-blur" href="{u(o["slug"])}"><figure><img src="{img(o["card"])}" alt="{escape(T((ph[1], ph[2])))}" loading="lazy"><figcaption>{o["n"]} · {o["title"]}</figcaption></figure></a>'
    collage = f'''<div class="collage">
  {fig(col[0], col[0]["photos"][0], "c1")}
  <div class="c2">{fig(col[1], col[1]["photos"][0])}{fig(col[4], col[4]["photos"][1])}</div>
  {fig(col[2], col[2]["photos"][0], "c3")}
</div>'''
    cards = "".join([
        arch_card(u("2027"), None, t("Edición 2027", "2027 edition"), t("En preparación", "In the works"), (t("Próximamente", "Coming soon"), "27", t("Segunda edición", "Second edition"))),
        arch_card(u("obras"), "fotos/2026/02/02-2-1024.520e08ca.webp", t("Edición 2026", "2026 edition"), t("Cinco obras · 1–30 sept.", "Five works · 1–30 Sept")),
        arch_card(u("lab"), "campana/taller-800.9971c5de.webp", "Efímera Lab 2026", t("20–30 ago. · C3A", "20–30 Aug · C3A")),
        arch_card(u("lab", "nuevas-miradas"), "campana/becas-800.0b743a12.webp", "Nuevas Miradas", t("Concurso audiovisual", "Film competition")),
        arch_card(u("archivo", "ultimo-trayecto"), "campana/collage-arco-800.ac0a124e.webp", "Último Trayecto", t("24–27 sept. · Cierre", "24–27 Sept · Closing week")),
        arch_card(u("archivo", "campana"), "campana/efimera-800.5f0f0d39.webp", t("Campaña gráfica", "Graphic campaign"), t("Siete collages", "Seven collages")),
    ])
    press = "".join(prensa_row(*p) for p in PRENSA[1:4])
    body = f'''
<section class="block hero">
  <div class="wrap">
    <h1 class="d d-xl rv">{t('Arquitectura que aparece, <span class="it">transforma</span> y se va.', 'Architecture that appears, <span class="it">transforms</span> and leaves.')}</h1>
    <p class="sub rv">{t("Festival internacional de arquitectura efímera, creación contemporánea y ciudadanía en el casco histórico de Córdoba.", "International festival of ephemeral architecture, contemporary creation and citizenship in the historic centre of Córdoba.")}</p>
    <div class="hero-media rv">
      <video id="v" data-zoom autoplay muted loop playsinline preload="metadata" poster="{img('video/portada-poster.95ab3b86.jpg')}">
        <source src="{img('video/portada.3f4800f8.webm')}" type="video/webm"><source src="{img('video/portada.8c7f6e58.mp4')}" type="video/mp4"></video>
      <div class="ui"><button class="chip" data-play="v">{t("Pausa", "Pause")}</button><button class="chip" data-sound="v" aria-pressed="false">{t("Activar sonido", "Sound on")}</button></div>
    </div>
  </div>
  {marquee([(t("Hasta 2027", "See you in 2027"), t("gracias, Córdoba", "thank you, Córdoba")), (t("Lo efímero deja huella", "The ephemeral leaves a mark"), "✦")])}
</section>

<section class="section"><div class="wrap statement">
  <span class="label rv">{t("El festival", "The festival")}</span>
  <p class="d" data-words>{t("Un mes. Cinco obras. Patios, una capilla y un palacio abiertos a quien quisiera entrar. Después, nada. Solo la ciudad, mirada de otra manera.", "One month. Five works. Patios, a chapel and a palace open to anyone who wanted to come in. Then, nothing. Only the city, seen in a different way.")}</p>
  <div class="btn-row rv">{btn(t("Leer el manifiesto", "Read the manifesto"), u("festival"))}</div>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="stats rv">
    <div><b>5</b><span>{t("obras en el casco histórico", "works in the historic centre")}</span></div>
    <div><b>30</b><span>{t("días abiertas al público", "days open to the public")}</span></div>
    <div><b>15</b><span>{t("ponentes en el Lab", "speakers at the Lab")}</span></div>
    <div><b>0 €</b><span>{t("la entrada, en todas", "entry fee, at every venue")}</span></div>
  </div>
</div></section>

<section class="section"><div class="wrap split">
  <div class="copy rv">
    <span class="label">{t("Obras 2026", "Works 2026")}</span>
    <h2 class="d d-l mt-s">{t('Cinco obras, <span class="it">cinco</span> lugares.', 'Five works, <span class="it">five</span> places.')}</h2>
    <p>{t("Sombra, agua y verde: la primera edición respondió al calor con los recursos de siempre de la ciudad.", "Shade, water and greenery: the first edition answered the heat with the city's age-old resources.")}</p>
    {btn(t("Ver las obras", "See the works"), u("obras"))}
    <div class="rule-short"></div>
  </div>
  {collage}
</div></section>

<section class="section bg-ink"><div class="wrap two-col" style="align-items:center">
  <figure class="frame rv-blur" style="aspect-ratio:1"><img src="{img('campana/taller-800.9971c5de.webp')}" alt="{escape(T(CAMPANA[3][1:]))}" loading="lazy"></figure>
  <div class="rv">
    <span class="label" style="opacity:.6">Efímera Lab</span>
    <h2 class="d d-l mt-s">{t("Aquí nacen las obras.", "Where the works are born.")}</h2>
    <p class="lead mt-m">{t("Diez días de taller internacional en el C3A, dirigido por Nina Chaltiel con estudiantes de la Architectural Association de Londres. Prototipos por la mañana, charlas al caer la tarde y la ciudad como aula.", "Ten days of international workshop at the C3A, led by Nina Chaltiel with students from the Architectural Association in London. Prototypes in the morning, talks at dusk and the city as a classroom.")}</p>
    <div class="reasons" style="grid-template-columns:repeat(3,1fr)">
      <div><h3>10</h3><p>{t("días de taller", "workshop days")}</p></div>
      <div><h3>15</h3><p>{t("ponentes invitados", "guest speakers")}</p></div>
      <div><h3>AA</h3><p>{t("School of Architecture, Londres", "School of Architecture, London")}</p></div>
    </div>
    <div class="btn-row mt-m">{btn(t("Conocer el Lab", "Discover the Lab"), u("lab"), "btn--light")}{btn(t("Convocatorias 2027", "2027 open calls"), u("2027", "convocatorias"), "btn--light")}</div>
  </div>
</div></section>

<section class="section bg-almagra on-color"><div class="wrap">
  <div class="two-col" style="align-items:end">
    <div class="rv"><span class="label" style="opacity:.75">{t("Convocatoria de empresas 2027", "2027 brand open call")}</span>
      <h2 class="d d-l mt-s">{t('Tu marca, un artista, <span class="it">un patio</span>.', 'Your brand, an artist, <span class="it">a patio</span>.')}</h2></div>
    <div class="rv"><p class="lead">{t("En septiembre de 2027, un grupo seleccionado de empresas crea, con un artista o con su propio equipo, una instalación en uno de los siete espacios del festival. 15 plazas: candidaturas hasta el 28 de febrero de 2027.", "In September 2027, a select group of companies will create, with an artist or their own team, an installation in one of the festival's seven venues. 15 places: applications until 28 February 2027.")}</p>
      <div class="btn-row mt-m">{btn(t("Ver la convocatoria", "See the open call"), u("patrocinio"), "btn--light")}{btn(t("Presentar candidatura", "Apply now"), u("patrocinio", "candidatura"), "btn--solid")}</div></div>
  </div>
  <div class="reasons rv">
    <div><h3>{t("7 espacios", "7 venues")}</h3><p>{t("San Basilio, Capilla Mudéjar, Bellas Artes, Casa de las Tazas, Palacio de los Angulo, Palacio de Viana y C3A.", "San Basilio, the Mudéjar Chapel, Fine Arts Museum, Casa de las Tazas, Palacio de los Angulo, Palacio de Viana and the C3A.")}</p></div>
    <div><h3>{t("Artista o in-house", "Artist or in-house")}</h3><p>{t("Tu artista, uno que te proponemos o tu propio equipo.", "Your artist, one we suggest, or your own team.")}</p></div>
    <div><h3>{t("30 días", "30 days")}</h3><p>{t("Abierta al público todo septiembre, con premio a la mejor instalación.", "Open to the public all September, with an award for the best installation.")}</p></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("En prensa", "In the press")}</h2>{btn(t("Toda la prensa", "All press"), u("archivo", "prensa"))}</div>
  <div class="rows">{press}</div>
</div></section>

<section class="section--s"><div class="wrap">{rail(t("Archivo", "Archive"), cards, btn(t("Todo el archivo", "Full archive"), u("archivo")))}</div></section>

<section class="section bg-ink">
  <div class="wrap two-col" style="align-items:end">
    <h2 class="d d-l rv">{t('La primera edición fue la semilla. <span class="it">La segunda</span> ya se está dibujando.', 'The first edition was the seed. <span class="it">The second</span> is already on the drawing board.')}</h2>
    <div class="rv"><p class="lead">{t("Lab del 20 al 31 de agosto e instalaciones durante todo septiembre de 2027. Del resto, te enteras antes que nadie.", "Lab from 20 to 31 August and installations throughout September 2027. You'll hear the rest first.")}</p>{news_form(t("¡Hecho! Te escribiremos cuando haya noticias de 2027.", "Done! We'll write when there's news about 2027."), "h")}</div>
  </div>
</section>
'''
    page("index", t("Inicio", "Home"), t("EFÍMERA CÓRDOBA: festival internacional de arquitectura efímera, creación contemporánea y ciudadanía en el casco histórico de Córdoba.",
                                          "EFÍMERA CÓRDOBA: international festival of ephemeral architecture, contemporary creation and citizenship in the historic centre of Córdoba."), "home", body, show_partners=True)


# ---------------------------------------------------------------------------
# FESTIVAL
# ---------------------------------------------------------------------------
def festival():
    faq = "".join(f'<details><summary>{T(q)}<span class="pm" aria-hidden="true">+</span></summary><div class="ans">{T(a)}</div></details>' for q, a in FAQ)
    body = f'''
<section class="block page-hero"><div class="wrap">
  <div class="eyebrow label"><a href="{u("index")}">{t("Inicio", "Home")}</a> <span aria-hidden="true">/</span> <span>{t("El festival", "The festival")}</span></div>
  <h1 class="d d-xxl rv">{t("Manifiesto", "Manifesto")}</h1>
  <div class="statement mt-l" style="text-align:left"><p class="d" style="margin:0;max-width:24ch" data-words>{t("Córdoba lleva siglos siendo la misma ciudad. Durante unas semanas, queremos que sea otra.", "Córdoba has been the same city for centuries. For a few weeks, we want it to be another.")}</p></div>
</div></section>

<section class="section"><div class="wrap two-col">
  <div class="prose rv">
    <p class="lead">{t("Creemos que caminar es la mejor manera de entrar en un museo. Que el patrimonio no es un decorado que conservar, sino un lugar desde el que seguir creando. Que una obra puede durar un mes y quedarse en la memoria durante años.", "We believe walking is the best way into a museum. That heritage is not a stage set to preserve, but a place from which to keep creating. That a work can last a month and stay in the memory for years.")}</p>
    <p class="lead">{t("No organizamos eventos: provocamos momentos que solo ocurren una vez. La ciudad es la sala, y el camino entre una obra y la siguiente también forma parte de la obra.", "We don't organise events: we spark moments that only happen once. The city is the gallery, and the walk from one work to the next is part of the work too.")}</p>
  </div>
  <p class="d d-l rv" style="color:var(--almagra)">{t('No vamos a cambiar Córdoba. <span class="it">Vamos a cambiar cómo la miras.</span>', 'We are not going to change Córdoba. <span class="it">We are going to change how you see it.</span>')}</p>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("Cuatro lenguajes", "Four languages")}</h2></div>
  <div class="cols">
    <div class="rv"><span class="k">a.</span><h3>{t("Arquitectura", "Architecture")}</h3><p>{t("Estructuras ligeras, sombras y cubiertas que duran días y cambian para siempre cómo recuerdas un lugar.", "Light structures, shade and canopies that last for days and change forever how you remember a place.")}</p></div>
    <div class="rv"><span class="k">b.</span><h3>{t("Cine", "Film")}</h3><p>{t("Cada obra tiene su pieza audiovisual, que la amplía y la deja archivada.", "Each work has its own film, which expands it and keeps it on record.")}</p></div>
    <div class="rv"><span class="k">c.</span><h3>{t("Arte", "Art")}</h3><p>{t("Música, poesía, danza, fotografía y cocina en conversación con el patrimonio.", "Music, poetry, dance, photography and food in conversation with heritage.")}</p></div>
    <div class="rv"><span class="k">d.</span><h3>{t("Ciudadanía", "Citizenship")}</h3><p>{t("Becas, talleres y actividades abiertas. El festival se completa cuando alguien decide participar.", "Grants, workshops and open activities. The festival is complete when someone decides to take part.")}</p></div>
  </div>
</div></section>

<section class="section bg-cal"><div class="wrap two-col" style="align-items:center">
  <div class="rv"><span class="label">{t("Hilo de 2026", "2026 theme")}</span><h2 class="d d-l mt-s">{t('Sombra, agua y <span class="it">verde</span>.', 'Shade, water and <span class="it">greenery</span>.')}</h2>
    <p class="lead mt-m">{t("La primera edición giró en torno al cuidado frente al cambio climático, con los mismos recursos con los que Córdoba se ha defendido siempre del calor. En las charlas, el río volvió una y otra vez como columna vertebral de la ciudad y como patrimonio inmaterial.", "The first edition revolved around care in the face of climate change, using the same resources Córdoba has always used against the heat. In the talks, the river came up again and again as the city's backbone and as intangible heritage.")}</p></div>
  <figure class="frame rv-blur" style="aspect-ratio:1"><img src="{img('campana/teaser-800.7b4c5ed8.webp')}" alt="{escape(T(CAMPANA[0][1:]))}" loading="lazy"></figure>
</div></section>

<section class="section"><div class="wrap two-col">
  <h2 class="d d-l rv">{t('De dónde <span class="it">viene</span>', 'Where it <span class="it">comes from</span>')}</h2>
  <div class="rv"><p class="lead">{t("EFÍMERA nace de <strong>Córdoba, Ciudad de las Ideas</strong>, el proyecto de la Fundación Artdecor para transformar la ciudad desde sus artistas y su gente. 2026 fue la primera piedra de un camino largo: convertir Córdoba en referente internacional de la intervención contemporánea en el patrimonio.", "EFÍMERA grows out of <strong>Córdoba, Ciudad de las Ideas</strong> (Córdoba, City of Ideas), Fundación Artdecor's project to transform the city through its artists and its people. 2026 was the first stone of a long road: making Córdoba an international reference for contemporary intervention in heritage.")}</p></div>
</div></section>

<section class="section--s" id="equipo"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("El equipo", "The team")}</h2></div>
  <div class="team">
    <article class="member rv"><img src="{img('img/logos/artdecor.ae34de74.png')}" alt="Fundación Artdecor"><span class="label role">{t("Titular y organización", "Owner and organiser")}</span><h3>Fundación Artdecor</h3>
      <p>{t("Nacida en Córdoba a principios de 2020 para transformar la ciudad a través de sus artistas y su cultura, con tres brújulas: ciudadanía, cultura y sostenibilidad.", "Founded in Córdoba in early 2020 to transform the city through its artists and culture, guided by three compasses: citizenship, culture and sustainability.")}</p>
      <div class="foot"><a href="https://www.fundacionartdecor.org" target="_blank" rel="noopener">fundacionartdecor.org ↗</a><a href="https://www.instagram.com/fundacionartdecor/" target="_blank" rel="noopener">@fundacionartdecor ↗</a></div></article>
    <article class="member rv"><img src="{img('img/logos/mudd.6f8b5b97.png')}" alt="MUDD Architects"><span class="label role">{t("Dirección artística · Efímera Lab", "Artistic direction · Efímera Lab")}</span><h3>MUDD Architects</h3>
      <p>{t("Estudio que une tecnología de vanguardia y materiales naturales. Su investigación con drones y tejidos 3D se ha presentado en ACADIA y en los Dezeen Awards.", "A studio combining cutting-edge technology with natural materials. Its research on drones and 3D textiles has been presented at ACADIA and the Dezeen Awards.")}</p>
      <div class="foot"><a href="https://www.muddarchitects.com/" target="_blank" rel="noopener">muddarchitects.com ↗</a><a href="https://www.instagram.com/mudd_architects/" target="_blank" rel="noopener">@mudd_architects ↗</a></div></article>
    <article class="member rv"><img src="{local('assets/logos/aa.svg')}" alt="Architectural Association" style="height:56px;width:auto"><span class="label role">{t("Con", "With")}</span><h3>Architectural Association School of Architecture</h3>
      <p>{t("La AA School de Londres participa a través de su programa de verano: sus estudiantes trabajan en el Efímera Lab junto a participantes locales, nacionales e internacionales.", "London's AA School takes part through its summer programme: its students work at the Efímera Lab alongside local, national and international participants.")}</p>
      <div class="foot"><a href="https://www.aaschool.ac.uk" target="_blank" rel="noopener">aaschool.ac.uk ↗</a></div></article>
    <article class="member member--accent rv"><span class="label role">{t("Comisaria", "Curator")}</span><h3>Nina Chaltiel</h3><p>{t("Cofundadora de MUDD Architects. Dirige el Efímera Lab.", "Co-founder of MUDD Architects. Leads the Efímera Lab.")}</p></article>
    <article class="member member--accent rv"><span class="label role">{t("Comisario", "Curator")}</span><h3>Fernando Vacas</h3><p>{t("Músico y productor (Eureka) y presidente de la Fundación Artdecor. Nominado a los Grammy Latinos; ha trabajado con Rosalía, Estrella Morente o Niño de Elche.", "Musician and producer (Eureka) and president of Fundación Artdecor. Latin Grammy nominee; he has worked with Rosalía, Estrella Morente and Niño de Elche.")}</p></article>
    <article class="member rv"><span class="label role">{t("El escenario", "The setting")}</span><h3>{t("El casco histórico", "The historic centre")}</h3><p>{t("Patrimonio Mundial. Patios, capillas y palacios que abren sus puertas a la creación contemporánea.", "World Heritage. Patios, chapels and palaces that open their doors to contemporary creation.")}</p><div class="foot"><a href="{u("recorrido")}">{t("Ver el recorrido →", "See the route →")}</a></div></article>
  </div>
</div></section>

<section class="section bg-cal" id="preguntas"><div class="wrap two-col">
  <div class="rv"><h2 class="d d-l">{t("Preguntas", "Questions")}</h2><p class="mt-m">{t("¿Falta algo?", "Anything missing?")} <a class="link" href="{u("contacto")}">{t("Escríbenos", "Write to us")}</a></p></div>
  <div class="faq rv">{faq}</div>
</div></section>
'''
    page("festival", t("El festival", "The festival"), t("Manifiesto, lenguajes, origen y equipo de EFÍMERA CÓRDOBA.", "Manifesto, languages, origins and team of EFÍMERA CÓRDOBA."), "festival", body)


# ---------------------------------------------------------------------------
# OBRAS + FICHAS
# ---------------------------------------------------------------------------
def obras():
    rows = "".join(work_row(o) for o in OBRAS)
    body = hero(t("Obras", "Works"), t('Obras <span class="it">2026</span>', 'Works <span class="it">2026</span>'),
                t("Cinco intervenciones en el casco histórico, del 1 al 30 de septiembre de 2026. Todas con entrada libre.", "Five interventions in the historic centre, from 1 to 30 September 2026. All free to enter."), "d-xxl") + f'''
<div class="block">{marquee([(t("Sombra, agua y verde", "Shade, water and greenery"), t("el cuidado frente al cambio climático", "care in the face of climate change"))])}</div>
<section class="section"><div class="wrap">
  <div class="works">{rows}</div>
  <div class="btn-row mt-m rv">{btn(t("Ver en el mapa", "See on the map"), u("recorrido"))}{btn(t("Cómo nacieron: el Lab", "How they were born: the Lab"), u("lab"))}{btn(t("Participa en 2027 como empresa", "Take part in 2027 as a company"), u("patrocinio"))}</div>
</div></section>'''
    page("obras", t("Obras 2026", "Works 2026"), t("Las cinco obras de EFÍMERA CÓRDOBA 2026.", "The five works of EFÍMERA CÓRDOBA 2026."), "obras", body)

    for k, o in enumerate(OBRAS):
        nxt = OBRAS[(k + 1) % len(OBRAS)]
        lat, lng = o["coords"]
        hours = "".join(f"<span style='display:block'>{T(h)}</span>" for h in o["hours"])
        priv = f"<small>{t('Recinto privado: solo se visitaba en este horario.', 'Private venue: open only during these hours.')}</small>" if o["private"] else ""
        text = "".join(f"<p>{T(p)}</p>" for p in o["text"])
        acc_txt = txt(o["color"])
        if o["photos"]:
            ph = o["photos"]

            def b(p):
                a = escape(T((p[1], p[2])))
                return f'<button type="button" data-full="{img(p[0])}" data-alt="{a}" aria-label="{t("Ampliar", "Enlarge")}: {a}"><img src="{img(p[0])}" alt="{a}" loading="lazy"></button>'
            pics = f'<div class="pics" data-gallery>{b(ph[0])}<div class="duo">{b(ph[1])}{b(ph[2])}</div>{b(ph[3])}{b(ph[4])}</div>'
            hero_media = f'<div class="hero-media rv"><img data-zoom src="{img(ph[0][0])}" alt="{escape(T((ph[0][1], ph[0][2])))}"></div>'
        else:
            pics = f'<div class="soon rv"><span class="label">{t("Fotografías", "Photographs")}</span><p class="d d-m mt-s">{t("Las imágenes de esta obra se publicarán muy pronto.", "Images of this work will be published very soon.")}</p><div class="btn-row mt-m">{btn(t("Mientras, en Instagram", "Meanwhile, on Instagram"), IG, ext=True, arrow="↗")}</div></div>'
            hero_media = ""
        en_title = f'<span class="obra-en">{o["title_en"]}</span>' if LANG == "en" else ""
        body = f'''
<section class="block hero" style="padding-bottom:{'0' if hero_media else 'clamp(40px,5vw,80px)'}"><div class="wrap">
  <div class="label" style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:clamp(20px,3vw,44px)"><a href="{u("obras")}">{t("Obras 2026", "Works 2026")}</a><span aria-hidden="true">/</span><span>{o["n"]}</span></div>
  <h1 class="d d-xxl rv"><span lang="es">{o["title"]}</span>{en_title}</h1>
  <p class="sub rv">{o["place"]}</p>
  {hero_media}
</div></section>
<section class="section" style="--acc:{o['color']}"><div class="wrap obra">
  <aside class="rv">
    <dl class="facts">
      <div><dt>{t("Obra", "Work")}</dt><dd>{o["n"]} {t("de", "of")} 05</dd></div>
      <div><dt>{t("Autoría", "Authors")}</dt><dd>{T(o["authors"])}</dd></div>
      <div><dt>{t("Lugar", "Venue")}</dt><dd>{o["place"]}<small>{o["addr"]}, Córdoba</small></dd></div>
      <div><dt>{t("Fechas", "Dates")}</dt><dd>{t("1–30 sept. 2026 · Entrada libre", "1–30 Sept 2026 · Free entry")}{priv}</dd></div>
      <div><dt>{t("Horario", "Opening hours")}</dt><dd>{hours}</dd></div>
    </dl>
    <div class="btn-row mt-m">{btn(t("Abrir en Maps", "Open in Maps"), f"https://www.google.com/maps/search/?api=1&query={lat},{lng}", ext=True, arrow="↗")}{btn(t("Recorrido", "Route"), u("recorrido"))}</div>
  </aside>
  <div class="body rv"><p class="tag">{T(o["tag"])}</p>{text}{pics}</div>
</div></section>
<a class="next" href="{u(nxt["slug"])}" style="--acc:{nxt['color']};--acc-txt:{txt(nxt['color'])}"><div class="wrap"><span class="label">{t("Siguiente obra", "Next work")} · {nxt["n"]}</span><div class="d d-xl mt-s"><span lang="es">{nxt["title"]}</span><span aria-hidden="true">→</span></div></div></a>
'''
        ld = json.dumps({"@context": "https://schema.org", "@type": "ExhibitionEvent", "name": o["title"], "startDate": "2026-09-01", "endDate": "2026-09-30", "inLanguage": LANG,
                         "isAccessibleForFree": True, "location": {"@type": "Place", "name": o["place"], "address": o["addr"] + ", Córdoba",
                         "geo": {"@type": "GeoCoordinates", "latitude": lat, "longitude": lng}}}, ensure_ascii=False)
        page(o["slug"], o["title"], t(f'{o["title"]}, obra {o["n"]} de EFÍMERA CÓRDOBA 2026 en {o["place"]}.', f'{o["title"]} ({o["title_en"]}), work {o["n"]} of EFÍMERA CÓRDOBA 2026 at {o["place"]}.'), "obras", body,
             bloque=o["color"], bloque_txt=acc_txt, head=f'<script type="application/ld+json">{ld}</script>')


# ---------------------------------------------------------------------------
# LAB
# ---------------------------------------------------------------------------
def lab():
    def ini(n):
        p = n.split()
        return (p[0][0] + p[1][0]).upper()
    sp = "".join(f'<div class="rv"><span class="ini">{ini(n)}</span><h3>{n}</h3><p>{T(r)}</p></div>' for n, r in PONENTES)
    body = hero("Lab", 'Efímera <span class="it">Lab</span>',
                t("El taller internacional donde nacen las obras. Diez días, íntegramente en inglés, en el C3A de Córdoba.", "The international workshop where the works are born. Ten days, entirely in English, at the C3A in Córdoba."), "d-xxl",
                f'<p class="label mt-m rv">{t("Próxima edición · 20–31 agosto 2027 · con estudiantes de la AA School", "Next edition · 20–31 August 2027 · with AA School students")}</p><div class="btn-row mt-m rv">{btn(t("Ponentes", "Speakers"), "#ponentes", "btn--light")}{btn("Nuevas Miradas", "#nuevas-miradas", "btn--light")}{btn(t("Colaborar con el Lab", "Partner with the Lab"), "#colabora", "btn--light")}</div>') + f'''
<section class="section"><div class="wrap">
  <div class="stats rv">
    <div><b>10</b><span>{t("días de taller · 20–30 ago.", "workshop days · 20–30 Aug")}</span></div>
    <div><b>3</b><span>{t("becas completas para estudiantes locales", "full grants for local students")}</span></div>
    <div><b>2</b><span>{t("ayudas a la producción", "production grants")}</span></div>
    <div><b>15</b><span>{t("charlas invitadas", "guest talks")}</span></div>
  </div>
</div></section>

<section class="section--s"><div class="wrap two-col">
  <div class="rv"><span class="label">{t("Cómo funciona", "How it works")}</span><h2 class="d d-l mt-s">{t('Prototipos de día, <span class="it">ideas</span> al atardecer.', 'Prototypes by day, <span class="it">ideas</span> at dusk.')}</h2></div>
  <div class="rv">
    <p class="lead">{t("Por la mañana y por la tarde: equipos, materiales, prototipos y revisiones. A mediodía y al caer el sol: charlas invitadas.", "Morning and afternoon: teams, materials, prototypes and reviews. At midday and at sunset: guest talks.")}</p>
    <p>{t("Lo dirige Nina Chaltiel (MUDD Architects) y reúne a participantes locales, nacionales e internacionales con estudiantes de la AA School de Londres. Las becas y ayudas se convocaron del 1 al 15 de julio de 2026: tres becas completas para estudiantes locales y dos ayudas a la producción para artistas, profesionales y colectivos.", "Led by Nina Chaltiel (MUDD Architects), it brings together local, national and international participants with students from London's AA School. Grants were open from 1 to 15 July 2026: three full grants for local students and two production grants for artists, professionals and collectives.")}</p>
  </div>
</div></section>

<section class="section bg-ink"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t("La ciudad como aula", "The city as a classroom")}</h2><p style="opacity:.7">{t("Cuatro sesiones fuera del taller.", "Four sessions outside the workshop.")}</p></div></div>
  <div class="cols">
    <div class="rv"><span class="k">1</span><h3>{t("Distrito UNESCO", "UNESCO district")}</h3><p>{t("Paseo por el casco histórico.", "A walk through the historic centre.")}</p></div>
    <div class="rv"><span class="k">2</span><h3>Plaza de la Fuenseca</h3><p>{t("Paseo de cine con Fernando Vacas.", "A film walk with Fernando Vacas.")}</p></div>
    <div class="rv"><span class="k">3</span><h3>Alcázar Viejo</h3><p>{t("Sesión en el patio con Lola Baena.", "A patio session with Lola Baena.")}</p></div>
    <div class="rv"><span class="k">4</span><h3>{t("Museo de las Aguas", "Water Museum")}</h3><p>{t("Sesión con Luis Celorio.", "A session with Luis Celorio.")}</p></div>
  </div>
</div></section>

<section class="section" id="ponentes"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t("Ponentes", "Speakers")}</h2><p>{t("Quince voces invitadas durante el Lab, en el C3A.", "Fifteen guest voices during the Lab, at the C3A.")}</p></div></div>
  <div class="speakers">{sp}</div>
</div></section>

<section class="section bg-almagra on-color" id="nuevas-miradas"><div class="wrap two-col">
  <div class="rv"><span class="label" style="opacity:.8">{t("Concurso audiovisual", "Film competition")}</span><h2 class="d d-xl mt-s">Nuevas <span class="it">Miradas</span></h2></div>
  <div class="rv">
    <p class="lead">{t("El concurso de cortometrajes de la primera edición, comisariado por Nina Chaltiel y Fernando Vacas. Inscripciones del 13 de julio al 20 de septiembre; premios entregados el 25 de septiembre en la Filmoteca de Andalucía.", "The first edition's short film competition (its name means “New Perspectives”), curated by Nina Chaltiel and Fernando Vacas. Entries from 13 July to 20 September; awards presented on 25 September at the Filmoteca de Andalucía.")}</p>
    <div class="box mt-m" style="border-color:rgba(255,255,255,.4)"><span class="label" style="opacity:.8">{t("Mención de honor", "Honourable mention")}</span><p class="d d-m mt-s" style="margin-bottom:8px">{t("María Isabel Ariza y Lucía Pozuelo", "María Isabel Ariza and Lucía Pozuelo")}</p><p style="margin:0">{t("Estudiantes de Publicidad y Marketing Digital, Universidad Loyola.", "Advertising and Digital Marketing students, Universidad Loyola.")}</p></div>
  </div>
</div></section>

<section class="section" id="colabora"><div class="wrap two-col" style="align-items:end">
  <div class="rv"><span class="label">{t("Universidades, escuelas y empresas", "Universities, schools and companies")}</span>
    <h2 class="d d-l mt-s">{t('El Lab es donde la colaboración <span class="it">se nota</span> antes.', 'The Lab is where partnership <span class="it">shows</span> first.')}</h2></div>
  <div class="rv"><p class="lead">{t("Becas con nombre propio, materiales y tecnología para los prototipos, o una voz en el programa de charlas. En 2026, Keyter Group, Restaurante Amaltea y Teulo ya formaron parte del Lab con sus ponentes.", "Named grants, materials and technology for the prototypes, or a voice in the talks programme. In 2026, Keyter Group, Restaurante Amaltea and Teulo were already part of the Lab through their speakers.")}</p>
    <div class="btn-row mt-m">{btn(t("Convocatoria de empresas", "Brand open call"), u("patrocinio"), "btn--solid")}{btn(t("Convocatorias 2027", "2027 open calls"), u("2027", "convocatorias"))}</div></div>
</div></section>
'''
    page("lab", "Efímera Lab", t("Efímera Lab: taller internacional, becas, ponentes y concurso Nuevas Miradas de EFÍMERA CÓRDOBA 2026.", "Efímera Lab: international workshop, grants, speakers and the Nuevas Miradas film competition of EFÍMERA CÓRDOBA 2026."), "lab", body)


# ---------------------------------------------------------------------------
# PATROCINIO 2027 (v4: modelo marca + artista invitado + espacio)
# ---------------------------------------------------------------------------
SPACES = [
    dict(n="01", img="patios-san-basilio", name="Patio de la Asociación de Amigos de los Patios Cordobeses", short=("Patio de San Basilio", "San Basilio patio"), pos=(155, 420), addr="C/ San Basilio, 44",
         desc=("En pleno barrio de San Basilio, un emblema vivo del patio cordobés: muros encalados, macetas, escaleras de cal y detalles históricos.",
               "In the heart of the San Basilio neighbourhood, a living emblem of the Cordoban patio: whitewashed walls, flowerpots, lime-washed stairs and historic details."),
         was=("En 2026 acogió «Bajo la fresca»", "Hosted “Bajo la fresca” in 2026")),
    dict(n="02", img="capilla-mudejar", name="Capilla Mudéjar de San Bartolomé", short=("Capilla Mudéjar", "Mudéjar Chapel"), pos=(350, 420), addr="Plaza del Cardenal Salazar, s/n",
         desc=("Joya del siglo XIV y uno de los mejores ejemplos de arte mudéjar de Andalucía: yeserías geométricas, azulejos y techumbre de madera.",
               "A 14th-century gem and one of the finest examples of Mudéjar art in Andalusia: geometric plasterwork, glazed tiles and a carved wooden ceiling."),
         was=("En 2026 acogió «Lo que permanece»", "Hosted “Lo que permanece” in 2026")),
    dict(n="03", img="bellas-artes", name="Patio del Museo de Bellas Artes", short=("Patio de Bellas Artes", "Fine Arts patio"), pos=(525, 545), addr="Plaza del Potro, 1",
         desc=("En la plaza del Potro, dentro de un antiguo hospital del siglo XV, une el Museo de Bellas Artes y el Museo Julio Romero de Torres. Naranjos, fuente de piedra y arcadas renacentistas.",
               "On Plaza del Potro, inside a former 15th-century hospital, it links the Museum of Fine Arts and the Julio Romero de Torres Museum. Citrus trees, a stone fountain and Renaissance arcades."),
         was=("En 2026 acogió «Sagrado florecer»", "Hosted “Sagrado florecer” in 2026")),
    dict(n="04", img="casa-de-las-tazas", name="Casa de las Tazas", short=("Casa de las Tazas", "Casa de las Tazas"), pos=(548, 290), addr="Plaza de las Tazas, 11",
         desc=("Patio privado con mucho carácter: debe su nombre a la colección de tazas, platos y cerámica tradicional que adorna sus muros entre flores de colores. Una versión íntima y personal del patio cordobés.",
               "A private courtyard with a distinctive character, named after its collection of ceramic cups, plates and traditional pottery set among colourful flowers. A charming, personal take on the classic Cordoban patio."),
         was=("En 2026 acogió «Esperar a la luz»", "Hosted “Esperar a la luz” in 2026")),
    dict(n="05", img="palacio-angulo", name="Palacio de los Angulo", short=("Palacio de los Angulo", "Palacio de los Angulo"), pos=(190, 160), addr="C/ San Pablo, 31",
         desc=("Casa nobiliaria del siglo XVI en el corazón histórico: portada de piedra con el escudo familiar y un patio-jardín que refleja el prestigio de la aristocracia renacentista.",
               "A 16th-century noble residence in the historic core: a stone doorway bearing the family coat of arms and a garden courtyard that reflects the prestige of the Renaissance aristocracy."),
         was=("En 2026 acogió «Leyendas»", "Hosted “Leyendas” in 2026")),
    dict(n="06", img="palacio-viana", name="Palacio de Viana", short=("Palacio de Viana", "Palacio de Viana"), pos=(372, 100), addr="Plaza de Don Gome, 2",
         desc=("Palacio del siglo XV con doce patios y un jardín, cada uno con su estilo: del renacentista al de los naranjos, un viaje por cinco siglos de patio cordobés.",
               "A 15th-century palace with twelve courtyards and a garden, each in its own style: from Renaissance layouts to orange-tree patios, a journey through five centuries of the Cordoban patio."),
         was=("Nuevo espacio en 2027", "New venue in 2027")),
    dict(n="07", img="c3a", name="C3A · Centro de Creación Contemporánea de Andalucía", short=("C3A", "C3A"), pos=(600, 800), addr="C/ Carmen Olmedo Checa, s/n",
         desc=("Al otro lado del Guadalquivir, en el Parque de Miraflores, el edificio de Nieto Sobejano Arquitectos: grandes naves, muros de hormigón y espacio exterior junto al río para instalaciones de gran escala.",
               "Across the Guadalquivir, in the Parque de Miraflores, the building by Nieto Sobejano Arquitectos: large halls, concrete walls and outdoor space by the river for large-scale installations."),
         was=("En 2026 acogió el Efímera Lab", "Hosted the Efímera Lab in 2026"),
         credit=("Foto: JamesNarmer, Wikimedia Commons, CC BY-SA 4.0", "Photo: JamesNarmer, Wikimedia Commons, CC BY-SA 4.0")),
]


DOSIER = {"es": "efimera-cordoba-2027-dosier-empresas.pdf", "en": "efimera-cordoba-2027-brand-deck.pdf"}

SHIMA = ("Shima Seiki (Wakayama, Japón, 1962) es líder mundial en máquinas de tejido rectilíneo computerizadas. En 1995 presentó WHOLEGARMENT, la tecnología que teje una pieza entera en tres dimensiones y sin costuras, y que hoy se aplica a formas complejas mucho más allá de la moda, como tapicerías e interiores. En EFÍMERA aporta su conocimiento técnico a marcas y artistas para llevar cada instalación de la idea al tejido.",
         "Shima Seiki (Wakayama, Japan, 1962) is a world leader in computerised flat knitting machines. In 1995 it introduced WHOLEGARMENT, the technology that knits an entire piece in three dimensions with no seams, now used for complex forms far beyond fashion, such as upholstery and interiors. At EFÍMERA it shares its technical know-how with brands and artists to take each installation from idea to textile.")

# CIFRAS PROVISIONALES (inventadas a petición del cliente; sustituir por las reales)
STATS_2026 = [(("38.400", "38,400"), ("visitantes en septiembre", "visitors in September")),
              (("3,2 M", "3.2M"), ("visualizaciones en redes", "views on social media")),
              (("64", "64"), ("apariciones en medios", "media mentions")),
              (("40", "40"), ("participantes en el Lab", "Lab participants"))]


def mapa_svg():
    """Mapa ilustrado de los siete espacios (esquemático, a partir del plano del dosier)."""
    F_D, F_S, F_B = "Unbounded, Arial Black, sans-serif", "Instrument Serif, Georgia, serif", "DM Sans, Arial, sans-serif"
    ink, crema, cal, arena, arena_o, arc = C["tinta"], C["crema"], C["cal"], C["arena"], C["arena_osc"], C["arcilla"]
    streets = ["M-10 330 C 140 300, 300 360, 710 250", "M60 40 C 120 260, 90 520, 140 720", "M250 20 C 280 220, 240 520, 300 780",
               "M470 10 C 430 220, 480 420, 420 760", "M-10 560 C 200 520, 420 600, 710 470", "M120 240 C 300 200, 520 260, 690 380",
               "M20 470 C 200 460, 330 300, 610 120"]
    st = "".join(f'<path d="{d}" fill="none" stroke="{arena}" stroke-width="3" stroke-linecap="round" opacity=".7"/>' for d in streets)
    order = ["01", "02", "07", "03", "04", "06", "05"]
    pos = {x["n"]: x["pos"] for x in SPACES}
    route = "M" + " L".join(f"{pos[n][0]} {pos[n][1]}" for n in order)
    hoods = [("SANTA MARINA", 372, 40, "middle"), ("SAN LORENZO", 40, 290, "start"), ("SAN ANDRÉS", 615, 185, "middle"),
             ("LA MAGDALENA", 610, 435, "middle"), ("JUDERÍA", 225, 610, "middle"), ("SAN BASILIO", 110, 525, "middle")]
    hd = "".join(f'<text x="{x}" y="{y}" text-anchor="{a}" font-family="{F_B}" font-size="13" font-weight="700" letter-spacing="3" fill="{C["arena_osc"]}">{h}</text>' for h, x, y, a in hoods)
    pins = ""
    for x in SPACES:
        px, py = x["pos"]
        pins += (f'<g><circle cx="{px}" cy="{py}" r="25" fill="{ink}" stroke="{crema}" stroke-width="5"/>'
                 f'<text x="{px}" y="{py + 5}" text-anchor="middle" font-family="{F_D}" font-size="15" fill="{crema}">{x["n"]}</text>'
                 f'<text x="{px}" y="{py + 50}" text-anchor="middle" font-family="{F_B}" font-size="16" font-weight="700" fill="{ink}" stroke="{cal}" stroke-width="6" paint-order="stroke" stroke-linejoin="round">{T(x["short"])}</text></g>')
    label = t("Mapa de los siete espacios de EFÍMERA CÓRDOBA 2027", "Map of the seven EFÍMERA CÓRDOBA 2027 venues")
    return f'''<svg viewBox="0 0 700 900" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
<rect width="700" height="900" rx="6" fill="{crema}"/>
<path d="M70 110 C 130 30, 430 10, 570 70 C 690 130, 690 420, 645 560 C 600 690, 430 750, 260 735 C 120 720, 40 610, 48 430 C 52 280, 38 190, 70 110 Z" fill="{cal}"/>
{st}
<path d="M-30 880 C 200 850, 380 830, 520 765 S 680 640, 730 600" fill="none" stroke="{arena_o}" stroke-width="58" stroke-linecap="butt"/>
<path d="M-30 880 C 200 850, 380 830, 520 765 S 680 640, 730 600" fill="none" stroke="{arena}" stroke-width="2" stroke-dasharray="2 14" opacity=".9"/>
<text x="230" y="848" transform="rotate(-6 230 848)" font-family="{F_S}" font-style="italic" font-size="22" fill="{crema}">Río Guadalquivir</text>
<line x1="497" y1="728" x2="552" y2="800" stroke="{ink}" stroke-width="9" stroke-linecap="round"/>
<text x="470" y="862" text-anchor="end" font-family="{F_S}" font-style="italic" font-size="19" fill="{ink}">Puente Romano</text>
<g transform="translate(296 650)"><rect width="46" height="34" fill="{arc}"/><path d="M8 34 V18 a6 6 0 0 1 12 0 V34 M26 34 V18 a6 6 0 0 1 12 0 V34" fill="none" stroke="{ink}" stroke-width="2.5"/></g>
<text x="319" y="712" text-anchor="middle" font-family="{F_S}" font-style="italic" font-size="20" fill="{ink}">Mezquita-Catedral</text>
<text x="92" y="770" text-anchor="middle" font-family="{F_S}" font-style="italic" font-size="19" fill="{ink}">Alcázar</text>
{hd}
<path d="{route}" fill="none" stroke="{arc}" stroke-width="3.5" stroke-dasharray="1 10" stroke-linecap="round" stroke-linejoin="round"/>
{pins}
<g transform="translate(652 52)"><path d="M0 -26 L10 6 L0 0 L-10 6 Z" fill="{ink}"/><text y="26" text-anchor="middle" font-family="{F_D}" font-size="14" fill="{ink}">N</text></g>
</svg>'''


def cal2027():
    items = [(t("Hasta el 28 febrero", "Until 28 February"), t("Candidaturas de empresas", "Company applications"), t("Cierre de la convocatoria de empresas: 15 plazas.", "The brand open call closes: 15 places.")),
             (t("Marzo", "March"), t("Selección", "Selection"), t("Comunicamos la resolución a todas las empresas candidatas.", "We let every applicant company know the outcome.")),
             (t("20–31 agosto", "20–31 August"), "Efímera Lab", t("Taller con estudiantes de la AA School de Londres.", "Workshop with students from London's AA School.")),
             (t("1–30 septiembre", "1–30 September"), t("Instalaciones de marcas y artistas", "Brand and artist installations"), t("Abiertas al público en los siete espacios durante todo el mes.", "Open to the public in all seven venues throughout the month.")),
             (t("Finales de septiembre", "Late September"), t("Premio EFÍMERA", "EFÍMERA Award"), t("Fallo del premio a la mejor instalación en la clausura.", "The award for the best installation is announced at the closing.")),
             (t("30 septiembre", "30 September"), t("Desmontaje", "Dismantling"), t("Las instalaciones se retiran y cada patio vuelve a ser patio.", "The installations come down and each patio is a patio again."))]
    return '<ol class="cal-2027">' + "".join(f'<li class="rv"><span class="when">{w} 2027</span><div><h3>{h}</h3><p>{d}</p></div></li>' for w, h, d in items) + "</ol>"


DEADLINE = ("28 de febrero de 2027", "28 February 2027")

DEZEEN = ("Dezeen, la revista online de arquitectura, interiorismo y diseño con sede en Londres, es el socio de prensa de la segunda edición.",
          "Dezeen, the London-based online magazine of architecture, interiors and design, is the media partner of the second edition.")

# Lo que el visitante toca, activa o recorre: el argumento principal para las empresas
SHOWCASE = [(("Materiales", "Materials"), ("Cerámica, textil, madera, piedra, metal, vidrio o nuevos compuestos, a escala de patio.", "Ceramics, textiles, wood, stone, metal, glass or new composites, at the scale of a patio.")),
            (("Tecnología", "Technology"), ("Luz, sonido, agua, clima, sensores o tejido 3D: sistemas que responden a quien entra.", "Light, sound, water, climate, sensors or 3D knitting: systems that respond to whoever walks in.")),
            (("Producto", "Product"), ("Tu producto dentro de la obra, usado y probado por miles de personas durante un mes.", "Your product inside the work, used and tried by thousands of people over a month.")),
            (("Relato", "Story"), ("Una pieza con autor que cuenta quién eres mejor que cualquier anuncio.", "A signed piece that says who you are better than any advert."))]

WAYS = [(("Con tu artista", "With your artist"), ("Trae al artista con el que siempre quisiste trabajar. Nosotros acompañamos el proyecto.", "Bring the artist you've always wanted to work with. We'll support the project.")),
        (("Con un artista que te proponemos", "With an artist we suggest"), ("Si no tienes uno en mente, buscamos artistas afines a tu marca, tu material o tu técnica.", "If you don't have one in mind, we'll find artists who suit your brand, your material or your technique.")),
        (("In-house", "In-house"), ("Tu equipo de diseño, I+D o producto firma la obra. Ideal para enseñar lo que sabéis hacer.", "Your design, R&D or product team signs the work. Ideal for showing what you can do."))]

GUESTS = [("Interioristas", "Interior designers"), ("Arquitectos", "Architects"), ("Propietarios de hoteles", "Hotel owners"), ("Invitados de negocio", "Business guests")]

# PREMIO: borrador inventado a petición del cliente; revisar bases
AWARD = [(("Qué se valora", "What counts"), ("La idea, el diálogo con el espacio, el uso del material o la tecnología y la experiencia del visitante.", "The idea, the dialogue with the venue, the use of material or technology, and the visitor's experience.")),
         (("Quién decide", "Who decides"), ("Un jurado independiente de arquitectura, interiorismo y prensa especializada.", "An independent jury from architecture, interior design and the specialist press.")),
         (("Qué se gana", "The prize"), ("Plaza directa en la edición de 2028 y un lugar destacado en la comunicación del festival.", "A guaranteed place in the 2028 edition and a prominent spot in the festival's communications."))]

INCLUDES = [("Un espacio patrimonial para tu instalación durante todo septiembre de 2027.", "A heritage venue for your installation throughout September 2027."),
            ("Un asistente de producción gratuito que te acompaña en la producción, los permisos y el montaje.", "A free production assistant to support you with production, permits and installation."),
            ("Acompañamiento de la dirección artística y, si lo necesitas, propuesta de artistas.", "Support from the artistic direction and, if you need it, artist suggestions."),
            ("El conocimiento técnico de Shima Seiki en tejido 3D.", "Shima Seiki's technical know-how in 3D knitting."),
            ("Encuentros con la lista de invitados: interioristas, arquitectos y propietarios de hoteles.", "Meetings with the guest list: interior designers, architects and hotel owners."),
            ("Presencia en la comunicación del festival, con Dezeen como socio de prensa.", "A place in the festival's communications, with Dezeen as media partner."),
            ("Opción al Premio EFÍMERA a la mejor instalación.", "Eligibility for the EFÍMERA Award for the best installation.")]


def patrocinio():
    sp = "".join(f'''<article class="rv"><figure><img src="{local('assets/espacios/' + x['img'] + '.webp')}" alt="{escape(x['name'])}" loading="lazy"></figure>
  <div class="txt"><span class="n">{x["n"]}</span><h3>{x["name"]}</h3><p>{T(x["desc"])}</p><span class="was">{T(x["was"])}{(" · " + x["addr"]) if x["addr"] else ""}</span>{('<small class="credit">' + T(x["credit"]) + '</small>') if x.get("credit") else ""}</div></article>''' for x in SPACES)
    cases = [
        ("Keyter Group", t("Empresa · Lab · Confirmada 2027", "Company · Lab · Confirmed 2027"), t("Su Head Manager, Carlos García, fue ponente del Efímera Lab. En 2027 vuelve, esta vez con instalación propia.", "Its Head Manager, Carlos García, spoke at the Efímera Lab. In 2027 it returns, this time with its own installation.")),
        ("Restaurante Amaltea", t("Gastronomía", "Food"), t("Aperitivo en el acústico de apertura del Patio de las Tazas y charla de la chef Raquel Pascual en el Lab.", "Aperitif at the opening acoustic set in the Patio de las Tazas, and a Lab talk by chef Raquel Pascual.")),
        ("Teulo", t("Plataforma · Lab", "Platform · Lab"), t("Su fundadora, Janelle Wynyard, y Hira Wynyard participaron como ponentes del Lab.", "Its founder, Janelle Wynyard, and Hira Wynyard took part as Lab speakers.")),
        ("Universidad Loyola", t("Universidad", "University"), t("Dos de sus estudiantes recibieron la mención de honor de Nuevas Miradas.", "Two of its students received the Nuevas Miradas honourable mention.")),
    ]
    cs = "".join(f'<div class="rv"><span class="label">{r}</span><h3>{n}</h3><p>{p_}</p></div>' for n, r, p_ in cases)
    venues = t("C3A, Filmoteca de Andalucía, Museo de Bellas Artes de Córdoba, Palacio de Viana, Asociación Amigos de los Patios Cordobeses, Universidad de Córdoba y Fundación Kutxabank también acompañaron la primera edición.",
               "C3A, Filmoteca de Andalucía, Museo de Bellas Artes de Córdoba, Palacio de Viana, Asociación Amigos de los Patios Cordobeses, Universidad de Córdoba and Fundación Kutxabank also supported the first edition.")
    places = "".join(f'<label><input type="checkbox" name="espacio" value="{x["n"]}"> {T(x["short"])}</label>' for x in SPACES) + f'<label><input type="checkbox" name="espacio" value="0"> {t("Sin preferencia", "No preference")}</label>'
    focus = "".join(f'<label><input type="checkbox" name="destacar" value="{i}"> {T(h)}</label>' for i, (h, _) in enumerate(SHOWCASE))
    how = "".join(f'<label><input type="radio" name="como" value="{v}"{" required" if i == 0 else ""}> {l}</label>' for i, (v, l) in enumerate([
        ("artista", t("Con un artista que ya tenemos", "With an artist we already have")),
        ("matching", t("Proponednos un artista", "Suggest an artist for us")),
        ("inhouse", t("In-house, con nuestro equipo", "In-house, with our own team")),
        ("nose", t("Aún no lo sabemos", "We don't know yet"))]))
    # RENDERS PROVISIONALES: sustituir por los renders de instalaciones grandes cuando lleguen
    rd = "".join(f'<figure class="rv-blur r{i}"><img src="{img(o["photos"][k][0])}" alt="{escape(T((o["photos"][k][1], o["photos"][k][2])))}" loading="lazy"><figcaption>{o["title"]}</figcaption></figure>'
                 for i, (o, k) in enumerate([(OBRAS[1], 1), (OBRAS[0], 0), (OBRAS[2], 0)]))
    ways = "".join(f'<div class="rv"><span class="k">{"abc"[i]}.</span><h3>{T(h)}</h3><p>{T(p_)}</p></div>' for i, (h, p_) in enumerate(WAYS))
    show = "".join(f'<div class="rv"><span class="k">{i + 1:02d}</span><h3>{T(h)}</h3><p>{T(p_)}</p></div>' for i, (h, p_) in enumerate(SHOWCASE))
    award = "".join(f'<div><h3>{T(h)}</h3><p>{T(p_)}</p></div>' for h, p_ in AWARD)
    guests = "".join(f'<li>{T(g)}</li>' for g in GUESTS)
    incl = "".join(f'<li>{T(x)}</li>' for x in INCLUDES)
    body = hero(t("Convocatoria de empresas 2027", "2027 brand open call"), t('Tu marca, un artista, <span class="it">un patio</span>.', 'Your brand, an artist, <span class="it">a patio</span>.'),
                t("Segunda edición, septiembre de 2027. Buscamos empresas que quieran crear una instalación en uno de los siete espacios del festival, con un artista o con su propio equipo. Hay 15 plazas y se cubren por selección.",
                  "Second edition, September 2027. We're looking for companies that want to create an installation in one of the festival's seven venues, with an artist or with their own team. There are 15 places, awarded by selection."), "d-xxl",
                f'<p class="deadline mt-m rv"><span>{t("Candidaturas abiertas", "Applications open")}</span>{t("hasta el", "until")} {T(DEADLINE)} · {t("15 plazas", "15 places")}</p>'
                f'<div class="btn-row mt-m rv">{btn(t("Presentar candidatura", "Apply now"), "#candidatura", "btn--light")}{btn(t("Ver los espacios", "See the venues"), "#espacios", "btn--light")}</div>') + f'''
<div class="block">{marquee([(t("Convocatoria abierta", "Open call"), "✦"), (t("15 plazas", "15 places"), t("hasta el 28.02.2027", "until 28.02.2027"))])}</div>

<section class="section--s"><div class="wrap">
  <div class="confirmed rv"><span class="label">{t("Ya confirmada para 2027", "Already confirmed for 2027")}</span><strong>Keyter Group</strong><p>{t("La primera empresa de la segunda edición. Las otras 14 plazas se deciden por selección.", "The first company of the second edition. The other 14 places are decided by selection.")}</p></div>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t('2026 en <span class="it">cifras</span>', '2026 in <span class="it">numbers</span>')}</h2></div>
  <div class="stats big-stats rv"><!-- CIFRAS PROVISIONALES: editar en STATS_2026 -->{"".join(f'<div><b>{T(n)}</b><span>{T(l)}</span></div>' for n, l in STATS_2026)}</div>
  <div class="stats mt-m rv">
    <div><b>5</b><span>{t("obras en espacios patrimoniales", "works in heritage venues")}</span></div>
    <div><b>30</b><span>{t("días de festival", "festival days")}</span></div>
    <div><b>15</b><span>{t("ponentes en el Lab", "Lab speakers")}</span></div>
    <div><b>{len(COLABORAN)}</b><span>{t("entidades colaboradoras", "supporting organisations")}</span></div>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("Cómo funciona", "How it works")}</h2></div>
  <ol class="steps">
    <li class="rv"><span class="k">01</span><h3>{t("Presenta tu candidatura", "Apply")}</h3><p>{t("Cuéntanos quién sois, qué espacio os interesa y qué queréis enseñar. Hasta el 28 de febrero de 2027.", "Tell us who you are, which venue interests you and what you want to show. Until 28 February 2027.")}</p></li>
    <li class="rv"><span class="k">02</span><h3>{t("Selección", "Selection")}</h3><p>{t("La dirección artística estudia cada propuesta y elige a las empresas participantes: 15 instalaciones en siete espacios.", "The artistic direction reviews every proposal and chooses the participating companies: 15 installations across seven venues.")}</p></li>
    <li class="rv"><span class="k">03</span><h3>{t("Creáis la instalación", "Create the installation")}</h3><p>{t("Con un artista de vuestra elección, con uno que os proponemos o in-house. Un asistente de producción os acompaña, sin coste. Un asistente de producción os acompaña, sin coste.", "With an artist of your choice, one we suggest, or in-house. A production assistant supports you, free of charge. A production assistant supports you, free of charge.")}</p></li>
    <li class="rv"><span class="k">04</span><h3>{t("Septiembre, abierta a todos", "September, open to all")}</h3><p>{t("Del 1 al 30 de septiembre de 2027, con entrada libre. Se desmonta el día 30.", "From 1 to 30 September 2027, free entry. It comes down on the 30th.")}</p></li>
  </ol>
</div></section>

<section class="section bg-ink"><div class="wrap">
  <div class="two-col" style="align-items:end">
    <div class="rv"><span class="label" style="opacity:.7">{t("Tu producto, dentro de la obra", "Your product, inside the work")}</span>
      <h2 class="d d-l mt-s">{t('Aquí tu producto no se mira: <span class="it">se vive</span>.', "Here your product isn't looked at: <span class='it'>it's experienced</span>.")}</h2></div>
    <p class="lead rv">{t("Las instalaciones pueden ser interactivas: quien entra toca el material, activa la tecnología, recorre la pieza por dentro. Es la mejor forma de enseñar de qué es capaz lo que fabricáis.", "Installations can be interactive: visitors touch the material, trigger the technology, walk through the piece. It's the best way to show what your products can do.")}</p>
  </div>
  <div class="cols mt-l">{show}</div>
</div></section>

<section class="section"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t('Piensa en <span class="it">grande</span>.', 'Think <span class="it">big</span>.')}</h2><p>{t("Instalaciones que ocupan un patio entero, cubren una capilla o se recorren por dentro. Algunas ideas para empezar.", "Installations that fill an entire patio, cover a chapel or can be walked through. A few ideas to get you started.")}</p></div></div>
  <div class="renders">{rd}</div>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t('Con un artista o <span class="it">in-house</span>', 'With an artist or <span class="it">in-house</span>')}</h2></div>
  <div class="formats">{ways}</div>
</div></section>

<section class="section bg-cal" id="espacios"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t('Siete <span class="it">espacios</span>', 'Seven <span class="it">venues</span>')}</h2><p>{t("Patios, capillas y palacios del casco histórico, Patrimonio Mundial, y el C3A junto al Guadalquivir. 15 instalaciones repartidas en siete espacios.", "Patios, chapels and palaces in the World Heritage historic centre, plus the C3A by the Guadalquivir. 15 installations across seven venues.")}</p></div></div>
  <div class="map-row rv"><figure class="map-art">{mapa_svg()}<figcaption>{t("Mapa esquemático, no a escala.", "Schematic map, not to scale.")}</figcaption></figure>
    <ol class="map-list">{"".join(f'<li><span class="n">{x["n"]}</span><div><strong>{x["name"]}</strong><small>{x["addr"] or "Córdoba"}</small></div></li>' for x in SPACES)}</ol></div>
  <div class="spaces mt-l">{sp}</div>
</div></section>

<section class="section"><div class="wrap two-col">
  <div class="rv"><span class="label" style="color:var(--almagra)">{t("Agenda profesional", "Professional programme")}</span>
    <h2 class="d d-l mt-s">{t('Tu instalación, ante quien <span class="it">decide</span>.', 'Your installation, in front of those who <span class="it">decide</span>.')}</h2>
    <p class="lead mt-m">{t("Durante septiembre, EFÍMERA invita a Córdoba a una lista de interioristas, arquitectos, propietarios de hoteles e invitados de negocio. Las empresas seleccionadas pueden quedar con ellos y enseñarles su instalación en persona.", "During September, EFÍMERA invites a list of interior designers, architects, hotel owners and business guests to Córdoba. Selected companies can meet them and show them their installation in person.")}</p></div>
  <ul class="guests rv">{guests}</ul>
</div></section>

<section class="section bg-almagra on-color" id="premio"><div class="wrap">
  <div class="two-col" style="align-items:end">
    <div class="rv"><span class="label" style="opacity:.75">{t("Premio EFÍMERA 2027", "EFÍMERA Award 2027")}</span>
      <h2 class="d d-l mt-s">{t('Premio a la mejor <span class="it">instalación</span>.', 'Award for the best <span class="it">installation</span>.')}</h2></div>
    <p class="lead rv">{t("Cada edición, un jurado elige la instalación que mejor ha unido marca, arte y lugar. El fallo se anuncia en la clausura, a finales de septiembre.", "Each edition, a jury chooses the installation that best brings together brand, art and place. The winner is announced at the closing, at the end of September.")}</p>
  </div>
  <div class="reasons rv">{award}</div>
</div></section>

<section class="section"><div class="wrap two-col">
  <div class="rv"><span class="label" style="color:var(--almagra)">{t("Participar", "Taking part")}</span>
    <h2 class="d d-l mt-s">{t('No alquilas un espacio: <span class="it">firmas una obra</span>.', "You don't rent a venue: <span class='it'>you sign a work</span>.")}</h2>
    <p class="lead mt-m">{t("Las empresas seleccionadas no pagan un alquiler. Pagan la oportunidad de crear, con un artista o con su equipo, una instalación en un espacio patrimonial y de presentar su marca ante miles de visitantes y una lista de invitados profesionales.", "Selected companies don't pay rent. They pay for the opportunity to create, with an artist or their own team, an installation in a heritage venue, and to present their brand to thousands of visitors and a list of professional guests.")}</p>
    <p class="mt-m">{t("Las condiciones económicas están en el dosier, que enviamos a las empresas candidatas.", "The financial terms are in the deck, which we send to applicant companies.")}</p>
    <div class="btn-row mt-m">{btn(t("Solicitar dosier", "Request the deck"), "#candidatura", "btn--solid")}</div></div>
  <div class="rv"><span class="label">{t("Qué incluye", "What's included")}</span><ul class="includes mt-s">{incl}</ul></div>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="tech rv"><span class="label">{t("Partner técnico", "Technical partner")}</span><div><h3 class="d d-m">Shima Seiki</h3>
    <p class="mt-s">{T(SHIMA)}</p></div></div>
  <div class="tech mt-m rv"><span class="label">{t("Socio de prensa", "Media partner")}</span><div><h3 class="d d-m">Dezeen</h3>
    <p class="mt-s">{T(DEZEEN)}</p></div></div>
</div></section>

<section class="section bg-ink"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("Calendario 2027", "2027 calendar")}</h2></div>
  {cal2027()}
</div></section>

<section class="section"><div class="wrap statement">
  <span class="label rv">{t("Por qué EFÍMERA", "Why EFÍMERA")}</span>
  <p class="d" data-words>{t("Una obra dura un mes. El recuerdo de quién la hizo posible dura mucho más.", "A work lasts a month. The memory of who made it possible lasts much longer.")}</p>
</div></section>

<section class="section--s"><div class="wrap">
  <div class="cols">
    <div class="rv"><span class="k">a.</span><h3>{t("Patrimonio Mundial", "World Heritage")}</h3><p>{t("Patios, capillas y palacios del casco histórico de Córdoba, declarado por la UNESCO, como escenario.", "Patios, chapels and palaces in Córdoba's UNESCO-listed historic centre as the setting.")}</p></div>
    <div class="rv"><span class="k">b.</span><h3>{t("Arte con nombre propio", "Art with a name")}</h3><p>{t("Tu marca no patrocina un logo: firma una obra, con un artista o con su propio equipo.", "Your brand doesn't sponsor a logo: it signs a work, with an artist or its own team.")}</p></div>
    <div class="rv"><span class="k">c.</span><h3>{t("Público y negocio", "Public and business")}</h3><p>{t("Entrada libre para miles de visitantes y encuentros con interioristas, arquitectos y hoteleros.", "Free entry for thousands of visitors, and meetings with interior designers, architects and hoteliers.")}</p></div>
    <div class="rv"><span class="k">d.</span><h3>{t("Red internacional", "International network")}</h3><p>{t("MUDD Architects, la AA School de Londres, Shima Seiki y Dezeen.", "MUDD Architects, London's AA School, Shima Seiki and Dezeen.")}</p></div>
  </div>
</div></section>

<section class="section bg-cal"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t('Así participaron en <span class="it">2026</span>', 'How companies took part in <span class="it">2026</span>')}</h2><p>{t("Marcas e instituciones que no solo aparecieron: participaron.", "Brands and institutions that didn't just appear: they took part.")}</p></div>{btn(t("Prensa", "Press"), u("archivo", "prensa"))}</div>
  <div class="cases">{cs}</div>
  <p class="mt-m rv">{venues}</p>
</div></section>

<section class="section" id="candidatura"><div class="wrap two-col">
  <div class="rv">
    <span class="label">{t("Candidaturas hasta el", "Applications until")} {T(DEADLINE)}</span>
    <h2 class="d d-l mt-s">{t('Presenta tu <span class="it">candidatura</span>.', 'Submit your <span class="it">application</span>.')}</h2>
    <p class="lead mt-m">{t("15 plazas. Cuéntanos quién sois, qué queréis destacar y qué espacio os interesa. Revisamos cada propuesta y te enviamos el dosier con las condiciones.", "15 places. Tell us who you are, what you want to highlight and which venue interests you. We review every proposal and send you the deck with the terms.")}</p>
    <p class="mt-m">{t("Directo:", "Direct:")} <a class="link" href="mailto:{MAIL}">{MAIL}</a></p>
  </div>
  <form class="form rv" data-form data-ok="{t("Gracias. Hemos recibido tu candidatura: te enviamos el dosier y te escribimos muy pronto.", "Thank you. We've received your application: we'll send you the deck and be in touch very soon.")} ({note()})" novalidate>
    <div class="two"><div class="field"><label for="s1">{t("Nombre", "Name")}</label><input id="s1" required autocomplete="name"></div><div class="field"><label for="s2">{t("Empresa o marca", "Company or brand")}</label><input id="s2" required autocomplete="organization"></div></div>
    <div class="two"><div class="field"><label for="s3">Email</label><input id="s3" type="email" required autocomplete="email"></div><div class="field"><label for="s4">{t("Teléfono (opcional)", "Phone (optional)")}</label><input id="s4" type="tel" autocomplete="tel"></div></div>
    <div class="field"><label for="s7">{t("Web de la empresa", "Company website")}</label><input id="s7" type="url" placeholder="https://" autocomplete="url"></div>
    <fieldset class="choices"><legend>{t("¿Qué queréis destacar?", "What do you want to highlight?")}</legend>{focus}</fieldset>
    <fieldset class="choices"><legend>{t("¿Qué espacio os interesa más? Podéis marcar varios.", "Which venue interests you most? Tick as many as you like.")}</legend>{places}</fieldset>
    <fieldset class="choices"><legend>{t("¿Cómo queréis crear la instalación?", "How do you want to create the installation?")}</legend>{how}</fieldset>
    <div class="field"><label for="s5">{t("Artista (si ya lo tenéis)", "Artist (if you have one)")}</label><input id="s5" placeholder="{t("Nombre, web o Instagram", "Name, website or Instagram")}"></div>
    <div class="field"><label for="s6">{t("Vuestra idea", "Your idea")}</label><textarea id="s6" placeholder="{t("Qué os gustaría construir y qué queréis que el visitante viva…", "What you'd like to build and what you want visitors to experience…")}"></textarea></div>
    {privacy_check()}
    {hp()}
    <div><button class="btn btn--solid" type="submit">{t("Enviar candidatura", "Submit application")} <span class="arr" aria-hidden="true">→</span></button></div>
    <p class="form-msg" role="status"></p>
  </form>
</div></section>
'''
    page("patrocinio", t("Convocatoria de empresas 2027", "2027 brand open call"), t("Convocatoria de empresas EFÍMERA CÓRDOBA 2027: crea, con un artista o con tu equipo, una instalación en uno de siete espacios de Córdoba en septiembre. 15 plazas; candidaturas hasta el 28 de febrero de 2027.",
                                                                                     "EFÍMERA CÓRDOBA 2027 brand open call: create, with an artist or your own team, an installation in one of seven venues in Córdoba in September. 15 places; applications until 28 February 2027."), "patrocinio", body, show_partners=True)


# ---------------------------------------------------------------------------
# RECORRIDO
# ---------------------------------------------------------------------------
def recorrido():
    stops = "".join(f'<a href="{u(o["slug"])}" data-n="{o["n"]}"><span class="dot-n" style="background:{o["color"]};color:{txt(o["color"])}">{o["n"]}</span><span><strong lang="es">{o["title"]}</strong><small>{o["place"]}</small></span><span aria-hidden="true">→</span></a>' for o in OBRAS)
    rows = "".join(f'<tr><td>{o["n"]} · <span lang="es">{o["title"]}</span><small>{o["place"]}<br>{o["addr"]}</small></td><td>{"<br>".join(T(h) for h in o["hours"])}</td><td>{t("Recinto privado: solo en su horario", "Private venue: only during opening hours") if o["private"] else "—"}</td></tr>' for o in OBRAS)
    pts = json.dumps([dict(n=o["n"], title=o["title"], place=o["place"], coords=o["coords"], color=o["color"], txt=txt(o["color"]), url=u(o["slug"]), more=t("Ver la obra →", "See the work →")) for o in OBRAS], ensure_ascii=False)
    walk = sorted(OBRAS, key=lambda o: o["coords"][1])
    route = ("https://www.google.com/maps/dir/?api=1&travelmode=walking&origin=" + ",".join(map(str, walk[0]["coords"])) +
             "&destination=" + ",".join(map(str, walk[-1]["coords"])) + "&waypoints=" + "|".join(",".join(map(str, o["coords"])) for o in walk[1:-1]))
    body = hero(t("Recorrido", "Route"), t("Recorrido", "Route"),
                t("Cinco paradas a pie por el casco histórico. Así se visitaba EFÍMERA en septiembre de 2026.", "Five stops on foot through the historic centre. This is how EFÍMERA was visited in September 2026."), "d-xxl",
                f'<div class="btn-row mt-m rv">{btn(t("Ruta a pie en Google Maps", "Walking route in Google Maps"), route, "btn--light", ext=True, arrow="↗")}</div>') + f'''
<section class="section--s"><div class="map-wrap rv"><div id="map" data-map="{escape(pts)}" role="region" aria-label="{t("Mapa de las cinco obras", "Map of the five works")}"></div><nav class="stops" aria-label="{t("Paradas", "Stops")}">{stops}</nav></div></section>
<section class="section"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t("Horarios", "Opening hours")}</h2><p>{t("Entrada libre en todos los espacios, del 1 al 30 de septiembre de 2026. Cada uno abría con su propio horario.", "Free entry at every venue, from 1 to 30 September 2026. Each one had its own opening hours.")}</p></div></div>
  <div class="scroll-x rv"><table class="hours"><thead><tr><th>{t("Obra", "Work")}</th><th>{t("Horario", "Hours")}</th><th>{t("Acceso", "Access")}</th></tr></thead><tbody>{rows}</tbody></table></div>
  <p class="note mt-m">{t("Se conserva como archivo: horarios y lugares corresponden a la edición 2026.", "Kept as an archive: hours and venues refer to the 2026 edition.")}</p>
</div></section>'''
    page("recorrido", t("Recorrido", "Route"), t("Mapa, paradas y horarios del recorrido de EFÍMERA CÓRDOBA 2026.", "Map, stops and opening hours of the EFÍMERA CÓRDOBA 2026 route."), "recorrido", body,
         head='<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" crossorigin="">',
         foot='<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" crossorigin=""></script>')


# ---------------------------------------------------------------------------
# ARCHIVO
# ---------------------------------------------------------------------------
def archivo():
    ag = "".join(f'<li class="rv"><span class="day">{T(d)}</span><span class="h">{h}</span><div><h3>{T(ti)}</h3><p>{T(p)}</p>{f"<span class=tag>{T(tag)}</span>" if tag else ""}</div></li>' for d, h, ti, p, tag in TRAYECTO)
    mos = "".join(f'<button type="button" data-full="{img(p)}" data-alt="{escape(T((a, e)))}" aria-label="{t("Ampliar", "Enlarge")}: {escape(T((a, e)))}"><img src="{img(p)}" alt="{escape(T((a, e)))}" loading="lazy"></button>' for p, a, e in CAMPANA[:6])
    press = "".join(prensa_row(*p) for p in PRENSA)
    body = hero(t("Archivo", "Archive"), t("Archivo", "Archive"),
                t("Todo lo que pasó en la primera edición, de la convocatoria a la fiesta de despedida.", "Everything that happened in the first edition, from the open call to the farewell party."), "d-xxl") + f'''
<section class="section"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t('2026, <span class="it">mes a mes</span>', '2026, <span class="it">month by month</span>')}</h2></div>
  <ol class="timeline">
    <li class="rv"><span class="when">{t("1–15 julio", "1–15 July")}</span><div><h3>{t("Becas y ayudas", "Grants")}</h3><p>{t("Tres becas completas para estudiantes locales y dos ayudas a la producción.", "Three full grants for local students and two production grants.")}</p></div></li>
    <li class="rv"><span class="when">{t("13 julio", "13 July")}</span><div><h3>{t("Abre Nuevas Miradas", "Nuevas Miradas opens")}</h3><p>{t("Inscripciones al concurso audiovisual, hasta el 20 de septiembre.", "Entries to the film competition, until 20 September.")}</p></div></li>
    <li class="rv"><span class="when">{t("20–30 agosto", "20–30 August")}</span><div><h3>Efímera Lab</h3><p>{t("Diez días de taller internacional en el C3A.", "Ten days of international workshop at the C3A.")} <a class="link" href="{u("lab")}">{t("Ver el Lab", "See the Lab")}</a></p></div></li>
    <li class="rv"><span class="when">{t("1–30 septiembre", "1–30 September")}</span><div><h3>{t("Las cinco obras", "The five works")}</h3><p>{t("Abiertas al público con entrada libre.", "Open to the public, free of charge.")} <a class="link" href="{u("obras")}">{t("Ver las obras", "See the works")}</a></p></div></li>
    <li class="rv"><span class="when">{t("24–27 septiembre", "24–27 September")}</span><div><h3>Último Trayecto</h3><p>{t("La semana de despedida: música, poesía, danza, cine y fiesta.", "The farewell week: music, poetry, dance, film and a party.")}</p></div></li>
  </ol>
</div></section>

<section class="section bg-ink" id="ultimo-trayecto"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-xl">Último <span class="it">Trayecto</span></h2><p style="opacity:.7">{t("24–27 de septiembre. Entrada libre hasta completar aforo.", "24–27 September. Free entry until full capacity. (The name means “Last Stretch”.)")}</p></div></div>
  <ol class="agenda">{ag}</ol>
</div></section>

<section class="section" id="campana"><div class="wrap">
  <div class="head rv"><div><h2 class="d d-l">{t("Campaña gráfica", "Graphic campaign")}</h2><p>{t("Torres, patios, burbujas y pérgolas: la imagen de la edición 2026.", "Towers, patios, bubbles and pergolas: the look of the 2026 edition.")}</p></div>{btn("@efimera_fest", IG, ext=True, arrow="↗")}</div>
  <div class="mosaic rv" data-gallery>{mos}</div>
</div></section>

<section class="section bg-cal" id="prensa"><div class="wrap">
  <div class="head rv"><h2 class="d d-l">{t("En prensa", "In the press")}</h2></div>
  <div class="rows">{press}</div>
  <div class="two-col mt-l">
    <div class="box rv" style="background:#fff"><span class="label" style="color:var(--almagra)">Media kit</span><h3 class="d d-m mt-s">{t("Logos, fotos con créditos y dossier", "Logos, credited photos and press pack")}</h3>
      <p class="mt-s">{t("Estará disponible muy pronto. Mientras tanto, pídenoslo y te lo enviamos.", "Coming very soon. In the meantime, ask us and we'll send it over.")}</p><p class="note" style="margin:0">{t("Cita siempre la autoría de cada obra y el crédito de cada fotografía.", "Always credit the authors of each work and the photographer of each image.")}</p></div>
    <form class="form rv" data-form data-ok="{t("Recibido. Te respondemos lo antes posible.", "Received. We'll reply as soon as possible.")} ({note()})" novalidate>
      <h3 class="d d-m">{t("Solicitud de prensa", "Press request")}</h3>
      <div class="two"><div class="field"><label for="p1">{t("Nombre", "Name")}</label><input id="p1" required autocomplete="name"></div><div class="field"><label for="p2">Email</label><input id="p2" type="email" required autocomplete="email"></div></div>
      <div class="field"><label for="p3">{t("Medio", "Media outlet")}</label><input id="p3" required></div>
      <div class="field"><label for="p4">{t("Qué necesitas", "What you need")}</label><textarea id="p4" required placeholder="{t("Entrevista, imágenes, acreditación…", "Interview, images, accreditation…")}"></textarea></div>
      {privacy_check()}
      {hp()}
      <div><button class="btn btn--solid" type="submit">{t("Enviar", "Send")} <span class="arr" aria-hidden="true">→</span></button></div>
      <p class="form-msg" role="status"></p>
    </form>
  </div>
</div></section>'''
    page("archivo", t("Archivo", "Archive"), t("Archivo de la primera edición de EFÍMERA CÓRDOBA: cronología, Último Trayecto, campaña gráfica y prensa.", "Archive of the first edition of EFÍMERA CÓRDOBA: timeline, Último Trayecto, graphic campaign and press."), "archivo", body)


# ---------------------------------------------------------------------------
# 2027
# ---------------------------------------------------------------------------
def y2027():
    calls = "".join(f'<div class="rv"><h3>{c}</h3><span class="pill">{t("Próximamente", "Coming soon")}</span></div>' for c in [t("Becas para estudiantes", "Student grants"), t("Ayudas a la producción", "Production grants"), "Efímera Lab", t("Concurso audiovisual", "Film competition")])
    body = hero("2027", "2027", t("Segunda edición: Efímera Lab del 20 al 31 de agosto e instalaciones de marcas y artistas en siete espacios durante todo septiembre.", "Second edition: Efímera Lab from 20 to 31 August, and installations by brands and artists in seven venues throughout September."), "d-xxl") + f'''
<div class="block">{marquee([(t("20–31 agosto", "20–31 August"), "Efímera Lab"), (t("1–30 septiembre", "1–30 September"), t("instalaciones", "installations"))])}</div>
<section class="section"><div class="wrap two-col">
  <div class="rv"><h2 class="d d-l">{t('Entérate <span class="it">antes</span> que nadie.', 'Hear it <span class="it">first</span>.')}</h2><p class="lead mt-m">{t("Te escribiremos solo cuando haya algo que contar: hilo conductor, artistas y apertura de convocatorias.", "We'll only write when there's something to tell: theme, artists and open calls.")}</p></div>
  <form class="form rv" data-form data-ok="{t("¡Hecho! Te avisaremos de todo lo que pase en 2027.", "Done! We'll keep you posted on everything about 2027.")} ({note()})" novalidate>
    <div class="field"><label for="e27">{t("Tu email", "Your email")}</label><input id="e27" type="email" required autocomplete="email"></div>
    <label class="check"><input type="checkbox" required> <span>{t("Quiero recibir novedades de EFÍMERA CÓRDOBA por email.", "I want to receive EFÍMERA CÓRDOBA news by email.")}</span></label>
    {privacy_check()}
    {hp()}
    <div><button class="btn btn--solid" type="submit">{t("Suscribirme", "Subscribe")} <span class="arr" aria-hidden="true">→</span></button></div>
    <p class="form-msg" role="status"></p>
  </form>
</div></section>
<section class="section--s"><div class="wrap"><div class="head rv"><h2 class="d d-l">{t("Calendario", "Calendar")}</h2></div>{cal2027()}</div></section>
<section class="section--s" id="convocatorias"><div class="wrap"><div class="head rv"><h2 class="d d-l">{t("Convocatorias", "Open calls")}</h2></div><div class="calls">{calls}</div></div></section>
<section class="section bg-almagra on-color mt-l"><div class="wrap two-col" style="align-items:end">
  <h2 class="d d-l rv">{t('¿Tu empresa, institución o espacio quiere <span class="it">formar parte</span>?', 'Does your company, institution or venue want to <span class="it">be part of it</span>?')}</h2>
  <div class="rv"><p class="lead">{t("Convocatoria de empresas: 15 plazas en siete espacios. Candidaturas hasta el 28 de febrero de 2027.", "Brand open call: 15 places across seven venues. Applications until 28 February 2027.")}</p><div class="btn-row mt-m">{btn(t("Ver la convocatoria", "See the open call"), u("patrocinio"), "btn--light")}</div></div>
</div></section>'''
    page("2027", "2027", t("EFÍMERA CÓRDOBA prepara su segunda edición. Suscríbete para conocer fechas y convocatorias.", "EFÍMERA CÓRDOBA is preparing its second edition. Subscribe to hear about dates and open calls."), "2027", body)


# ---------------------------------------------------------------------------
# CONTACTO
# ---------------------------------------------------------------------------
def contacto():
    opts = [t("Información general", "General information"), t("Convocatoria de empresas 2027", "2027 brand open call"), t("Convocatorias y Efímera Lab", "Open calls and Efímera Lab"),
            t("Propuesta artística", "Artistic proposal"), t("Prensa", "Press"), t("Otro", "Other")]
    body = hero(t("Contacto", "Contact"), t("Hablemos", "Let's talk"), t("Propuestas, candidaturas, convocatorias o simplemente una duda. Te leemos.", "Proposals, applications, open calls or just a question. We're listening."), "d-xxl") + f'''
<section class="section"><div class="wrap two-col">
  <div class="rv">
    <span class="label">{t("Directo", "Direct")}</span>
    <p class="d d-m mt-s"><a class="link" href="mailto:{MAIL}" style="word-break:break-word">{MAIL}</a></p>
    <p><a class="link" href="{IG}" target="_blank" rel="noopener">@efimera_fest ↗</a></p>
    <div class="mt-l"><span class="label">{t("Dónde estamos", "Where we are")}</span>
      <p class="mt-s"><strong>Fundación Artdecor</strong><br>C/ Juramento, 1 · 14002 Córdoba</p>
      <p><strong>MUDD Architects</strong><br>Gallery Building, Carrer de l'Escar, 26 · 08039 Barcelona</p></div>
    <p class="mt-m">{t("¿Eres una empresa?", "Are you a company?")} <a class="link" href="{u("patrocinio", "candidatura")}">{t("Presenta tu candidatura", "Submit your application")}</a></p>
    <p>{t("¿Eres periodista?", "Are you a journalist?")} <a class="link" href="{u("archivo", "prensa")}">{t("Solicitud de prensa", "Press request")}</a></p>
  </div>
  <form class="form rv" data-form data-ok="{t("Gracias por escribir. Te respondemos pronto.", "Thanks for writing. We'll reply soon.")} ({note()})" novalidate>
    <div class="two"><div class="field"><label for="c1">{t("Nombre", "Name")}</label><input id="c1" required autocomplete="name"></div><div class="field"><label for="c2">Email</label><input id="c2" type="email" required autocomplete="email"></div></div>
    <div class="field"><label for="c3">{t("Sobre qué", "About")}</label><select id="c3">{"".join(f"<option>{o}</option>" for o in opts)}</select></div>
    <div class="field"><label for="c4">{t("Mensaje", "Message")}</label><textarea id="c4" required></textarea></div>
    {privacy_check()}
    <label class="check"><input type="checkbox"> <span>{t("Quiero recibir novedades de EFÍMERA CÓRDOBA por email.", "I want to receive EFÍMERA CÓRDOBA news by email.")}</span></label>
    {hp()}
    <div><button class="btn btn--solid" type="submit">{t("Enviar mensaje", "Send message")} <span class="arr" aria-hidden="true">→</span></button></div>
    <p class="form-msg" role="status"></p>
  </form>
</div></section>'''
    page("contacto", t("Contacto", "Contact"), t("Contacta con EFÍMERA CÓRDOBA.", "Get in touch with EFÍMERA CÓRDOBA."), "contacto", body, show_partners=True)


# ---------------------------------------------------------------------------
# LEGALES (contenido jurídico del sitio actual, resumido; EN informativo)
# ---------------------------------------------------------------------------
def legales():
    upd = f'<p class="note mt-l">{t("Última actualización: 27 de octubre de 2026.", "Last updated: 27 October 2026.")}</p>'
    prevail = "" if LANG == "es" else '<p class="note">This English version is provided for information only. In case of discrepancy, the Spanish version prevails.</p>'
    aviso = prevail + t(f'''<h2>Titular</h2><p>En cumplimiento del artículo 10 de la Ley 34/2002 (LSSI-CE), este sitio es titularidad de:</p>
<ul><li><strong>Fundación Artdecor</strong> · CIF G16673691</li><li>C/ Juramento, 1 · 14002 Córdoba</li><li>{MAIL}</li><li>Registro de Fundaciones de Andalucía, n.º [POR CONFIRMAR]</li></ul>
<p>EFÍMERA CÓRDOBA es un proyecto de la Fundación Artdecor, organizado junto a MUDD Architects y la Architectural Association School of Architecture (Londres).</p>
<h2>Objeto</h2><p>Informar sobre el festival, conservar el archivo de sus ediciones y permitir suscribirse a sus novedades y, cuando estén abiertas, participar en sus convocatorias.</p>
<h2>Condiciones de uso</h2><p>Al navegar aceptas usar el sitio de forma lícita y sin dañar su funcionamiento ni derechos de terceros. La Fundación puede modificar contenidos y condiciones en cualquier momento.</p>
<h2>Propiedad intelectual</h2><p>Textos, diseño, logotipos y código pertenecen a la Fundación Artdecor o a sus titulares. Las obras, sus imágenes y piezas audiovisuales pertenecen a sus autoras y autores y a sus fotógrafas y fotógrafos. Puedes compartir los contenidos citando fuente y autoría; cualquier otro uso, especialmente comercial, requiere autorización previa por escrito.</p>
<h2>Responsabilidad</h2><p>La Fundación procura que la información sea correcta, pero no garantiza la ausencia de errores ni responde de daños derivados de su uso o de interrupciones del servicio. Horarios y lugares de ediciones pasadas se conservan como archivo.</p>
<h2>Enlaces externos</h2><p>El sitio enlaza con webs y redes de terceros, como Instagram, de cuyos contenidos y políticas no se responsabiliza.</p>
<h2>Legislación</h2><p>Se rige por la legislación española; para cualquier controversia, juzgados y tribunales de Córdoba, salvo que la normativa de consumidores disponga otra cosa.</p>''',
                            f'''<h2>Owner</h2><p>In accordance with article 10 of Spanish Law 34/2002 (LSSI-CE), this site is owned by:</p>
<ul><li><strong>Fundación Artdecor</strong> · Tax ID G16673691</li><li>C/ Juramento, 1 · 14002 Córdoba, Spain</li><li>{MAIL}</li><li>Andalusian Registry of Foundations, no. [TO BE CONFIRMED]</li></ul>
<p>EFÍMERA CÓRDOBA is a project of Fundación Artdecor, organised with MUDD Architects and the Architectural Association School of Architecture (London).</p>
<h2>Purpose</h2><p>To provide information about the festival, keep the archive of its editions and allow you to subscribe to its news and, when open, to apply to its calls.</p>
<h2>Terms of use</h2><p>By browsing, you agree to use the site lawfully and without harming its operation or the rights of third parties. The Foundation may change content and terms at any time.</p>
<h2>Intellectual property</h2><p>Texts, design, logos and code belong to Fundación Artdecor or their owners. The works, their images and films belong to their authors and photographers. You may share content citing source and authorship; any other use, especially commercial, requires prior written permission.</p>
<h2>Liability</h2><p>The Foundation strives to keep information accurate but does not guarantee it is error-free and is not liable for damages arising from its use or from service interruptions. Hours and venues of past editions are kept as an archive.</p>
<h2>External links</h2><p>The site links to third-party websites and networks, such as Instagram, whose content and policies are not its responsibility.</p>
<h2>Governing law</h2><p>Spanish law applies; any dispute falls under the courts of Córdoba, unless consumer law provides otherwise.</p>''') + upd
    priv = prevail + t(f'''<p class="lead">Qué datos recogemos, para qué y qué derechos tienes, conforme al RGPD (UE) 2016/679 y la LOPDGDD 3/2018.</p>
<h2>Responsable</h2><ul><li>Fundación Artdecor · CIF G16673691</li><li>C/ Juramento, 1 · 14002 Córdoba</li><li>{MAIL}</li></ul>
<h2>Datos y finalidades</h2><div class="scroll-x"><table><thead><tr><th>Tratamiento</th><th>Datos</th><th>Finalidad</th><th>Base legal</th><th>Conservación</th></tr></thead><tbody>
<tr><td>Novedades</td><td>Email, fecha e IP de alta y confirmación</td><td>Informarte sobre EFÍMERA CÓRDOBA</td><td>Consentimiento (6.1.a), doble opt-in</td><td>Hasta la baja</td></tr>
<tr><td>Convocatorias</td><td>Los que pida cada convocatoria</td><td>Gestionar tu candidatura</td><td>Ejecución de las bases (6.1.b)</td><td>Según bases y plazos legales</td></tr>
<tr><td>Contacto y candidaturas</td><td>Nombre, empresa, email, teléfono y mensaje</td><td>Responderte y enviarte información</td><td>Consentimiento (6.1.a)</td><td>Lo necesario para atenderte</td></tr>
<tr><td>Analítica</td><td>Navegación agregada</td><td>Saber cómo se usa la web</td><td>Consentimiento (6.1.a)</td><td>Ver <a href="{u("cookies")}">cookies</a></td></tr></tbody></table></div>
<p>No tomamos decisiones automatizadas ni elaboramos perfiles.</p>
<h2>Destinatarios</h2><p>No cedemos datos salvo obligación legal. Encargados de tratamiento: alojamiento y correo, STRATO GmbH (Alemania, UE); analítica, solo si la aceptas, Google Ireland Ltd., con posibles transferencias a EE. UU. amparadas en el Marco de Privacidad de Datos UE-EE. UU.</p>
<h2>Derechos</h2><p>Acceso, rectificación, supresión, oposición, limitación, portabilidad y retirada del consentimiento en {MAIL}. Cada email incluye un enlace de baja. Puedes reclamar ante la AEPD (<a href="https://www.aepd.es" target="_blank" rel="noopener">aepd.es</a>).</p>
<h2>Menores</h2><p>Las convocatorias para estudiantes indicarán la edad mínima y, si procede, la autorización de madres, padres o tutores.</p>''',
                           f'''<p class="lead">What data we collect, why, and what your rights are, under the GDPR (EU) 2016/679 and Spanish Organic Law 3/2018 (LOPDGDD).</p>
<h2>Controller</h2><ul><li>Fundación Artdecor · Tax ID G16673691</li><li>C/ Juramento, 1 · 14002 Córdoba, Spain</li><li>{MAIL}</li></ul>
<h2>Data and purposes</h2><div class="scroll-x"><table><thead><tr><th>Processing</th><th>Data</th><th>Purpose</th><th>Legal basis</th><th>Retention</th></tr></thead><tbody>
<tr><td>News</td><td>Email, sign-up and confirmation date and IP</td><td>Keeping you informed about EFÍMERA CÓRDOBA</td><td>Consent (6.1.a), double opt-in</td><td>Until you unsubscribe</td></tr>
<tr><td>Open calls</td><td>Whatever each call requires</td><td>Managing your application</td><td>Performance of the call's rules (6.1.b)</td><td>As per the rules and legal deadlines</td></tr>
<tr><td>Contact and applications</td><td>Name, company, email, phone and message</td><td>Replying and sending you information</td><td>Consent (6.1.a)</td><td>As long as needed to assist you</td></tr>
<tr><td>Analytics</td><td>Aggregated browsing</td><td>Understanding how the site is used</td><td>Consent (6.1.a)</td><td>See <a href="{u("cookies")}">cookies</a></td></tr></tbody></table></div>
<p>We do not make automated decisions or build profiles.</p>
<h2>Recipients</h2><p>We do not share data unless legally required. Processors: hosting and email, STRATO GmbH (Germany, EU); analytics, only if you accept it, Google Ireland Ltd., with possible transfers to the US covered by the EU-US Data Privacy Framework.</p>
<h2>Your rights</h2><p>Access, rectification, erasure, objection, restriction, portability and withdrawal of consent at {MAIL}. Every email includes an unsubscribe link. You may lodge a complaint with the Spanish Data Protection Agency (<a href="https://www.aepd.es" target="_blank" rel="noopener">aepd.es</a>).</p>
<h2>Minors</h2><p>Calls for students will state the minimum age and, where applicable, the need for parental or guardian consent.</p>''') + upd
    ck = prevail + t('''<p class="lead">Qué cookies usamos, conforme al artículo 22.2 de la LSSI-CE y las guías de la AEPD.</p>
<h2>Tu elección</h2><p>Aceptar, Rechazar y Configurar pesan lo mismo. Si rechazas, no se carga nada de Google. Puedes cambiarlo cuando quieras:</p>
<p><button class="btn" type="button" data-cookies-open>Configurar cookies</button></p>
<h2>Cookies</h2><div class="scroll-x"><table><thead><tr><th>Cookie</th><th>Titular</th><th>Tipo</th><th>Finalidad</th><th>Duración</th></tr></thead><tbody>
<tr><td>efm_consent</td><td>Propia</td><td>Necesaria</td><td>Guardar tu elección</td><td>12 meses</td></tr>
<tr><td>_ga</td><td>Google (GA4)</td><td>Analítica</td><td>Distinguir visitantes de forma anónima</td><td>24 meses</td></tr>
<tr><td>_ga_*</td><td>Google (GA4)</td><td>Analítica</td><td>Mantener la sesión</td><td>24 meses</td></tr></tbody></table></div>
<p>La analítica solo se activa si la aceptas (Modo de consentimiento v2). No usamos cookies de publicidad.</p>
<h2>Mapa y vídeo</h2><p>El mapa usa teselas de OpenStreetMap, que no instalan cookies. El vídeo de portada se sirve desde el propio sitio.</p>
<h2>Navegador</h2><p>También puedes bloquear o borrar cookies desde tu navegador; si bloqueas las necesarias, te volveremos a preguntar en cada visita.</p>''',
                         '''<p class="lead">Which cookies we use, under article 22.2 of the LSSI-CE and the Spanish Data Protection Agency's guidelines.</p>
<h2>Your choice</h2><p>Accept, Reject and Settings carry equal weight. If you reject, nothing from Google is loaded. You can change it at any time:</p>
<p><button class="btn" type="button" data-cookies-open>Cookie settings</button></p>
<h2>Cookies</h2><div class="scroll-x"><table><thead><tr><th>Cookie</th><th>Owner</th><th>Type</th><th>Purpose</th><th>Duration</th></tr></thead><tbody>
<tr><td>efm_consent</td><td>First party</td><td>Necessary</td><td>Store your choice</td><td>12 months</td></tr>
<tr><td>_ga</td><td>Google (GA4)</td><td>Analytics</td><td>Distinguish visitors anonymously</td><td>24 months</td></tr>
<tr><td>_ga_*</td><td>Google (GA4)</td><td>Analytics</td><td>Keep the session</td><td>24 months</td></tr></tbody></table></div>
<p>Analytics is only activated if you accept it (Consent Mode v2). We do not use advertising cookies.</p>
<h2>Map and video</h2><p>The map uses OpenStreetMap tiles, which set no cookies. The homepage video is served from the site itself.</p>
<h2>Browser</h2><p>You can also block or delete cookies in your browser; if you block the necessary ones, we will ask you again on every visit.</p>''') + upd
    for key, ti, c in [("aviso-legal", t("Aviso legal", "Legal notice"), aviso), ("privacidad", t("Privacidad", "Privacy"), priv), ("cookies", "Cookies", ck)]:
        page(key, ti, f"{ti} · EFÍMERA CÓRDOBA.", "", hero(ti, ti, "", "d-xl") +
             f'<section class="section--s"><div class="wrap legal">{c}</div></section>', bloque=C["cal"], bloque_txt=C["tinta"])


def build_all():
    global LANG
    for LANG in ("es", "en"):
        home(); festival(); obras(); lab(); patrocinio(); recorrido(); archivo(); y2027(); contacto(); legales()


if __name__ == "__main__":
    build_all()
