#!/data/data/com.termux/files/usr/bin/bash
# Asistente de ADB inalámbrico para Termux (Android 11+).
#
#   ./termux-adb-pair.sh              empareja y conecta (pregunta IP, puertos y código)
#   ./termux-adb-pair.sh --list       lista dispositivos
#   ./termux-adb-pair.sh --mdns       descubre dispositivos _adb-tls-* en la red
#   ./termux-adb-pair.sh --off        desconecta todo
#   ./termux-adb-pair.sh --connect IP:PUERTO   conecta sin emparejar (ya emparejado)
#
# El puerto de EMPAREJAMIENTO y el de CONEXIÓN son distintos: el primero sale en el
# diálogo "Emparejar dispositivo con código", el segundo en la pantalla principal de
# "Depuración inalámbrica". El de conexión cambia al reiniciar el dispositivo.
set -uo pipefail

if [ -t 1 ]; then C_CYAN=$'\033[1;36m'; C_YELLOW=$'\033[1;33m'; C_RED=$'\033[1;31m'; C_OFF=$'\033[0m'
else C_CYAN=""; C_YELLOW=""; C_RED=""; C_OFF=""; fi
say()  { printf '%s%s%s\n' "$C_CYAN" "$*" "$C_OFF"; }
warn() { printf '%s%s%s\n' "$C_YELLOW" "$*" "$C_OFF" >&2; }
die()  { printf '%s%s%s\n' "$C_RED" "$*" "$C_OFF" >&2; exit 1; }

case "${1:-}" in
  -h|--help)
     sed -n '2,12p' "$0" | sed 's/^# \{0,1\}//'
    exit 0
    ;;
esac

command -v adb >/dev/null 2>&1 || die "adb no está instalado. Ejecuta: pkg install android-tools"

ask() {  # ask <prompt> <default>
  local prompt="$1" def="${2:-}" out
  if [ -n "$def" ]; then
    read -r -p "$prompt [$def]: " out || true
    printf '%s' "${out:-$def}"
  else
    read -r -p "$prompt: " out || true
    printf '%s' "$out"
  fi
}

# IP local del propio móvil (para proponerla como valor por defecto)
local_ip() {
  local ip
  ip=$(ip -4 route get 1.1.1.1 2>/dev/null | grep -oE 'src [0-9.]+' | awk '{print $2}')
  [ -z "$ip" ] && ip=$(ifconfig 2>/dev/null | grep -oE 'inet (192|10|172)\.[0-9.]+' | head -1 | awk '{print $2}')
  printf '%s' "${ip:-127.0.0.1}"
}

case "${1:-}" in
  --list|-l)
    adb devices -l
    exit 0
    ;;
  --mdns)
    say "Buscando dispositivos ADB en la red (10 s)…"
    adb mdns check 2>/dev/null || warn "tu adb no soporta 'mdns check'"
    adb mdns services
    exit 0
    ;;
  --off)
    adb disconnect
    exit 0
    ;;
  --connect)
    [ $# -ge 2 ] || die "uso: $0 --connect IP:PUERTO"
    exec adb connect "$2"
    ;;
  "")
    ;;
  *)
    die "opción desconocida: $1 (usa --help)"
    ;;
esac

DEF_IP="$(local_ip)"
say "== ADB inalámbrico desde Termux =="
echo "  1) En el OTRO dispositivo: Opciones de desarrollador → Depuración inalámbrica →"
echo "     \"Emparejar dispositivo con código\". Mantén ese diálogo abierto"
echo "     (pantalla dividida con Termux para que no se cierre)."
echo

IP=$(ask "IP del dispositivo (localhost si es este mismo teléfono)" "$DEF_IP")
PAIR_PORT=$(ask "Puerto de EMPAREJAMIENTO (el del diálogo)")
CODE=$(ask "Código de 6 dígitos")

say "Emparejando ${IP}:${PAIR_PORT}…"
if ! adb pair "${IP}:${PAIR_PORT}" "${CODE}"; then
  warn "El emparejamiento falló. Causas típicas: el diálogo se cerró,"
  warn "el puerto no es el de emparejamiento, o el código ya caducó."
  exit 1
fi

CONN_PORT=$(ask "Puerto de CONEXIÓN (pantalla principal de Depuración inalámbrica)")
say "Conectando ${IP}:${CONN_PORT}…"
adb connect "${IP}:${CONN_PORT}" || true

sleep 1
echo
say "Dispositivos:"
adb devices -l

if adb devices | grep -q "${IP}:${CONN_PORT}[[:space:]]*device"; then
  say "Listo. Prueba:  adb -s ${IP}:${CONN_PORT} shell"
  if command -v termux-toast >/dev/null 2>&1; then
    termux-toast "ADB conectado a ${IP}" || true
  fi
else
  warn "Conectado pero no aparece como 'device'."
  warn "Si dice 'unauthorized', acepta el diálogo en el otro dispositivo."
  warn "Si dice 'offline', ejecuta: adb kill-server && adb connect ${IP}:${CONN_PORT}"
fi
