# Instalação do Flutter, Dart e Android Studio no Ubuntu

Este guia registra o procedimento que funcionou no notebook para configurar **Flutter**, **Dart**, **Android Studio**, **Android SDK** e conexão de dispositivos Android.

O erro inicialmente encontrado foi:

```text
Unable to locate Android SDK.
```

A solução utilizada foi instalar o **Android Studio**, permitir que ele instalasse o Android SDK e depois informar explicitamente ao Flutter onde o SDK estava localizado.

---

# 1. Instalar dependências do Flutter

Atualize os repositórios:

```bash
sudo apt update
```

Instale as dependências básicas:

```bash
sudo apt install -y curl git unzip xz-utils zip libglu1-mesa
```

Para desenvolvimento Flutter no Linux também foram instalados:

```bash
sudo apt install -y clang cmake ninja-build pkg-config libgtk-3-dev mesa-utils
```

---

# 2. Instalar o Flutter

Crie uma pasta para desenvolvimento:

```bash
mkdir -p ~/develop
cd ~/develop
```

Clone o Flutter no canal estável:

```bash
git clone https://github.com/flutter/flutter.git \
  --depth 1 \
  -b stable \
  ~/develop/flutter
```

Adicione o Flutter ao `PATH`:

```bash
echo 'export PATH="$HOME/develop/flutter/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

Valide:

```bash
flutter --version
```

---

# 3. Dart

Não foi necessário instalar o Dart separadamente.

O Flutter já inclui uma versão compatível do Dart.

Confira:

```bash
dart --version
```

---

# 4. Java utilizado

Na máquina onde a instalação funcionou, o Java instalado era:

```bash
java -version
```

Resultado:

```text
openjdk version "21.0.11" 2026-04-21
OpenJDK Runtime Environment (build 21.0.11+10-1-26.04.2-Ubuntu)
OpenJDK 64-Bit Server VM (build 21.0.11+10-1-26.04.2-Ubuntu, mixed mode, sharing)
```

Portanto, o ambiente funcional utilizava **OpenJDK 21**.

Caso seja necessário instalar:

```bash
sudo apt install -y openjdk-21-jdk
```

Depois valide:

```bash
java -version
```

---

# 5. Verificar inicialmente o Flutter

```bash
flutter doctor
```

Também:

```bash
flutter devices
```

Nesse momento pode aparecer o erro relacionado ao Android SDK:

```text
Unable to locate Android SDK.
```

---

# 6. Instalar o Android Studio

Crie uma pasta para aplicações:

```bash
mkdir -p ~/apps
```

Considerando que o arquivo baixado seja:

```text
android-studio-quail3-linux.tar.gz
```

Extraia:

```bash
tar -xzf android-studio-quail3-linux.tar.gz -C ~/apps/
```

Entre na pasta:

```bash
cd ~/apps/android-studio/bin
```

Execute:

```bash
./studio.sh
```

---

# 7. Configuração inicial do Android Studio

Na primeira execução do Android Studio, conclua o assistente de configuração.

É importante permitir que ele instale o Android SDK.

O caminho utilizado no notebook foi:

```text
/home/felipe/Android/Sdk
```

ou, de forma genérica:

```text
$HOME/Android/Sdk
```

No Android Studio, confira em:

```text
Settings
→ Languages & Frameworks
→ Android SDK
```

Verifique se o campo **Android SDK Location** aponta para:

```text
/home/felipe/Android/Sdk
```

Também confira se estão instalados os componentes necessários do SDK, principalmente:

```text
Android SDK Platform
Android SDK Platform-Tools
Android SDK Build-Tools
Android SDK Command-line Tools
```

---


# 7.1. Abrindo o SDK Manager na tela inicial do Android Studio

Na tela **Welcome to Android Studio**, abra:

```text
More Actions
→ SDK Manager
```

Esse caminho foi confirmado na instalação utilizada.

Dentro do SDK Manager, o caminho do SDK deve estar como:

```text
/home/felipe/Android/Sdk
```

Na aba **SDK Platforms**, para a versão atual do Flutter utilizada neste procedimento, mantenha instalado pelo menos o **Android SDK com API Level 36**.

Na aba **SDK Tools**, a documentação atual do Flutter recomenda os seguintes componentes:

```text
Android SDK Build-Tools
Android SDK Command-line Tools (latest)
Android Emulator
Android SDK Platform-Tools
CMake
NDK (Side by side)
```

## Componentes encontrados na instalação

Na tela analisada, o estado era aproximadamente:

| Componente | Situação | Ação |
|---|---|---|
| Android SDK Build-Tools | Instalado, atualização disponível | Manter marcado / atualizar |
| Android SDK Command-line Tools (latest) | Não instalado | **Instalar obrigatoriamente** |
| Android Emulator | Instalado | Manter |
| Android SDK Platform-Tools | Instalado | Manter |
| CMake | Não instalado | Instalar para deixar o ambiente conforme a recomendação completa do Flutter |
| NDK (Side by side) | Não instalado | Instalar para deixar o ambiente conforme a recomendação completa do Flutter |

Para corrigir especificamente o erro:

```text
Android sdkmanager not found.
```

o componente essencial é:

```text
Android SDK Command-line Tools (latest)
```

Marque-o e clique em:

```text
Apply
→ OK
```

Aguarde o término da instalação.

Depois confirme no terminal:

```bash
find ~/Android/Sdk/cmdline-tools -name sdkmanager -type f
```

O resultado esperado é semelhante a:

```text
/home/felipe/Android/Sdk/cmdline-tools/latest/bin/sdkmanager
```

Depois execute:

```bash
flutter doctor --android-licenses
```

e, por fim:

```bash
flutter doctor -v
```


# 8. Reiniciar o computador

Após a instalação/configuração do Android Studio:

```bash
reboot
```

---

# 9. Informar ao Flutter o caminho do Android SDK

Depois que o Android Studio criar o diretório do SDK:

```bash
flutter config --android-sdk /home/felipe/Android/Sdk
```

Também pode ser utilizado:

```bash
flutter config --android-sdk "$HOME/Android/Sdk"
```

Confira:

```bash
flutter doctor -v
```

---

# 10. Aceitar as licenças do Android

Execute:

```bash
flutter doctor --android-licenses
```

Aceite as licenças solicitadas.

> Observação:
>
> O comando utilizado durante os testes também incluiu:
>
> ```bash
> flutter doctor --android-licenses -y
> ```
>
> Porém, a forma normal e recomendada é:
>
> ```bash
> flutter doctor --android-licenses
> ```

Depois valide novamente:

```bash
flutter doctor -v
```

---

# 11. Confirmar os dispositivos

```bash
flutter devices
```

O Flutter deverá listar os dispositivos disponíveis.

---

# 12. Instalar o ADB

No notebook também foi instalado o pacote:

```bash
sudo apt install google-android-platform-tools-installer
```

Depois valide:

```bash
adb version
```

---

# 13. Conectar um celular Android pela rede

No procedimento utilizado, o celular estava disponível em:

```text
192.168.1.81:38975
```

A conexão foi realizada com:

```bash
adb connect 192.168.1.81:38975
```

Resultado esperado:

```text
connected to 192.168.1.81:38975
```

Depois:

```bash
flutter devices
```

O celular deverá aparecer na lista de dispositivos do Flutter.

---

# 14. Sequência de comandos que funcionou no notebook

O histórico de comandos utilizado foi:

```bash
flutter devices

