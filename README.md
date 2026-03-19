### EA801 - PROJETO 1

### Motor Virtual com BitDogLab V7

**Autores:** 
- Raul Galdino Tancredo (RA: 223908 / [@r223908](https://github.com/r223908))
- Arthur Lucas Da Silva Nogueira (RA: 213293 / [@arthurnog](https://github.com/arthurnog)))

**Professor:** Eric Rohmer

* **Proposta de Projeto**: [Proposta em G-Docs](https://docs.google.com/document/d/1G3z908f7dJlOCZDHbCRtvI69GEogoIHE9IDFKYlxk1Y) (acesso "Comentador" para UNICAMP)
* **Relatório de projeto (in-work)**: [Relatório em G-Docs](https://docs.google.com/document/d/1HIWm7d9RQejxlOvIOjTr2Ctj0aDDG9ewAJ-PNJI3KWs) (acesso "Comentador" para UNICAMP)
* **Demonstração do projeto no YouTube (in-work)**: [Vídeo](link)

---
## ⚙️ DESCRIÇÃO DO SISTEMA
Motor virtual implementado apenas com os componentes disponíveis na BitDogLab V7. O motor é simulado com os 2 LEDs da extremidade da matriz 5x5, com controle de velocidade através do eixo Y do joystick, seleção de cor com os botões e feedback de velocidade através do display OLED.

![alt text](/docs/images/blockDiag_v2.png "Title")

---
## ❗REQUISITOS
1. BitDogLab V7: Já possui todos os periféricos necessários.
2. Cabo micro USB
3. Ambiente de desenvolvimento configurado para MicroPython.

---
## 📚 REFERÊNCIAS
1. Repositório BitDogLab V7: [Repositório no GitHub](https://gitlab.unicamp.br/fabiano/bitdoglab-v7)
2. Banco de Informação de Hardware: [BitDogLabV7_BIH](https://docs.google.com/document/d/13-68OqiU7ISE8U2KPRUXT2ISeBl3WPhXjGDFH52eWlU/edit?tab=t.0)

---
## 📄LICENÇA
* Ver o arquivo `LICENSE`.

---
## 📂 ESTRUTURA DO PROJETO
``` text
├── .vscode/                        → Listagens das config. e bibliotecas
├── docs/                           → Documentação do projeto
│   ├── images/                     → Imagens para relatórios e referências
│   ├── video/                      
│   │   └── Vídeo(s) original(is)   → Vídeo original
│   │   └── link.md                 → Link para o vídeo no YouTube
│   └── (...)                       → Relatórios, diagrama de bloco
├── libs/                           → Bibliotecas
│   └── (...)
├── src/                            → Código-fonte
│   └── (...)
├── LICENSE                         → Licença de uso do código
└── README.md                       → Resumo e estrutura do projeto
```
