name: Compilar APK Android

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Descarregar código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Instalar dependências do sistema e Buildozer
        run: |
          sudo apt-get update
          sudo apt-get install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
          pip3 install --upgrade buildozer cython==0.29.33

      - name: Gerar APK com Buildozer
        run: |
          buildozer -v android debug

      - name: Guardar o APK gerado
        uses: actions/upload-artifact@v4
        with:
          name: meu-aplicativo-apk
          path: bin/*.apk