flutter doctor

sudo apt install -y clang cmake ninja-build pkg-config libgtk-3-dev mesa-utils

flutter doctor --android-licenses

flutter config --android-sdk /home/felipe/Android/Sdk

mkdir -p ~/apps

tar -xzf android-studio-quail3-linux.tar.gz -C ~/apps/

cd ~/apps/android-studio/bin

./studio.sh

reboot

flutter doctor --android-licenses

flutter doctor -v

flutter devices

adb connect 192.168.1.81:38975

sudo apt install google-android-platform-tools-installer

adb connect 192.168.1.81:38975

flutter devices
```

---

# 15. O que causava o erro `Unable to locate Android SDK`

Na máquina com problema foi executado:

```bash
ls -la ~/Android/Sdk
```

E o retorno foi:

```text
ls: cannot access '/home/felipe/Android/Sdk': No such file or directory
```

Isso significa que o Android SDK ainda não estava instalado.

O comando:

```bash
flutter config --android-sdk /home/felipe/Android/Sdk
```

sozinho não instala o SDK.

Ele apenas informa ao Flutter onde procurar.

Se a pasta:

```text
/home/felipe/Android/Sdk
```

não existir, o Flutter continuará mostrando:

```text
Unable to locate Android SDK.
```

---

# 16. Solução utilizada

A solução que funcionou foi:

1. Instalar o Flutter;
2. Instalar as dependências Linux do Flutter;
3. Instalar o Android Studio;
4. Executar o Android Studio;
5. Concluir o assistente inicial;
6. Permitir que o Android Studio instalasse o Android SDK;
7. Confirmar a existência de:

```text
/home/felipe/Android/Sdk
```

8. Executar:

```bash
flutter config --android-sdk /home/felipe/Android/Sdk
```

9. Aceitar as licenças:

```bash
flutter doctor --android-licenses
```

10. Validar:

```bash
flutter doctor -v
```

---

# 17. Diagnóstico rápido

Para verificar se o ambiente está correto:

```bash
java -version
```

```bash
flutter --version
```

```bash
dart --version
```

```bash
ls -la ~/Android/Sdk
```

```bash
adb version
```

```bash
flutter doctor -v
```

```bash
flutter devices
```

---

# 18. Resultado esperado

Ao final:

```bash
flutter doctor
```

deve apresentar algo semelhante a:

```text
[✓] Flutter
[✓] Android toolchain - develop for Android devices
```

E:

```bash
flutter devices
```

deve listar os dispositivos Android conectados ou disponíveis.

---

# Resumo

O ponto mais importante deste procedimento é:

**O Android Studio instalou o Android SDK em `/home/felipe/Android/Sdk`.**

Depois disso, o Flutter foi configurado para utilizar esse SDK:

```bash
flutter config --android-sdk /home/felipe/Android/Sdk
```

e as licenças foram aceitas com:

```bash
flutter doctor --android-licenses
```

Isso resolveu o erro:

```text
Unable to locate Android SDK.
```

---


# 19. Corrigir o Linux toolchain do Flutter

Após concluir a configuração do Flutter e do Android SDK, o `flutter doctor -v` apresentou somente o seguinte problema:

```text
[✗] Linux toolchain - develop for Linux desktop

