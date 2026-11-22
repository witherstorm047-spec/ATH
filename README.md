# ATHENA NEXUS — Versão Android (APK via GitHub Actions)

Este pacote contém o jogo **ATHENA NEXUS** adaptado para ecrãs táteis de telemóvel e pronto a ser compilado automaticamente em **APK** através do **GitHub Actions** (sem precisares de instalar Android Studio ou Linux no teu computador).

## Ficheiros incluídos

- `main.py` — Código principal adaptado para Android (suporte nativo a toque, escalonamento automático para qualquer resolução de telemóvel, barra de botões táteis no topo `MENU / NOVO / VIRAR / VOZ`, gravação de dados na memória privada da app e síntese de voz Android TTS em português).
- `buildozer.spec` — Configuração do Buildozer/python-for-android (`sdl2`, `pygame-ce`, `numpy`, orientação horizontal `landscape`).
- `.github/workflows/build_apk.yml` — Pipeline automática do GitHub Actions que compila o `.apk` na cloud.

## Como gerar o APK pelo GitHub (Passo a Passo)

1. **Cria um repositório novo no GitHub** (ex.: `athena-nexus-mobile`).
2. **Envia todos os ficheiros deste ZIP** para a raiz desse repositório, mantendo a estrutura exata:
   - `main.py`
   - `buildozer.spec`
   - `.github/workflows/build_apk.yml`
3. No GitHub, abre o separador **Actions** do teu repositório.
4. O workflow **Compilar APK Android (ATHENA NEXUS)** arranca automaticamente após o `push` (ou podes clicar em **Run workflow**).
5. Aguarda cerca de **15 a 25 minutos** na primeira compilação (as seguintes demoram ~5 minutos graças à cache).
6. Quando aparecer o visto verde, clica na execução concluída e descarrega o ficheiro em **Artifacts -> ATHENA-NEXUS-APK**.
7. Extrai o `.apk`, envia para o teu telemóvel Android e instala (ativa *"Instalar apps de fontes desconhecidas"* se o telemóvel pedir).
