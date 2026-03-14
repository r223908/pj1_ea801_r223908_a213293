### EA801 - PROJETO 1

### Título do projeto (TBD)

**Autor:** Raul Galdino Tancredo (RA: 223908 / [@r223908](https://github.com/r223908))

**Professor:** Eric Rohmer

* **Proposta de Projeto**: [Proposta em G-Docs](https://docs.google.com/document/d/10GHDXTv5ku1wA1S0LICiZAJUiHmAb50JJuictFbWFdU/edit?usp=sharing) (acesso "Comentador" para UNICAMP)
* **Relatório de projeto**: [Relatório em G-Docs](https://docs.google.com/document/d/1BPoY0Bv_kntMQyELVzm91qtyFT8J9KDplXFu-kLHmjU/edit?usp=sharing) (acesso "Comentador" para UNICAMP)
* **Demonstração do projeto no YouTube**: [Vídeo](link)

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
├── docs/                           → Documentação do projeto
│   ├── images/                     → Imagens para relatórios e referências
│   ├── video/                      
│   │   └── Vídeo(s) original(is)   → Vídeo original
│   │   └── link.md                 → Link para o vídeo no YouTube
│   └── (...)                       → Relatórios, diagrama de bloco
├── lib/                            → Bibliotecas externas e dependências
│   └── lib.md                      → Listagem das bibliotecas necessárias
├── src/                            → Código-fonte
│   └── (...)
├── LICENSE                         → Licença de uso do código
└── README.md                       → Resumo e estrutura do projeto
```
