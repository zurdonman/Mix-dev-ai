# ADB desde el móvil con Termux

Guía para usar **ADB sin PC**: tu teléfono hace de "ordenador" y depura/controla otro
dispositivo Android (u otro perfil del mismo teléfono) por Wi-Fi.

> `sdb` **no** es esto. `sdb` (Smart Development Bridge) es la herramienta de **Tizen**
> (teles Samsung, relojes antiguos), no de Android, y no existe como paquete en Termux.
> Para Android lo que quieres es **adb**.

---

## 1. Instalar Termux (importante: no desde Play Store)

La versión de Play Store está abandonada y rompe `pkg`.

- F-Droid: <https://f-droid.org/packages/com.termux/>
- O releases oficiales: <https://github.com/termux/termux-app/releases>

Abre Termux y actualiza:

```bash
pkg update -y && pkg upgrade -y
```

## 2. Instalar ADB (y fastboot)

```bash
pkg install android-tools -y
adb version
```

`android-tools` trae `adb`, `fastboot` y `mkbootimg` (paquete oficial del equipo de Termux,
versión 37.x). Opcionales útiles:

```bash
pkg install termux-api -y     # para integraciones con el sistema (portapapeles, notificaciones…)
termux-setup-storage         # acceso a ~/storage (para instalar APKs que descargues)
```

## 3. Preparar el dispositivo **destino**

En el móvil/tablet que quieres controlar:

1. Ajustes → Acerca del teléfono → toca **7 veces** "Número de compilación".
2. Ajustes → Sistema → **Opciones de desarrollador**.
3. Activa **Depuración inalámbrica** (Android 11+) y, si vas a usar cable OTG,
   **Depuración USB**.
4. Ambos dispositivos en la **misma red Wi-Fi**.

### 3.1 Emparejar (solo la primera vez, o tras revocar autorizaciones)

En el destino: *Depuración inalámbrica → **Emparejar dispositivo con código***.
Te muestra un **IP:PUERTO de emparejamiento** y un **código de 6 dígitos**.

En Termux (usa pantalla dividida para que el diálogo no se cierre):

```bash
adb pair 192.168.1.50:37419     # IP:puerto DE EMPAREJAMIENTO
# te pedirá el código de 6 dígitos
# -> Successfully paired to 192.168.1.50:37419
```

### 3.2 Conectar

Ojo: el **puerto de conexión es distinto** al de emparejamiento y **cambia al reiniciar**.
Lo ves en la pantalla principal de *Depuración inalámbrica* → "Dirección IP y puerto".

```bash
adb connect 192.168.1.50:41235
adb devices -l
# 192.168.1.50:41235  device  product:... model:... device:...
```

Si es el **mismo teléfono** (depurarte a ti mismo): usa `localhost` en lugar de la IP.

```bash
adb pair localhost:37419
adb connect localhost:41235
```

### 3.3 Alternativa por cable (OTG)

Con un cable USB‑C OTG entre los dos móviles:

```bash
adb devices        # debe listar el otro dispositivo
```

Si sale `unauthorized`, mira la pantalla del destino y acepta "Permitir depuración USB".
Si sale `no permissions`, quita y vuelve a conectar el cable / prueba otro adaptador OTG.

## 4. Script de ayuda

```bash
./scripts/termux-adb-pair.sh            # asistente: empareja y conecta
./scripts/termux-adb-pair.sh --list     # dispositivos conectados
./scripts/termux-adb-pair.sh --mdns     # descubre dispositivos _adb-tls-* en la red
./scripts/termux-adb-pair.sh --off      # desconecta todo
```

## 5. Comandos que más vas a usar

```bash
adb devices -l                        # listar
adb -s 192.168.1.50:41235 shell        # shell en el dispositivo
adb shell pm list packages | grep foo # apps instaladas
adb install -r app.apk                # instalar / actualizar
adb install --user 10 app.apk         # instalar en un perfil concreto (usuario 10)
adb uninstall com.paquete             # desinstalar
adb push fichero /sdcard/Download/    # subir
adb pull /sdcard/Download/x.png .     # bajar
adb logcat -v time | grep -i miproceso
adb shell dumpsys window | grep mCurrentFocus    # actividad en primer plano
adb exec-out screencap -p > pantalla.png         # captura sin romper binario
adb shell input tap 500 1200                     # tocar
adb shell input text "hola"                      # escribir
adb reboot                                        # reiniciar
adb disconnect                                        # cerrar conexiones
adb kill-server && adb start-server                   # reiniciar el daemon
```

## 6. Ver el otro móvil en pantalla (scrcpy)

Si tu repo de Termux tiene `scrcpy` disponible (`pkg search scrcpy`), necesitas además un
servidor X:

```bash
pkg install x11-repo -y
pkg install termux-x11-nightly -y     # + instalar la app Termux:X11 (APK del repo termux/termux-x11)
termux-x11 :0 & 
DISPLAY=:0 GALLIUM_DRIVER=virpipe scrcpy -m 1024 -b 4M
```

Si `scrcpy` no aparece en tu repo, alternativas: **Easycontrol** (app Android que hace de
cliente scrcpy) o usar `adb exec-out screencap` en bucle.

## 7. Problemas típicos

| Síntoma | Causa / solución |
| --- | --- |
| `failed to connect: Connection refused` | El puerto de *conexión* no es el de emparejamiento, o cambió tras reiniciar. Mira la pantalla de Depuración inalámbrica. |
| `adb pair` → `failed: Unable to start pairing client` | El diálogo de emparejamiento se cerró. Usa pantalla dividida y repite rápido. |
| `unauthorized` | Acepta el diálogo en el destino, o revoca autorizaciones en Opciones de desarrollador y vuelve a emparejar. |
| Funciona y a los minutos se corta | Android 12+ mata procesos "fantasma" y con ellos el servidor adb de Termux. Vuelve a `adb connect`. Solución estable requiere root o desactivar el killer (`settings put global settings_enable_monitor_phantom_procs false`). |
| Se conecta pero `adb devices` vacío | Prueba `adb kill-server`, luego `adb connect` de nuevo. |
| Wi-Fi con "aislamiento de clientes" (redes de hotel/universidad) | Los dispositivos no se ven entre sí: usa datos compartidos por hotspot desde el propio móvil. |

## 8. Seguridad

El emparejamiento usa TLS y una clave por dispositivo; las conexiones quedan listadas en
*Depuración inalámbrica → Dispositivos emparejados*. Revócalas cuando termines, y no dejes
la depuración inalámbrica activa en redes públicas: cualquiera que empareje puede ejecutar
comandos como tu usuario.
