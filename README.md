# Gerador Pseudoaleatório Blum Blum Shub (BBS)

Implementação em Python do gerador de números pseudoaleatórios criptograficamente seguro **Blum Blum Shub (BBS)** desenvolvida para a disciplina de Segurança em Sistemas de Computação.

---

## 📋 Parâmetros Utilizados

Os parâmetros escolhidos atendem rigorosamente a todas as premissas matemáticas do algoritmo BBS:

* **Primo $p$**: $18899$ (maior que 10.000 e $p \equiv 3 \pmod 4$)
* **Primo $q$**: $19163$ (maior que 10.000 e $q \equiv 3 \pmod 4$)
* **Módulo $n$**: $362161537$ ($n = p \times q$)
* **Semente $s$**: $1234567$ ($\text{MDC}(n, s) = 1$)

---

## 🚀 Como Executar

1. Execute o script no terminal:
```bash
python blumblumshub.py

```


2. O arquivo `bbs_sequencia.txt` contendo os 100.000 bits gerados será criado no mesmo diretório.

---

## 🤖 Agradecimentos e Ferramentas

* **Gemini**: Utilizado como assistente de IA para auxiliar na compreensão do desafio proposto, estruturação lógica do algoritmo e elaboração desta documentação (`README.md`).
