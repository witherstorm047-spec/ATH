[app]

# Nome da aplicação no telemóvel
title = ATHENA NEXUS

# Nome do pacote
package.name = athenanexus

# Domínio do pacote
package.domain = org.athena

# Pasta onde está o main.py
source.dir = .

# Ficheiros incluídos no APK
source.include_exts = py,png,jpg,kv,atlas,npz,txt,md

# Versão da aplicação
version = 1.0.0

# Dependências Python compiladas pelo python-for-android
# Nota: usamos pygame-ce (compatível com SDL2/Android) e numpy
requirements = python3,pygame-ce,numpy,pyjnius

# Orientação horizontal (landscape) ideal para o tabuleiro e mesa de bilhar
orientation = landscape

# Ecrã inteiro
fullscreen = 1

# Permissões Android (INTERNET opcional caso queiras ligar a um servidor Ollama externo)
android.permissions = INTERNET,VIBRATE

# Arquiteturas Android modernas (64-bit e 32-bit ARM)
android.archs = arm64-v8a, armeabi-v7a

# Níveis de API Android
android.api = 34
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True

# Bootstrap SDL2 para aplicações Pygame
p4a.bootstrap = sdl2

[buildozer]

# Nível de detalhe do log (2 = detalhado para diagnóstico)
log_level = 2

# Mostrar aviso ao correr como root no GitHub Actions
warn_on_root = 0
