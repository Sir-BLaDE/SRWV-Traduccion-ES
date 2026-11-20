# Super Robot Wars V — Traducción al español (España) · pre-release 0.9

Parche **no oficial** de aficionados que traduce al español de España la versión de **Steam** de *Super Robot Wars V*.
Nombres y ataques siguen el doblaje de España cuando existe; si no, traducción propia o de fansub
(p. ej. «gamilas», «Mobile Suit»).

> ⚠️ **Pre-release 0.9**: jugable, pero aún con detalles pendientes (ver abajo). Haz copia de tus partidas.
> Necesitas tu propia copia legal del juego. No se redistribuye ningún fichero del juego: el parche son
> diferencias binarias (zstd) que solo se aplican sobre los ficheros originales de Steam.

## Qué está traducido
- Menús, ayudas, intermisión y pantallas de nivel (SysText, LayoutData, LayoutImage, KPACK, TPACKWIN).
- HUD de combate, rótulos gráficos y títulos de la intro (CMN00, OP, effwin).
- Diálogos de todos los escenarios (STGEST) y de los escenarios especiales/DLC (30 paquetes).
- Resúmenes de historia y prólogo, nombres de pilotos/unidades/ataques, comandos espirituales y habilidades.
- Concordancia de género del protagonista (versión masculina/femenina) y de personajes femeninos.

## Instalación
1. Descarga `SRWV-ES_v0.9_parche.zip` desde **Releases** y descomprímelo.
2. Cierra el juego. Con Python 3.8+ ejecuta:
   ```
   python instalar_parche.py "D:\Juegos\Super Robot Wars V"
   ```
   (la ruta es la carpeta donde está `SRWV.EXE`). Si falta el módulo `zstandard`, el script intenta instalarlo con pip.
3. El instalador comprueba que cada fichero sea el original de Steam, guarda una copia en
   `_backup_traduccion_es/` y verifica el resultado con SHA-256.
4. Para volver al original: `python instalar_parche.py "<ruta>" --restaurar`.

Ficheros que no coincidan con el original (otra versión, otro parche) se **omiten** y se avisa; nunca se sobrescriben a ciegas.
`LT00_EN.cpk` es la excepción: no disponíamos del original para generar la diferencia, así que se sustituye entero (el instalador hace copia antes).

## Limitaciones conocidas (0.9)
- Quedan algunos gráficos de combate y rótulos sueltos en inglés; los títulos de series («Traje móvil …») en la enciclopedia siguen sin pasar a «Mobile Suit» por falta de espacio en el fichero.
- Algunos nombres de piloto van sin tilde por limitaciones de tamaño del archivo `OP.CPK`.
- Frases compartidas entre ramas con género ambiguo pueden quedar en un género; se corrigen según se detectan.
- Probado en una instalación de Steam concreta (PC, 2019 build). No se garantiza compatibilidad con otras ediciones.

## Cómo informar de errores
Abre un *issue* indicando escenario/pantalla, la frase exacta y una captura si es posible.

## Créditos y aviso
Traducción y herramientas: Luis (Sir-BLaDE). Herramientas reutilizables para otros SRW de PC:
[SRW-Translation-Toolkit](https://github.com/Sir-BLaDE/SRW-Translation-Toolkit).
*Super Robot Wars* y todos los personajes, nombres y obras son propiedad de sus respectivos titulares
(Bandai Namco, B.B. Studio, Sunrise y otros). Proyecto sin ánimo de lucro y sin afiliación.
Código bajo licencia MIT.