✗ clang++ is required for Linux development.
✗ CMake is required for Linux development.
✗ ninja is required for Linux development.
✗ GTK 3.0 development libraries are required for Linux development.
! Unable to access driver information using 'eglinfo'.
```

O restante do ambiente já estava funcionando corretamente:

```text
[✓] Flutter
[✓] Android toolchain - develop for Android devices
[✓] Chrome - develop for the web
[✓] Connected device
[✓] Network resources
```

Para instalar as dependências necessárias para desenvolvimento Flutter no Linux:

```bash
sudo apt update
sudo apt install -y clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev mesa-utils
```

Depois valide os principais componentes:

```bash
clang++ --version
```

```bash
cmake --version
```

```bash
ninja --version
```

```bash
pkg-config --version
```

Em seguida execute:

```bash
flutter doctor -v
```

O esperado é que o Linux toolchain passe a aparecer como:

```text
[✓] Linux toolchain - develop for Linux desktop
```

## Observação sobre o `eglinfo`

Caso reste somente o aviso:

```text
! Unable to access driver information using 'eglinfo'.
```

verifique se o pacote `mesa-utils` está instalado:

```bash
sudo apt install -y mesa-utils
```

Depois execute novamente:

```bash
flutter doctor -v
```

---

# 20. Estado final do ambiente

Após toda a configuração, o ambiente deve ter:

```text
Flutter
Dart
Android Studio
Android SDK
Android SDK Command-line Tools
Android SDK Platform-Tools
Android SDK Build-Tools
Android Emulator
Java 21
ADB
Linux desktop toolchain
Chrome/Web support
```

Comandos principais de diagnóstico:

```bash
flutter --version
dart --version
java -version
adb version
flutter devices
flutter doctor -v
```

O objetivo final é obter um `flutter doctor` sem erros relevantes:

```text
[✓] Flutter
[✓] Android toolchain - develop for Android devices
[✓] Chrome - develop for the web
[✓] Linux toolchain - develop for Linux desktop
[✓] Connected device
[✓] Network resources
```

---

# 21. Resumo completo da solução

A configuração que funcionou foi:

1. Instalar o Flutter em:

```text
/home/felipe/develop/flutter
```

2. Utilizar o Dart fornecido pelo próprio Flutter.

3. Instalar e abrir o Android Studio.

4. No Android Studio acessar:

```text
More Actions
→ SDK Manager
```

5. Utilizar o Android SDK em:

```text
/home/felipe/Android/Sdk
```

6. Instalar no SDK Manager:

```text
Android SDK Build-Tools
Android SDK Command-line Tools (latest)
Android SDK Platform-Tools
Android Emulator
CMake
NDK (Side by side)
```

7. Configurar o Flutter:

```bash
flutter config --android-sdk /home/felipe/Android/Sdk
```

8. Aceitar as licenças:

```bash
flutter doctor --android-licenses
```

9. Instalar as dependências do Linux desktop:

```bash
sudo apt install -y clang cmake ninja-build pkg-config libgtk-3-dev libstdc++-12-dev mesa-utils
```

10. Validar tudo:

```bash
flutter doctor -v
```

